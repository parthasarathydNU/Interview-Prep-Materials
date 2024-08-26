“Let me start with a local cache. Here is how I would implement an in-memory data storage for a single server”

Local cache implementation is an algorithmic problem. We need to come up with data structures for storing and retrieving data. 

A simple data structure that comes to mind is a hash table. But the problem with having a hash table is that it is of fixed size. Old entries need to be removed from the hash table to make way for new entries. 

> Differences and similarities between dictionaries and hash tables in python [](https://medium.com/@burakroccia/understanding-python-dictionaries-and-hash-tables-differences-and-similarities-4d777a946ea0#:~:text=Data%20Structure%20Type%3A%20In%20Python,dictionaries%20and%20other%20data%20structures.)

### Eviction of entries in the hash table

There are various rules / policies that can be used for eviction of data from a hash table. 

One of it is called the least recently used policy ( LRU ), when we discard the least recently used item before adding the new entry when the table is full. 

Practice this implementation: https://leetcode.com/problems/lru-cache/

But the hash table does not keep track of when an item was used, it only stores keys and values. So this means, we will need another data structure to keep track of what was used when.

We need some kind of queue with constant time for add update and delete operations. We go with a doubly LinkedList for this purpose.

![[Pasted image 20240826014123.png]]


![[Pasted image 20240826015105.png]]

GoTo [[02 Making it Distributed]]