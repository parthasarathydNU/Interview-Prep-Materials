A small and light weight library that is integrate with the service code and is responsible for cache host selection. 

All cache clients should have the same list of servers, otherwise each client will have their own view of the consistent hashing circle. And the same key might be routed to different cache hosts.

Cache client stores the list of all servers in sorted order by hash value. 

Binary search O(logn) can be used to quickly identify the server.

Cache client uses TCP or UDP protocol to talk to servers. If server is unavailable, client proceeds as though it was a cache miss.

![[Screenshot 2024-08-26 at 3.20.19 PM.png]]

The list of cache hosts is the most important part for any cache client. We need to understand how this list is created, maintained and shared among all clients. 

GoTo [[05 Maintaining Cache Hosts]]