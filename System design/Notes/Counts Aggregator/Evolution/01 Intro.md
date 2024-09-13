What are the important concepts of system design interviews ? Let's look at the concepts by going through a system and designing it.

#### Problem Statement:

> Design a system that does counting

This sort of problem appears in systems such as 
- Counting views of youtube videos
- Counting likes on facebook or instagram

![](ProblemStatement.png)

**Usually such problems are stated in a vague or a general manner.**

For example we might not be asked to calculate a single metric like number of views but a number of metrics. For example: "*calculate the performance metrics of so and so application.*"

- We need to count number of requests that go through the service
- Errors that service produces
- Average response time

Further interviewers can make it more generic like design a system that "analyzes data in real time".

There are a lot of ambiguities here:
- What does data analysis mean ?
- Who sends us data ?
- Who uses the results of this analysis ?
- What real time really means ?

Such questions need to be clarified. Even if the requirement seems well defined here are two reasons as to why we need to ask interviewers clarifying questions.
