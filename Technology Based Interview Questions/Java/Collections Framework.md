https://en.wikipedia.org/wiki/Java_collections_framework

![[Collections.png.png]]

 ![[Map.png.png]]

Set of classes and interfaces that implement commonly reusable collection of `data structures`.

Thought it is referred to as a `framework` it is more of a `library` that provides both interfaces that define various collections and the classes that implement them.

### How is this different from Arrays ?

`Collection` and `Arrays` are similar in that they both hold a `reference` to objects and they can be managed as a group. However unlike arrays, `Collection`(s) need not be assigned a certain capacity when instantiated. 

`Collection`(s) can automatically grow and shrink when objects are added or removed.

`Collection`s cannot hold primitive data types such as `int`, `long`, `char`, `double`, `float`, `byte`, `short` or `boolean`. Instead, `Collection`(s) hold `wrapper classes` such as `Integer`, `Long`, `Char`, `Double`. ....

## Architecture

Almost all collections in Java are derived from the `Collection` interface. 

```Java
add(E e)
remove(E e)
toArray() -> Object[]
contains(E e)
```

The `Collection` interface is a sub interface of `Iterable`. So any collections may be the target of a `for-each` statement. All `Collection`s hav an `Iterator` that goes through all of the elements in the collection.

## Types of collections

**Generic Types of Collections:**
- Queues - The base interface for queues is called `Queue`
- Maps - The base interface for maps/ dictionaries is called `Map`
- Lists - Base interface is called `List`
- Sets - The base interface for sets is called `Set`

### List Interface

Lists are implemented via the <`List` interface>. It is a more flexible version of an array. 

Characteristics of the `<<List Interface>>`
- Elements have specific order
- Duplicate elements are allowed
- Elements can be placed in a specific position
- Elements can be searched within a list

**Concrete Implementations**
- `ArrayList` Class
- `LinkedList` Class
- `Vector` class has `Stack` as it's direct sub class.
- `Stack` class (extends `Vector`)
	- push(E e)
	- pop( )
	- peek( )
	- empty( )
	- search(Object o)
	- `Last in first out`

### Queue Interface

Stores elements in order in which they are inserted. Creates a `First in First out` system. 

**Concrete Implementations**
- PriorityQueue Class
	- Additional `comparator()` method
- ConcurrentLinkedQueue Class
	- Thread safe implementation of queue interface

### Double ended queue Interface

**Concrete Implementations**
- ArrayDeque class
- LinkedList class

### Set Interface

**Concrete Implementations**
- HashSet Class
	- Uses a has table ( linked hash map) to prevent duplicates
- LinkedHashSet Class
	- Creates a doubly linked list 
	- Maintains insertion order
	- Ensures iteration over the set is predictable

### Sorted Set Interface
- Extends the Set interface
- Uses the element's `compareTo(T o)` method or  a method provided to the constructor
- First and last elements can be retrieved using the `first()` and `last()`

**Concrete Implementations**
- `TreeSet` Class
	- Uses a red-black tree implemented by a `TreeMap`

### Map Interfaces

**Concrete Implementations**

- HashMap
	- Hashes of the keys are used to find elements in various buckets
- LinkedHashMap
	- Extends hash map by creating a doubly linked list between elements
- TreeMap
	- Uses a red black tree