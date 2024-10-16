Call method is used to borrow functions from other objects and call the with a given context
Example: 
```js
const object1 = {
	name: "dhruv",
	lastName: "partha",
	printFullName: fucntion(){
		console.log(this.name + " " + this.lastName);
		}
	}

const object2 = {
	name: "Akshay",
	lastname: "Saini"
	}

// now instead of writing the print method again, we borrow it from the original object and call that method with a new context

object1.printFullName.call(object2); // Akshay Saini

```

## Cases with multiple arguments

If we were to do this with multiple arguments, and we use the call method, this is how it looks
```js
const print = function(hometown, state){
	console.log(`${this.name} ${this.lastName} ${hometown} ${state}`);
}

const obj1 = {
	name: "haha",
	lastName: "hihi"
}

const obj2 = { 
	name: 'hoho',
	lastName: "huhu"
}

print.call(obj1, "chennai", "TN"); 
// haha hihi chennai TN

print.call(obj2, "hyderabad", "AP");
// hoho huhu hyderabad AP

const obj3 = {
	name: "hehe",
	lastName: 'hulhul'
}
// using apply
print.apply(obj3, ["nagasaki", "pawan"])
// hehe hulhul nagasaki pawan
```

### The only difference with `call` and `apply` is that in case the input is an `array`, we use the `apply` method

## `Bind`

While apply and call invoke the functions,  the `bind` method just saves the context and returns a copy of the method which can be invoked later. 


## Polyfill for bind
```js
// In this snippet, we will be implementing our own implementation of the bind method in js

// how bind works

const obj = {
    firstName: "Dhruv",
    lastName: "Parthasarathy"
}

function printDetails(state, country){
    console.log(
        `${this.firstName} ${this.lastName} ${state} ${country}`
    )
}

// now if we call the function with the obj, it should print my first and last name
// const printMyDetails = printDetails.bind(obj, "TN", "India");
// printMyDetails();

// now let's implement another method that acts just like the bind method

//1. first it should return a function
//2. when that function is called, 
// it should invoke the function it is bound to with the given context
// 3. it should be available in the function prototype

Function.prototype.myBind = function (obj, ...args){
    const func = this;
    return function(..._args){
        return func.apply(obj, [...args, ..._args]);
    }
}

const newFunction = printDetails.myBind(obj, "TN");
newFunction("India");
```
