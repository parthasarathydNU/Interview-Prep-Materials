### Higher order function

A function that takes a function as an argument or returns a function is known as a higher order function. 

```js
function x(){
	console.log("Hello")
}

// Higher order function
// X is the call back function
function y(x){

	// calling the call back function
	x();
}

y(x);

```


### Recreating the inner implementation of Array.map
```js

let radius = [2,4,6,8];

// we create a calculate function that takes in a logic to return the result

function area(radius){
 return Math.PI * radius * radius; 
}

Array.prototype.calculate = function(logic){
	// here `this` will refer to the array, 
	// since it is part of the array prototype
	let out = [];
	for(let elem of this){
		out.push(logic(elem));
	}
	return out;
}

// print the areas of all the circles
console.log(radius.calculate(area));

// this is similar to 
console.log(radius.map(area));

```


### Recreating the internal implementation of Array.reduce
```js

let radius = [1,1,1,1,1];

Array.prototype.newReduce = function(initialValue, reduceLogic){

	// this reffers to the array
	for(let elem of this){
		initialValue = reduceLogic(initialValue, elem);
	}
	
	return initialValue;

}

console.log(radius.newReduce(0, (a,b) => a+b));
console.log(radius.newReduce(1, (a,b) => a*b));
console.log(radius.newReduce(0, (a,b) => a-b));
console.log(radius.newReduce(0, (a,b) => Math.max(a,b)));


let users = [
    {firstName: "akshay", lastName: "saini", age: 26} , 
    { firstName: "donald", lastName: "trump", age: 75 },
    { firstName: "elon", lastName: "musk", age: 50 },
    { firstName: "deepika", lastName:"padukone", age: 26} 
];

// write a function to get the count of unique age values
// {26: 2, 75: 1, 50: 1}


// other way to implement reduce

let reduceFn = function(accumulator, currentValue){

    // accumulator will be an object in this case
    if(!accumulator[currentValue.age]){
        accumulator[currentValue.age] = 0;
    }

    accumulator[currentValue.age] ++;

    return accumulator;
    
}

let out = users.reduce(reduceFn, {});

console.log(out);


function lessThan30Reduce( accumulator, currentUser ){

    // here the current value will be a user
    // accumulator will be an array of elements
    if(currentUser.age < 30){
        accumulator.push(currentUser.firstName);
    }

    return accumulator;
    
}


let outLessThirtyName = users.reduce(lessThan30Reduce, []);

console.log(outLessThirtyName);

```