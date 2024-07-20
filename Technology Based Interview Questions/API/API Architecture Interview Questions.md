https://blog.postman.com/api-design-interview-questions/

### Open API : 
Formerly known as Swagger is a machine readable and human friendly specification format that is used to define HTTP APIs. 
Relies on JSON Schema to describe the API's underlying data, methods and request / response types and codes. 

OpenAPI 3 is the newer version of Swagger 2 specification. 

Provides a bridge between API developers and the consumers of that API. 

It's a universal language for describing the API. 

Not suitable to other types of APIs such as a the RPC or SOAP APIs and other non HTTP based APIs. 

### API First design
Begin with first designing and developing the API so that it can act as a contract between the various software components allowing for seamless integration and collaboration

### What is REST ? 
REST is a set of guidelines or principles to follow for designing APIs

REST has the following principles
1. It is resource based
2. It has well defined methods that define the action on the resource
3. The APIs have to be stateless
4. Metadata about the resource has to be made available for various purposes such as content caching, detct transmission errors, negotiate the appropriate representation format and to perform authentitaction or access control

### What is a REST API ? 

REST stands for **Representational State Transfer** , is a **set of principles** for creating systems that can interact and share data over a network.

REST APIs are stateless, resource based and lever a set of HypterTextTransfer Protocol methods for client and server communication. 

#### Components of a HTTP Request: 

1. Method
2. URI - Uniform resource identifier example `/product/1234`
3. Request Headers: Contains metadata such as authentication, content type that is being expected, caching information, etags, tokens
4. Request Body: The payload that is sent to the API Service 

#### Components of a HTTP Response
1. Body
2. Response Headers
3. HTTP Status Code 1xx - informational, 2xx success, 3xx redirection, 4xx client side error, 5xx server side error

#### Ensuring consistent API design

1. Naming conventions
2. Endpoint structures
3. HTTP Methods
4. Response Formats
5. API Documentation explaining all the payload / query parameters

#### Pagination in API responses and how to design it ?

Helps clients retrieve and display large amounts of data in smaller chunks. 

- Cursor based pagination and index based pagination : Users can either provide the previous or next parameter to fetch previous or next result
- Or if users need to navigate to a certain page, using index based pagination can also help

### What are some disadvantages of RESTful APIs: 

1. There is a problem of overfetching or underfetching - along with the request and response headers, his leads to slow response times in case of lesser bandwidth network that is often the case in mobile devices or when many devices are using the same network bandwidth
2. There is too much overhead on the client side to know and maintain all the different end points, request and response structures for the various respources and this only grows as the software becomes increasingly complex
3. There is the problem of implementing API versioning, whenever there is any change in the response model or the end point structure

### How to handle a long running operation with a REST API

Long running processes are handled as Asynchronous REST API calls. The API server returns a token / identifier that denotes the progress / completion state of the API call through which the client can notify the user accordingly. 

These are oftentimes represented as progress bars or loaders on the UI

