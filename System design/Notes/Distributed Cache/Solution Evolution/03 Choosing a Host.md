**A Naive approach**

*CacheHostNUmber = HASH_FUNCTION(key) MOD NumberOfCacheHosts*

Example: 
- cache_key= “some_cache_key”
- hash = HASH_FUNCTION(cache_key) = 8
- number_of_hosts = 3
- 8 % 3 = 2

Now this key’s value is stored in the host number 2

Problems with this approach: 
- What if new instances are added or one of the cache host goes down ? 

number_of_hosts = 4
8 % 4 = 0

So till now the instances were mapped to node 2, but now they are getting mapped to node 4. This will lead to a lot of cache misses and it is unacceptable in a production level system. This is used for testing purpose only. 

### Consistent hashing


We have a circle from 0 to 2 ^ 32.

Then we take each host and calculate the hash of the host using the host identifier.  We hash the id of the host and it will fall in one of the values from 0 to 2 ^ 32.

The hashed value tells us where on the hash range each host lives. 

Then once we have done this, we can associate each host to a hash range that it owns.

![[Pasted image 20240826145629.jpg]]


Each host will own all the cache items that lives between this host and the nearest clockwise neighbor. 

So for a particular item to  identify which host it lies in , we calculate a hash and move counter clockwise backwards to identify which host it lives in. 

#### What happens when we add a new host to the cache cluster ? 

![[Pasted image 20240826145918.jpg]]

Now that we have added host 6 to the list of hosts, host 4, now becomes responsible for a smaller range, host 6, takes up responsibility of a subset of the range that host 4 was initially responsible for .

Nothing has changed for all the other hosts. And we will only need to rehash a minimal number of keys rather than the MOD based hashing technique. 

Consistent hashing is a much better strategy than MOD based hashing as a significantly smaller number of keys are rehashed when new hosts are added or hosts are removed.

Who is responsible to running all hash calculations and routing the selected request to the correct cache host.

GoTo [[04 Cache Client]]