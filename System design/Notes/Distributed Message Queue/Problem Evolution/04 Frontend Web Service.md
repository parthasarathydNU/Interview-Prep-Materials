- A lightweight web service 
- Stateless and deployed across several data centers

### Takes care of
- Request Validation
- Authentication / Authorization
- TLS (SSL) Termination
- Server side data encryption 
- Caching
- Rate limiting
- Throttling
- Request dispatching
- Request deduplication
- Usage data collection

#### Request Validation
- Helps to ensure all required parameters are present in this request
- Values of this parameters are within constraints
- Example: Queue name is present in every request, message size is within threshold

#### Authentication and Authorization Check
- Verify that message sender is a registered customer of the distributed queue service
- Verify that the sender is allowed to publish messages to the queue it claims

#### TLS Termination
- TLS is a protocol that aims to provide privacy and data integrity
- TLS termination refers to the process of decrypting request and passing on an unencrypted request to the backend service - *Read about TLS handshake mechanism and the encryption and key sharing process*
- We want to do termination on the Frontend host because TLS on the load balancer is expensive. TLS termination is not handled by the FrontEnd service itself but a separate HTTPs proxy that runs as a separate process on the same host

#### Server side encryption
- Messages are encrypted as soon as frontend receives them
- Messages are stored in encrypted form and FrontEnd decrypts messages only when they are sent back to a consumer
#### Caching
- Cache stores copies of source data
- In frontend cache, we will store metadata information about the most actively used queues as well as user identity information as a way to save costs on the user authentication and authorization service

#### Rate Limiting ( Throttling )
- Throttling is the process of limiting the number of requests you can submit to a given operation in a given amount of time
- Throttling protects the web service from being overwhelmed with requests
- [Leaky bucket algorithm](https://www.tutorialspoint.com/what-is-leaky-bucket-algorithm-in-computer-networks) is one of the most famous 
- *Note: Token Bucket Algorithm is used for one of the implementations of throttling*

#### Request Dispatching (Frontend Service)
- The frontend service makes requests to at least two other services. The metadata service and the backend service
- Front end services creates HTTP clients to both the services and ensures requests to both the services are properly isolated
- There are patterns such as bulkhead and [circuit breaker](https://www.youtube.com/shorts/Rr3nhxWwQGs?feature=share) that helps to implement resource isolation and makes services resilient when remote calls start to fail

#### Request Deduplication
- May occur when a response form a successful `sendMessage` request failed to reach a client
- This is a lesser issue for `at least once` delivery semantics, but a bigger issue for `excatly once` and `at most once` delivery semantics when we need to guarantee that message wasn't processed more than once at a time
- Caching is usually used to store previously listened request ids to avoid de-


#### Usage Data Collection
- Gather real time information that can be used for audit and billing purposes
