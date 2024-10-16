- `null` : 
  A primitive that has only one value `null`.. for variables that are defined but now have no value associated with them..
  > A known bug in JS is that `typeof null` returns `undefined`
  
- `undefined`: has only one value `undefined`. This is for variables that are declared but not initialized
  
- boolean: `true`, `false`
  
- number
  
- string :
  Strings are immutable in javascript
  `Sequence` of zero or more characters . Can use `'` or `"` to define a string value.. Need to use `\` if `'` or `"` appears within a string.
  
- NaN
- symbol <-- from ES2015
- bigint <- from ES2020
  
- object: 
  Collection of properties represented by `key value` pairs.
  A property of an object can hold another object


![JavaScript data types](https://www.javascripttutorial.net/wp-content/uploads/2022/01/JavaScript-data-types.svg)

JS is a Dynamically typed language. Find type of variable using `typeof` operator.

----------------------------------------------------------------
### `Number` Data type

Represent both integers and floating point values. 

Represent `decimal` values. 

Can hold `octal` values

Therefore, ES6 introduced a new [octal literal](https://www.javascripttutorial.net/es6/octal-and-binary-literals/) that starts with the `0o` followed by a sequence of octal digits (from 0 to 7). For example:
```
let num = 0o71;
console.log(num);  // 57
```

Invalid `Octal` Value : `0o80`
Because `octal` digits don't hold the digit `8`, only from `0` to `7`.

Can hold `hexadecimal` values. Number starts with `0x or 0X`.
Digits from `0` to `9` and `a` to `f`.


----------------------------------------------------------------
### `BigInt` Data type

To allow representation of numbers larger than `2^53 - 1`

Append `n` to the end of number literal.

`let bigInt = 9007199254740991n;`
`let bigInt = BigInt(9007199254740991);`

Here we see that adding one to the largest max safe integer remains the same
```javascript
let x = Number.MAX_SAFE_INTEGER;
x = x + 1; // 9007199254740992
x = x + 1; // 9007199254740992 (same as above)
```

We need to use BigInt to fix this since number is greater than `2^53 - 1`

``` javascript
let x = BigInt(Number.MAX_SAFE_INTEGER);
x = x + 1; // 9007199254740992n
x = x + 1; // 9007199254740993n (correct now)
```

#### Operator Support

Supports `+, *, -, **, %`

The division of big int will not hold fractional values. 

Example `5n / 2n` will equal `2` and not `2.5`. But `5/2` will equal `2.5`.

#### Comparisons

A `BigInt` is not strictly equal (`===`) to a `Number`:

```javascript
console.log(1n === 1); // false
```

However, a `BigInt` is loosely equal to a number when you use the `==` operator:
```javascript
console.log(1n == 1); // true    
```



----------------------------------------------------------------

#### Binary Literals

Before `ES6` JS didn't provide any form for binary numbers. To parse a binary string, we used the `parseInt('111', 2); 

But in `ES6` we have the `0b` prefix that we can add before a sequence of `0 and 1` to represent a binary number literal. 

`const binNumber = 0b111;`

----------------------------------------------------------------

#### Object

- Object is a collection of key value pairs
- Use the `.` dot notation or the ['bracket_notation'] to access object properties
- Use the `delete` operator to remove property from an object
- use the `in` operator to check if a property exists in an object

----------------------------------------------------------------

