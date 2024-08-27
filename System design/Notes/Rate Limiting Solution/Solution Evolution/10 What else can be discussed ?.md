#### **In theory it is possible that many token buckets can be created and stored in memory**

If millions of clients send a request at the same second. In practice we don't need to keep buckets in memory if there are no requests that come through for a given period of time. 

This is similar to the implementation of a distributed cache, where we can assign a TTL for the bucket key and delete the bucket if it's no longer being used after a point in time, freeing up space to make other required buckets.

#### Failure Modes

Daemon can fail, causing other nodes in the cluster lose visibility of this service host. In this case, this particular host can leave the group and can continue to independently throttle requests without communicating with other hosts in the cluster. 

Nothing really bad happens, just lesser requests throttled per second. A similar issue occurs in case of network partition failures or delays or issues. For example the case where we had 3 hosts and 12 requests were send across the three hosts at the same second.

#### Rules Management

With regards to rules management, we will need to create a self service tool so that service teams can create, update and delete rules when needed.


#### Synchronization being a bottleneck

We have synchronization in the token bucket class where we only allow a method of a Class to only be called by one thread at a time. There is a better way to implement thread safety in that class using Atomic References. Refer to this leetcode discussion [](https://leetcode.com/discuss/interview-question/system-design/124558/Uber-or-Rate-Limiter)

Another place that might require synchronization is the token bucket cache. If there are too many buuckets stored in the cache, we might want to delete the buckets and recreate them when needed. We will end up with synchronization. So here instead of simple hashmap, we will use the `ConcurrentHashMap` which is a `thread Safe` hash map in Java.

Unless the service handles insanely large requests per second, this shouldn't be an issue.

#### What should clients do with failed requests ? 
- Add them to queue and resend them later
- Retry requests with exponential backoff and jitter ( adds randomness to retry intervals to spread out the load ) Jitter helps to spread the retries.