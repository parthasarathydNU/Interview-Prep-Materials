Python is a general purpose high level programming language.
Python is dynamically typed and is portable across operating systems

Python is partially compiled and partially interpreted
The compilation part is done first and here the python code is converted to byte code and then this byte code gets converted by the Python Virtual Machine  according to the underlying OS to be executed. 

#### Immutable data types in python
String, Tuple etc..

Everything in Python is an object, so all values are passed by reference in python. If it is mutable it can be mutated, else it cannot. 

#### Set vs Dictionary in Python

- A set an unordered collection of data types that is iterable mutable and contains no duplicate elements
- A dictionary is an ordered set of elements that are stored in the format of a key and a value. By order it means, when iterating over a dictionary, elements are returned in the same order in which they were added to the dictionary


#### List comprehension in Python

This is a syntax construction to ease the creation of a list based on an existing iterable

my_list = [i for i in range(1, 10)]

#### Lambda functions in python

```python
x = lambda a, b, c : a + b + c  
print(x(5, 6, 2))
```

#### `pass` keyword in python

The pass statement is a placeholder statement used in places where either no operation has to be performed or where code needs to be written in the future

#### Error handling in Python

```python
```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("I am the except clause!")
finally:
    print("I am the finally clause!")
```

#### * *args and *kwargs

Both are special parameters passed to a function. This acts as an iterator that has access to all the parameters that were passed into the function. While args helps us access the parameters value as it was passed in. Kwargs helps us terate through the parameters as a key value pair. 

#### Data Types in Python:

Built In Data Types:
1. Numeric : integer, float, boolean , complex
2. Sequence: String, List, Tuple, Range
3. Mapping: Dictionary
4. Set: Set

#### What is a tuple
Tuple is an ordered, indexable, immutable set of objects that can contain duplicates. 

#### Dictionary Comprehension

Is a syntax to create a dictionary based on an existing iterable

```python
my_dict = {i:i+7 for i in range(1, 10)}
```

#### Sorting in python

By default the Tim Sort is used for sorting in python. This is a combination of Merge Sort an Insertion Sorting. Which has a worst case run time of O(N log N).

#### Decorators in python

Decorators are higher order functions that can take in the current function and return a modified version of it. 

They can used for any given function by typing the @ symbol followed by the decorator function name right above a function definition. 

Multiple decorators can be sequentially placed one below the other to chain their functionality and they will be processed in the order defined above the function defintion. 

#### Iterators in Python: 

Iterators are used to iterate over a group of elements that are contained in data structures like list, string, tuple and dictionary in python. 

An iterator in python implements the _ itr _ and the `next()` method to iterate across stored elements. 

### The underscore in python (_) 

1. A single underscore ' _ ' returns the last executed expression value , it has to be some operation.
2. _ can  be used as a throwaway variable

```python
# Ignore a value of specific location/index
for _ in range(10)
	print ("Test")

# Ignore a value when unpacking
a,b,_,_ = my_method(var1)
```

3. Single underscore after a name : This is used to use reserved key words. 
   
```python
class MyClass():
	def __init__(self):
		print("OWK")


def my_definition(var1=1, class_=MyClass):
	print(var1)
	print(class_) # here class is a reserved key word, but to use it as a parameter here we use class_


my_definition()

# 1
# <class '__main__.MyClass'>

```

4. Single underscore before a variable/ function/ method name. 
   
   This indicates to a programmer that this is supposed to be a private member of the class. If we use `import * from className`, this \_private_member will not be imported.

5. Double underscore before a Name 
   
   Here we ask the interpreter to rewrite the name in order to avoid variable naming conflict in a sub class. The interpreter changes this variable name to  `_Myclass__variable`
```python
   class Myclass():
	def __init__(self):
		self.__variable = 10

```

6. Double Underscore before and after a name
   
   These methods are used as operator overloading depending on the user. Python provides this convention to differentiate between user defined function with the module's function. 
   
   For all predefined operations like +, -, \*, >, < , there are several inbuilt methods that get called.  To modify these operations, we use the double underscore before and after the special method to overload these operations. 

	https://www.geeksforgeeks.org/operator-overloading-in-python/

Examples:
```python
class MyClass:
	def __init__(self, value):
		self.value = value

	def __and__(self, other):
		return MyClass(self.value and other.value)

a = MyClass(True)
b = MyClass(False)
c = a & b # c.value is False

# ===========================================

# Python program which attempts to
# overload ~ operator as binary operator

class A:
	def __init__(self, a):
		self.a = a

	# Overloading ~ operator, but with two operands
	def __invert__(self):
		return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)

print(~ob1)

# =============================================

# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)



