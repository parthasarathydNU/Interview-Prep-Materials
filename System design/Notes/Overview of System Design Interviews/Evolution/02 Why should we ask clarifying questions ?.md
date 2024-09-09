
| Why is it important for interviewer ?                                                                                                                                                                                                                               | Why it is important for you ?                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Interviewer wants to understand how the candidate can deal with ambiguity                                                                                                                                                                                           | For any given problem there can be many possible solutions. Only if we understand what features of the system we need to design, we can come up with the proper technologies and the building blocks |
| Can the candidate understand the key pieces of information and define the scope of the problem ?                                                                                                                                                                    |                                                                                                                                                                                                      |
| They want to understand how we approach design problems in real life.It is impossible to solve such problems in 45 to 60 minutes, so we should be clear on what functional pieces of requirements are we going to solve and keep that as the focus of the interview |                                                                                                                                                                                                      |

For example: Let's take the problem of counting the number of youtube video views. If we ask this problem to an experienced software engineer with experience in SQL databases, they will explain whey SQL databases is a good fit.

Engineer with profound technologies with NoSQL Databases, they will tell you how we can use Apache Cassandra for this use case.

We can also use a distributed Cache to count the number of views or apply stream processing. Various cloud vendors these days offer Cloud Native Stream processing like Amazon Kinesis. 

Engineers with experience with Batch Processing will solve this problem using Hadoop MapReduce.

![](WhyRequirementsGathering.png)

The problem can be in fact solve with all of the above technologies. But we need to pick the ones that address the requirements. And be able to address the pros and cons of each system.

Next Go To [[03 Requirements Clarification]]
