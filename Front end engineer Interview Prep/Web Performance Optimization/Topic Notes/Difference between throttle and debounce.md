The difference between debouncing and throttling. 

Example: We have a button that users can click to trigger some functionality. 

When the users click this multiple times consecutively, it triggers the event callback that many times. In case this is a computationally expensive function / an API call triggering it that many times might affect the application's performance. 

The way to handle this is not trigger the function call on every other click of the button. We can restrict which clicks trigger a function call in two ways. 

1. By setting a time value, such that only for those button clicks which have the given time value delay between the two clicks, the function is triggered. 
   
   Example: if the delay is 250 ms. This function call will only be triggered in the next click if the next click happens after 250 ms, if incase it happens before 250 ms, then another 250ms wait is added before the next function call get's triggered. This will extend indefinitely until there happens a button click that has a gap of 250ms after the previous one. 

	![[Pasted image 20231017120011.png]]

2. By setting intervals such that the function call is triggered only after the time has elapsed, this does not worry about how frequent this button is clicked, it only worries if a certain amount of time has passed after the last time when the function was called
   
	   ![[Pasted image 20231017120222.png]]