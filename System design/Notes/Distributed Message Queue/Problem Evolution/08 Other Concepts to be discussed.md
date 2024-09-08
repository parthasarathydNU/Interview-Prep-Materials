#### **Queue creation**
- Queue can be created in multiple ways. Once can be when the message first arrives, the queue can be generated 
- We can create an API for queue creation - this is a better option as we will have more control over queue configuration parameters

#### **Queue Deletion**:
- This must be executed with caution
- Most well known queue services, do not expose the delete functionality through a public facing api but rather can be done through a command line utility only by experienced admin users

#### **Message deletion**:
- (1) One option is not to delete a message right after it is consumed
	- In this case consumers need to be responsible for what has already been consumed
- (2) Further we need to maintain some kind of order for messages in queue and keep track of the offset ( position of a message within a queue ), messages can be deleted several days later by a job - This idea is implemented by Kafka
- (3) We can do something that is employed by Amazon SQS where messages are not deleted immediately but are marked as invisible so that other consumers can't get access to retrieve messages. Consumers who have processed these messages can then manually call the Delete API to delete the messages from the queue. 
	- In case the message is still not deleted after a given period - it is made available for other consumers to process
	- In case the message is not explicitly deleted by a consumer, then the message becomes visible and may be re delivered and processed again by other consumers leading to duplicate records

#### **Message Replication:**

If we have only one copy of data, it may be lost due to hardware failure

- Messages can be replicated synchronously or asynchronously 
	- Synchronous replication means that the request is marked as complete only when messages are copied from the selected host to all other hosts
	- Asynchronous replication means that the response is returned to the user as successfully submitted to queue as soon as message is stored in the selected backend data host. Message is later replicated to other hosts

| *Synchronous Replication*                                       | *Asynchronous Replication*                                                        |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Higher durability but higher latency for send message operation | More performant but does not guarantee that message will survive hardware failure |

#### **Message Delivery Semantics:**

| *At most once*                                   | *At least once*                                | *Exactly once*                             |
| :----------------------------------------------- | :--------------------------------------------- | :----------------------------------------- |
| Messages may be lost, but are never re delivered | Messages are never lost, but maybe redelivered | Messages are delivered once and only onces |

***Why will people need other methods of delivery apart from Exactly once delivery ?***

In distributed message queue system, there are many potential points of failure.
- Producer may fail to deliver or deliver multiple times
- Data replication might fail
- Consumer may fail to retrieve or process the message

All these leads adds complexity and leads to the fact that most distributed queue solutions these days provides at least once delivery that provides a good balance between durability, availability and performance.

#### Push vs. Pull Model

| Push Model                                                                                                                                    | Pull Model                                                                                                                    |
| :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| Consumer is not constantly bombarding the service with requests, instead the consumer is notified whenever a new message arrives to the queue | Consumer constantly sends retrieve message requests and when new message is available in the queue it is sent to the consumer |
| From a consumer perspective, it is easier for them to work with a push                                                                        | From a distributed message queue perspective, Pull is easier to implement                                                     |

#### FIFO

***First in First out***

- In distributed systems it is hard to maintain a strict order
- Message A may be produce prior to message B, but it is hard to guarantee that message A will be consumed before message B
- For this reason many distributed message queue solutions out there either does not guarantee a strict order, or have limitations around throughout as a queue cannot be fast while it is doing many additional validations and coordination when doing many operations

#### Security

- We need to ensure messages are securely transferred to and from a queue
- Encryption using SSL over HTTP helps to protect messages in transit
- We also may encrypt messages while storing them over backend hosts - we mentioned this when we spoke about the Frontend Service host responsibilities [[04 Frontend Web Service]]

#### Monitoring
- Monitoring is critical for every system
- We need to monitor Frontend, Metadata and Backend Services as well as provide visibility of customer's experiences
- We need to monitor health of our distributed queue system and also give customers ability to track state of their queues

#### Metrics and Log Data
- We need to create dashboards of our service and set up alerts
- Customers of our queue have to be able to create dashboards and setup alerts as well
- Integration with monitoring system is required