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

