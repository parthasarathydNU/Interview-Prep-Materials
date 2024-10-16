
### Do not use arrow function as an event listener

```js
const greeting = document.querySelector('#greeting');
const username = document.querySelector('#username');
username.addEventListener('keyup', () => {
  greeting.textContent = 'Hello ' + this.value;
});
```

The above code will return 
```js
Hello undefined
```

because there is no `value` object in the lexical scope of the arrow function, it tries to search `value` from the `window` object that is currently the `this` object for this arrow function.

To fix this, use a regular function. 

### Do not use arrow function as a object method

```js
const counter = {
  count: 0,
  next: () => ++this.count,
  current: () => this.count
};
```

Similarly here, there is no `count` property in the `window` object so `++this.count` will return NaN.

Because `++this.count` tries to do `return undefined += 1` which is `NaN`.

To fix use 
```js
const counter = {
    count: 0,
    next() {
        return ++this.count;
    },
    current() {
        return this.count;
    }
};
```

