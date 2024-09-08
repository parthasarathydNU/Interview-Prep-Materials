Every time a queue is created, we store information about it in the database. 
- Conceptually the metadata service is a caching layer between the frontend service and persistent storage
- It relatively has more number of reads and lesser number of writes
	- We read every time a message arrives and write only when a new queue is created
- Even though consistent storage is preferred to avoid potential concurrent updates, but it is strictly not required.

An Aside on the use of cache for building a distributed queue service

> Caching is a crucial technique used in building a distributed queue service to improve performance, scalability, and reliability. Here's a brief overview:
> 
> In a distributed queue service, caching is used to temporarily store messages or data in memory (RAM) or a dedicated cache layer, like Redis or Memcached. This approach helps:
> 
1. *Reduce latency*: By storing frequently accessed data in a cache, the system can quickly retrieve messages without needing to access the underlying database or persistent storage, which can be slower.

2. *Increase throughput*: Caching enables the queue service to handle a higher volume of requests and messages by reducing the number of times the system needs to read from or write to disk.

3. *Improve reliability*: If a node or service fails, the cache can help recover messages or data that might have been lost, ensuring the queue operates correctly.

4. *Enhance scalability*: Caching allows the distributed queue to scale more efficiently, as it reduces the load on individual nodes and enables the system to handle increased traffic.

Some common caching strategies in distributed queue services include:

- *Message caching*: Storing entire messages or payloads in the cache.
- *Metadata caching*: Storing message metadata, like message IDs or timestamps, in the cache.
- *Queue state caching*: Storing the current state of the queue, like the number of messages or queue depth.
### Approaches to organize Cache Clusters

Check out notes on [Distributed Cache](https://github.com/parthasarathydNU/Interview-Prep-Materials/tree/main/System%20design/Notes/Distributed%20Cache)

**When cache is relatively small and we can store all data on every cluster node**
- Frontend Host can call a randomly selected metadata server host, because all the hosts contain the same information.

**Second approach : Partition data into multiple chunks or shards**
- When data is too big to be placed in the memory of a single host, it can be split and stored across multiple hosts based on a unique key
- Frontend knows which shard stores the data and calls that shard directly

**Third Approach: Frontend does not know which host to call**:
- Rather the frontend randomly sends the request to any metadata cache host, and the hosts know to which shard to forward the requests to

#### Note:
The components that we have built so far are relatively straightforward, but not easy of course. But if you have an understanding of core design principles, you will proceed this far in the interview. 

The set of components that we have discussed, VIP, Load Balancer, Web Service, Metadata Web Service + Caching layer on top of the database is so popular in the world of distributed systems that we can consider it as a standard and apply it to many system designs.

Next: Move on to the [[06 Backend Service]] - this is where the real challenge starts