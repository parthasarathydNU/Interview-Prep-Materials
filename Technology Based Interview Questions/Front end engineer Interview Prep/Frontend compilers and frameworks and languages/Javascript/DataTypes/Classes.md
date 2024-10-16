Javascript classes are just syntactic sugar over `protypal inheritance`. ES6 classes are just special functions. 

Before ES6

```js
function Person(name) {
    this.name = name;
}

Person.prototype.getName = function () {
    return this.name;
};

var john = new Person("John Doe");
console.log(john.getName());  // John Doe
```

Here the `getName()` function is assigned to the `prototype`.

Now all instances of the `Person` type can share the `getName()` function. 

In the above example, the `john` object is an instance of `Person` and `Object` through `Prototypal Inheritance`.

```js
console.log(john instanceof Person); // true
console.log(john instanceof Object); // true
```

### ES6 introduced a new syntax for class declaration

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    getName() {
        return this.name;
    }
}
```

This makes it closer to how classes are created in languages like Java.

However this class is still a function under the hood.. 

```js
console.log(typeof Person); // function
```

Prototypal inheritance still applies.

```js
let john = new Person("John Doe");
let name = john.getName();
console.log(name); // "John Doe"
console.log(john instanceof Person); // true
console.log(john instanceof Object); // true
```


### Key differences

Unlike function definitions, `Class declarations are not hoisted in javascript.` 

Unlike using custom types to define objects , objects defined using classes need to be instantiated using the `new` keyword. 

```js
let john = Person("John Doe");
Uncaught TypeError: Class constructor Person cannot be invoked without 'new'
```

