### PACELC Theorem - And extension of CAP theorem

![PAC ELC Theorem - An extension to CAP Theorem](PACELC_Theorem.png)

**CAP Theorm :**
- Whenever there is a network partition, then one has to choose between Availability or Consistency
- High Availability means that every request will be served with some response or the other, but it might not be the correct response
- Consistency in CAP theorem points to the fact that to preserve that only the correct data is served for every request, if the correct data is not available, an error message will be returned
- A system can be highly consistent in some parts, while prioritize availability for some of it's other services
- It is more about the tradeoff that impacts user experience that we want to think about when looking at Consistency and Availability

For example, say we have 5 servers, 3 on the west coast and three on the east cost. Suppose there is some issue in communication between the servers on either coasts. 

Suppose data is written to the server on the east coast, but it is not able to communicate with the server on the west coast to replicate the data, when a request comes to the server on the west coast, what do we do ?

- Should we return an error message stating that the correct data is not available
- Or should we return the latest available data and be done with it

Later when the network issues get resolved, the data can be partitioned, bringing both servers back to the same state, but meanwhile, when there is a network issue, what do we prioritize ?


## What about when there is no network partition ?

Similarly say suppose we don't have a network partition, even at that point, a system has to be designed to prioritize **Latency** or **Consistency**

For example if we have a cluster of 5 nodes where data sent to the cluster has to be replicated to other nodes. 

When a particular node receives a request, does it return a success response the moment, it is just saved in it's memory, or does it wait until data is replicated across all the other servers, so that all servers stay at the same state after every request. 

Here comes the question of Latency vs Consistency and the concept of Eventual Consistency. 

In case the system is designed with the idea of eventual consistency, then the request is marked as success right after data is stored in one of the cluster hosts and is eventually copied to all the other hosts. In this case, the rate of processing requests is higher and latency is lower. 

If not, if we want to ensure the system is strongly consistent, then we need to hold the request and make it wait until the data is propogated across the cluster to all the nodes, before returning a success response. This adds latency to the system but it ensures that the system is strongly consistent.

Go To [[03 Understanding Scale]]