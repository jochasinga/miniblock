import hashlib

class Block(object):
    """
    A Block represents a block in a singly-linked merkel list. It contains a unique hash,
    a reference to the previous block, and arbitrary data attribute.
    """
    def __init__(self, data, previous=None):
        """Only a genesis block can have None as previous"""
        self.data = data
        source = ''
        if previous:
            source = str(previous.hash) + str(data if data else 'doodlepoodle')
        else:
            source = str(data if data else 'doodlepoodle')
            
        self.hash = hashlib.md5(source).hexdigest()
        self.previous = previous

    def is_genesis(self):
        return self.previous is None

    def hashes(self, li=[]):
        """Note: Python is pretty bad at tail recursion"""
        if not self.previous:
            return li
        else:
            li.append(self.hash)
            return self.previous.hashes(li)
        
    def __str__(self):
        hash_str = self.hash
        arrow = '=>'
        template = '({hash}){arrow}'.format(hash=hash_str, arrow=arrow)
        hashes = self.hashes()

        for i, hash in enumerate(hashes):
            
            if i >= len(hashes) - 1:
                arrow = ''
            else:
                arrow = '=>'
                
            block_template = '[{hash}]{arrow}'.format(hash=hash, arrow=arrow)
            template += block_template

        return template

