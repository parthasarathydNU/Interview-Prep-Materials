[YoutubeVideo Link](https://youtu.be/iJLL-KPqBpM)

Let's say we have two services called the producer and consumer and they need to communicate with each other. 

#### One way is through synchronous communication. 

The producer makes a call to the consumer and waits for the response. 

**Pros**:
- easy and fast to implement

**Cons**:
- Makes it harder to deal with consumer service failures
- Additional work on the producer side 
	- What do do with failed requests
	- Ensuring we are not over loading the consumer with too many requests
	- Dealing with slower consumer hosts


#### Asynchronous Communication

Another way is to have another component that the producer can send this message to. And exactly one consumer get's this component a short time after. Such a component is called a queue. And this is distributed because data is stored across several machines.

**Important | Do not confuse a queue with a Topic:**

> In a topic message that is published is received by each and every subscriber
> 
> In a queue, message is received by one and only consumer

![[images/ProblemStatementIntroduction.png]]


