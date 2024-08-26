Here we decide how to split data across hosts. For example if the keys are from A-Z, then we can store values for keys A-M in `Host A` and keys `N` to `Z` in `Host B`

The service host will decide which shard to pick from and fetch the data from that shard. 

There are two ways to design this, one is by using a Dedicated Cache Cluster and the other is using Co-Located Cache.
![[Pasted image 20240826015508.png]]


**Dedicated Cache ”Cluster”**
- Isolation of resources between service and cache: Both the cache and service do not share memory and CPU and can scale on their own
- Can be used by multiple services: We can utilize the same cluster across several micro services that our team owns
- Flexibility in choosing hardware: This lets us choose hardware with large memory and high network bandwidth. Public cloud providers these days provide a variety of memory optimized hardware

**Co-located cache ”cluster”**
- No extra hardware and operational cost
- Scales together with the server - we add more hosts to the service cluster as needed

![[Pasted image 20240826020054.png]]

Now we have implemented a Least Recently Used Cache and made it run as separate process. 

The cache clients can call this cache process either using a TCP or a UDP connection.  But how do cache clients decide which cache shard to call first.

GoTo [[03 Choosing a Host]]