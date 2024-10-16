In the [[Async await]] section we saw examples of the various orders in which resolved values from promises are returned. 

We observed two things, if the first promise takes longer to resolve, the value of the second promise is also available to be used after the first promise is resolved.

```sh
time1: 10005.67919921875 ms
Promise1 resolved!
Hello World

# this was reolved in 5 seconds but waited before getting printed
time2: 10006.114990234375 ms
Promise2 resolved!
Hello World
```

However if the earlier promise get's resolved earlier, it get's printed and the sub sequent promise is printed later:

```sh
# This was called first with a time out of 5 secs
time2: 5004.72607421875 ms
Promise2 resolved!
Hello World


# this was called second with a time out of 10 secs
time1: 10003.501953125 ms
Promise1 resolved!
Hello World
```


### Insights
- The JS engine has not frozen when this process happens 
- When we use the `await` key word, this does not mean the main thread is frozen - if this was the case, the browser would hang whenever we make API calls!

### So how does await work ?
Whenever the execution reaches the line which has await in it, the execution of the async function within which the await line is present, will get suspended and removed from the call stack. 

Once the api call is resolved, the code execution continues from inside the function after the await line.

### Fetch API

Like async functions, the `fetch` browser API returns a `Response object`

```js
let url = "https://api.github.com/users/parthasarathydNU";

async function fetchData(){
	const response = await fetch(url);
	const data = await response.json();
	console.log(data);
}

fetchData();
```

### When should we use async await and when should we use then/catch

Async - await is just a syntactical sugar over then and catch. 

Then, catch involves callbacks, and promise chaining, but by using async await, we eliminate promise chaining and have a cleaner code.