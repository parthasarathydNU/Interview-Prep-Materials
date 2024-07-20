*Whats this system:*
Collects and aggregates data on Ad Clicks - when users click on ads, the data is collected and logged - then advertisers are shown metrics

When we start any interview for system design, the first step is to outline the functional and non functional requirements.

Functional Requirements are the features of the system - users can be customers, internal users, machines that use this system or just the APIs - what is the expectation for this system ?

Functional Requirements:
- Users click on an ad and get redirected to the advertisers website
- Advertisers can query clicks over time w/ 1 minute min granularity that our system is going to support ( details here )

In an interview it is often times useful to be on the same page with the interviewer - what are the things that are out of scope : 

--- out of scope ---
- Ad targeting and serving : decision of what ad shows up on the user's page
- Cross device tracking
- Integration with offline channels