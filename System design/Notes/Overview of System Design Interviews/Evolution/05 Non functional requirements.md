> Usually the interviewer will not tell us about non functional requirements. Usually they will challenge us by mentioning big scale and high performance as it is hard to achieve both at the same time.

We will need to find trade offs. It is generally recommended to focus on Scalability, Performance and Availability as top priority requirements. 

- **Scalable:** We want to build a system that can handle 10s of 1000s of video views per second
- **Highly performant:** We want to retrieve the view statistics of total view counts of a video within 10s of milli seconds
- **Availability**: Data should be able to retrieved even if there is network or hardware failures

It is also important to talk about two other important concepts: 
- Consistency requirements in the context of CAP theorem
- Taking about cost minimization

Next, GoTo [[06 High Level Architecture]]