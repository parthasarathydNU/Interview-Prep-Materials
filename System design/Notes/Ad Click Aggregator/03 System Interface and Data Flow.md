Clearly outlining what data the system receives and the output

Input:
- Click data that is coming in from the user 
- Advertiser queries - comes in from advertisers

Output: 
- Redirection when users click on ads
- Click metrics when users query for it

Data Flow:  - This should meet all the functional requirements that was mentioned earlier
A simple linear list of the steps necessary to transform input to output
1. Click data comes into the system - FR
2. user is redirected - FR
3. validate the click data - handle the idempotency concern
4. log the raw click data
5. click data aggregated
6. Aggregated data queried by advertisers - FR