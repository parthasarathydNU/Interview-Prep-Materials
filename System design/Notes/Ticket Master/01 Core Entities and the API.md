We have this since this is a user facing system.

> Usually don't spend more than 2 minutes `ris:Timer` on the Core Entities. 

### Core Entities
- Event
- Venue
- Performer
- Ticket

### User Facing API
> The APIs that the client is going to make to satisfy the functional requirements
> 
> So build APIs to solve the functional requirements and return the core entitites

- Users should be able to book tickets
- Viewing an event
- Search for events

`GET /event?eventId='1234'` -> Event Object & Venue & Peformer & Tickets[ ]

`GET /search?term={term}&location={location}&type={type}..... -> Partial<Event>[]`

Booking a ticket
1. This will reserve the ticket for 10 minutes
	`POST /booking/reserve`
	```
	header: JWT | sessionToken
	body: {
		ticketId
	}
	```
	
2. This is sent after the user completes the payment and the confirmation is saved in the database
   ```
   PUT/PATCH /bocking/confirm
   heaeder: JWT | sessionToken
   body: {
	   ticketId,
	   paymentDetails
   }
	```

3. Unreserve a ticket - this happens when the booking did not happen when the timer ended after 10 minutes
	```
	PUT/PATCH /booking/unreserve
	body: {
	   ticketId
   }
	```

------------------------------------------------------------------

Usually we should reach here by the 15 minute `ris:Timer` mark
