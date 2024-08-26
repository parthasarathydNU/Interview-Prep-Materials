- We started with a single host and implemented a Least Recently Used Cache
- But since local cache has memory limitations and does not scale, we implemented cache as a stand alone process
- Next to be able to effectively manage memory, we introduced the concept of sharding - Mod based sharding
- But since this is ineffective when new cache host servers are added or removed, we implemented consistent hashing
- Now to ensure the service is able to talk to the cache hosts and pick the right shard, we introduced a cache client
- This client uses a binary search algorithm to quickly identify the host containing the shard and redirect this request to the host

Memcached which is an open sourced high performance cache system is built on top of these principles: 

![[Screenshot 2024-08-26 at 7.46.35 PM.png]]

But this does not provide high availability and there are a lot of issues with consistency.

- We introduced a configuration service like zoo keeper that keeps track of all the cache hosts
- Whenever a new cache host is added , it registers itself with the zoo keeper service, and maintains its live state using a heartbeat mechanism
- Now all the cache clients can maintain the same view of the cache hosts through the zookeeper service
- Other issues include hot shards, data availability and data consistency
- To address the issue of hot shards and data availability, we brought in the concept of replica nodes for each cache host
- These replica nodes try to follow and keep up with the master node, replica nodes handle most of the read requests and the writes are send to the master node
- Further a configuration service can be used to keep track of the load on these nodes, check for failures 
- The replica nodes are spread across multiple data centers so this ensures that in case of any node failure data is still available
- However since we are still working across a network partition there will be issues where before processing a particular write, the master node might go down and this entry can be lost, this will result in a cache miss
- Further we looked as other issues with consistent hashing like the domino effect that can be mitigated with other strategies like the jump hashing algorithm or consistent proportional hashing 
- Security - encryption and decryption - performance hits
- Stale data in cache - along with the fact that we are using an LRU, we can use the concept of TTL for the keys in the cache, this can either be passively or actively checked - In redis keys can be set with a TTL value and internally redis runs a probablistic algorithm that randomly checks certain nodes at a given cadence and evicts the key form the cache in case it is stale
- Monitoring and logging
- Simplifying the cache client by introducing a proxy between the cache client and the cache servers or making the cache servers decide which shard to pick based on the sharding algorithm

![[Screenshot 2024-08-26 at 7.57.44 PM.png]]