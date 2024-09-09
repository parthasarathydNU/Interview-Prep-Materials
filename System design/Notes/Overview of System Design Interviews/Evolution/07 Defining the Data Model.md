We have two options for what data we might want to store. 


| Individual Video  Events                                                                                                                                                                                                      | Aggregate data (e.g. per minute) in  real-time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capture all attributes of the event, videoId, timeStamp, user information, country, device type, etc..                                                                                                                        | We calculate a total count per some time interval, let's say one minute, and we lose details of each individual event                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br>**Pros**<br><br>- Can be stored really fastt<br>- We can slice and dice however we want<br>- Filter based on specific attributes, aggregate based on rules<br>- Recalculate numbers from scratch if required<br>          | <br>**Pros :**<br><br>- Reads become fast , we don't need to calculate individual events, we just retrieve total count value<br>- Use it for `decision making in real time`, we can send the total count values to recommendation or trending service for popular videos to be promoted to trends                                                                                                                                                                                                                                       |
| <br>**Cons:**<br><br>- We cannot read data quickly, we will have to read individual events when count is requested, it takes time<br>- Data storage cost will be high. .Youtube generates billions of view events per day<br> | <br>**Cons :**<br><br>- We can only query data the way it was aggregated<br>- Ability to filter data or aggregate it in another way is highly limited<br>- Requires us to implement data aggregation pipeline, we need to somehow pre aggregate data in memory and store it in database, this is not an easy task and later in this document, we will see why<br>- It is hard / impossible to fix errors, let's say there was an issue with the aggregation logic, and we haven't stored individual events, how do we fix the bug ?<br> |

##### Which option should we choose ? 

Store row events or aggregate data in real time. This is where the interviewer can help us make decisions. We should. ask interviewer about:
- Expected data delay
- Time between when the event happens and when it was processed 

If it should be no more than several minutes, we need to aggregate on the fly (stream processing). If several hours is okay, we can store row events and process data in the processing. (Batch processing).

Sometimes combining both options makes sense for many systems out there.

Example: 
- Individual event data can be stored in raw unstructured format while processed aggregated data can be stored in OLAP databases for fast retrieval.
- For how long do the individual events need to be stored ? Based on compliance requirements, if it is not mandatory to store all events data, it can be purged after a specified point in time or it can be shifted to low cost storage systems after a given point for longer time storage

Therefore by storing both aggregated and row level data, we get the best of both world, we get fast reads, we can re aggregate data in other forms, and aggregations can be re calculated by using stored row level data.

There is a price to pay for all this flexibility, and the various options to manage this storage and cost is a great topic to discuss with the interviewer.

Further in this document we will be focussing on the Real Time Streaming approach as there are a lot to concepts to design on that front.

Go To [[08 Storing the Data]]