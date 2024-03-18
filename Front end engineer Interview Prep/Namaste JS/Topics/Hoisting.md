**Hoisting** in JS is when we can *access variables in functions in an Execution context even before we initialize it*. 

This is a consequence of the Memory Allocation Phase of the Execution Context Creation. When the first phase runs, variables are assigned memory locations and values as `undefined`, and function snippets are stored as is. 

### 1 point to Note:
In the below snippet, though we have defined delta as a function, when the execution context of the getName function is created, unless `delta` in invoked anywhere within the getName function, memory is not allocated to it. 
```javascript
getName();
console.log(x);

var x = 7;

// defined during mem allocation phase
function getName() {
    console.log("Namase JS")

    function delta(){
        console.log("delta");
    }

    // delta();
}
```

### 2 Point to Note
In the below snippet, we see that getName has been defined just like a variable, so when we try to access getName before it get's defined, we get the value `undefined`. Because variables are given the memory value of `undefined` during the memory allocation phase of the EC creation.
``` js
getName();
console.log(x);

var x = 7;

// undefined during MEM allocation phase
var getName = () => { 
    console.log("Namase JS")

    function delta(){
        console.log("delta");
    }

    // delta();
}

```
