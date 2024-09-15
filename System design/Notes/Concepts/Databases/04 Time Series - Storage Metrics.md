**INFLUX DB , OpenTSDB**

Suppose we want to build an application metrics tracking system. Suppose we are building a monitoring and observability system where we capture metrics such as throughput, latency, cpu utilization and stuff like that, we will need to be able to capture this information over time. This is where we bring in the concept of time series databases. 

> ***Think of time series databases as an extension of relational databases, but with not all the functionalities but certain additional functionalities.***

Whenever we use a regular relational database we can add any random entry and update a random entry. But when we are building a metrics monitoring system or any time series based system we will not be doing random updates but only appending entries sequentially. 

#### Types of data updates

We use this database in an append only mode. So whenever we add an entry at time `t1` the next entry happens only at time `t2` which is greater than `t1`.

#### Types of data reads

The data that we query is also bulk reads. We query for last day’s data, last week’s, month’s or year’s data. We don’t do random reads or random updates. Time series databases are optimized for this kind of query and input patterns. 

Some of the common databases are `InfluxDB` or `OpenTSDB`