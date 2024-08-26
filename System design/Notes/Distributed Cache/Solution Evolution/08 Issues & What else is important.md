In the current implementation we have talked about adding new nodes to the cache cluster and adding replicas to nodes to scale reads. 

But this is not truly a fully available system. In case there is some data written to the leader and the leader fails before the data is replicated to the follower nodes, that data is lost. The true focus of a caching system is performance and we need to ensure fast reads and writes to cache. 

Distributed caching system favors availability and performance over consistency.
### Issues that can lead to inconsistency
- We do data replication asynchronously to have a better performance
- Since we follow eventually consistency here, a put request processed by a master node might not be replicated to the follower nodes, so a get call on the follower node might result in a wrong value or a cache miss

Another potential issue:
- Clients can have a different view of cache servers
- Cache servers may go down and go up again, and it is possible that a client can write values that no other client can read

This can be fixed with using synchronous replication and can be fixed by ensuring that all the clients share a single view of the cache servers list. But this will increase latency and overall complexity of the system.

### Stale data in cache: 

We are using an LRU cache policy. But what if the cache does not become full, stale data sits in the cache, so we can also add an TTL to each entry in the cache. This way we can ensure that stale data is not served.

We can passively expire an item when a client accesses a key, we can check if it is expired and evict it from the cache, or we can use an active thread that runs a job at a given frequency and evicts expired items from the cache. 

But there might be billions of entries, so we can't keep iterating over billions of items every time. Usually a probabilistic algorithm is used to decide which items to check at random. Caches like redis have.

### Local And Remote Cache

Services that use cache clients also use a local cache. If data is not available in the local cache call to the distributed is initiated. 

We can add an LRU implementation for the Local Cache.

#### Security

Caches are often accessed by trusted clients inside trusted environments. We should not expose cache servers directly to the internet if not absolutely required. So we need to add a Firewall for the ports that give access to the cache servers. 

Further we also need to encrypt and decrypt the cached data upon reads and writes. But with this we should expect a performance impact. 

#### Monitoring and Logging

If we aim to provide cache as a service, we will need to implement monitoring and logging, this way we can monitor metrics and access patterns. Teams using this caching service across the organization will come to us asking why the service is performing poorly and we should be able to answer their questions. 

Metrics that we want to emit: 
- Number of faults while calling the cache
- Latency
- Number of hits and misses
- CPU usage
- Network IO

Logging:
- Who and when access the cache
- Return key and status code
- Log entries should be small but useful

#### Responsibilities of the Cache Client:
- Maintain the list of cache servers - This can be handled by zookeeper configuration service
- Picking a shard to route to - based on hashing algorithm ( Consistent Hashing )
- Hande remote code and potential failures
- Emit metrics

### Techniques implemented by companies

We can simplify the cache client

Introducing a proxy between the cache client and cache server. This proxy will be responsible for picking the cache shard - take a look at the [twemProxy](https://github.com/twitter/twemproxy?tab=readme-ov-file) project by twitter

Another idea is to , make cache servers responsible for picking the shard.  The cache client sends the request to a random cache server and the server is responsible to pick the shard based on the sharding algorithm. This is implemented by the redis cluster.


#### Issues with Consistent Hashing

**Domino Effect with Consistent Hashing**
- When a cache server dies, all of it's load is transferred to the next server
- This transfer might overload the next server making it to fail, and this proceeds

**Servers do not split the circle evenly**
- Some servers may reside close to each other and some far apart
- This could very well be a cause for the problem of hot shards
- One simple idea is to add each server 

To resolve ths issues in Consistent hashing, there are some techniques introduced

1. Is to add each server on the circle multiple times - how does this help ? 
2. Other one is the Jump Hash Algorithm introduced by google [](https://arxiv.org/pdf/1406.2294)
3. Proportional Consistent Hashing [](https://cs.rice.edu/~as143/COMP480_580_Fall22/scribe/Lec7.pdf)
