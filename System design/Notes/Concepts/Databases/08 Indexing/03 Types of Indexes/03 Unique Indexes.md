This is an addition on top of the clustered / non clustered index. Along with considering a column / group of columns as the index, it will also add a constraint on the columns that are marked as unique in this unique (clustered/non clustered) index.

-------------> Read the above line slowly and carefully again <--------

I want to select this column or this group of column to be unique. For example say we had employeeId, Name and Salary. Here `employeeId` has to be unique, so we can create a unique index on `employeeId`.

Whenever someone tries to insert a duplicate value into that, it will throw an error. And because there is errors, we have to inform the developer teams about this.

If we create a unique constraint on a clustered index, then we create a primary key for the table. 

For a non clustered index, similarly when we do a creation script, we can just add a `Unique` constraint to the non clustered index creation. 

# Questions and Answers

### When we have a key on a table that has a unique constraint by default, will an index created on top of that key by default have the unique constraint as well ?

1. Keys with Unique Constraints:
    - When a key (like a primary key or a unique key) has a unique constraint, an index is typically created automatically to enforce this uniqueness.
    - This automatically created index will be unique.
2. Creating Additional Indexes:
    - If you create an additional index on a key that already has a unique constraint, by default, this new index will also be unique.
    - This is because the database system recognizes that the underlying data must be unique due to the existing constraint.
3. Explicit Index Creation:
    - However, if you explicitly create a new index and specify it as non-unique, even on a key with a unique constraint, most database systems will allow this.
    - But keep in mind, creating a non-unique index on a unique key is usually not beneficial, as the unique index already provides the necessary functionality.
4. Uniqueness Enforcement:
    - The uniqueness of an index is primarily determined by how it's created, not just by the underlying key's properties.
    - You can create a unique index on columns that don't have a unique constraint, which will then enforce uniqueness.
5. Database-Specific Behavior:
    - The exact behavior can vary slightly between different database management systems.
    - For example, in SQL Server, creating an index on a primary key column without specifying uniqueness will create a unique index by default.
6. Best Practices:
    - It's generally best to let the database system handle index creation for keys with unique constraints.
    - If you need additional indexes for performance reasons, consider carefully whether they need to be unique or non-unique based on your specific requirements.

In summary, when you have a key with a unique constraint, any index created on that key will typically be unique by default, unless you explicitly specify otherwise. The uniqueness of the constraint is usually reflected in the associated indexes, but you have the flexibility to create additional indexes with different properties if needed for specific performance optimizations.

### How does the system work if we create a unique index on a database column that does not have a unique constraint ? Does it now get added to the database column as well ? That feels odd

1. Unique Index vs. Unique Constraint: When you create a unique index on a column that doesn't have a unique constraint, you're essentially adding a uniqueness enforcement mechanism without altering the table's defined constraints.
2. Effect on the Column: Creating a unique index does not automatically add a unique constraint to the column itself. The column's definition in the table structure remains unchanged.
3. Enforcement Mechanism: The uniqueness is enforced by the index structure, not by the column properties. This might seem odd, but it's a feature of how database systems implement certain integrity rules.
4. Practical Impact:
    - The system will prevent duplicate values in the indexed column(s), just as if there was a unique constraint.
    - However, from a metadata perspective, the column is not marked as having a unique constraint.
5. Differences from a Unique Constraint:
    - A unique constraint is part of the table's definition and is typically enforced by creating a unique index behind the scenes.
    - A unique index created directly is just an index with uniqueness properties.
6. Behavior with NULL values:
    - A unique index typically allows multiple NULL values, whereas a unique constraint usually treats NULL values as distinct.
    - This behavior can vary between different database management systems.
7. Performance Considerations:
    - Both methods (unique constraint and unique index) typically have similar performance characteristics for enforcing uniqueness.
8. Use Cases:
    - Creating a unique index without a constraint can be useful when you want to ensure uniqueness for query optimization purposes without changing the table's logical structure.
    - It's also sometimes used as a workaround in scenarios where adding a constraint might be more disruptive to existing applications.
9. Database Integrity:
    - While the unique index enforces uniqueness at the data level, it doesn't provide the same level of declarative integrity as a unique constraint from a database design perspective.

In essence, creating a unique index on a column without a unique constraint is a valid operation that enforces uniqueness through the index mechanism rather than through the table's constraint definitions. This approach provides flexibility in how you manage data integrity and optimize query performance, but it's important to understand the subtle differences in how it's implemented compared to a true unique constraint.

### So now once we implement the unique constraint at the index level, will system interacting with the database now have to handle this particular column as unique even though initially it was not marked as unique and the systems were allowing duplicates

Once you implement the unique index, the system's behavior regarding that column will indeed change, even though the table schema itself hasn't been altered. Let's break this down:

1. Change in Data Integrity:
   - The system will now enforce uniqueness for the Email column at the database level.
   - Any attempt to insert or update a record with a duplicate email will fail, regardless of how the application is designed.

2. Error Handling:
   - Systems interacting with the database will now encounter errors when trying to insert or update records with duplicate emails.
   - If these systems weren't designed to handle such errors (because duplicates were previously allowed), they might fail in unexpected ways.

3. Application Impact:
   - Existing applications that were built with the assumption that duplicate emails are allowed will need to be updated.
   - This could involve adding error handling, updating user interfaces, and modifying business logic.

4. Data Retrieval:
   - Queries that relied on the possibility of multiple records with the same email might now behave differently.

5. Performance Considerations:
   - While not directly related to uniqueness, the new index will affect the performance of queries involving the Email column, usually improving read performance but potentially impacting write performance.

6. Backward Compatibility:
   - The database will enforce this new rule, but old versions of applications might not be aware of it, leading to potential issues.

7. API Contracts:
   - If you have APIs that interact with this table, their contracts might implicitly change, as operations that were previously successful could now fail.

8. Data Migration and Cleanup:
   - Existing duplicate data won't be automatically resolved. You'll need to handle this separately.

9. Testing Requirements:
   - All systems and processes that interact with this table will need to be thoroughly tested to ensure they can handle the new uniqueness requirement.

This situation highlights why adding a unique index to an existing column can be a significant change, even if it's not reflected in the table schema. It's a perfect example of why database changes, even seemingly minor ones like adding an index, can have far-reaching implications in a complex system.

To manage this change effectively, you would typically:

1. Communicate the change to all stakeholders and development teams.
2. Update application code to handle potential uniqueness violations.
3. Implement a grace period where violations are logged but not enforced, if possible.
4. Gradually roll out the change, possibly using feature flags or phased deployment.
5. Have a rollback plan in case of unexpected issues.

This scenario underscores the importance of carefully considering the full impact of database changes, even when they don't involve altering the table schema directly.