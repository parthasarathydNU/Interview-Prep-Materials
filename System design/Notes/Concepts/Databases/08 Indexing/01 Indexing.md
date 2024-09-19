[YouTube Video](https://youtu.be/lYh6LrSIDvY)

Let's say we have an employess table in your database and we want to find the employee by name `SELECT * FROM emmployees WHERE name = 'Felix' ` : ![[ExampleEmployeeData.png]]

Let's talk about how the `database program` get's this data under the hood.

In the actual database, the actual records are stored in blocks. And each block has a fixed amount of storage for example `8KB`.

In this example, let's say each block can store 2 records. 

### Data Stored in Disk as blocks

| Block | 0      | 1      |
| ----- | ------ | ------ |
| 0     | Ed     | Kevin  |
| 1     | Sam    | Julia  |
| 2     | Amanda | Lalith |
| 3     | Todd   | Fellix |

So what the process looks like, is now that each block as a specific number of records associated with it, the database program takes all these blocks and loads it up into memory and sequentially checks each block for the required record...

### Data gets loaded into Memory - Full Table Scan

Now the program traverses all the records and checks if any record's value matches the condition and then returns the record. This is an O(n) operation.

![[FullTableScan.png]]

### What if we had billions of records ? A full table scan for every query is going to be very very slow - how can we handle this ? 

## Indexes

We add indexes to `specific columns` in our database. Say in this example, we add an index to the `name column`. It creates a separate data structure for this purpose based on the values in the `name` column.

![[IndexDataStructure.png]]

Here on the right we see that we only have the names, we don't have Salary, we don't have ID, we just have the index based on name that tells us which block and which index within the block does this name lie in.

> Further the rows are also `sorted in ascending order` based on the value in the `name column`.

### How does this help ? 

The most famous data structure for this use case is the `B-Tree`. 

Now since the data is sorted on the order based on the values in this column, search becomes faster. 

Now we can perform a Binary Search and quickly retrieve the block and the index of the associated data.

Here we are halfing the data to be searched after each iteration. This brings down the time complexity from O(n) to O(logN).

## Drawbacks: 

### Cost and storage considerations
Even thought these help us find data faster, we also need to use up memory to store the data in the given order in the index, so that needs to be considered as well. So unless the reduction in the cost due to indexing is significanly higher than the cost of storing this extra data to maintain the indexes, it is. unwise to implement this in a production application.

### Indexing is itself a time consuming process

Indexing can lead to performance hits. Say suppose we are writing data a lot, then we will have to update the main table and also update the index to accurately reflect this change. So indexing only makes sense when the read percentage is significantly higher than the right percentage. 


