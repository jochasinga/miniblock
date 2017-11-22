import unittest
import hashlib

from block import Block


class BlockTest(unittest.TestCase):
    def setUp(self):
        self.genesis = Block('gen')

    def tearDown(self):
        self.genesis = None

    def linklist_test(self):
        """Test the creation of a genesis block node"""
        a = Block('a', self.genesis)
        b = Block('b', a)
        c = Block('c', b)

        assert a.previous == self.genesis
        assert b.previous == a
        assert c.previous == b

    def hashing_test(self):
        """Test the hashing"""
        
        assert hashlib.md5('gen').hexdigest() == self.genesis.hash

        a = Block('a', self.genesis)
        b = Block('b', a)

        assert hashlib.md5(str(self.genesis.hash) + str(a.data)).hexdigest() == a.hash
        assert hashlib.md5(str(a.hash) + str(b.data)).hexdigest() == b.hash
