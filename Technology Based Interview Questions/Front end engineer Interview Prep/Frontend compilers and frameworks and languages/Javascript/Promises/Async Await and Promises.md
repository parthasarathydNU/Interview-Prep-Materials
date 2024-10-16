Say we have a set of users and we have a get users and findUser functions

```js
function getUsers() {
  return [
    { username: 'john', email: 'john@test.com' },
    { username: 'jane', email: 'jane@test.com' },
  ];
}

function findUser(username) {
  const users = getUsers(); 
  const user = users.find((user) => user.username === username);
  return user;
}

console.log(findUser('john'));

```

The func user function is `synchronous` and `blocking`

In this case, the `getUsers()` function returned the user's data immediately, but in most cases, it will be a database call or a call to a third party system which might require some wait time before we can run the  next line. 

`const user = users.find((user) => user.username === username);`

#### Simulating the delay

To simulate the delay, let's add a 1 second delay before the users are returned

```js
function getUsers(){

	let users = [];

	setTimeout(() => {
		users = [
			{ username: 'john', email: 'john@test.com' },
		    { username: 'jane', email: 'jane@test.com' },
		]
	}, 1000);
	
	return users;

}
```

If this is the case, then we will receive an `[]` whenever we call the `getUsers` function. 

### How can we fix this.

One is through call backs as we studied earlier. 

We can perform each of these steps synchronously. 

```js

function getUsers(callback) {

	setTimeout(() => {
		callback(
			[
				{ username: 'john', email: 'john@test.com' }, 
				{ username: 'jane', email: 'jane@test.com' },
			]
		)
	}, 1000)

}


function findUser(userName, callback) {

	getUsers(
		(users) => {
	
			const user = users.find(user => user.username == userName)l
			callback(user);
		}
	)
}

findUser("john", console.log);
```

How does this work ? 

We call the `findUser` function and pass in the `userName` and `console.log` as the call back.
The `findUser` function calls the `getUsers` with an `anonymous` function as the `callback`
This `anonymous` function takes in a list of `users` and finds the `required` user and passes it to the `console.log` function as the callback

Inside the `getUsers` function, the `callback` that was passed to it (`the anonymouus`) function is called after 1 second with the list of `users`.

This makes the code difficult to follow and highly convoluted and leads to maintenance issues. 

To resolve this we use the concept of promises.

## Promises

A promise is an `object` that encapsulates the result of an `asynchronous` operation.

A promise object has a state that can be one of the following: 
- Pending
- Fulfilled with a `value`
- Rejected for a `reason`

In the beginning the state of a promise is `pending` indicating that an `asynchronous` operation is in `progress`. But later based on the result of the `asynchronous` operation, the state can either shift to `fulfilled` or `rejected`

### Creating a promise:

A promise object, takes in a function that takes two parameters, `resolve` and `reject` and a function body that defines the sequence of operations to be executed, typically an `asynchronous` operation.

```js
const promise = new Promise( (resolve, reject) => {

	// sequence of operations
	if(success){
		resolve(value)
	} else {
		reject(error)
	}
});
```

They keywords are `resolve` and `reject` by convention only. 

These are in turn functions that get executed based on either the `value` or the `error` message.

When a `new Promise` is created, it's state is `pending` then internally it moves to `resolved` or `rejected`

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promises.svg)

> We will rarely create promises in practice, instead we will consume promises provided by libraries. 


### Consuming a promise:

To get the `value` of a promise when it is fulfilled we can call the then method of the promise object. 

Internally whatever value is passed into the `resolve` method is received in the `then` method of the promise object.

We can do both of this in the `then` method of the promise itself. 

`promise.then(onResolved, onRejected);`

The onResolved takes in the value that is passed in to the `resolved` method within the promise
The onRejected takes in the value that was passed in to the `rejected` method within the promise body.

Example:
```javascript
function getUsers(){
	return new Promise((resolve, reject) => {

		setTimeout(() => {
			resolve([
				{ username: 'john', email: 'john@test.com' }, 
				{ username: 'jane', email: 'jane@test.com' },
			])
		}, 1000)
	})

}


const promise = getUsers();

const onFulfilledUsers(users){
	console.log(users);
}


// Here we pass the onFulfilledUsers as the resolve callback to the returned promise from the getUsers function.

promise.then(onFulfilledUsers)
```


Alternate:

```javascript

const promise = getUsers();

promise.then((users) => {
	console.log(users);
})
```

Alternate: 
```javascript

getUsers().then(console.log)

getUsers().then(console.log, console.error)

getUsers().then(console.log).catch(console.error)

```

## Promise chaining

### Multiple handlers for a given promise:

```javascript
let p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(10);
    }, 3 * 100);
});

p.then((result) => {
    console.log(result); // 10
    return result * 2;
})

p.then((result) => {
    console.log(result); // 10
    return result * 3;
})

p.then((result) => {
    console.log(result); // 10
    return result * 4;
});
```

