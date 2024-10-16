![[Pasted image 20231014003423.png]]

![[Pasted image 20231014003513.png]]


### Inversion of control

When we pass in callbacks to other functions, we as programmers lose control when that function will be executed. So rather than us controlling when the callback function will be execute, we are at the mercy of the function calling the callback to decide that. 

```js
let cart = ["Pant", "shoe", "kurta"];

api.createOrder(cart, api.proceedToPayment);
```

Here in the above example, we need to proceed to payment after creating the order. So we pass the proceed to payment as a `callback` function to the `createOrder` method.  Here the control of `proceedToPayment` is with `createOrder`



