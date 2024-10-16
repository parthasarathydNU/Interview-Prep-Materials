Call back functions are powerful in JS, it gives us access to a while asynchronous world in a single threaded language.

When we call a function and we pass another function inside it, it is called as the callback function.

```js
function x(y){
 // ...
}

var y = function(){...}

x(y); 
// here y is passed as the callback while calling function x
// y can be called any time within function x, so it is called as a call back function

// EXAMPLE

// Here the anonymous function is passed as a callback to the set time out function
setTimeout( function() { } , 3000);


```


### Closures play an important role in callback functions and event listeners

Example: If we want to create a click button and we want to remember the number of times the button was clicked , we enclose the callback function with this count variable, and this will help us keep track of the click count. 
```js

function clickHandler(elemId){
	let countClicked = 0;
	
	function clickAction(){
		console.log("Button clicked ", ++countClicked);
	}

	document.getElementById(elemId).attachEventListener('click', clickAction);
}

clickHandler("buttonId");

```

In the above example, we see that when the clickHandler function is called, it attaches the clickAction function to the button as the click handler. 

Also to note, the `countClicked` variable is part of the `clickAction` function's closure, so whenever the function is run, it has access to the reference of the `countClicked` variable and it is able to increment it.

### Important 

Why is it important to remove event listeners?

Whenever an event listener is created, the call back function along with it's closure is allocated memory. 

So when there are large objects that are associated with the event listener callback's closure, having many such event listeners will prevent objects from being garbage collected, thus bloating the application's memory footprint!

Therefore it is a good practice to remove any event listeners that are unused. Event listener removal is important !


Follow into [[Microtask queue]]
