Suppose we are designing a system like Amazon, where sellers put a lot of information about product like images and videos. 

Similarly we could be building a system like Netflix and will have to store a lot of videos.

So wherever we have the requirement to store images / videos, we will use something called as a blob storage.  These are not really databases. Databases are meant for data that we can query on. A file is not something that we will query on but rather serve as is.

There are a lot of providers out there, but one of the most common ones and the fairly cheaper one is AmazonS3.

Along with S3, we generally use a Content Delivery Network. CDN helps bring data and cache it in data centers that are much closer to the client's locations geographically. 

