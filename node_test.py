"""
"""

import hashlib
from node import Chain, Node

def blockchain_test():
    """Test the creation of a genesis block node"""

    init_hash = hashlib.md5('foobarbaz').hexdigest()
    chain = Chain(genesis=Node(data=None, hash_str=init_hash))

    genesis = chain.genesis

    assert chain
    assert chain.size == 1
    assert init_hash == genesis.hash

    chain.new_node(data='hello')

    expected_hash = hashlib.md5(init_hash + 'hello').hexdigest()

    assert chain.size == 2
    assert chain.last_node.hash == expected_hash

    chain.new_node(data='world')

    expected_latest_hash = hashlib.md5(expected_hash + 'world').hexdigest()

    assert chain.size == 3
    assert chain.last_node.hash == expected_latest_hash