```

Binary Operators

|Operator|Magic Method|
|---|---|
|**+**|__add__(self, other)|
|**–**|__sub__(self, other)|
|*****|__mul__(self, other)|
|**/**|__truediv__(self, other)|
|**//**|__floordiv__(self, other)|
|**%**|__mod__(self, other)|
|******|__pow__(self, other)|
|>>|__rshift__(self, other)|
|<<|__lshift__(self, other)|
|&|__and__(self, other)|
|\||__or__(self, other)|
|^|__xor__(self, other)|

#### Comparison Operators:

|Operator|Magic Method|
|---|---|
|**<**|__lt__(self, other)|
|**>**|__gt__(self, other)|
|**<=**|__le__(self, other)|
|**>=**|__ge__(self, other)|
|**==**|__eq__(self, other)|
|**!=**|__ne__(self, other)|

**Assignment Operators:**

|   |   |
|---|---|
|Operator|Magic Method|
|**-=**|__isub__(self, other)|
|**+=**|__iadd__(self, other)|
|***=**|__imul__(self, other)|
|**/=**|__idiv__(self, other)|
|**//=**|__ifloordiv__(self, other)|
|**%=**|__imod__(self, other)|
|****=**|__ipow__(self, other)|
|**>>=**|__irshift__(self, other)|
|**<<=**|__ilshift__(self, other)|
|**&=**|__iand__(self, other)|
|**\|=**|__ior__(self, other)|
|**^=**|__ixor__(self, other)|

**Unary Operators:**

|Operator|Magic Method|
|---|---|
|**–**|__neg__(self)|
|**+**|__pos__(self)|
|**~**|__invert__(self)|

### the `__name__` variable in Python

Sometimes you write a script with functions that might be useful in other scripts as well. In Python, we can import that script as a module in another script.

The `__name__` variable helps us decide whether we want to run the script or we want to import functions defined in the script. 

When you run your script, the `__name__` variable equals `__main__`. When you import the containing script, it will contain the name of the script.

Assume we have a script file called nameScript.py
```python
def myFunction():
	print `The value of __name__ is ` + __name__

def main():
	myFunction()

if __name__ == '__main__':
	main()
```

Now if we run this script `python nameScript.py`, this will be the flow:

1. First the value of `__name__` will be set to `__main__`
2. Now when the script is executed, since name is set to main, the main function is invoked, 
3. This inturn invokes the muFunction which prints the value of name

`The value of __name__ is  __main__`


However, let's import this script in another file

```python
import nameScript as ns

ns.myFunction()
```

Now only `muFunction` is called from the script, and this is the execution steps

1. name will be set to `nameScript`
2. myFunction is invoked that executed the line `print `The value of __name__ is ` + __name__
3. Now since the value of name is nameScript here is the output

`The value of __name__ is  nameScript`

### Generators in python

A generator is a normal function in python. But whenever it uses the `yield` keyword instead of the return keyword, it is considered as a generator. 

We can access the next value yielded by a generator using the `next(generatorInstance) `method

Example: 
```python
def fib(limit) :

	# Initializing the start point 
	a, b = 0, 1

	while a < limit:
		yield a
		a, b = b,  + b

x = fib(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for i in x :
	print(i)
```

this prints the first 5 fibonacci numbers. 

And if we try to call the next method after the limit it throws an error: 
```
Try programiz.pro
0
1
1
2
3
Traceback (most recent call last):
  File "<main.py>", line 18, in <module>
StopIteration
```


## Object oriented programming in python

#### Multiple Inheritance in python

Unlike Java, python supports inheritance from multiple parent classes.

If a parent class has a method `abc` then a child class can also have the same method.

**Method Over riding**:  A method with the same name and same number and type of arguments. 
- This allows the child class to give it's own implementation to the method different than the parent class. 
- The binding of methods is done at run time - **run time** poly morphism


#### Polymorphism in python

- **Method over loading**. A method with the same name but a different number and type of arguments. 
- Takes place within a class a class
- The binding of methods is done at compile time . **compile time** polymorphism

### Slice Object in python

```python
stringA = "0123456789"
sl1 = slice(-1)  # Removes the last element from the iterable
sl2 = slice(0) # Returns nothing as minimum end value is 1
sl3 = slice(1) # Returns the 1-1th element( 0TH ELEMENT )
sl4 = slice(0, 3) # Returns from 0th to 3 - 1th element 1, 2 nd
sl5 = slice(0, 9, 1) # Returns 0th to 9 - 1th element, jumping to every next element
sl6 = slice(0, 9, 2) # Returns from 0th to 9-1st element, jumping every 2nd element
sl7 = slice(0, 10, 4) # Returns from 0th to 10-1th element, printing every 4th element

print(stringA[sl1]) # 012345678
print(stringA[sl2]) # 
print(stringA[sl3]) # 0
print(stringA[sl4]) # 012
print(stringA[sl5]) # 012345678
print(stringA[sl6]) # 02468
print(stringA[sl7]) # 048

```

