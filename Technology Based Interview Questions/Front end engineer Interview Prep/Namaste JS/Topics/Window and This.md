Window is a object created along with the global execution context. 

All JS engines create this global object to give access to the global execution context. 

In a browser it will be called `window` but on other run times, it might be called something else. Example in NodeJS this is called `global`

The `this` keyword points to the global object in the current execution context. 
In the global execution context `this` points to `window`.

Even in different execution contexts, unless we bind a different object to it, it will still point to the same window object. 

For example in the below snippet, unless we do a bind, even inside the execution context of b, this.a will still point to 10.

Once we perform the bind, the `this` keyword is entirely changed to point to the object that is passed within the bind method.
```js
var a = 10; // in global context

// this points to the window object, where this.a == 10

function b(){
    var a = 20; // local execution context
    console.log("function a");
}

b.bind({
    x: 50,
    y: 20,
    z:100
})();

console.log(a + 20);
```