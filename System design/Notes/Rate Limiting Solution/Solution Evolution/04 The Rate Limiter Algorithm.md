The simplest algorithm is called the Token Bucket Algorithm

Each bucket has three characteristics
- One each bucket is filled with tokens at a constant rate
- Each bucket has a maximum capacity of tokens that it can hold
- Every time a request comes, one token is assigned to that request and taken out of the bucket
- When a request arrives, if there are no tokens available in the bucket, then the request is rejected
![[Screenshot 2024-08-26 at 11.21.52 PM.png]]
![[Screenshot 2024-08-26 at 11.22.28 PM.png]]![[Screenshot 2024-08-26 at 11.22.37 PM.png]]

And the bucket is refueled at a constant rate.
![[Screenshot 2024-08-26 at 11.23.09 PM.png]]

GoTo [[05 Token Bucket Algorithm Code]]