Everything in JS happens inside the Execution Context.

The execution context has two parts the Variable Environment (memory) and the Code component (Thread of execution). 

JS is a Synchronous -> Single -> Threaded Language

![[Pasted image 20231012192746.png]]

### Behind the scenes in the Javascript Engine

Whenever we run a JS program an Execution Context is created
An execution context is created in two phases 
- Memory Creation Phase
- Code Execution Phase

Memory Creation Phase : 
- JS Goes through all the lines of code and allocates memory to all variables and functions. 
- Variables are given the memory value of `undefined`
- For functions the whole code snippet is saved !

Code Execution Phase: 
- JS Goes through the program line by line and executes the program
- It could be either variable value assignment or a **function invocation**
- ***When a function is invoked a brand new execution context is created !***
- Once the function execution is complete, the execution context for that function invocation is deleted

### The call stack
- The call stack is populated whenever a new execution context is created
- The EC at the top of the stack is executed, and popped off the stack when execution is complete

JS can only execute the EC that's there on top of the stack. 





