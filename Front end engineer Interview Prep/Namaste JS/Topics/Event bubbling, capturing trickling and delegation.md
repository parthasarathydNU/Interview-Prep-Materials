There are two things, event bubbling and event capturing. 

- An event is bubbled up `ris:ArrowUp` from the child to the root node 
- An event is captured / trickled down `ris:ArrowDown` from the parent node all the way to the leaf nodes

### The start from the root node, goes all the way to the target and is bubbled up

## Default case - false - bubble
The default flag ( false ) is set to event bubbling. 
When we don't pass any argument, the event listeners are triggered when the event bubbles up from the target. 

So the event handler will be triggered whenever this current element is the target for the event or if the event passes through this element while bubbling up.

## Capture / trickle - flag is set to true
If the flag is set to true,(capture/trickle) the event handler is triggered whenever an event passes this element while trickling down or if this current element is the target. 


## Event delegation

Event delegation is basically, instead of having the event handler right at the target, we let the event bubble up and we handle the logic at the parent's level in the bubbling phase of the event cycle. 

This way we end up writing lesser number of event handlers and reduce the memory overhead on the browser. 

Example:  Using the data attribute to implement uppercase functionality
```html
<div id="inputForm">
	<input type="text" id="firstName" data-uppercase >
	<input type="number" id="number" >
	<input type="text" id="lastName" data-uppercase>
</div>
```

Now in our js code, we can attach a single event listener on to the inputForm and convert all input fields that have the data attribute of uppercase to uppercase text `e.target.dataset.uppercase`
```js
document.querySelector("#inputForm").addEventListener('keyup' (e) => {
	if(e.target.dataset.uppercase!== undefined){
		e.target.value = e.target.value.toUpperCase();
	}
}, false); // bubbling
```

### Now we can define different behaviors in the event handler and attach those behaviors to those input fields. 

### Pros:
- memory
- less code
- Faster dom manipulation

### Cons: 
- not all events are bubbled up
- stop propagation can limit usage of event delegation