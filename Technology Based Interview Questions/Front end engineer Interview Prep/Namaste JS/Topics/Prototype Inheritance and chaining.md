Everything in javascript is an object of some type. 

And `_proto_` is the object that is attached to all our objects to define what methods and values can be accessible from that object. 

Even the `arr._proto_` has a `_proto_` for itself ( which is the `Object`)
And `Object.__proto__.__proto__` is null
![[Pasted image 20231018212017.png]]

This chaining of prototypes is called prototype chaining. 

Further properties that aren't available in the object's value, will be checked for in it's prototype.

In the below example, we see that , though object2 does not have a `city` property, it is being accessed from its proto.
![[Pasted image 20231018212528.png]]