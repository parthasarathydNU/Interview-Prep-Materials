https://blog.postman.com/api-design-interview-questions/

- **API Design:** - The process of making intentional decisions about how an API will allow different software component to interact and exchange data with one another. These decisions are captured in a specification format such as Open API, help ensure that the API is user friendly and able to meet both present and future needs. 
- **What is a REST API ? :** REST Stands for Representational State Transfer, is a set of principles for creating simple, scalable and flexible systems that can interact and share data over a network.
  
  Stateless, Resource Based and leverage a standardized set of HTTP methods for client and server communication.

### Parts of REST Architecture: 
1. Method: A standard verb that describes the acton being applied to the resource
2. Uniform Resource Identifier (URI): Identifies a resource on the server. A URL is also known as API End Point, can either be a relative or absolute path, can contain query parameters
3. Request Headers: Metadata about the request as k-v pairs
4. Request Body: Payload - ususally JSON/ XML that is sent to the server. 

### Components of a HTTP Response
1. HTTP Status Code : 100, 200, 300, 400, 500
2. Response HEADERS: Content Type, Server Details, Caching Directives, Auth Tokens, eTag, redirect links
3. Response body; Payload that the server sends in response to the request - Document, JSON, Bundled files, etc..

100 - informational response
200 - success responses
300 - redirect responses
400 - client side errors
500 - server side errors


### Why is versioning important in API design
- Versioning enables APIs to be updated and modified over time in a decoupled manner from the clients
- It enables backward compatibility and easier migration for API users to newer versions
- It allows for clearer communication about updates and documentation across the various versions

### Key Principles of good API design : 
- Clear and consistent naming conversion
- versioning
- helpful error codes, messages
- Using well defined data formats and request response structures
- Incremental improvements while meeting backward compatibility
- Resource based approach rather than action based approach

### Purpose of pagination in API and how to design it
- Pagination helps clients retrieve and display large amounts of data in smaller and manageable chunks
- This provides clients better control over data consumption
- This can be designed by defining the chunk size and offset value in the api call parameter - this is index based pagination - this gives clients better control over the data that is fetched
- The API can also be designed to have the next and previous key words to retrieve data

### Advantages of RESTful APIs : 
- Known for simplicity and scalability
- Map operations to resources using standard HTTP methods
- Encourages lose coupling between clients and servers
- Well established ecosystem of tools and libraries

### Disadvantages of RESTFul APIs:
- Need to create a new end point for every different type of resource
- Problem of over fetching / under fetching
- Higher overhead data along with each request - unsuitable for low bandwidth situations
- Not suitable for live connections

### How to handle long-running operations with REST API: 
- We break down the task into three phases
- Creating the task - trigger the task using a REST API call
- Polling for updates - fetch task completion percentage at a given cadence and check for completion
- Obtaining the final result - once completed, fetch the data associated with the completed task - this can either be through a separate API call or can be passed as a redirect as part of the last update poll

A better way to handle long running task would be to trigger the task and subscribe to a message queue that pushes a notification whenever a task is completed and the client can be informed

## Advanced

### What's the process of designing an API from scratch ?
- Define API's goals, scope and purpose - requirements of both developers and users
- Supported HTTP methods, specific data formats and system availability windows
- Create a programming interface that is clear, consistent, versatile, evolvable and user-friendly. 
- Decide capabilities that we want our API to have
- Define resource paths, and meaningful status codes
- Pay attention to fine grained modeling of input and output data

### Best Practices for RESTful API design
- Versioning
- Stateless
- Pagination
- Right Resource Names and right HTTP verb
- Input output types
- Standard response codes
- Make APIs cacheable

### Caching Best Practices
- Caching can improve API performance by minimizing redundant data requests and leveraging conditional requests.
- Using cache keys that specifically identify resources, using the right cache control headers, and choosing the cache expiration strategies that take data volatility into account are some of the most important caching best practices

### Ensuring security in API design, especially when handling sensitive data ?
- Leave out features / data that isn't absolutely necessary
- Use different API operations for sensitive and non sensitive data
- Avoid passing sensitive information through api query parameters, and always ensure sensitive API's are secured with authentication mechanisms and encryption for data in transit

## Other API design factors

### Rate Limiting: 