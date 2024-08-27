There are different techniques / strategies to ensure communication between various hosts. This also comes with various pros and const with each setup.

### 1. Tell Everyone everything

Full match network topology, here every node communicates with every other node in the cluster and informs it about token usage. 

How do hosts discover each other, we can use a third party service that hosts register themselves to. Using the heartbeat mechanism the third party service ensures that the host is alive. So when hosts need to broadcast messages, they fetch the list of hosts from this third party service and send messages to all hosts. 

Another way is to manually update a local copy of a config file that has information about other host ip and port. Every time a host is removed or added to the cluster, a process has to be triggered to update this file in all the nodes of this cluster to reflect that change. We can use tools like Ansible, Chef or Puppet to do this.

**Problems :**
- This is not scalable
- Number of messages grows quadratically with the size of the cluster

### 2. Gossip Protocol
This is based on the way epidemics spread. Computer systems typically implement this protocol with a form of random peer selection. With a given frequency, each machine picks another machine at random and shares data. Rate Limiting Solution at Yahoo uses this option!

https://highscalability.com/gossip-protocol-explained/

### 3. Distributed Cache Cluster
Example Redis. 
- This distributed cache cluster can be hoster separately and can be relatively small as this only needs to have information about each host, the buckets it has for each client and the tokens used
- The service can scale independently of this cache cluster
- This can be used across multiple teams in the org or each team can set up their own cluster

### 4. Third Party Coordination service
This third party service choses a leader
- All follower nodes send information to the leader, then calculates the tokens used and sends back the final result
- Each leader is also responsible for it's own keys
- Consensus algorithms like Paxos and Raft can be used to implement this coordination service

**Drawback :**
- We need to set up and separately maintain this service
- Is this really a need for our system ?

## Communication Protocols

How do these hosts talk to each other? 

We have two options here TCP and UDP. 
- TCP guarantees delivery of data and order of packets delivery
- UDP does not guarantee order and delivery of all packets, but because UDP does not perform these checks communication is faster between the nodes in the cluster

If we want rate limiting solution to be more accurate but with a little bit of performance overhead, we need to go with TCP

But if performance is the main goal, then we need to go with UDP. 

But now how do we implement all of these with the service ? 


