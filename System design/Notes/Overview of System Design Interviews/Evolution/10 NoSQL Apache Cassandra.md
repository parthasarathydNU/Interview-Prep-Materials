In NoSQL World also we split the data into chunks - shards, also known as nodes.

- Here instead of having leaders and followers, we say each shard is equal
- Instead of having a configuration service we allow shards to speak to each other sharing information about their state
- Further to reduce network load, we don't need each shard to talk to every other shard
- Every second a shard may exchange information with a few other shards using peer to peer communication, no more than three other nodes
- Quickly enough, information about every shard propagates throughout the cluster, this procedure is called the [`Gossip Protocol`](https://www.geeksforgeeks.org/gossip-protocol-in-cassandra/)

In the previous SQL based approach, we used a cluster proxy component, to route request a specific shard as only the cluster proxy knows information about which node contains which shard.

But in this case all nodes know about all other nodes, so clients of this database no longer need a separate proxy to decide which shard to send the request to, but rather can randomly pick any given shard and send the request, and the shards internally can decide which shard to route the data to.

There are actually several distributed SQL systems that do utilize gossip protocols for communication and coordination. However, gossip protocols are not universally adopted in distributed SQL databases for a few key reasons:

## Note on Gossip Protocol Usage in Distributed SQL

Some distributed SQL systems that employ gossip protocols include:

- Cassandra: Uses gossip for node discovery, failure detection, and propagating schema changes[1][4].
- CockroachDB: Utilizes gossip for cluster metadata dissemination[1].
- TiDB: Employs gossip for node status updates and topology changes[1].

## Reasons for Limited Adoption

### 1. Consistency Requirements

Many distributed SQL systems prioritize strong consistency guarantees, which can be challenging to achieve with gossip protocols. Gossip protocols are better suited for eventual consistency models [ 1, 2 ].

### 2. Latency Considerations 

Gossip protocols introduce some latency in information propagation. For transactional SQL workloads that require low latency, this delay may be unacceptable [2].

### 3. Bandwidth Usage

In large clusters, gossip protocols can consume significant network bandwidth as messages are repeatedly exchanged between nodes [4].

### 4. Determinism and Debugging

The probabilistic nature of gossip protocols can make system behavior less deterministic and more difficult to debug compared to more centralized coordination mechanisms [4].

## Alternative Approaches

Instead of gossip protocols, many distributed SQL systems opt for:

- Consensus algorithms (e.g., Raft, Paxos) for strong consistency
- Centralized metadata management services
- Direct node-to-node communication for queries and transactions

While gossip protocols have their place in distributed systems, including some SQL databases, their eventual consistency model and other trade-offs mean they are not universally adopted across all distributed SQL implementations.

Citations:
[1] https://highscalability.com/gossip-protocol-explained/
[2] https://www.linkedin.com/advice/0/how-do-you-choose-suitable-gossip-protocol
[3] https://en.wikipedia.org/wiki/Gossip_protocol
[4] https://newsletter.systemdesign.one/p/gossiping-protocol
[5] https://www.youtube.com/watch?v=WEHM_xU2A0Y
[6] https://www.reddit.com/r/golang/comments/11e1c9m/i_completed_gossip_glomers_a_series_of/
[7] https://www.linkedin.com/pulse/gossip-protocol-failure-detection-distributed-systems-gaurav-pandey