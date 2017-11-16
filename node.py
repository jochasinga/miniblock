"""
"""

import hashlib

class Chain(object):
    """
    A Chain is a merkel chain in a form of a singly-linked list.
    Each node holds a reference to the previous peer's hash, which
    is formed by hashing the previous node's hash string concatenated
    by the string representation of the current node's data.
    Each node also keeps a reference to an atomic chain.

    >>> starting_hash = hashlib.md5('foobarbaz').hexdigest()
    >>> gen_node = Node(data=None, hash_str=starting_hash)
    >>> chain = Chain(genesis=gen_node)
    >>> assert chain
    >>> assert chain.size
    >>> assert chain.genesis.hash == starting_hash
    """
    __genesis = None

    def __init__(self, genesis=None):
        """
        In order to initiate a chain, a genesis block node is needed.
        Otherwise, a default one is created.
        """
        if not genesis:
            hash_str = hashlib.md5('doodlepoodlemoodledoo').hexdigest()
            Chain.__genesis = Node(data="I'm genesis", hash_str=hash_str)
        else:
            Chain.__genesis = genesis

        self._blocks = [Chain.__genesis]
        Chain.__genesis.chain = self

    @property
    def genesis(self):
        return Chain.__genesis

    @property
    def last_node(self):
        return self._blocks[len(self._blocks) - 1]

    def get_node(self, hash_str):
        for node in self._blocks:
            if hash_str == node.hash:
                return node
        return None

    def new_node(self, data):
        previous_node = self._blocks[len(self._blocks) - 1]
        previous_hash = previous_node.hash
        new_hash_src = previous_hash + str(data if data else 'doodlepoodlemoodledoo')
        new_hash = hashlib.md5(new_hash_src).hexdigest()
        
        self._blocks.append(Node(data, new_hash, self))
        return self

    @property
    def size(self):
        return len(self._blocks)

    def genesis_hash(self):
        return self.genesis.hash

    def __str__(self):
        result = ''
        for i, block in enumerate(self._blocks):
            arrow = '' if i == self.size - 1 else ' -> '
            block_str = '|{hash}|{arrow}'.format(hash=block.hash, arrow=arrow)
            result += block_str
        return result

class Node(object):
    """
    A Node represents a block in a unique blockchain. It contains a unique hash,
    a reference to the previous block's hash, and the hard reference to its parent chain.
    The most forward Node should be responsible for creating a new Node and update
    the Chain for bookkeeping purpose.

    >>> init_hash = hashlib.md5('doodle').hexdigest()
    >>> node = Node(data=None, hash_str=init_hash)
    >>> assert node
    >>> chain = Chain(genesis=node)
    >>> assert node.hash == hashlib.md5('doodle').hexdigest()
    >>> assert node.is_genesis()
    >>> assert chain.genesis == node
    """
    def __init__(self, data, hash_str=None, chain=None):
        self.data = data
        self.hash = hash_str
        self.chain = chain

    def is_genesis(self):
        return self.hash == self.chain.genesis.hash

if __name__ == '__main__':
    import doctest
    doctest.testmod()
