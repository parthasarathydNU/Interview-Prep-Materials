Here are examples to illustrate when to use a subclass versus an inner class:

Subclass Example:
```java
class Vehicle {
    void move() {
        System.out.println("Vehicle is moving");
    }
}

class Car extends Vehicle {
    @Override
    void move() {
        System.out.println("Car is driving");
    }
}
```
Use subclass when: You want to create a specialized version of an existing class, inheriting and potentially overriding its behavior.

Inner Class Example:
```java
class ShoppingCart {
    private List<Item> items = new ArrayList<>();

    class Item {
        private String name;
        private double price;

        Item(String name, double price) {
            this.name = name;
            this.price = price;
        }
    }

    void addItem(String name, double price) {
        items.add(new Item(name, price));
    }
}
```
Use inner class when: You have a class that is closely related to another class and needs access to its private members, or when the class only makes sense in the context of another class.

These examples demonstrate the different relationships and use cases for subclasses and inner classes.

## Key Differences 

The key differences between subclasses and inner classes are:

1. Definition:
   - Subclass: A class that inherits from another class
   - Inner class: A class defined within another class

2. Inheritance:
   - Subclass: Uses 'extends' keyword, inherits properties and methods
   - Inner class: No inheritance relationship with enclosing class

3. Access:
   - Subclass: Can't access private members of superclass
   - Inner class: Can access all members of enclosing class, including private

4. Usage:
   - Subclass: Used for specialization and extending functionality
   - Inner class: Used for encapsulation and logical grouping

5. Instantiation:
   - Subclass: Can be instantiated independently
   - Non-static inner class: Requires instance of enclosing class to be instantiated

6. Relationship:
   - Subclass: "is-a" relationship with superclass
   - Inner class: "part-of" relationship with enclosing class

These distinctions reflect their different purposes in object-oriented design.

### Are private methods accessible within sub classes and internal classes ?

Here's how private methods behave in relation to subclasses and inner classes:

1. Subclasses:
   - Private methods are not accessible in subclasses
   - They are not inherited by subclasses

2. Inner classes:
   - Private methods of the enclosing class are accessible within inner classes
   - This includes non-static inner classes, static nested classes, local classes, and anonymous classes

3. Enclosing class:
   - The enclosing class can access private members of its inner classes

This behavior reinforces encapsulation while allowing inner classes to work closely with their enclosing class. It's one reason why inner classes are often used to implement private helper classes or interfaces.