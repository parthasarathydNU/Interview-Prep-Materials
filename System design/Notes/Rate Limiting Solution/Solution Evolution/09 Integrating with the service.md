There are two options to integrate: 
- Run rate limiter as part of the service code
- Run rate limiter as a separate process

### Integrated as part of service code:
- Rate limiter is distributer as a collection of classes
- A library that has to be integrated into the code

Pros: 
- This is faster
- Resilient to interprocess call failures - there is none
- Both the rate limiting service and the service process runs on the same host

### As a separate process: 
- We have two libraries, the daemon itself and the service client
- The client is responsible for inter process communication - between the service process and the daemon
- Client is implemented with the service code

Pros: 
- Programming language agnostic
- While the rate limiter daemon can be written in any language, the client has to be native to the codebase of the service
- We don't have to do integration at the code level
- The rate limiter process uses it's own memory space, this helps us control behavior for both the service and the daemon

Service teams tend to be very cautious when you come to them and ask to integrate their service with your super cool library: We will hear tons of questions: 
- How much memory and CPU will your library consume ?
- What will happen in case of network partition or any other exceptional scenario ? 
- Can we see results of load testing of your library
- What are your mom's favorite flowers and many others

So which option is better ? Both are good options and it depends on the needs of a particular service team.

GoTo: [[10 What else can be discussed ?]]