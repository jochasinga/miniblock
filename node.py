import hashlib

class Chain(object):
    """
    A Chain is a merkel chain in a form of a singly-linked list.
    Each node holds a reference to the previous peer's hash, not the pointer.
    Each node also keeps a reference to an atomic chain. 

    >>> starting_hash = hashlib.md5('foobarbaz').hexdigest()
    >>> gen_node = Node(starting_hash)
    >>> chain = Chain(gen_node)
    >>> assert chain is not None
    >>> assert len(chain._chain)
    >>> target = hashlib.md5('foobarbaz').hexdigest()
    >>> original = chain._chain[0]
    >>> assert original == target
    """
    id = 0
    
    def __init__(self, gen=None):
        """In order to initiate a chain, a genesis block node is needed"""
        self.gen = gen
        if self.gen is None:
            hash_str = hashlib.md5('doodlepoodlemoodledoo').hexdigest()
            self.gen = Node(hash_str, genesis=True)

        self.gen.id = self.id
        self.id += 1
        self._chain = [self.gen.hash]
        self.gen.chain = self
        
    def append(self, node):
        if node.hash:
            self._chain.append(node.hash)
            return self._chain
        
        raise ValueError('New block node is missing its hash')

    def size(self):
        return len(self._chain)

    def get_gen_hash(self):
        if self._chain[0].hash:
            return self._chain[0].hash
        
        raise ValueError('The genesis block node is missing its hash')

class Node(object):
    """
    A Node represents a block in a unique blockchain. It contains a unique hash,
    a reference to the previous block's hash, and the hard reference to its parent chain.
    The most forward Node should be responsible for creating a new Node and update 
    the Chain for bookkeeping purpose.
    
    >>> hash = hashlib.md5('doodle').hexdigest()
    >>> node = Node(hash)
    >>> assert node is not None
    >>> assert node.hash == hashlib.md5('doodle').hexdigest()
    >>> assert node.id == 0
    >>> assert node.is_genesis() 
    """
    def __init__(self, hash_str=None, genesis=False):
        if hash_str is not None:
            self.hash = hash_str
        self.previous_hashes = []
        self.id = 0
        self.data = None

    def is_genesis(self):
        return not (self.id and self.previous_hashes)

    def new_block(self, hash_str=''):
        forward_block = Node()
        forward_block.hash = hash_str
        self.chain = self.chain.append(forward_block)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
        
        
