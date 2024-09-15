Whichever system we are designing during an interview, we will be using some sort of caching solution there. 

There are a lot of use cases for caching
- If we are regularly querying a database and we don't want to do repeated queries, we can use a cache
- If we are querying a remote service and that has a high enough latency, we can use a cache to store the response locally at out end

Generally how the cache stores data is in key value pairs. 

Keys are normally the `where clauses in a SQL query` and what are the `query params that we use when make an API call` and the values are the response values that we expect when we make a request to the system.

#### Commonly used solutions
- Redis
- Memchached

Go To [[02 File (Blob) Storage Options]]