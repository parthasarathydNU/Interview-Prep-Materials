At this stage of the interview, the statement is ambiguous. 
- What are the functional requirements? 
- What non functional requirements have priority over others ? 
- What is the scale that we need to deal with ?

These are the questions that one needs to discuss with the interviewer before we get started. Let's do our best and define requirements ourselves. 
### Functional 
Let's start with the basic required functionalities that a distributed queue should provide

1. sendMessage(messageBody)
2. receiveMessage()

### Non Functional
- Scalable ( handles load increases, more queues and messages )
- Highly Available ( survives hardware and network failures )
- Highly performant ( single digit latency for both send and receive operations )
- Durable ( once submitted data is not lost )

These are the basic requirements that we can get started with, however, with interviews, there might be other requirements that an interviewer might mention:
- Create and Delete queue API
- Delete Message API
- Producer needs to avoid creating duplicate submissions
- Implement order guarantees

For non functional requirements, the interviewer might ask you to implement certain agreed upon Numbers ( SLAs )
- Minimum throughput our system needs to support
- Need to minimize hardware cost 
- Minimize operational cost

Lets Move to [[02 High Level Architecture]] next