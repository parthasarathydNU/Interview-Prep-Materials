There are 4 types of NoSQL Databases:
- Column
- Document
- Key Value 
- Graph

We chose Cassandra because:
- It is fault tollerant
- Scalable
- Both read and write throughput increases linearly as new machines are added
- It supports multi data center replication and works well with time series data

For a typical Sys Design interview, we need to know advantages and disadvantages and when to use what.

Each NoSQL Database uses a different architecture:
- Cassandra is a wide column database that supports Synchronous Masterless replication
- MongoDB which is a Document Database uses Leader Based Replication
- HBase which is another column oriented datastore, similar to Cassandra, uses Master-based replication

Go To [[16 Data Processing]]