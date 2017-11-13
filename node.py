class Chain(object):
    """
    A Chain is a merkel chain in a form of a singly-linked list.
    Each node holds a reference to the previous peer's hash, not the pointer.
    Each node also keeps a reference to an atomic chain. 

    >>> gen_node = Node()
    >>> gen_node.hash = '9876543210'
    >>> chain = Chain(gen_node)
    >>> assert chain is not None
    >>> assert chain.get_get_hash() == '9876543210'
    """
    def __init__(self, gen):
        """In order to initiate a chain, a genesis block node is needed"""
        if gen.hash:
            self._chain = [gen.hash]
        else:
            raise ValueError('The genesis block node is missing its hash')

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
    >>> node = Node()
    >>> assert node is not None
    >>> assert node.hash == ''
    >>> assert node.previous_hash == ''
    >>> assert node.id == 0
    >>> assert node.data is None
    >>> assert node.is_genesis() 
    >>> node.new_block()
    >>> assert node.chain.size == 2
    """
    def __init__(self):
        self.chain = Chain()
        self.hash = ''
        self.previous_hashes = []
        self.id = 0
        self.data = None

    def is_genesis(self):
        return not (self.id and self.previous_hashes)

    def new_block(self):
        forward_block = Node()
        self.chain = self.chain.append(forward_block)
    
        
        
