Create an array of given size using the `Array(size)` method.

Get the length of the array using the `length` property.

`Mutator methods that modify the original array`
- `push(elem)` to add element to the end of an array
- `unshift(elem)` to add element to beginning of the array
- `pop()` to remove an element from the end of the array
- `shift()` to remove element from beginning of the array
- `splice()` // Changes contents by removing/replacing elements
- `sort()` // Sorts the elements 
- `reverse()` // Reverses the order of elements

Accessor methods - Do not modify the original array

- `indexOf(elem)` returns index of element in array // Returns -1 if not present
- `typeof` array returns `object`
- `slice()` - returns a shallow copy of a portion of an array
- `concat()` - merges and returns two arrays 
- `includes()` - true or false
- `join()` - joins all elements and returns a string
- Array.isArray(arr) returns true if arr is an array


Iteration Methods:
- `forEach(function)` Executes a function for each element of the array
- `map(function)` Creates a new array with the results of calling a function for every elem on this array
- `filter(condition)` Creates a new array with elements that pass the check
- `reduce(reducer)` Reduces the array to a single value from left to right
- `reduceRight(reducer)` Reduces the array to a single value from right to left
- `some(test)` Check if at least one element paasses the test
- `every(test)` Check if every element from this array pass the test

Reducer function can look like this:
`(acc, curr) => acc + curr, 0`
- Acc is the accumulator, and initial value is set to 0 here

#### New methods in ES6




There is no `Array(s)` only `Array`



