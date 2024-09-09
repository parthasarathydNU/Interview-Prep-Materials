Another important topic to talk about is consistency

When we defined our non functional requirements, we decided to go with Availability over Consistency. Which simply means that we prefer to show stale data over no data at all.

Synchronous data replication is slow, we prefer to replicate data asynchronously. In case of leader follower setup, some read replicas may lag behind the master. For example in case of youtube video views, a request sent to the master vs a read replica might get a different view count. But this difference is temporary, and data replication will propagate through the cluster over time. This effect is called as Eventual Consistency. Cassandra extends the concept of eventual consistency by offering `tunable consistency`.

Go To [[14 Data Modeling - How we store the data]]