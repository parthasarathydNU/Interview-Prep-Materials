
A table can be stored either as a HEAP or with a `Clustered Index`.

### Heap
- Stored on disk in a non-sorted order
- Faster to insert data into
- Slower to read data from 

#### Unsorted Pros
Since data is stored in a non sorted order, while inserting data, it just finds the next available memory block and saves the data there. While this is fast and is an up side for write heavy systems, the read performance will be pretty slow. 

#### Unsorted Cons
Sine we don't know where each entry lies, while having to search for a particular piece of information, the program has to load all data into memory from the disk, do a linear scan of the data and return the one that matches the given conditions and checks. 

![[DataStoredWithIndexingAndWithout.png]]
### Clustered Index
- Stored on disk sorted in the order of the clusstered key
- Slower to insert data into 
- Faster to read data from

Here it works in the opposite way for read and write operations, while writing the data, the fact that we have to find the right block to store the data in is the time consuming factor since ordering of data has to be maintained. However while reading it is pretty fast, since the time to search for that particular block is very less since the system knows the sorting order.

