[YouTube](https://youtu.be/iGaRzxKsgNI) <--- Everything you need to know about Indexes

![blog.algomaster.io](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6ae9541-eeed-474f-9de2-2f2810a1ec18_1200x828.png)
### Understanding Indexes

- Indexes are structures in a database service that provide quick access to data within the database , similar to how an index in a book helps us to quickly navigate to a page
- Indexes `store a subset of the data in a table` enabling faster data retrieval

> If using MySQL Server all indexes will be stored in Memory when it needs to read data. We only have limited memory on the server, so it is crucial to be as strict with indexes as possible. 


### Types of Indexes
- [[01 Clustered Indexes]]
- [[02 Non Clustered Indexes]]
- [[03 Unique Indexes]]