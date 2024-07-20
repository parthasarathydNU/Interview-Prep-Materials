We have laid the landscape and we know what it is that we need to build. The Goal of the High Level Design is to satisfy the functional requirements

In out case the two functional requirements that we have are :
- Users click on an ad and get redirected to the advertisers website
- Advertisers can query clicks over time w/ 1 minute min granularity that our system is going to support ( details here )

### Components of the high level diagram

**`Browser`** - asks ads placement service for ads
**`Click Processor Service`** 
**`Ad Placement Service`** -- out of scope --
**`Ads DB`** : { Ad id, redirect url, metadata }

### Interactions

***First Functional Requirement: Users click on an ad and get redirected to the advertisers website***

- Users click on the ad and the click is going to get recorded in our `click processor service`
- The users can be sent the redirect url in two ways 
	- One is through the `Ad placement service` , along with the `ad data`, we also send the `redirect url`
		- In this approach, the user clicks on the add - and they are redirected to the `redirect url` and in parallel an entry is logged in the `click processing service`
		- The downside with this approach is that users with `ad blockers`, can directly extract the `redirect url` from the `DOM` and go there directly , circumventing our app's logic to send the click event to the `click processor service`
	- The other way is to only send the `ad id`  from  the `ad placement service`, once a user clicks on the ad, a request is sent to the `click processor service`
		- Here within the click processor service, the redirect url is fetched from the ad db and sent back to the user , and the click event is also logged.

![[Screenshot 2024-07-13 at 5.39.38 PM.png]]

This approach satisfies the first functional requirements.

--------------------------------------------------------------

***Second Functional Requirement: Advertisers should be able to query click metrics***

Till now what we have is `users` are `redirected` to the `advertisers website` and that `click data` is available to the `click processor server`

Now we have to perform the required steps to make it available to the advertiser

#### Components

- `Click DB` - stores the click data | Click Events { eventId, userId, adId, timeStamp ...addlMetadata }
- `Query Service` : Constructs the query and queries the db to fetch the relevant data
- `Advertiser's browser` : Queries information from query service

![[Screenshot 2024-07-13 at 5.46.26 PM.png]]

> This is a decent start to the implementation but not enough to get a passing score - this is just for junior level
#### Considerations: 
- We need to talk about which database type / Database Engine to use and why for this particular use case
- We need to talk about read write speeds and read write loads since this application is data intensive
- Continue reading at [[00 Starter]] 
- We can pick a DB like `Cassandra` for this use case, cause it is optimized for fast writes and it writes event to a `MemTable` which is a` Log Like Structure`
- However the problem here is that, while this DB can handle row level reads, it is not optimized for range queries
- Example: 
	
	```SQL 
	SELECT 
		COUNT(*) as total_clicks, 
		COUNT(DISTINCT userid) as unique_users 
	FROM clickEvents 
	WHERE AdId = 123 
		AND Timestamp BETWEEN 16400000000 AND 16400000001 
		GROUP by AdID
	```
	- Count the number of total clicks by unique users and group by ad id given a given time range.

We know that we have 10k ad clicks per second at peak, so running this group by queries on any database for a given time range will be a slow process.

> ***So for this reason when the advertiser hits the query service, it fails to satisfy the Non-Functional Requirement of having the query return < 1 second***

![[Screenshot 2024-07-13 at 6.01.02 PM.png]]
### Improving the process.

*The key here is to aggregate the data, put it into some database and make it read optimized*

This database is write optimized, but not read optimized. 

#### New Components
- Spark
- OLAP
- Cron Scheduler

#### Modifications
- We can add a `spark` layer : this is going to run a `map reduce job`, which goes through all the `shards` of data in `cassandra`, aggregate the data and store it in an `aggregated format` at a `minute interval` to some `Read Optimized Database`
- This database can be an Online Analytical Processing Database (`OLAP`) - *in this use case, we only have the requirement to query by time range, so we can use any database, but for advanced use case, OLAP databases allow for querying across multiple dimensions*
- And to ensure the spark job runs at a regular cadence, we set up a `cron` scheduler that kicks off every 5 minutes to run the `spark` job

![[Screenshot 2024-07-13 at 6.11.49 PM.png]]
#### Questions:
- Why two databases here ? Why can't we aggregate the data and store it back in the same database ?
	- First reason: **Separating the write heavy and read heavy work loads**, reduces contention and resource competition - different threads
	- Second Reason: **Fault Isolation** - Issues in the write path does not affect issues in the read path - so if one system goes down, the other is still available
	- *The above two features are really important to the system*

> This is `close to passing` for a `mid level candidate` but not a definite pass
> This is a great `starting point` for `senior / staff level candidates`

This is where the design stops for most junior to mid level roles, we have covered the basic functional requirements, and have barely explored the non functional requiremnets

Head on to [[05 Deep Dives]] to continue refining the architecture for the non functional requirements