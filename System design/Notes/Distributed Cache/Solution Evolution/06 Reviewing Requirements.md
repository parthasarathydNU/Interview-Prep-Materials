We have the following Non Functional Requirements: 

Highly Performant
Highly Scalable and Highly Available

To store more data in memory we partition data into shards and put each shared in a different cache host.

All cache clients know about all cache shards.

Have we met performance requirements? 

- We have used a least recently used cache implementation for each individual cache host: Both Get and Put Operations are in O(1) time complexity. 
- And since we have distributed this, we have the cache client that uses the constant hashing algorithm and selects the cache host to access in O( log n ) time complexity
- Connection between cache client and cache server is done using TCP  / UDP which is also fast

What about Scalability and Availability ?

Scalability is there :
	We can easily create create more shards and bring in more hosts to store data if requirements arise.

### Problems that might arise

**Hot Shards**

Even though we perform sharding of data some of them might become hot. Some shards may process more data that their peers. This might become a bottle neck. And adding more cache servers may not solve this issue.

With consistent hashing in place, a new cache server will split some shard into two smaller shards. But we don't want to split some shard, we want to split a very particular one that is handling most of the requests. 

**High Availability**

We have not designed for high availability at all. If some shard dies or becomes unavailable due to a network issue, all the data along with that shard is lost. And all requests to that shard will result in a cache miss.

GoTo [[07 Ensuring High Availability and Solving Hot Shard Problem]]