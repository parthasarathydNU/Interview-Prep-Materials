### How do Indexes use memory ? 

As indexes are accessed , data is loaded into memory, say we have a memory of 100GB, and each index has 20GB of memory,, and say we load 5 indexes into memory because some query required data that had to do with that particular index, then when we need to load in more data, what the database program does is that, it takes the oldest pages that are in memory and sends it back to disk and then pulls in new data from disk back to memory. This way memory is managed by the database program. 

We want to have as much relevant data in memory as possible as reading from memory is fast but reading from disk is relatively slow. 

### Cycling data issue

If our indexes are poorly designed, and we keep querying for data, we are going to be pulling data into memory and then pushing it back to disk repeatedly this leads to performance overheads and sometimes having such poorly designed indexes might hurt the system more than help it.

### Statistics

Every index will get a statistic behind them. SQL Server samples the data in the table and creates a histogram. Statistics is what a SQL server uses when creating an execution plan for executing a query and returning the data to the user. **However, there are some problems with this as well**

#### Problems with Statistics
- Statistics get created when we create an index or rebuild it.- it will get refreshed immediately.
- When we hit a threshold, that is around 10% of data that has changed SQL server will automatically rebuild your statistics
- Between those two points, SQL server does not have information about how data is distributed in your index. This is accentuated by the **Ascending Key Problem**

### Ascending Key Problem

When we have auto incrementing keys or strictly ascending keys, there will be a point when the statistics stop getting updated and a point where they get refreshed. 

In between those points, any new data that has been inserted, SQL server will not be able to figure out what is the best path to reach that data because it has not been reflected in the statistic. 

So it is important to keep monitoring the maintenance part of the SQL database and ensure the statistics are updated every once often so that this issue does not arise.
