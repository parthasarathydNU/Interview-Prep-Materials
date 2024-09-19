The term "clustered" in database indexing refers to how the data is physically organized and stored on disk. Let's break down what it means for both clustered and non-clustered indexes:

Clustered Index:

1. Physical Order: In a clustered index, the actual data rows of the table are stored in the order of the index key.

2. Data Organization: The term "clustered" means that the data is grouped together (or clustered) based on the index key values.

3. Table Structure: A clustered index determines the physical structure of the table itself. The data pages are arranged in a B-tree structure based on the index key.

4. One Per Table: Because it defines the physical order of data, there can only be one clustered index per table.

5. Leaf Level: In a clustered index, the leaf level of the index is the data itself. There's no separate structure pointing to data rows.

Non-Clustered Index:

1. Separate Structure: A non-clustered index creates a separate structure from the actual data rows.

2. Logical Order: The term "non-clustered" means that this index doesn't determine the physical order of the data in the table.

3. Pointer Structure: It creates a structure where the leaf level contains the index key values and pointers to the actual data rows.

4. Multiple Per Table: You can have multiple non-clustered indexes on a single table.

5. Data Access: To retrieve full row data, the database engine first finds the key in the index, then uses the pointer to fetch the full row from the data pages.

The Key Difference:

- "Clustered" fundamentally refers to whether the index defines the physical storage order of the table data (clustered) or exists as a separate structure that points to the data (non-clustered).

In essence, "clustered" in this context means "grouped together" or "organized in a specific order." A clustered index clusters (organizes) the actual data rows according to the index key, while a non-clustered index doesn't affect the physical data storage but provides a separate, ordered structure for faster data retrieval.

Understanding this distinction is crucial for database design and query optimization, as it affects how data is stored, accessed, and maintained in the database system.