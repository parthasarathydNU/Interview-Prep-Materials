Refer to Overview Of System Design / Evolution / [[07 Defining the Data Model]] for a precursor before defining the Data Model. There we discuss about concepts such as Normalization vs De normalization. That ultimately defines what data we store in the system. 

**Note :** It is also beneficial to understand the data flow before defining the data base schema. Aspects like system performance and how the data is consumed and by who and for what purpose also come into play to understand how and in what form we need to store the data in our system. 

Further refer to the following under Templates:
- [[Questions for selecting Databases]]
- [[Requirement_Gathering]]

----------------------------------------------------------
### Entities in the System

Here we go with a simple normalized approach where each entity is represented in a separate table. 

Let's refer to the APIs ( [[04 System API]] ) to decide what entities we will need to create in the database...

We will need
- Url Mapping Table that stores the short url and the long url along with the expiration epoch and metadata
- User Data Table
- Not sure if we want to store Raw Events in a database as it might grow exponentially in size, it is good to have raw events in a reliable store for a given period of time in case we want to re run aggregations but it can be purged after a set expiry time
- Url stats table that will store aggregated url stats over different time periods

![[UrlShortnerDataModel]]

Reading: [[06 Fact Tables vs Dimension Tables]]

Here we can ask the interviewer if we want to dig further in depth about how we will be modeling the data, what sort of Database that we want to go with and evaluate multiple options for the storage system.

Again it is wise to be prudent about time here:
- The basic requirement is to list down the data model
- Then start asking the interviewer questions about if they want to discuss further about, where we will be storing data, and about database selection
- Referring to [[Questions for selecting Databases]] will help here

Further, it is not like we are done with defining the database and data model after this point. As we evolve the system towards solving both the functional and non functional requirements, we might have to revisit this section to modify the data model / add / remove entities, and discuss how the database type influence the system's requirements.