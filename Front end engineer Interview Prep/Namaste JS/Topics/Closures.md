Closures are nothing but functions combined with their lexical scope. 

***Example:***  
Here we see that the return value `z` of function `x` is sent along with the closure associated with it in it's scope.  This let's us run the function z, and print the output value as 20 even though that the function z is being called somewhere else from the place where it was declared.
![[Pasted image 20231013004722.png]]

We test multi level closures: We see that both the parent's lexical scope is available when executing function y.
![[Pasted image 20231013005954.png]]

### Advantages of closures: 
- Data hiding and encapsulation
- Ability to form constructor functions
- Memoization
- Run only once function
### Disadvantages:
- Could cause memory bloat if there are lot of closures lying around
- Data in closures are not garbage collected