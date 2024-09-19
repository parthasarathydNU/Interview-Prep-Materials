The non clustered index serves to mitigate the issue introduced by having a clustered index.

By Introducing a non clustered index, the database program, creates a separate copy of the data that is sorted based on the non clustered index key that we have defined. 

So here the cost to pay is memory required to store this additional copy of data. However let's look at some of the advantage of this way of storing data, along with the primary non clustered index key, we can also provide several secondary index keys on which the data has to be sorted. 

Or we could provide additional keys that can show up along with the data but the database system need not sort the data by.

### Characteristics of Non Clustered Indexes
- Additional copies of the data
- Sorted in the order of the indexed columns
- Can include non sorted data
- Multiple per table allowed

### Data Read Statistics 

![[StatisticsForDataReads.png]]

Here we are trying to execute the query `SELECT DisplayName, Reputation from Users Where DisplayName = "John_Skeet`;

This is on a database running on a laptop with physically attached disk. 

On the left we see how the read performance fares vs on the right. 


| Without Supporting Index                                                                                                                                                                     | With Supporting Index                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| The database program had to load the data on to memory                                                                                                                                       | The Database program loads data into the memory                                                                             |
| Perform a linear scan                                                                                                                                                                        | This data structure holds the data in sorted order based on the provided index keys                                         |
| And then return the information that matched to the query                                                                                                                                    | The search performance is faster                                                                                            |
| Here we see that it did 86813 Reads - here each read refers to a single block in the disk storage and each block stores 8KB of data                                                          | Lesser documents have to be read through the process                                                                        |
| The time we see is 208ms - however, we need to notice that this was only because the data was available in a physically connected hard disk                                                  | Here the time taken drastically reduces to 0ms and only has read 3 pages of data in order to identify the right information |
| If it was through an attached network drive, we need to also add the time taken for the data to be downloaded from the database into memory and then perform the search and return the value |                                                                                                                             |
| For a Read Heavy System this is a potential drawback expecially in case of cloud settings where everything is saved across partitioned servers.                                              |                                                                                                                             |

# Questions:

### A clustered index is basically modifying the current copy of the data itself, while an unclustered index is making a copy and modifying that in the required order. Is this right ?

Clustered Index:
1. You're correct that a clustered index modifies the actual data storage of the table.
2. It determines the physical order of data rows in the table.
3. There can only be one clustered index per table because the data can only be sorted in one way.
4. The leaf nodes of a clustered index contain the actual data pages of the table.

Non-Clustered Index:
1. Your understanding is close. A non-clustered index doesn't make a full copy of the data, but it does create a separate structure.
2. It creates a structure that contains the indexed column(s) and a pointer (or row locator) back to the full data row.
3. You can have multiple non-clustered indexes on a table.
4. The leaf nodes of a non-clustered index contain the index key values and row pointers, not the actual data.

Key Differences:
1. Data Storage: Clustered index defines the table's data storage, while non-clustered creates a separate structure.
2. Quantity: One clustered index per table, multiple non-clustered indexes allowed.
3. Speed: Clustered index is often faster for range queries, while non-clustered can be faster for selective queries.
4. Size: Clustered doesn't require extra storage (besides the index pages), while non-clustered requires additional space for the index structure.

In practice:
- If the table has a clustered index, the non-clustered index uses the clustered index key as the row locator.
- If the table is a heap (no clustered index), the non-clustered index uses a row identifier (RID) to locate the full row.

Your intuition about the basic difference is sound – clustered affects the main data structure, while non-clustered creates an additional structure. This understanding is a good foundation for working with database indexing strategies.

### Can there be multiple columns on which data is ordered in a clustered index ?

A clustered index can indeed be created on multiple columns. This is known as a composite clustered index. Here's a more detailed explanation:

1. Composite Clustered Index:
   - A clustered index can be created on multiple columns, just like a composite key.
   - The data rows are physically ordered based on the combined values of these columns.

2. Column Order Matters:
   - The order of columns in the index definition is crucial.
   - Data is sorted first by the first column, then by the second within the first, and so on.

3. Example:
   If you have a clustered index on (LastName, FirstName), the data would be organized:
   - First, sorted alphabetically by LastName
   - Then, within each LastName, sorted by FirstName

4. Usage Scenario:
   - Commonly used when queries frequently filter or sort by multiple related columns.
   - For instance, in an Order table, you might create a clustered index on (CustomerID, OrderDate).

5. Limitations:
   - While you can have multiple columns in a clustered index, you still can have only one clustered index per table.
   - The total size of the indexed columns should be considered, as it affects performance.

6. Performance Implications:
   - Can greatly improve queries that use all or the leftmost subset of the indexed columns.
   - May not be as beneficial for queries that only use latter columns in the index.

7. Design Considerations:
   - Choose columns that provide a good balance of uniqueness and query support.
   - Consider the most common access patterns for the table.

8. SQL Example:
   ```sql
   CREATE CLUSTERED INDEX IX_Customer_Order
   ON Orders (CustomerID, OrderDate);
   ```

9. Relationship with Primary Key:
   - By default, the primary key of a table often becomes the clustered index.
   - If you define a different clustered index, the primary key will be a non-clustered index.

10. Impact on Non-Clustered Indexes:
    - Non-clustered indexes on a table with a composite clustered index will use the full clustered index key as their row pointer.

Understanding composite clustered indexes is crucial for database design and query optimization, especially in scenarios where data is frequently accessed based on multiple related criteria. It allows for more flexible and powerful indexing strategies, but it should be used judiciously, considering the specific needs of your database and application.