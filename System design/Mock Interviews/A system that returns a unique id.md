https://youtu.be/N0mqqI87_g4

### Thoughts
- When we attempt system design problems, how much should we worry about numbers and what sort of number should we be aware of that can be generally used for any interview ?
- Can a distributed caching system work for this system design ?
- Use an iterative design approach, after every stage in the design, highlight the advantages and disadvantages of the current setup with respect to the gathered requirements
- In system design interviews, don;t always go for the next big step, try to ask questions, and try to see if current system can be evolved in smaller ways to address the issue rather than jumping to a new approach completely.
- Follow the framework for system design-- start from requirements, then use appropriate representation for each stage of the system design

### Topics to study
- Atomic value - thread safe implementations
- The difference between five 9s vs four 9s
- Split Brain Problem when designing distributed systems
- Hashing algorithms, URL shortening system
- Pre generating keys and storing in cache instead of generating keys only when user calls
- Number of entries each data type can hold in SQL databases
- Whats a vector clock ?
- Revise AWS notes about services generally used in System Design Interviews like types of load balancers
- Revise API Gateway concepts AWS
- Cloud Front Vs DNS
- Review AWS Mock Exam notes
- Review Status codes


For providing unique keys for each request: 
- We can append user metadata along with time stamp so that way even multiple requests hit our distributed system at the same time, the id generated will be unique
- Do not use auto incrementing keys because it will hit the limit at some point or other and Relational Tables can't be easily scaled vertically

------------------------------------------------------------------------

### Suggestions from interviewer for a real interview that is for 45 minutes:

- You will have to keep talking through
- Keep questioning the design decisions that you are making to check if it is helping you move towards the goal of the system that you want to design


