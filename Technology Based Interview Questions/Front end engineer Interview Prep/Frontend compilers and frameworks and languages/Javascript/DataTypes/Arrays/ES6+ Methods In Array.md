### from(arrayLikeObject)

An array-like object in JavaScript is an object that has some characteristics of an array, but isn't actually an instance of the Array type. Specifically, an array-like object:

1. Has a `length` property that reflects the number of elements it contains.
2. Uses numeric indices to access its elements (e.g., `obj[0]`, `obj[1]`, etc.).
3. Doesn't have array methods like `push()`, `pop()`, `forEach()`, etc.

``` javascript
const arrayLike = {
    0: 'a',
    1: 'b',
    2: 'c',
    length: 3
};

console.log(arrayLike.length);  // 3
console.log(arrayLike[0]);      // 'a'
console.log(Array.isArray(arrayLike));  // false
```

Here's how we can use the `from` method
```javascript
// Convert to an array
const realArray = Array.from(arrayLike);
console.log(Array.isArray(realArray));  // true

// Now we can use array methods
realArray.forEach(item => console.log(item));
```

For DOM collections, which are reliable examples of array-like objects:

```javascript
const divs = document.getElementsByTagName('div');
console.log(divs.length);  // number of divs
console.log(divs[0]);      // first div element
// divs.map(...)  // This would throw an error

// Convert to an array to use array methods
const divsArray = Array.from(divs);
divsArray.map(div => /* do something */);
```

### .findIndex(condition)

```javascript
// Array.prototype.indexOf(searchElement[, fromIndex])
// Returns the first index at which a given element can be found in the array, or -1 if it is not present.

// Array.prototype.findIndex(callbackFn(element[, index[, array]])[, thisArg])
// Returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1.

// Example 1: Basic usage
const numbers = [10, 20, 30, 40, 50];

console.log(numbers.indexOf(30));  // 2
console.log(numbers.findIndex(num => num === 30));  // 2

console.log(numbers.indexOf(35));  // -1
console.log(numbers.findIndex(num => num === 35));  // -1

// Example 2: Complex objects
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Charlie' }
];

console.log(users.indexOf({ id: 2, name: 'Bob' }));  // -1 (doesn't work with objects)
console.log(users.findIndex(user => user.id === 2));  // 1

// Example 3: Using with NaN
const mixedArray = [1, NaN, 2, 3];

console.log(mixedArray.indexOf(NaN));  // -1 (doesn't work with NaN)
console.log(mixedArray.findIndex(num => Number.isNaN(num)));  // 1

// Example 4: Performance consideration
const largeArray = Array(1000000).fill(0).map((_, i) => i);

console.time('indexOf');
largeArray.indexOf(999999);
console.timeEnd('indexOf');

console.time('findIndex');
largeArray.findIndex(num => num === 999999);
console.timeEnd('findIndex');

// Example 5: Flexibility of findIndex
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

console.log(words.findIndex(word => word.length > 6));  // 3
// No direct equivalent with indexOf
```


### .flat(depth)

```javascript
// Array.prototype.flat() 
// Creates a new array with all sub-array elements concatenated into it recursively up to the specified depth 
console.log("\nArray.prototype.flat():"); 
const nestedArray = [1, 2, [3, 4, [5, 6]]]; 
console.log(nestedArray.flat()); // [1, 2, 3, 4, [5, 6]] 
console.log(nestedArray.flat(2)); // [1, 2, 3, 4, 5, 6]
```

### .flatMap(mapperFunction)

```javascript
// Array.prototype.flatMap() 
// Maps each element using a mapping function, then flattens the result into a new array 
console.log("\nArray.prototype.flatMap():"); 
const sentences = ["Hello World", "Good Morning"]; 
const words = sentences.flatMap(sentence => sentence.split(' ')); 
console.log(words); // ['Hello', 'World', 'Good', 'Morning']
```

First applies the mapper function to all elements and gets the response. It will be a 2d list. 
Then it flattens the 2d list into a 1d list.

