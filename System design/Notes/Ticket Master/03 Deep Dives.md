Reference non functional requirements: 

- High availability for searching and viewing events
- Low Latency Search  `ris:Check`
- Read Write Ratio ?: More reads than writes
- Scalable such that it can handle surges during popular events

### Low Latency Search

The first thing that comes to mind while thinking about Low Latency Search is Elastic Search. This indexes the 

The first thing that comes to mind with enabling low latency search is using Elastic Search. This converts the entities ( documents ) into indexes and enables us to quickly search information across multiple keys. This also enables features like `faceted search and filtering`
![[Screenshot 2024-07-19 at 10.40.31 PM.png]]

Additionally, Redis can be placed in between the search service and elastic search to further boost search speed. 

Similarly Redis can be used for caching event information so that users who are viewing event data can quickly see the details.

Further a CDN can be used to cache responses at the API level. This might not work for all use cases - and only some queries can be cached. 

For example whether a seat is booked or not cannot be caches, as during the event booking time, seats can rapidly get reserved and un reserved. 

![[Screenshot 2024-07-19 at 10.48.18 PM.png]]

### Handling surges during popular events

Further to handle surges a virtual waiting queue can be implemented to handle surges for popular events. This can be configurable by the admin or programmatically enabled.

![[Screenshot 2024-07-19 at 10.50.40 PM.png]]

### Additional consideration

To further enhance user experience - a pub sub topic / Server Side Events / Web Socket connection can be set up to provide real time updates to users who are performing seat selection to show available / booked tickets. 

![[Screenshot 2024-07-19 at 10.53.19 PM.png]]