
### For requirements gathering ask these questions:

Requirements can be gather under the following 4 categories.

| Users/ Customers                                                            | Scale (read and write)                                                                                                                                                                                          | Performance                                                                                                                      | Cost                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>**Who will use the system ?**<br><br>**How will this system be used ?** | <br>**How many read queries per second does the system need to process** ?<br><br>**How much data is queried per request ?**<br><br>**Should we deal with sudden traffic spikes ? How big might they be ?**<br> | <br>**What is the expected p99 latency for read queries ?**<br><br>**How fast does data need to be retrieved from the system ?** | Understand budget constraints<br><br>If the requirement is towards minimizing costs, we should lean towards well regarded open source frameworks<br><br>If future maintenance cost is a primary concern, we should consider public cloud services for our design |

### Here is a little secret

During the requirements clarification section, the interviewer starts to understand our level of expertise with system design.

As with coding interviews, if we don't ask questions, it is a warning sign for interviews. Think along the following 4 categories, 
- think about data, 
- how much data, 
- what data, 
- how does it get in and get out of the system

### For non functional requirements

> Usually the interviewer will not tell us about non functional requirements. Usually they will challenge us by mentioning big scale and high performance as it is hard to achieve both at the same time.

We will need to find trade offs. It is generally recommended to focus on Scalability, Performance and Availability as top priority requirements. 

