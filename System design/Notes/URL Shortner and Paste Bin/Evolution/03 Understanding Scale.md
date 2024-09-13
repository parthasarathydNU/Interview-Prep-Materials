Making calculations helps us generally understand the scale of the system. 

Here we can ask the interviewer to help us understand the scale, how many users, how many requests that we will be getting per second for our system to handle.

### Requests Estimates

Say we have around `500 * 10^6` URLs per month to handle
- This comes down to close to `( 500 * 10^6 ) / 30 / 24 / 60 / 60 = 192.9012 / s`
- `200 URLs to process per second`

Similarly say we have a `100 : 1 read / write ratio`, we will have about `20,000` URLs to redirect per second

This will be difficult to pull of on a single instance system, so we will have to distribute the load especially the redirects.

### Storage Estimates

Refer [[Data Units Converstion]] under the Templates Folder 

- Total URLs to be stored over 5 Years 
	- `500 * 10^6  * 12 * 5 = 30 * 10^9 ( 30 Billion URLs )` to be stored in total
	- Say each url is around `500 bytes`
	- We need a storage of 30 * 10 ^ 9 * 500 = 15 * 10^12 bytes ( 15 TB )

How does this impact our design ? We need 15 TB space for 5 years. These days we have hard disks that can store more than 16 TB of data, so I don't think we will need super large servers to handle this scale of data storage. We should revisit this when it comes to cost estimation and the hardware that we want to select and also think about how we want to handle the data storage. Will we need a distributed data storage solution, or can we have a single database that all servers point to ? Let's explore that through this session ....

> Unless these numbers really determine the way the system's design changes, it is a waste of time to perform these calculations. Just a brief calculation that gives us an estimation of concurrent users and storage will suffice.

Go To [[04 System API]]