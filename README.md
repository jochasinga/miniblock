# miniblock

A small light-weight blockchain engine.

# description

Blockchain has been out in the wild now, and there have been many adaptations that it has become a concept rather than a single implementation. This is another implementation to tinker with the idea.

Blockchain in its essence is an atomic, immutable singly-linked list where each "block" or node holds a hashed value of the previous's data, hash, or both combined. 

The idea of consensus comes in when some kind of network is involved, and this atomic list is copied to each client either in a synchronous manner or asynchronous, eventually-consistent one.

Whenever a new block is about to be created on the master list, it needs a certain amount of clients to compare their copy to one another and to the master. If the equality test passes, then the master list is allowed to create it, and then the new state of the master list is copied to all clients once again.




