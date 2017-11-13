class Node(object):
    """
    >>> node = Node()
    >>> assert node is not None
    >>> assert node.hash == ''
    >>> assert node.previous_hash == ''
    >>> assert node.id == 0
    >>> assert node.data is None
    """
    def __init__(self):
        self.hash = ''
        self.previous_hash = ''
        self.id = 0
        self.data = None
        
        
