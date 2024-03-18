Async function are functions that return a promise. 
If inside the function we don't return a promise but a value, the async function wraps that value inside a promise and sends it back to the client.

```js
async function hello(){
	return "Hello World";
}

// here result object will be a promise
const resultPromise = hello(); 

console.log(resultPromise);

//Hello world
resultPromise.then((data) => console.log(data)); 
```

![[Pasted image 20231014142831.png]]

### Another way of defining a promise
```js


let flag = true;

async function returnPromise(){
    
    const promise = new Promise((resolve, reject) => {
        flag 
        ? resolve("Hello World") 
        : reject("Rejected hello world");
    });

    return promise;
}

const returnedPromise = returnPromise();

returnedPromise
.then(result => console.log(result))
.catch(err => console.log(err));
```

### Handling promises using async await

- `await` is a keyword that can only be used inside Async Functions
- `await` is used in front of a promise and only resolves a promise, 
- As compared to the `promise.then` method, using the `await` keyword, holds the execution until the promise is resolved. 

```js
const flag = false;
const promise = new Promise((resolve, reject) => {
	flag 
	? resolve("Hello World") 
	: reject("Rejected hello world");
});

**async** function promiseHandler(){
    try{
        const response = **await** promise;
        // the program execution is halted until the promise is resolved and the resopnse is received
        console.log("Promise resolved! ", response);
    }
    catch(err){
        console.log("Promise rejected :( ", err);
    }

}

promiseHandler();
```

### Curious case of promise resolving

When we have multiple promises, we see that both the promises get resolved in the same time!!

Case 1:
```js
console.time("time1");
console.time("time2");


const flag = true;
const promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        	flag 
        	? resolve("Hello World") 
        	: reject("Rejected hello world");
    }, 10000)
});

const promise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        	flag 
        	? resolve("Hello World") 
        	: reject("Rejected hello world");
    }, 5000)
});


async function promiseHandler(){
    try{
        const response1 = await promise1;
        console.timeEnd("time1");
        console.log("Promise1 resolved!");
    	console.log(response1);


        const response2 = await promise2;
        console.timeEnd("time2");
        console.log("Promise2 resolved!");
    	console.log(response2);
        
        
    }
    catch(err){
        console.log("Promise rejected :(");
        console.log(err);
    }

}

promiseHandler();
```

```sh
time1: 10005.67919921875 ms
Promise1 resolved!
Hello World
time2: 10006.114990234375 ms
Promise2 resolved!
Hello World
```


Case 2: 
When the first promise gets resolved in 5 seconds but the second promise get's resolved in 10 seconds: 

We see that the second promise was also returned 10 seconds from t0, but the promise that took only 5 seconds returned first since it was called first.
```sh
time2: 5004.72607421875 ms
Promise2 resolved!
Hello World


time1: 10003.501953125 ms
Promise1 resolved!
Hello World
```

[[Follow to Promise Handling in JS for deeper insights]]