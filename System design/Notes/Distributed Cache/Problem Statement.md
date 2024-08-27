Design a distributed caching system.

Problem statement: https://www.youtube.com/watch?v=iuqZvajTOyA

Say we have a simple system where a client talks to a web service that fetches data from a DataStore. 

Problems with current approach: 
1. Sometimes calls to datastore can have latency issues
2. DataStore can go down, it would be good to still continue serving requests to the clients even though it isn’t up to date

![[Pasted image 20240826001335.png]]

Why do we need a Distributed Cache ? 
- The amount of data is too large to be stored in memory of a single machine
- And we will need to split the data and store it across several machines


Go to [[01 Local Cache Implementation]]
