[YouTube Video](https://youtu.be/a-F45Jov0Ck?list=PLliXPok7Zonm0trweRA2UeSTTLVYiPzNG)
### Components
What are the components that we will have in a system like Uber or Ola: 
- Driver
- Cabs
- User
- Locations

Drivers and Cabs and we are going with the assumption that cabs and drivers have a one to one association with each other. 

The next important factor is the creation of a trip or a ride.

We have a rider who want to go from a source to destination uses the app to create a trip for themselves. 

With this assumption let's start building the app.

### Flow of the app

Now that we have all the different components, whats the first step ? 

User has said from where till where do they want to go .. so the first thing we need to do is ....

### Driver Matching - who is going to fulfill this particular trip

What are the different ways in which we can do driver matching ?
- the nearest driver
- the driver with highest rating
- the driver who. has done the least trip in last couple of hours
- or a combination of these conditions ? 

Now we have the user, we have the source and the destination and we also have a driver,, what do we do next ? 

### Pricing - how much should the user pay for this particular trip ? 

- Do we want to charge more for highly rated drivers ? 
- Do we want to charge highly rated customers less ? 
- Do we want to charge based on demand ? 
- Do we want to charge based on distance ? 
- Do we want to charge based on vehicle ? 
- Do we want to charge based on traffic ? 
- Do we want to charge based on time of the day ?
