
**HADOOP**

When we want to perform analytics on company wide data. Like how many orders do we have, which geographies are giving me more revenue, which are the most sort after items and other analysis like that, we will need  something like a Data Warehouse.

This is generally a large scale database, where we can dump all of the data and provide querying capabilities to serve all of the reports. These are generally not used for transactional systems, but are used for offline reporting.

If we have this kind of use case we can use Hadoop, where we can put in data from various transactional systems and then we can build a lot of systems on top of this datawarehouse that can provide us with reporting capabilities.

Transaction——>. Transactional Database (RDBMS) —-> Data Warehouse —> Reporting Systems

