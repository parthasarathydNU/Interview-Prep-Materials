> In the current state of the design, we should have satisfied the functional requirements
> And now we are going to deep dive with the goal of satisfying non functional requirements


![[Screenshot 2024-07-13 at 6.26.56 PM.png]]

### Non functional requirements that we will be looking at
- ***`Latency`*** - In this current state of the system, advertisers do not really know what happens to their ad immediately after they launch it, they have to `wait` for the first five minutes, and then for the spark job to be triggered and only then will any data be available in the `OLAP` database for querying - This does not satisfy the low latency and near realtime streaming functionality requirement
- Further the advertiser has to wait every 5 minutes to see the next update, this is not ideal

Now to address this issue, we can make the spark job run every minute or every 30 seconds, but as the application scales up, and the size of data increases, starting a spark job every 30 seconds or so is computationally expensive, we hit a limit. So we need to change the way the aggregation happens.


### Other options: 

#### Near Real Time Requirement

***Introducing `Flink`***: Flink is a software that can help us perform aggregation on `streaming data`. 

So now instead of storing click events to a `click db`, we write the click events to an `event stream`, and have `Flink`  aggregate this information at a `minute level` and write it to the OLAP database at the end of every minute.

This way the `advertiser no longer needs to wait for 5 minutes to get to know updates`, but can query information at a minute level of granularity. 

Since the non functional requirement is to `provide aggregated data at a minute level granularity,` this ***`satisfies the real time condition as well.`***

`Flink`  supports something called as a `flush interval`. This indicates the cadence at which data is written from `Flink` to the `OLAP` database.

Here we see two metrics: 
- Aggregation Window: 1 minute
- Flush Interval: 10 seconds

What this does is, this allows `Flink` to push partial aggregated data to the OLAP database, this way the advertiser can see what's the clicks are for the current minute after 10 seconds of a minute, and refresh it again at the 20 second mark.

The granularity still stays at the minute level, but data get's updated every 10 seconds. 
***This adds towards the near real time  non functional requirement***

-----------------

![[Screenshot 2024-07-13 at 7.00.48 PM.png]]

> This system is better than the previous one as now advertisers can get data almost immediately.
> 
> Senior and staff level candidates start from here as their high level design

--------------------------------------------------

### Scalability for a peak of 10K clicks per second

The first obvious candidate is adding horizontal scaling to the `ad placemnet service` and the `click processor service` fronted by their individual load balancer. 

This system can then be fronted by an Managed API Gateway that the browser can talk to , this handles routing and authentication and is load balanced internally.

More importantly it is important for us to handle the scaling of the event stream: 
- Amazon Kinesis has a limit of `1000 records per second` or 1MB / s, so this will not work for a peak load of 10K / s
- So we will need some sort of `sharding` here - shard by `adId`

Scaling Flink: 
- We can have separate Flink jobs `segregated by adId` as well. This works well for our system because we are only going to provide aggregation at an `ad Id level`, so each flink job can handle aggregation for it's own adId

Scaling The OLAP database
- This can be sharded by `AdvertiserId` cause each advertiser will have their own set of ads that they might want to query for 