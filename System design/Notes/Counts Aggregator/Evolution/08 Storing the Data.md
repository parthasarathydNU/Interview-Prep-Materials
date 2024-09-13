### Where we store the data

Let's talk about where we store the data. Both SQL and NoSQL databases can scale and perform well. So we may want to evaluate both options. 

Here is where we should recall non functional requirements: Scalability, performance and availability. So we should evaluate databases against these requirements and other requirements along the way.

Feel free to use this template for other interview questions and system design in general: 

- How to scale writes ?
- How to scale reads ?
- How to make both writes and reads fast ?
- How not to lose data in case of hardware faults and network partitions ?
- How to achieve strong consistency ? What are the tradeoffs ?
- How to recover data in case of outage ?
- How to ensure data security ?
- How to make it extensible for data model changes in the future ?
- Where to run (cloud vs on-premise data centers) ?

Let's see how [[09 SQL Databases]] handle these requirements..