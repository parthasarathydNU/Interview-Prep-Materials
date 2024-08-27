**Ideally don't services have to be scaled to handle higher load ?**

> The problem with scaling up or scaling out, does not happen immediately, auto scaling takes time.

By the time the scaling operation is completed, the load might have significantly increased and the server might have crashed.

**What about max connections in the load balancer and max threads count on the service end point? Do we still need throttling ?**

> The problem with relying on the max connection limit and the max threads in the load balancer is that, the load balancer is indiscriminate. It does not know which services complete faster vs which services take longer and are operationally expensive.

Therefore rate limiting / throttling needs to be achieved at the service level rather than relying on the load balancer to handle this issue.

**This does not seem to be a system design problem**

Is this an algorithmic problem ? - Yes
We need to define data structures and algorithms to count how many requests each client has made so far.

Is this an Object Oriented Problem ? - Yes
We might need to define a set of classes to manage throttling rules. Rules define an allowed throttling limit for each operation.

**If we implement throttling for a single host are we done ?**

In an ideal world - yes, but not in the real world. In the real world we need a distributed solution where application servers can talk to each other and together handle the throttling. 

In an ideal world, the load balancer evenly distributes the load across the servers and each server processes the same job and it takes the same amount of time and resources to complete. In this case, just implementing the throttling at the service level where each server individually throttles requests to it will work. This will be a single host problem

![[Screenshot 2024-08-26 at 10.06.56 PM.png]]

But it is not so in the real world.
- Load can be unevenly distributed by the load balancer
- Each request might take different time to process the request and can have different performance metrics
- There might be background processes running on some servers while not on others
- Each of the individual servers might also be of different configurations in terms of memory, CPU and I/O

So in this case we will need a solution where application servers can communicate with each other and how many requests each one of them has processed so far.

![[Screenshot 2024-08-26 at 10.11.28 PM.png]]