Some distributed SQL systems that employ gossip protocols include:

- Cassandra: Uses gossip for node discovery, failure detection, and propagating schema changes[1][4].
- CockroachDB: Utilizes gossip for cluster metadata dissemination[1].
- TiDB: Employs gossip for node status updates and topology changes[1].

There are actually several distributed SQL systems that do utilize gossip protocols for communication and coordination. However, gossip protocols are not universally adopted in distributed SQL databases for a few key reasons:
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