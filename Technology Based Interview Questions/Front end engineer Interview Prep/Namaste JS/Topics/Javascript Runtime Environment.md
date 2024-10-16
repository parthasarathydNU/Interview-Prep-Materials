![[Pasted image 20231013224505.png]]

### Javascript Engine

The JS engine, is a program that takes in high level JS code and converts it to a low level ( probably machine ) code.

There are three stages in which the JS engine handles a particular piece of code: 

1. Parsing - Goes through code line by line and forms the [Abstract Syntax Tree](https://astexplorer.net)
2. Compilation 
3. Execution

#### Compilation

Initially Javascript was designed to be run through an interpreter in the JS engine. 

But browsers these days and depending on the engine they use, they use a combination of an Interpreter and a compiler - this term is called as [[Just In Time Compilation]]  

The interpreter and the compiler work hand in hand during the compilation stage. As the interpreter parses through the code line by line, the compiler compiles it to an optimal format to help with efficiency when the code is executed. 

There is also another form of compilation called [[Ahead of Time compilation]], where the JS engine in the Compile stage, takes a snippet of code and compiles it ahead of time and send the compiled code to the Execution Phase. 

![[Pasted image 20231013230704.png]]
### Execution Phase

In the execution phase, now, both the memory heap and the call stack are used to execute the compiled code. 
