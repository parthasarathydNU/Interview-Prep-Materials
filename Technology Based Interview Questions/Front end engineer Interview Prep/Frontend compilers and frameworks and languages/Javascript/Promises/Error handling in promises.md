
### Throwing errors outside the promise

```js
function getUserById(id) {
    if (typeof id !== 'number' || id <= 0) {
        throw new Error('Invalid id argument');
    }

    return new Promise((resolve, reject) => {
        resolve({
            id: id,
            username: 'admin'
        });
    });
}


getUserById('a')
    .then(user => console.log(user.username))
    .catch(err => console.log(`Caught by .catch ${err}`));

```

Here we throw an error in the function and also return a promise at the end. 

For the promise call, we have a try and a catch. But if we have it this way, the error that is thrown inside the function is not caught, because only the values passed into the `reject` gets called in the catch.

```js
Uncaught Error: Invalid id argument at getUserById (PromiseErrorHandling:3:15) at PromiseErrorHandling:15:1
```

### Throwing error inside the promise
However if we update the function to call rejects inside the promise, we can catch it using the `.catch` method.

```js
function getUserById(id) {
    
    return new Promise((resolve, reject) => {

        if (typeof id !== 'number' || id <= 0) {
            reject(Error('Invalid id argument'));    <----------
        }
        
        resolve({
            id: id,
            username: 'admin'
        });
    });
}

getUserById('a')
    .then(user => console.log(user.username))
    .catch(err => console.log(`Caught by .catch ${err}`));     <---------

// Caught by .catch Error: Invalid id argument
// VM23992 PromiseErrorHandling:1 Promise {<fulfilled>: undefined}
```


### Handling errors outside promises

```js
function getUserById(id) {
    if (typeof id !== 'number' || id <= 0) {
        throw new Error('Invalid id argument');
    }

    return new Promise((resolve, reject) => {
        resolve({
            id: id,
            username: 'admin'
        });
    });
}


try{
	getUserById('a')
	    .then(user => console.log(user.username))
	    .catch(err => console.log(`Caught by .catch ${err}`));
} catch(error){
	console.log(`Error missed by promise catch but caught by outer try/catch, ${error}`);
}

// Error missed by promise catch but caught by outer try/catch, Error: Invalid id argument
```
