To handle billions of URLs, the database must be partitioned across multiple server so that the read becomes easy aw ell.
#### Range Based partitioning

**Approach** : Store URL in partitions based on the first letter of the hash key (eg: all keys starting with A falls in one partition, B in another)

**Issue :** Can lead to unbalanced partitions if some letters have significantly more URLs

#### Hash Based Partitioning: 

**Approach** : Use the hash of the key to determine partition stores the URL.

Example: Take a URL and pass it to another hashing function that maps it to a number.

This number can lie anywhere between 0 to 2 ^ 31 - 1 [Reference](https://stackoverflow.com/questions/3826704/why-has-the-int32-type-a-maximum-value-of-2%C2%B3%C2%B9-%E2%88%92-1)

Then when we create servers, we also place them somewhere on the hashing circle.. Refer to Consistent Hashing to learn about this.





