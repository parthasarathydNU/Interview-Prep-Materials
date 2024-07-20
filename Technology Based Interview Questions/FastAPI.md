
https://interviewprep.org/fastapi-interview-questions/

Is a web framework for building APIs with Pythin 3.6 +.  It is designed to be easy to use, and also provides automatic interactive API documentation which can significantly streamline the development process. 

### Differences between Fast API and Flask: 
- Fast api is built on Pydantic for Data validation
- Automatically generates API documentation using OpenAPI and JSON Schema standards
- This makes it easier to test and debug API during development

### Role of Pydantic in FastAPI
- Provides data validation using python type annotations that ensure that the incoming data matches the expected types
- This defines how requests and responses should be typed, that enables automatic request body parsing, validation, serialization and documentation

### How would you implement authentication and authorization in FastAPI : 
- FastAPI provides a security module to implement authentication and authorization
- This can be added to the api definition as dependencies, where we pass in a function to fetch user infromation and define the scopes against which this user's access is checked. 
- This is wrapped inside the `Security` module

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.detail}"},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
```
### Disadvantages of Fast API
- Relatively new
- Smaller community, compared to Flask and Django
- Highly agile and small learning curve making it suitable for smaller projects and quick prototyping

### Error Handling and custom error responses in Fast API
- We can use the HTTPException module from the fastapi library
- We can then pass this as the exception handler class to fast API
- Within every api call, we can raise a HTTP exception with the `status_code` and `detail` which is returned back to the client

### How to handle file uploads in FastAPI ?
- FastAPI provides a simple way to handle file uploads using the `File` and `UploadFile` classes.
- We define the API end point function handler to take in an object of type `UploadFile` which is treated as the `form data` parameter

### How does Starlette and Pydantic work together in FastAPI ?
- FastAPI uses Starlette for web routing and Pydantic for data validation and serialization.
- When a request data is made, Starlette handles the HTTP specifics, such as path operations, request/responses. And also provides the async capabilities. Pydantic comes into the picture for validating the incoming JSON, ensuring type correctness and serializes data into Python Types that can be used in your application. 

### How to add rate limiting to your end points in FastAPI
- To use this , we can import Limiter and _rate_limit_exceeded_handler_ from `slowapi` which is another open source library
- Further using the get_remote_address utility function, we can create a limiter object and pass that as a `Dependency` to the end point handler that we want to rate limit

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/home", dependencies=[Depends(limiter.limit("5/minute"))])
async def home(request: Request):
    return {"Hello": "World"}
```

### Setting up Unit tests 
- Install pytest and requests library
- Create a test file and import the app, pytest and FastAPI's test Client
- Instantiate the TestClient with the FastAPI app as an argument
- This client will be used to simulate API requests to the API
- For each end point, write a function that simulates a request to it and check the response
- Use pytest's assert statements to verify the status codes, headers and body of the response 
- Isolate all tests by mocking dependencies
- Pytest fixtures can help you manage setup and teardown

### BackgroundTasks in fastapi
- This lets us

To continue from question 14//...
https://interviewprep.org/fastapi-interview-questions/