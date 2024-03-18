This is a classic problem that uses  a set time out to complicate the implementation. 
```js
for (var i = 0; i < 10; i++) {
  setTimeout(function() {
    console.log(i);
  }, 0);
}
```

In the above snippet what happens is that since i is a global variable, by the time the execution lands into the console log line, the value of `i` is incremented to 10. 

So we just get 10 logged 10 times on the console. 

Ways to fix this

1. Using a local variable
```js
for (var i = 0; i < 10; i++) {
    let y = i;
    setTimeout(function() {
        console.log(y);
      }, 0);
}
```
2. Using an IFFE
```js
for (var i = 0; i < 10; i++) {
  ((index) => {
        setTimeout(function() {
            console.log(index);
          }, 0);
  })(i);
}
```
3. By simply changing from `var` to `let`
```js
// let i
for (let i = 0; i < 10; i++) {
    setTimeout(function() {
        console.log(i);
      }, 0);
}
```
