Scope - the specific lines of code where a particular variable can be accessed. 

Scope is directly linked to the lexical environment. 

***Lexical environment is the local memory + the lexical environment of it's parent***

For example in the snippet below, `function e` is lexically inside `function c`
`Function c` is lexically inside `function a` and `function a` is lexically inside the `global exec context`.

So all variables and function defined in a function's lexical env will be available to it. 

In this case, anything defined within the global scope, function a and function c will be accessible to function e.

**`It is like a tree structure` the path from the child to the parent is called `scope chain`**

```js
var b = 10;
a();
function a(){
    let d = 5;
    function c(){
        console.log(b);
        console.log(d);
        var f = 30;
        function e(){
            console.log(b);
            console.log(d);
            console.log(a);
            console.log(f);
        }
        e();
    }
    c();   
}

```