![JavaScript Promise Chaining - multiple handlers](https://www.javascripttutorial.net/wp-content/uploads/2020/03/JavaScript-Promise-Chaining-multiple-handlers.png)


#### Chained

```javascript
function generateNumber(num) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(num);
    }, 3 * 1000);
  });
}

generateNumber(10)
  .then((result) => {
    console.log(result);
    return generateNumber(result * 2);
  })
  .then((result) => {
    console.log(result);
    return generateNumber(result * 3);
  })
  .then((result) => console.log(result));

```

Alternate
```javascript
step1()
    .then(result => step2(result))
    .then(result => step3(result))
    ...
```

Alternate
```js
step1()
    .then(step2)
    .then(step3)
    ...

```

## Promise.all()

The `Promise.all()` is a static method that returns a single promise that resolves when all the input promises have been resolved. The returned promise resolves to an array of the results of the input promise.

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise.all-Fulfilled-1.svg)

The `Promise.all()` waits for all input promises to resolve and returns an array the consists of the results of each input promise. 

If one of the input promise is rejected, the `Promise.all()` method immediately returns a promise that is `rejected` with an error of the first rejected promise. 

![JavaScript Promise.all Rejected](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise.all-Rejected.svg)

In the above diagram, we see that promise2 is rejected, and later promise1 get's fulfilled, however in the promise that is returned from the `Promise.all()` method, that promise get's `rejected` and we can handle that accordingly based on the `error` value received.

### Examples:

Here we have three promise objects: 

```javascript
const p1 = new Promise((resolve, reject) => { 
	setTimeout(() => { 
		console.log('The first promise has resolved'); 
		resolve(10); 
	}, 1 * 1000); 
}); 

const p2 = new Promise((resolve, reject) => { 
	setTimeout(() => { 
		console.log('The second promise has resolved'); 
		resolve(20); 
	}, 2 * 1000); 
}); 

const p3 = new Promise((resolve, reject) => { 
	setTimeout(() => { 
		console.log('The third promise has resolved'); 
		resolve(30); 
	}, 3 * 1000); 
});
```


Here we call all the promises in no particular order:

```javascript
Promise.all([p1, p2, p3])
.then(result => {
	const total = results.reduce((acc, curr) => acc + curr, 0);
	console.log(`Results: ${result}`);
	console.log(`'Total: ${total}`);
});

```

Result
```js
Promise {<pending>}
The first promise has resolved
The second promise has resolved
The third promise has resolved
Results: 10,20,30
Total: 60
```


**IMPORTANT NOTE**:

Here one important thing to note is that, though the order in which the promises are resolved does not depend on the order in which they were passed in to the `Promise.all()` method. The order in which the responses are returned depend on the order in which they were passed in to the `Promis.all()` method.

Have a look at the two results here: 
```js
Promise.all([p3, p2, p1])
...
...

// Result
Promise {<pending>}
The first promise has resolved
The second promise has resolved
The third promise has resolved
Results: 30,20,10                  <-----  This depends on the call order
Total: 60


======================================

Promise.all([p1, p2, p3])
		 ...
		 ...

// Result
...
The first promise has resolved
The second promise has resolved
The third promise has resolved
Results: 10,20,30                   <----- This depends on the call order
Total: 60
...
```

### Failing promises:

```js
const p1 = new Promise((resolve, reject) => {
    ...
    
const p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('The second promise has rejected');
        reject('Failed');
    }, 2 * 1000);
});

const p3 = new Promise((resolve, reject) => {
    ...
```

Here we have a situation where only the second promise `rejects`.. let's look at the response. 

```js
Promise.all([p1, p2, p3])
    .then(console.log) // never execute
    .catch(console.error);

// Promise {<pending>}
// The first promise has resolved
// The second promise has rejected
// Failed
// The third promise has resolved
```

If we look at the logs, we see that though we got the console log statements, we never go the `then` method to be called on the `Promise.all` object.

## Promise.race()

This method is like a do or die method.. It returns as soon as any one promise resolves or rejects. 

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise-Race-Fulfilled.svg)

Here `p1` got fulfilled first, so it immediately returns `v1` to the `then` method of the `Promise.race()` object.

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise-Race-Rejected.svg)

In the above one, `promise2` fails first so the `catch` method of `Promise.race()` is called with the error from `promise2`.

## Promise.any()

`Promise.any(iterable);` iterable is a list of Promise objects.

Whichever is the first promise that fulfills, the `Promise.any()` returns the value of the first fulfilled promise. 

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise.any-Fulfilled.svg)

Here `promise1` was fulfilled first, so the `Promise.any()` object returns `v1`.

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise.any-rejected.svg)

Here even though  promise 1 rejected, the `Promise.any()` returns v2 since that `fulfilled` first.

![](https://www.javascripttutorial.net/wp-content/uploads/2022/02/JavaScript-Promise.any-all-rejected.svg)

If everything rejects, we get a list of `errors` from each promise in the order it was called.
