```js
// There are two ways to implement a debounce

// The element we are going to work with is a button element

(() => {
    a = document.createElement("button")
    document.body.prepend(a)
    a.innerText = "Click Me Baby!"
    a.id = "testButtonDhruv"
})();


function attachEventListener(){
    const button = 
    document.getElementById("testButtonDhruv");

    let count = 0;
    function clickButton(){
        console.log(`Oh baby ! `, ++count);
    }

    button.addEventListener('click', 
    debounce1(clickButton, 300));    
}

attachEventListener();



// Implementation 1 where we debounce based on time interval
function debounce1(callback, timeDelay=300){

	// timer present in closure initialized 
	// to undefined
    let timer; 
    
    // returns this function
    return function (...args){
        
        // whenever the function is run 
        // the current timer is cleared, 
        // so if we click againm the previous 
        // click's action is not processed
        clearTimeout(timer); // don't let prev action happen
		
		// Call the function only when the timer expires
        timer = setTimeout(() => { 
            // the function is set to 
            // run after the given time delay
            callback.apply(this, ...args)   
        }, timeDelay);
    }
}


// Implementation 2, we debounce every subsequent event

function debounce2(callback, timeDelay=300){

    let timer; 
    
    return function(...args){
        
        // Only when there is no timer initially set
        if(!timer){ 
            callback.apply(this, ...args); 
            // call the function only if there 
            // is no timer
        }
        
        clearTimeout(timer);
        // clear the timer for every 
        // subsequent click
    
	    // Push subsequent delay further
        timer = setTimeout(
        () => timer = undefined, 
        timeDelay) 
    }
    
}

// since debounce is a higher order function, 
// it will return the anonymous function inside that has 
// to run whenever the action is triggered

// So the variable timer will remain in the closure of the returned function

```