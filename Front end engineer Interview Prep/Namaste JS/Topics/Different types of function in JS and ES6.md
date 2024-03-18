
1. Function statement
2. Function Declaration
3. Function Expression
4. Anonymous functions
5. Named function expressions 
6. Params and Arguments

Let's see the first 3 items in action below `ris:ArrowDown`

```js
// Function Statement - this way of creating a function 
// This is hoisted right away
// AKA Function Declaration 
function a(){
	console.log("a");
}

// Function Expression - assigning a function to a variable
// this is not hoisted until the execution crosses this line
var b = function(){
	console.log("b");
}
```

What is the difference between a function statement and a function expression ? 

The major difference is hoisting! Function a is available to run right at the beginning, but the function b is only available to run after it is assigned as the value of `var b`.


4. Anonymous function
	
	What is an anonymous function, it is a function that does not have a name assigned to it. This is used in function expressions. 

```js

var b = function (){...} // here the right hand side of the equation is an anonymous function

// Anonymous functions cannot be written by themselves
// the following will throw an error
function(){
	// code block
}

```

5. Named function expression

	It is like a function expression but instead of an anonymous function on the right hand side of the equation, we use a named function .
	
	The main fact to note here is that, scope of xyz is local within the function itself.  And it cannot be accessed anywhere in the scope of `b` .
```js
var b = function xyz(){ console.log(xyz) }
```


6. Params and Arguments
   
   The values that we call the function with are called arguments, the values with which we defined the function, they are called function parameters. 

7. First class functions
	Instead of values, we can also pass functions inside functions as an argument - so since they behave just like variables in this case, we call them first class functions in JS.
	Functions can also be returned from functions as return values. 

ES6 - Introduced in 2015

Let, const and arrow functions were introduced as part of ES6
