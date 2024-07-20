Qualities of the System 
What qualities that the system needs to have to provide a good user experience: 

Users can again be external users, internal users

In this case, the users are the end customers and advertisers. 

For non functional requirements, it is a good to understand the scale of the system, try to get numbers here. 

These numbers influence our design - particularly around the concept of scalability.
#### Some Numbers
- 10M ads at any given time
- 10k ad clicks per second at peak

#### Ility statements
- Availability
- Scalability
- Latency
- Data Integrity
- Reliability
- Redundancy
- Idempotency
- Security
- Durability
- other characteristics that we need to list down here

Identify which of the above are uniquely relevant to this system, put them in the context of this system and quantify them when appropriate. 


### Non Functional Requirements for this system
- SCALABILITY to support a peak of 10_000 clicks per second - Data input
- LOW_LATENCY of queries < 1 s per query - for the advertisers who want to use the system - Data output
- FAULT_TOLERACE  and DATA_INTEGRITY - We don't want to lose clicks ( this influences how much advertisers pay us )
- As REAL_TIME as possible - so advertisers can know whats happening in real time
- IDEMPOTENCY of ad clicks - This goes towards SECURITY of the system

--- out of scope ---
- Spam Detection --- random clicks
- Filtering and demographic profiling not in built
- Conversion tracking - not inbuilt