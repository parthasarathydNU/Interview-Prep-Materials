### What are Quorum Writes (n/2) + 1

Quorum writes are an important concept in distributed database systems for ensuring consistency and fault tolerance. Here are the key points about quorum writes:

1. Definition: A quorum write requires that a write operation be acknowledged by a minimum number of replica nodes before it is considered successful.

2. Purpose: Quorum writes help maintain consistency across distributed replicas and provide fault tolerance in case some nodes fail.

3. Calculation: The quorum is typically calculated as (N/2 + 1), where N is the total number of replica nodes. This ensures a majority.

4. Trade-offs: 
   - Higher consistency but potentially lower availability and higher latency compared to eventual consistency models.
   - More fault-tolerant than requiring all nodes to acknowledge, but less available than single-node writes.

5. Read/Write Quorums: Often paired with read quorums to ensure that reads always see the most recent write.

6. Consistency Guarantee: When combined with read quorums, provides strong consistency if read quorum + write quorum > total nodes.

7. Examples: Used in systems like Apache Cassandra, Amazon DynamoDB, and other distributed databases.

8. Flexibility: Allows tuning of consistency levels by adjusting quorum size based on application needs.

9. Network Partitions: Helps maintain consistency even when the network is partitioned, as long as a quorum can be reached.

10. Performance Impact: Can increase write latency as the system waits for acknowledgments from multiple nodes.

Quorum writes are a key mechanism for balancing consistency, availability, and partition tolerance in distributed systems, allowing developers to tune these properties based on their specific requirements.

Citations:
[1] https://www.designgurus.io/answers/detail/what-is-quorum-in-distributed-systems
[2] https://www.educative.io/answers/what-is-quorum-in-distributed-systems
[3] https://blog.sofwancoder.com/distributed-system-understanding-quorum-based-systems
[4] https://en.wikipedia.org/wiki/Quorum_%28distributed_computing%29
[5] https://stackoverflow.com/questions/78279634/what-is-the-point-of-a-write-with-consistency-quorum-if-the-consistency-is-not-a
[6] https://www.reddit.com/r/golang/comments/11e1c9m/i_completed_gossip_glomers_a_series_of/
[7] https://www.linkedin.com/advice/0/how-do-you-choose-suitable-gossip-protocol
[8] https://highscalability.com/gossip-protocol-explained/

#### In case of Apache Cassandra, when Sharding the data across various nodes, suppose we use consistent hashing, we say that each node/shard is responsible for one portion of the data, are the other nodes used as replicas for this data or do they just hold data within the range of the keys that the shard is responsible for ? Because if we store all data in all nodes, then whats the use of sharding ?

In Apache Cassandra, when using consistent hashing for data distribution, each node is indeed responsible for a specific range of data, but the system also maintains replicas of that data on other nodes. Here's how it works:

1. Primary Data Range: Each node is responsible for storing and managing a primary range of data based on the partition key hash values[1][5].

2. Replication: Cassandra also maintains replicas of data on multiple nodes for fault tolerance and availability. The number of replicas is determined by the replication factor configured for the keyspace 1* 5*.

3. Data Distribution:
   - The primary copy of data within a specific hash range is stored on the node responsible for that range.
   - Replicas of that data are stored on other nodes in the cluster, typically the next nodes in the ring according to the consistent hashing algorithm 1* 5*.

4. Purpose of Sharding:
   - Even though data is replicated, sharding (partitioning) is still crucial for scalability and performance[6].
   - It allows Cassandra to distribute the read and write load across the cluster.
   - Each node primarily serves requests for its own range, reducing contention and improving throughput[6].

5. Consistency Levels: Cassandra allows you to configure consistency levels for reads and writes, determining how many replicas must respond for an operation to be considered successful[8].

6. Virtual Nodes (Vnodes): Cassandra uses virtual nodes to improve load balancing and make it easier to add or remove physical nodes from the cluster 1* 5*.

