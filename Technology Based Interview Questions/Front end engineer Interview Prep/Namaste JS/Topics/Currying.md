Function currying is a feature in javascript that helps us convert a function with multiple arguments into a nested function that takes in lesser number of arguments. 

Example: 
```js
function add(a, b, c) {
	return a + b + c;
}

// now if we were to call 
add(1, 2, 3) // we will get 6
```

If we were to implement currying, it will turn out this way
```js
function add(a, b, c) {
	return a + b + c;
}

function curry(func, ...args){
	return func(..._args, ...args);
}

// So now instead of calling add(1, 2, 3)
// we can do
const curryAdd10 = curry(add, 10); 

curryAdd10(20, 30); // 10 + 20 + 30 = 60
curryAdd10(50, 50); // 110
```

Similarly we can nest it to how many ever levels we want
Example:
```js
function curry(a){
	return function(b){
		return function (c) {
			return a + b + c;
		}
	}
}

// now to add sum of three numbers we can do 
curry(1)(2)(3) // this will return 6

// or 
const add10 = curry(10);

add10(20)(30); // this gives 60
add10(50)(50); // this gives 110
```

## Partial application
A curry is only when there is as many sub function as there are parameters, if there are lesser nesting than the number of parameters, it is partial application. 


## Using the bind method

Another way rather than using an explicit curry function is by using the bind method

Example: 
```js
function add(x, y){
	console.log(x+y);
}

// by using the bind method we can create a copy of the add function but with different parameters
const add10 = add.bind(this, 10);

// by doing this we are adding the parameter 10 as the default value of x
add10(100); // 110
add10(50); //60
```

This way we can create different variations of the same function with minimal code. 

This is made possible with the help of closures. 
