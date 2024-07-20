Always it is recommended to work from left to right in the request lifecycle ie. from the client to the backend servers and other services.

### High level design

#### Components

- ***Client***
- ***ALB** :* With round robin routing algorithm - since all our servers are going to be stateless, we opt for the round robin technique and we don't have the need for sticky sessions for now ( if we have a need for sticky sessions, we can use routing based on IP address by using a hashing based algorithm )
- ***API Gateway**:* Since we are going to opt for a microservice based architecture, we prefer the API gateway as this can help us route traffic to the appropriate service based on the request url or other parameters

----------------------------------

Now we have hit a point where the design now becomes custom to this use case, the components defined above, are common for 90% of the system design processes, subsequent  parts need focus on the Functional Requirements to begin with.

Refer: [[01 Functional Requirement]]

#### Components required to suit the functional requirements:

All below services are HS (Horizontally scaled)
- Tweet CRUD service 
- Reply CRUD service
- Search Service
- Timeline service
- User Account CRUD service
- Auth Service

![[Screenshot 2024-07-13 at 7.59.04 PM.png]]