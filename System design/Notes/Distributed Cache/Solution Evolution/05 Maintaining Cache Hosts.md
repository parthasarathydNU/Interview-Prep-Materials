![[Screenshot 2024-08-26 at 3.24.23 PM.png]]

There are three ways in which we can maintain a shared list of Cache Hosts. 

Approach 1:
Having a local copy of cache server host names and ports in a file in each cache client service. 

The drawbacks of this approach is that everything a host is added / removed, this file needs to be updated in all cache services. 

Approach 2:
Having a shared storage option - here the cache client service, periodically fetches data from a shared storage like S3, and all cache clients refer to this single file. But the drawback here is that, everything we have a host update / delete, we will have to set up an automation job to update this file in the shared storage. 

Approach 3:
Using a configuration service like Zookeeper. Here whenever a cache host server starts, using a daemon service, we register this host with the configuration service. As long as this cache host is alive, it sends a heartbeat to the configuration service. 

Once the cache host goes down, it stops sending heartbeats to the configuration service and it get's de registered. 

All cache clients fetch the list of hosts from this configuration service. This approach is the most difficult to set up and contains operational overhead.