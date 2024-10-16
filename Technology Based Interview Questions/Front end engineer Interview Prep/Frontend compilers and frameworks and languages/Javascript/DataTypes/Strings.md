Strings are primitive values and also they are `immutable`.  

	ES6 introduced Template Literals

#### Template Literals

Allows us to work with string templates more safely and cleanly.

- Multiline strings
- String formatting using variables and expressions a.k.a. string interpolation
- HTML Escaping: ability to transform a string to it is safe to include in HTML.. like working with html tags in the string.

------------------------------------------------------------------

#### Properties.

`length`

Access a character using `index`
```
let str = "Hello";
console.log(str[0]); // "H"
```

`charAt(index)`

Compare strings using `=, <, >, <=, >=`

Comparisons happen in a `caseSensitive` manner. So convert both to `upper` or `lower` case before comparing.

`string.concat(newString)`

`string.endsWith(searchString)`

`string.includes(searchString)`

`string.indexOf(searchValue)` -> returns first occurrence of search value or -1

`string.lastIndexOf(searchValue)` -> Returns last occurrence of search value or -1

`string.localCompare(compareString)` -> dealing with user-facing text that needs to be sorted in a language-appropriate way

`String.prototype.replace()`  -> replace only the first occurrence with the replace option

`string.replaceAll(searchFor, replaceWith)` -> Replaces all occurrences of a pattern in a string. (Introduced later in 2021 ES12)

```javascript
// Using replace()
console.log('apple apple'.replace('apple', 'banana'));
// Output: "banana apple"

console.log('apple apple'.replace(/apple/, 'banana'));
// Output: "banana apple"

console.log('apple apple'.replace(/apple/g, 'banana'));
// Output: "banana banana"

// Using replaceAll()
console.log('apple apple'.replaceAll('apple', 'banana'));
// Output: "banana banana"

console.log('apple apple'.replaceAll(/apple/g, 'banana'));
// Output: "banana banana"

// This will throw an error:
// console.log('apple apple'.replaceAll(/apple/, 'banana'));
// TypeError: String.prototype.replaceAll called with a non-global RegExp argument
```

Replace all with regex should include `g` global regex. Else it throws and error. Since it is `replaceAll` the regex must also represent a global check.

##### Slice and Substring

Both do the same work effectively, but just that they handle negative indexes differently. 

Substring considers all negative indexes as 0, while slice works more like python and considers negative indexes as indexes from the end.







