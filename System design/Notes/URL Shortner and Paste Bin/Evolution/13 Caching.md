#### **Caching URLs** : 

The server can itself has a cache or this can be an externally distributed cache.

| Inbuilt cache                                                                                                                                                                                                                   | External Distributed cache                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimal latency as there is no call to external system                                                                                                                                                                          | The application server and the cache can be scaled separately                                                                               |
| But when scaling up the application server, we need to adjust the configuration whether we want to scale up the number of CPU so support more processing or increase the RAM to support storing more data in the internal cache | There is an added latency to each request where in the application server has to hit the distributed cache every time it gets a new request |
By thinking about the pros and cons of both use cases, it looks like having caching at both ends seems like a good idea. 

There can be a server level local cache that acts as the first level of cache and the external distributed cache that can act as the second level of cache post which the requests are routed to the Database.

Both these caches need to be configured with appropriate TTL and cache eviction policies, to ensure no stale data is sent back to the user.

#### Storage requirements for caching: 

We can go with the` 80-20 rule` here. 80% of the read traffic comes from 20% of the data. 

80% of the traffic will be for 20% of the URLs : 
- We have `20,000` URLs to redirect per second
- Which adds up to 20000 * 60 * 60 * 24 = 1728000000 URLs Per Day
- 20% of daily traffic comes up to 20 * 1728000000 / 100 = 345600000 URLs to cache
- if we have 6 bytes per URL and assuming 50 bytes for the long url
- 60 Bytes in total
- 345600000 * 60 = 20736000000 Bytes = 20.7 GB


#### Cache Eviction Policy 
LRU eviction policy.

