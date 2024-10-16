Let and const are in the temporal dead zone for the time being.

Temporal dead zone is the time between memory is allocated to `a` and when it is initialized with a value. 

***A variable cannot be accessed when it is in a temporal dead zone. We get a Reference Error.***

In the below example, a was in a temporal dead zone from the start of the program till it reached line 3.

In the snippet below, we see that, though `a` has memory allocated to it, until it has some value assigned to it, it will not be attached to the global object. It is stored in a separate space reserved for let and const.

![[Pasted image 20231012224608.png]]

Even after we run the initialization of `a` it still is stored in a separate space. 
![[Pasted image 20231012224752.png]]

Proceed to [[Variable declaration in JS]]

