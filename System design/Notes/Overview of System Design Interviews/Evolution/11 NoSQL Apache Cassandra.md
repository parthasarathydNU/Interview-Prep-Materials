In NoSQL World also we split the data into chunks - shards, also known as nodes.

- Here instead of having leaders and followers, we say each shard is equal
- Instead of having a configuration service we allow shards to speak to each other sharing information about their state
- Further to reduce network load, we don't need each shard to talk to every other shard
- Every second a shard may exchange information with a few other shards using peer to peer communication, no more than three other nodes
- Quickly enough, information about every shard propagates throughout the cluster, this procedure is called the [`Gossip Protocol`](https://www.geeksforgeeks.org/gossip-protocol-in-cassandra/)

In the previous SQL based approach, we used a cluster proxy component, to route request a specific shard as only the cluster proxy knows information about which node contains which shard.

But in this case all nodes know about all other nodes, so clients of this database no longer need a separate proxy to decide which shard to send the request to, but rather can randomly pick any given shard and send the request, and the shards internally can decide which shard to route the data to.

#### Example Walk through

- Processing service makes a request to a randomly selected node in the cluster using a round robin process
- For this node selection process, there can be some optimizations made such as the node with the least load or the node that is geographically closest to the location of the processing service host that makes this call
- Now the node has to then decide which shard the data for this request has to be placed in 
- For this a consistent hashing algorithm or an advanced version, proportional consistent hashing can be implemented: Refer [[08 Issues & What else is important#Issues with Consistent Hashing]]
- Now the selected node sends a request to the appropriate shard to store the data, and simultaneously send the data to other shards to create replicas
- Waiting for three responses form 3 replicas can be slow, so the response is considered successful as soon as writes to 2 replicas are succeeded - this approach is called quorum writes
- Similar to quorum writes, there is a quorum reads approach while retrieving data. 
- When query service retrieves views count for Video B, the selected coordinator node triggers several read requests in parallel
- The coordinator node might retrieve different data from replica nodes - why ? Because when the data was initially replicated (write request), one of the replica nodes might have been down, so it might be returning stale data
- Read quorum defines a minimum number of nodes that have to agree on the returned data to consider a read as successful
- Cassandra uses version number to determine staleness of data
- And similar to Distributed SQL data centers, each node in this set up can have its follower nodes across several data centers

![Distributed NoSQL Database Cassandra](../Images/DistributedNoSQLDatabase.png)
