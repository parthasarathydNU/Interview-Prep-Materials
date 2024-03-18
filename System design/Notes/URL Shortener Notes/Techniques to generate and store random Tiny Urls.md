### 1. Check if exists and then put

In this technique, each worker node, when sent a request, generates a random tiny url.
It checks if there already exists a record for this key in the database, if not it adds one.

#### **Issue**: 
When we have multiple worker nodes doing this process, there could be a situation, where more than one worker thread happens to generate the same random tiny url which is not present in the DB for two different long urls. 

So when this happens, the second put request would over write the long url that was added by the first worker node in the DB. Therefore a stable production system will not incorporate this technique.

### 2. Put if absent

In this technique, instead of a normal put request, the put if absent method is used. 
-  This method is only supported in certain relational databases like MySQL and Oracle. 
- This method is only supported in databases that support the [[ACID Properties]]
- This cannot be used in no SQL databases because they might or might not support put if absent method

### 3. Put and get to check if the same

- In this technique, the worker thread, puts the long url for the generate tiny url as the key
- Then it does a get for the generated tiny url
- While the get value is not equal to the input long url, new tiny urls are generated
- This way collisions can be handled effectively and we can be sure that the system is stable

Drawback of this method is that, if in case the tiny url generation function is not that random, the worker thread will have to perform multiple get and put operations during the process. Selecting a good random function will usually keep this risk minimal.