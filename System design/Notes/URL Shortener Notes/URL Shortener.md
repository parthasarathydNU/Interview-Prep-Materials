https://www.youtube.com/watch?v=fMZMm_0ZhK4

#### Scope:
- Given a long url return a short url
- Given a short url return the original long url
#### Challenges: 
- Designing this at scale
#### Focus areas:
- Scalability
- Durability

1. How do we generate a tiny url which is unique? Actual url might be 100's of characters long, we have to generate a URL that will be 7 to 8 characters and be unique
2. How will you design the persistence layer? Where will you store the short URL and the long URL

![[Url Shortener High level Diagram]]

### High level approach

- The high level idea is that, the client communicates to the application via a load balancer.
- The load balancer delegates the task to the various available worker nodes
- These nodes generate the Unique short URL, store it in cache and also store it in persistence
- Now when the larger URL is requested back for the short URL, it is retrieved from persistence and sent back to the client.

[[Generating the tiny URL]]