### Block

This is a perfectly valid javascript code
```js
{

}
```

A block is also known as a compound statement. Blocks are used to group multiple codes of javascript. 

***Blocks can be used in places where javascript uses a single statement.*** 

Blocks are used with if, else, else if for, while and do statements. 

Example an if block. 
```js
if(true) true; // this is a valid js code


// this is also a valid js code
if(true){
	// group of statements 
}
```

### Block scoped 

What are the variables and functions that can be accessed in a block.

***Here when we halt execution just inside the block, we immediately notice that while a and b are present within the Block's scope, c is present in the global scope.***
![[Pasted image 20231013002300.png]]

Once we finish executing the block, the variable no longer exists in memory:
![[Pasted image 20231013002527.png]]

### Shadowing

If we have a same `var` variable name defined within the block, it shadows the variable that was defined in it's paren't scope. This is because `var` is global scoped, so whenever we define a new `var` with the same name. It shadows the previously defined `var`.
![[Pasted image 20231013003048.png]]

But this is not the case with `let`.

We see that each block has it's own copy of `a`
![[Pasted image 20231013003311.png]]

### How are different types of variables scoped

- var : function scoped / global scoped if not inside a function
- let: block scoped
- const: block scoped