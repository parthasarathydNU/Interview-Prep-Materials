No communication between servers just yet. 

Parts of a single server rate limiter implementation.

1. The service owner defines the `rule` for their service ( this service can handle a max of 5 requests per second )
2. These `rules` are stored in a `database`
3. Then within the `service` that has to be rate limited, there is a `retriever` that retrieves these rules and stores it in a `local throttling cache`
4. The retriever periodically queries the database for `updates in the rules` and updates the local cache in the service
5. This local cache is then made accessible to the `rate limiter object `defined within this service: this object is the one that `decides` whether or not a `request` has to be `throttled`
6. For every client that makes a request to this service, a `unique client identifier key` is added to the local throttle cache and every time this client makes a call to this service, the requests made by this client in the last second is updated
7. For every request to this service, the rate limiter fetches checks if the number of calls by this client has exceeded the limit set by the service owner
8. The rate limiter can then make 2 decisions - one to allow the request to be processed and 2 allow it to fail
9. And for the failure case, we can do three things, one drop the request without doing anything about it, (2) return a status code indicating the throttling issue or (3) add it to a queue and process it later

![[Screenshot 2024-08-26 at 11.14.32 PM.png]]

This implementation is pretty straightforward.

From here the interview may go in several directions:
- The rate limiting algorithm [[04 The Rate Limiter Algorithm]]
- Object oriented design and implement classes and interfaces of the rate limiter library [[06 Object Oriented Design]]
- Focus on distributed serving solution and how the service host will share data between each other