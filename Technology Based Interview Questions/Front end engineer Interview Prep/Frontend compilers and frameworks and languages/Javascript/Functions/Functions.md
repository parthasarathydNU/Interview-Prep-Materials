```javascript
function functionName(parameters) {
	// function body
	//
	
	// if this returns anything
	return expression;
}
```

Calling a function 

```javascript
functionName(arguments);
```

We define a function with parameters but call them with arguments for each parameter.

### The arguments object

Inside a function we can access an object called `arguments` that represents the `named arguments` of that function.

The `arguments` object is an `ArrayLike` object. We can access the arguments, by index and it also has the `length` proprty.

### Function Hoisting

In js we can `use a function before declaring it`. 

```javascript
showMe(); // a hoisting example

function showMe(){
    console.log('an hoisting example');
}
```

How does this work ? 

When the execution context is created, the js engine first creates the memory of all the members in memory, and for funnctions, the content of the function is associated with the memory pointer that the function name holds. 

Unlike variables that only get assigned a memory location, for the function the value is also assigned that is referenced by the function name. 

So during the execution step, the function can be executed even if it is defined below in the javascript file. 

However there are somethings we need to be aware of : 

This works
```javascript
const apple = "Fruit"

functionName()

function functionName() {
    console.log(`apple is a ${apple}`)
}

// "apple is a Fruit"
```

This throws error
```js
functionName()

const apple = "Fruit"

function functionName() {
    console.log(`apple is a ${apple}`) // Error: `apple` is undefined
}
```

### Function Type

In js all `functions` are objects and they are instances of the `Function` type. 

Each function has two important properties `length` and `prototype`.

- The `length` property determines the number of named arguments specified in the function declaration.
- The `prototype` property references the actual function object.

```js
function add(x, y) {
    return x + y;
}
```

```js
console.log(add.prototype)

/**
1. constructor: ƒ add(x, y)
	1. arguments: null
	2. caller: null
	3. length: 2
	4. name: "add"
	5. prototype: {}
	6. [[FunctionLocation]]: VM9587:1
	7. [[Prototype]]: ƒ ()
	8. [[Scopes]]: Scopes[2]
2. [[Prototype]]: Object
*/
```


### Function Methods

A function object has three important methods: `apply`, `call` and `bind`

#### Apply and call methods

The apply and call methods, call a function with a given `this` value and `arguments`. 

The only difference is in the way we pass the arguments. 

Suppose we have two objects: 
```js
let cat = { type: 'Cat', sound: 'Meow' };
let dog = { type: 'Dog', sound: 'Woof' };
```

And we have a function that operates on a `this` object. 
```js
const say = function (message) {
  console.log(message);
  console.log(this.type + ' says ' + this.sound);
};
```

How can we use this function on one of the two objects that we have. We can use the `call` or the `apply` method to use this on any of the objects. 

Difference in the way we pass in the arguments.. 
- `call()` accepts arguments individually (comma-separated).
- `apply()` accepts arguments as an array or an array-like object.

Syntax
- `func.call(thisArg, arg1, arg2, ...)`
- `func.apply(thisArg, [arg1, arg2, ...])`

Compatibility with spread operator:
- In ES6+, the spread operator (`...`) can be used with `call()`, making it more versatile.


### Bind methods

The `bind()` method creates a new function instance whose `this` value is bound to the object you provide.

Suppose we have an object `car` that has the `start` method associated in it's prototype.

```js
let car = {
    speed: 5,
    start: function() {
        console.log('Start with ' + this.speed + ' km/h');
    }
};

```

We have another object called `aircraft` that does not have the start method but it has the speed property.

```js
let aircraft = {
    speed: 10,
    fly: function() {
        console.log('Flying');
    }
};
```

How do we create a function to start the aircraft, we need to do something about it. Here we can borrow the start function of the car and bind it to this aircraft object. 

`const taxiing = car.start.bind(aircraft);`

Here we have created a new function called `taxiing` which considers the `aircraft` object as the `this` object in it's `lexical environment`. 

```js
taxiing();
// Start with 10 km/h
```


#### Alternate

Another way to do this is dynamically use the `start()` method of the `car` by using the `aircraft` object as the this keyword. This is a temporary way to `borrow` the `start()` function.

`car.start.call(aircraft)`
`car.start.apply(aircraft)`

### Closure

A closure is a function that preserves the outer scope in it's inner scope. 

```js
function greeting(message) {
   return function(name){
        return message + ' ' + name;
   }
}
let sayHi = greeting('Hi');
let sayHello = greeting('Hello');

console.log(sayHi('John')); // Hi John
console.log(sayHello('John')); // Hello John
```

Here we see that the `greeting` function takes in a `message` parameters and binds it to the outer scope of the inner function that it returns. 

So in these two lines
```js
let sayHi = greeting('Hi');
let sayHello = greeting('Hello');
```

the `sayHi` variable is associated with a function that has `Hi` associated with the variable `message` in its outer scope  and 

`sayHello` points to a `function` that has `Hello` stored in the `memory` that is referenced by the `message` variable in it's outer scope

So when we call sayHi and sayHello , the value of `message` is still available. 

```js
console.log(sayHi('John')); // Hi John 
console.log(sayHello('John')); // Hello John
```

### Closures in a loop:

```js
for (var index = 1; index <= 3; index++) {
    setTimeout(function () {
        console.log('after ' + index + ' second(s):' + index);
    }, index * 1000);
}
```


What happens here : ? 

We have a globally scoped variable `var index`.

Each instance of the `anonymous` function inside the `setTimeout` refers to the `index` variable in it's outer scope. 

However since the `index` variable is a globally scoped variable, all instances of the anonymous function point to the same value referred by the `index` variable. 

So when each of these `queued` functions get executed they refer to the same index value .

```js
after 4 second(s):4
after 4 second(s):4
after 4 second(s):4
```

To resolve this we have two options. 

1. To use an Immediately invoked function expression
2. To use the let keyword to define the `index` variable

Using IIFE: 
```js
for (var index = 1; index <= 3; index++) { 
	(function (index) { 
		setTimeout(function () { 
			console.log('after ' + index + ' second(s):' + index); 
			}, index * 1000); 
		}
	)(index); 
}
```

Here the inner function 
```
function (index) {

}(index)
```

Is immediately invoked with the current value of `index` and this current value of `index` is associated to the outer scope of the `setTimeout` function call
```js
setTimeout(function () { 
	console.log('after ' + index + ' second(s):' + index); 
	}, index * 1000); 
}
```

Using the `let` keyword

```js
for (let index = 1; index <= 3; index++) {
    setTimeout(function () {
        console.log('after ' + index + ' second(s):' + index);
    }, index * 1000);
}
```

Here since we are using the `let` keyword... in each iteration of the loop a new `index`variable is created. 

This way we have no issues. 

```js
after 1 second(s):1
after 2 second(s):2
after 3 second(s):3
```

