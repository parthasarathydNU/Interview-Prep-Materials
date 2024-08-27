
Here we design the classes and interfaces

![[Screenshot 2024-08-26 at 11.14.32 PM.png]]


### Interfaces and Classes

Interfaces - Define behaviors of various classes

In this system we see the following: 
1. Job Scheduler interface is responsible to run a job every several seconds and retrieve rules from the rules service
2. The RulesCache interface responsible for saving the retrieved rules and providing access to rules when requested by the rate limiter
3. The Rate Limiter Interface that is responsible to decide whether or not to allowARequest
4. The ClientIdentifier that is responsible for deciding which client this request belongs to
5. A Task Interface that executes a defined task


Concrete Classes that implement these interfaces: 
1. The `RetrieveJobScheduler` is the class that implements the `JobScheduler Interface`. It is responsible to run the `RetrieveRulesTask`
2. The `ThrottleRulesCache` is the object that implements the `RulesCache Interface`. This internally builds a key value map that associates each service with the rules passed into it
3. The `ServiceRateLimiter` object implements the `RateLimiter Interface`. This object is responsible to run the rate limiting algorithm in a thread safe manner and ensure requests are accurately throttled for different clients. This internally uses objects of the `TokenBucket` Class for each unique client identified by the `Clientidentifier` object
4. The `Clientidentifier` object takes in unique identifying details of a client and maintains an in memory data structure that returns a unique bucket identifier for each given request
5. The `ThrottleRuleRetrieverTask` class implements the `TaskInterface`. This class has a task definition that can be executed when triggered as a separate process on a thread as part of a job scheduler service. This retrieves throttle rules for various services from  the `throttle rules service `and passes it to the `ThrottleRulesCache` object

![[Screenshot 2024-08-27 at 12.07.58 AM.png]]

GoTo [[07 Making this a Distributed Service]]