### Zip function in python

https://realpython.com/python-zip-function/

The python zip function returns a `zip` object which maps a similar index of multiple containers. It returns an iterator of tuples. 

Example:
```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', ..., 'zip']

# ============================

## Constructing the zip object

>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> zipped = zip(numbers, letters)
>>> zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
>>> type(zipped)
<class 'zip'>
# To retrieve the final list object, you need to use `list()` to consume the iterator.
>>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]

# ============================

# Passing in two iterables
>>> s1 = {2, 3, 1}
>>> s2 = {'b', 'a', 'c'}
>>> list(zip(s1, s2))
[(1, 'a'), (2, 'c'), (3, 'b')]

# ============================

# Passig in just one iterable
>>> a = [1, 2, 3]
>>> zipped = zip(a)
>>> list(zipped)
[(1,), (2,), (3,)]


# ============================

# Iterables with unequal length

>>> list(zip(range(5), range(100)))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# ============================

# Iterables with unequal length - zip_longest

>>> from itertools import zip_longest
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> longest = range(5)
>>> zipped = zip_longest(numbers, letters, longest, fillvalue='?')
>>> list(zipped)
[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

# ============================

# Looping over multiple iterables and bringing them together

>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> operators = ['*', '/', '+']
>>> for l, n, o in zip(letters, numbers, operators):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')
...     print(f'Operator: {o}')
...
Letter: a
Number: 0
Operator: *
Letter: b
Number: 1
Operator: /
Letter: c
Number: 2
Operator: +

# ============================

# Traversing dictionaries in parallel

>>> dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
>>> dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
>>> for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
...     print(k1, '->', v1)
...     print(k2, '->', v2)
...
name -> John
name -> Jane
last_name -> Doe
last_name -> Doe
job -> Python Consultant
job -> Community Manager



# We can do more like unzipping a sequence, sorting parallel iterators, calculating in paris, building dictionaries

```


### Pickling and un pickling in python

This is similar to marshaling and unmarshaling an object in java. This is used to convert an object to a serializable binary format to enable storage and easy transfer across networks. 

Python has built in functions in the pickle module. 

### With Statement in Python
https://www.geeksforgeeks.org/with-statement-in-python/

The with statement is similar to the resource based try block in java. This can be used with objects that have defined the `__enter__` and `__exit__` methods in their API.

Using the with operator ensures that the commands inside the with block are only run if the required object is defined and it also calls the clean up steps in the exit method the operation is complete. This can be used in situations where we need to close connections / close read / write streams after an operation is completed to avoid memory leaks within our application. 

```python
# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
	file.write('hello world')
finally:
	file.close()

# ================================

# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')

# ========== A custom file writer object

# a simple file writer object

class MessageWriter(object):
	def __init__(self, file_name):
		self.file_name = file_name
	
	def __enter__(self):
		self.file = open(self.file_name, 'w')
		return self.file

	def __exit__(self, *args):
		self.file.close()

# using with statement with MessageWriter

with MessageWriter('my_file.txt') as xfile:
	xfile.write('hello world')


```


### Monkey Patching in python

To modify a class during run time. An example could be defining a method overload during run time

```python
# g.py  
class GeeksClass:  
    def function(self):  
        print "function()"  
  
import m  
def monkey_function(self):  
    print "monkey_function()"  
   
m.GeeksClass.function = monkey_function  
obj = m.GeeksClass()  
obj.function()
```


### Access Modifiers in Python'

- Public : By default all members are public
- Protected : Adding a single underscore before a class member makes it protected => this is accessible only by the inheriting class and not from outside
- Private: Only available for mermbers within the same class. Double Under Score

### Python Global Interpreter Lock:  GIL
This ensures python runs in a single threaded fashion . The performance of the single-threaded process and the multi-threaded process will be the same in Python and this is because of GIL in Python. We can not achieve multithreading in Python because we have a global interpreter lock that restricts the threads and works as a single thread.

### Function annotations in python

This is like adding parameter types and return types to a function in python like how we do in typescript. 

And similar to typescript, these contain no meaning during the runtime of a function but rather they are just to enforce type safety during compile type of a function. 


#### Switch Statements in python : 

Old Style: Programmers used to simulate a switch case

```python
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))  

"""
Output: 
You can become a web developer.
You can become a backend developer.
You can become a mobile app developer
"""
```

New Syntax: Structural matching pattern

```python
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
```