https://en.wikipedia.org/wiki/Object-oriented_programming

Closely Related Read: [[06 UML Diagrams]]

Programming paradigm based on concepts of objects, which can contain data and code: data in thr form of fields, and code in form of Procedures (aka methods).

## Inheritance

This allows for code reuse and extensibility in form of classes.

Each object is an instance of a particular class where the class defines the data format or `type` ( including member variables and their types ) and available Methods.

`Think class diagram here` [[06 UML Diagrams]]

Objects are created by calling a special method called as constructor. A class can inherit from another class, they are arranged in a hierarchy and this is represented by "is-a-type-of" relationships. 

Procedures ( Methods ) and Variables ( Fields ) can be either at a class level or at an instance level. 

Procedures and Variables at a Class level are called as `Static members`.

#### Abstract Class

Is a class that cannot be directly instantiated. It can only be instantiated when extended by a concrete sub class. 

It can either be `labelled` `abstract` or can define `abstract methods`, thereby making this an abstract class. 

Before a class derived from an abstract class can be instantiated, all `abstract` methods of it's parent classes must be implemented by some class in the derivation.

A class consisting of only `pure abstract methods` is known as an `Interface`.

While a `class` cannot `extend` multiple parent classes, it can `implement` multiple `Interfaces`.

Go To [[02 Diamond Problem]] for details on why we cannot extend from multiple classes in Java but we can in other languages.

### Sealed / Final Classes

Cannot be sub classed, opposite of an abstract class, which must be derived to be used. Sealed class is implicitly concrete.

Example: The String Class

## Data Abstraction and Encapsulation

Data abstraction is a design patten in which data are only visible to semantically related functions to prevent misuse. This leads to the frequent incorporation of `data hiding` as a design patten. 

Similarly encapsulation prevents external code from being concerned with the internal workings of an object. This facilitates `easy code refactoring`.

Only expose methods and variables that are required from a `Class`.

This allows authors of the class to change how objects of that class represent their data internally without changing any external code. This encourages, decoupling and separating the abstraction from it's implementation.

## Access restrictions

` private `, `public`, `protected`.

- **Public** : Accessible from anywhere
- **Protected** : Accessible within the same package and subclass
- Default ( No access modifier ) Accessible only within same package
- **Private** : Accessible only within the same class

## Polymorphism

Always use a real world example while explaining an OOPs concept. 

It is the responsibility of the Object to select the procedural code to execute in response to a method call, typically by looking up the method at run time in a table associated with the object. 

This feature is called as `dynamic dispatch`. If a method is not present in a given object or class, the `dispatch` is `delegated` to it's parent class and so on going up the chain of inheritance.

Objects of the type Circle and Square are derived from a common class called shape. The `Draw` function of each `Type` of `Shape` impelments what is necessary to draw itself while the calling code can remain indeffirent to the particular type of `Shape` being drawn. 

This is another type of abstraction that simplifies code external to the class hierarchy and enables strong `separation of concerns`.
