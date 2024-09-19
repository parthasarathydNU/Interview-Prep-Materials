These are always "Non clustered" indexes.  On the creation of the index, we can add a where clause. For example, we have a database with information about `Orders` and we are constantly querying for `Open` orders. So what we can do in this case, is that, we can create a `Non clustered Filtered Index` on the `Orders` table for entries `WHERE`, `orderStatus` is not closed. 

Now instead of containing all the rows in the underlying table, this non clustered filtered index will only contain rows that have the relevant data, this can be useful for reducing the amount of data that the query searches through in order to make the queries more efficient. 

### Catches

This cannot work by using variables, for example, we can't create a filtered non clustered index using a filter that says index all rows with `orderPrice > 10000`. This won't work.

You can only do it on explicit values. 

Further we can add filtering on to the index using a WHERE Clause so that way we can created filtered indexes with additional checks. Have a look at the following example. 

![[FilteredIndexes.png]]
