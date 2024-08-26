Functional
- put (key, value) 
- get (key)

Non - Functional

- Scalable ( scales out easily together with increasing number of requests and data )
- Highly Available ( Survives network/ hardware failures and is also available across network partitions) - This also ensures lesser cache misses and therefore lesser calls to the database and more information served from the cache
- Highly performant ( fast puts and gets ) 

High performance in possibly the number one requirement for the distributed cache because it is called on every requests. 

### TIP:
Thinking about functional requirements is easy, but it is hard to think about non functional requirements. 

For systems like a distributed cache, think about scalability, availability and performance. 

If persistence is important, then think about Durability as well.

### TIP: 

Remember the interviewer is your friend. Our goal is to provide as many positive data points as possible, and the interviewer’s goal is to collect as many positive data points as possible.

In Practice, we should start approaching any design problem with small and simple steps, and evolve it. This is a win-win situation. We show progress, ability to deal with ambiguity and simplify things. This will help the interviewer bring data points to the table and champion our case.