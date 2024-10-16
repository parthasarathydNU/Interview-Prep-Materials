
![[Pasted image 20231013220837.png]]

The browser wraps all the APIs and provides it to Javascript through the window object to be accessed within any execution context in the call stack. 

***console, setTimeOut, document, fetch and localStorage are browser APIs and not javascript apis.***

### Event loop

The Event-loop is the secret sauce that helps give JavaScript its multi-tasking abilities (almost!). ***This loop constantly checks whether the call stack is empty or not and if it is, the functions waiting to be executed in the callback queue get pushed to the call stack***.

![[Pasted image 20231013221630.png]]

![[Pasted image 20231013221716.png]]
