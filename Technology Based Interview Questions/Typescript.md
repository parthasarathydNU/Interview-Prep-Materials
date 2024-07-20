Typescript is a strongly typed superset of JavaScript developed by Microsoft. 

Combines static typing with modern ECMAScript features allowing developers to catch errors during development and enhance code maintainability. 

### Data Types in Typescript

TODO:
- `never` - Never returns anything - mostly for functions
- classes and interface in typescript
- scopes of variables
- namespaces and modules and scope
- hoisting
- temporal dead zone, memory allocation
- example of implementing an interface in typescript
- example of using inheritance in typescript
- tsconfig.json breakdown
- declaration files

1 **Built in Data types** : String, Number, Boolean, Null, Undefined, any, void
- Null - An empty value deliberately assigned to a variable
- Undefined - Variable declared but not defined
- consistency checks while writing typescript code
- compiling typescript code

2 **User Defined Data Types** : arrays, enums, classes, Interface

3 Unlike in Javascript - arrays have to be defined by specifying the static data types that can be stored in it. 

4 Three ways to declare variables in Typescript - var, let ( block scope ), const

5 Declaring explicit variables in Typescript: Mention variable name along with type and value
`let variable-name: data-type = value;`

6 Declaring functions mention return value along with function declaration, use types for parameters

7 `any` type in Typescript - Lets store value of any data type in a variable. Generally helpful in cases of reading data from API calls where the structure of the response is not known

8 Advantages:: 
- Can compile to js and can be run on any browser
- Throws error at compilation time during development rather than at run time given strong type checks and other consistency checks

9 Disadvantages: 
- Requirement of type definition file for every new import
- Code compilation to javascript is time consuming

10 `void` usually used to define return values of functions that don't return anything. 

11 `null` keyword: Indicates the unavailability of a value. Can be used to check if a value is provided to a particular variable or not

12 Syntax for creating objects in Typescript: objects can be defined by defining the property name and the type of key it is going to store:
> const myObj: { name: string, desc: string } = { 
>  name: "GeeksforGeeks",  
>  desc: "A Computer Science Portal" 
>  };

13 **`Never`** type - indicate the values that may never be occured used with functions that return nothing and always throw an exception or an error. 

Can be used for error handlers, a function that is defined with never as a return type, never returns a value. It is different from a `void` type

14 `Enums` in typescript: 
Used to create a collection of constants, it is a class that allows us to create multiple constants of `numeric` as well as `string` type. Default numeric constant starts from 0 and increases incrementally by margin of 1. But this can be changed to other start values. 

enum demoEnum {
	milk = 1,
	curd,
	rice,
	cheese
}

console.log( demoEnum.cheese ) // prints: 4

15 Is typescript a `strictly` `statically` typed language ?

It is an optionally `statically` typed language. Developers have the power to define the type of a variable during initialization. 

We can also use the `any` type to allow for the variable to accept any data type. 

16 ts vs tsx files: tsx files are used to create react components that return a jsx code at the end, ts files are used to contain pure typescript code like enums, functions , classes and reducers. 

17 `typeof` operator: Use to identify the type of the value in a given variable, also used to explicitly set the type of a variable to another. 

18 Explain interfaces in typescript
Interface defines the syntax that must be followed by the entity of that interface - it defines the methods, properties of the members of the interface. 

Only contains declarations while the initialization or the assignment will be done by the class that is deriving ( inheriting ) the interface. 

```typescript
interface interface_name{
	// define methods properties and events
}
```

19 How to compile a TypeScript file ?

It has to be compiled to javascript as typescript code is not executed directly. We can use the typescript compiler `tsc` to compile a typescript file to javascript

Multiple files can be combined and converted to a single js file through the tsc cli. 

`tsc --outfile combined.js script1.ts script2.ts script3.ts`

Not specifying the output file name makes this process take the name of the first typescript file. 

`--watch` is used to compile a typescript file in realtime.

20 the `extends` keyword can be used to make a class inherit the properties and methods from a parent class.

21 Modules in Typescript: 

Modules are used to create a collection of multiple data types that may include classes, functions, interfaces and variables. Modules have their own scope. Members defined inside a module cannot be accessed outside of it. Modules can be imported using the import key word and exported using the export key word.

22 `tsconfig.json` ?

Helps to compile the project by providing compiler options. It also makes the working directory as the root directory of the project.

35 Decorators in typescript:

Decorator is a special kind of declaration that can be attached to a class declaration, method, accessor, property or a parameter. 

This can be used to modify the behavior / attributes of a function / class / attribute in typescript

It is a higher order function that takes in a target element as argument and returns the modified version of it

26 Ways to control the visibility of a class member in typescript

- Private - Can only be accessed by code inside the class
- Protected - Can be accessed by code inside the class and all it's sub classes
- Public - Can be accessed by code outside of the class through class instances

27 Debugging a typescript file: 

A typescript file can be debugged by turning on the `--sorucemap` flag while running the `tsc` command. This generates a source map for the file `script.ts` wuth the name `script.ts.map`

In projects, to generate source maps for the typescript fiels, we have to compile the project with the `--sourcemap` flag and also set `sourceMap` to `true` in the `tsconfig.json` file. 

Whenever we set a breakpoint in the original source, VS Code tries to find the generated source by searching the files specified by glob patterns in `outFiles`. to enable breakpoint binding. 

28 Declaration files in typescript: 

We can convert a .ts file into a typescript definition file using the `--declaration` flag while running the `tsc` cli. 

`tsc --declaration script.ts`

29 Union Types in Typescript

Represents that the vario can be one of the speficied types. They use a | symbol to show the options of the various types. 

30 Type Aliases in Typescript

Used to give a meaning full name for a combined or a new type. This will not create a new type, instead it will create a new name for the combination it refers to. 

`type combinationType = number | boolean`

31 Immutable object properties in Typescript

We can use the `readonly` property before the property names while **defining objects**. This makes the properties of the object to be initialized at the time of declaring the object. If we try to update it during run time / compile time, it will be flagged as an error as it is readonly.

32 `in` operator - used to check if a given property is present within an object - It will return True if Present or False if not.

33 **Conditional Typing** - We can use a ternary operator to assign the dynamic types to a property, This will assign a type dynamically based on the conditions defined in the ternary operator.


