**We have a cluster that consists of 3 hosts and we want the rate limiting service to allow 4 requests  per second for each client, how many tokens should we give to a bucket on every host ?**

**Should we give 4/3 for each host for this bucket ?**

> No the answer is 4. This is because, while the load balancer knows about the hosts, it does not know anything about they keys. This particular host might have lesser load so the load balancer decides to route all requests to this host, in that case each host must be able to individually handle the throttling. In theory this is possible and in real life, the load balancer does not always evenly distribute requests to all hosts

![[Screenshot 2024-08-27 at 1.53.39 AM.png]]

Let's run a simulation:
- Request 1 hits host A and it consumes one token from there
- Request 2 hits host B and it consumes one token from there
- Request 3 and 4, hits host C and it consumes two tokens from there

Now as per rate limiting rules, we have allowed 4 requests to this service across multiple hosts. But we will need to throttle all other requests that try to access this host this second. How can we achieve that ?

![[Screenshot 2024-08-27 at 1.55.26 AM.png]]

We must allow hosts to talk to each other and share how many tokens have been consumed all together.

![[Screenshot 2024-08-27 at 2.00.33 AM.png]]

In this case, host A sees that other hosts ( B + C ) have consumed 3 tokens, so it does remaining -3
B subtracts 2 ( A + C ) from its' available tokens
C subtracts 3 (A + B) from it's available tokens 

![[Screenshot 2024-08-27 at 2.01.50 AM.png]]

Now 4 requests have been processed and no more are allowed.

### Issue

Say we have a situation where 4 requests hit each bucket at the same second. This is a total of 12 requests. Can all these 12 requests be processed instead of just the 4 allowed ? 

A more realistic scenario. Communication between hosts take time. Untill the hosts agree upon what is the number of requests that have been done together, can there be other requests that slip into the system at that time ? 

Yes, unfortunately this is the case. We need to scale our cluster accordingly to handle this issue. 

#### By the way the token bucket algorithm will handle this use case well. It has to be slightly modified.

If in case 12 requests hit the bucket at the same second, each bucket will have -8 tokens for the next second and all requests will be throttled for the next two seconds. 

So what happens here is that on average we processed 4 requests per second ( 12 requests over 3 seconds ) but all 12 requests hit at the service at the very first second.

This is one loop hole in the system, and our system needs to be designed to handle this situation and scale accordingly before the throttling mechanism kicks in.

GoTo [[08 Communication Between Hosts]]


