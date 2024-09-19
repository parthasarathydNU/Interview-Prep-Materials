- Treats requests as objects.
- Performs multiple internal request as needed and necessary to form the requested object
- Much more control around the data that we fetch - only necessary data


### CONS:
- More complexity and overhead in terms of setting up the GraphQL API server that has the logic to  breakdown and perform the calls internally
- Caching is more challenging, because of the dynamic nature of the queries

This complexity is the price that we can pay for a more fine tuned response


