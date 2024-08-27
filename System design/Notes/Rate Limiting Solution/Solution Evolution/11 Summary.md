- Service owners can use self service tools for rules management
- Rules are stored in the database
- One the service host, we have the `Rules Retriever` that stores rules in the local cache
- When a request comes the rate limiter client builds client identifier and passes it to the rate limiter to make a decision
- Rate limiter communicates with the message broadcaster that talks to other hosts in the cluster

Non Functional Requirements: 

We wanted to build a service that is Highly Scalable, really Fast and accurate. And has this solution met all the requirements ? The answer is not always true. The correct answer depends on various factors. 
- Number of hosts in the cluster
- Number of rules
- Request rate

For majority of clusters out there, where cluster size is  < several thousands of nodes and number of active buckets per node is < 10,000, Gossip communcation over UDP will work really fast and is quiet accurate.

In larger clusters with 10, of 1000 of nodes, we may no longer rely on Host to Host communication in the service cluster and this becomes costly. This is the distribute cache option that we discussed. But the drawback of this approach is that it increases latency and operational cost.