So, to answer your specific question:
- Nodes do not store all data in the cluster.
- Each node stores its primary range of data plus replicas of data from other ranges.
- The use of sharding (partitioning) is to distribute both the data and the workload across the cluster, improving scalability and performance.

This approach allows Cassandra to balance data distribution, fault tolerance, and performance in a distributed environment.

Citations:
[1] https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html
[2] https://towardsdatascience.com/system-design-consistent-hashing-43ddf48d2d32?gi=f4f8b811b3c0
[3] https://stackoverflow.com/questions/30610535/how-to-ensure-that-consistent-hashing-works
[4] https://www.linkedin.com/pulse/guide-consistent-hashing-how-works-why-its-effective-michael-worku
[5] https://docs.datastax.com/en/dse/6.9/architecture/database-architecture/consistent-hash.html
[6] https://highscalability.com/consistent-hashing-algorithm/
[7] https://cassandra.apache.org/doc/3.11/cassandra/data_modeling/intro.html
[8] https://stackoverflow.com/questions/78279634/what-is-the-point-of-a-write-with-consistency-quorum-if-the-consistency-is-not-a

#### If each node stores replicas of other nodes data as well, then how can the database cluster scale when the number of keys increase ?

You're asking an excellent question about how Cassandra scales as the number of keys increases, given that each node stores replicas of other nodes' data. Here's how Cassandra manages to scale effectively:

1. Data distribution: Cassandra uses consistent hashing to distribute data across nodes. Each node is responsible for a range of data based on the partition key hash[3]. This ensures even distribution of data across the cluster.

2. Replication: While nodes do store replicas of other nodes' data, this is controlled by the replication factor (RF) configured for each keyspace[3]. The RF determines how many copies of each piece of data are stored across the cluster.

3. Horizontal scaling: As data volume grows, you can add more nodes to the cluster. When new nodes are added, Cassandra automatically redistributes data across all nodes, including the new ones[1][2]. This process is called "bootstrapping".

4. Virtual nodes (vnodes): Cassandra uses virtual nodes to improve load balancing and make it easier to add or remove physical nodes[3]. Each physical node is responsible for multiple smaller ranges of data (vnodes) rather than one large contiguous range.

5. Incremental scaling: You don't need to double your cluster size each time. You can add nodes incrementally as needed[2].

6. No full data replication: While nodes store replicas, each node doesn't store all data. The replication strategy and factor determine which nodes store which replicas[3].

7. Efficient reads and writes: Cassandra allows you to configure consistency levels for reads and writes, determining how many replicas must respond for an operation to be considered successful[2].

So, even though nodes store replicas, Cassandra can still scale effectively because:
- Not all data is replicated to all nodes
- Data is evenly distributed across the cluster
- New nodes can be added to increase capacity
- The system is designed for horizontal scaling

This approach allows Cassandra to balance data distribution, fault tolerance, and performance in a distributed environment, enabling it to scale to handle large volumes of data and high write throughputs[1][2].

Citations:
[1] https://www.pythian.com/blog/technical-track/why-your-cassandra-cluster-scales-poorly
[2] https://stackoverflow.com/questions/45183884/cassandra-write-throughput-and-scalability
[3] https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/architecture/archDataDistributeAbout.html
[4] https://stackoverflow.com/questions/25337043/what-does-it-mean-when-we-say-cassandra-is-scalable
[5] https://towardsdatascience.com/system-design-consistent-hashing-43ddf48d2d32?gi=f4f8b811b3c0
[6] https://cassandra.apache.org/doc/3.11/cassandra/data_modeling/intro.html
[7] https://www.ksolves.com/blog/big-data/apache-cassandra/apache-cassandra-scaling-guide-why-does-scalability-matter
[8] https://stackoverflow.com/questions/30610535/how-to-ensure-that-consistent-hashing-works

Go To [[13 Consistency]]