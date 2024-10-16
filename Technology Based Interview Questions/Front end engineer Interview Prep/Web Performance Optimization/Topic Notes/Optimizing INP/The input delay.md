## Optimize Input Delay

Input delay can happen when there are other tasks that are blocking the main thread thereby causing the user interaction event call back to be fired very late.  This could be due to activity occurring on the main thread (perhaps due to scripts loading, parsing and compiling), fetch handling, timer functions, or even from other interactions that occur in quick succession and overlap with one another.

### Minimizing input delay:

- Avoid recurring timers that kick off work on the main thread
- Avoid long time outs before the input's callback is fired - example wrapping the callback with a set timeout
- Avoid long tasks from executing before firing the event related to the input
  ![[Pasted image 20231015094038.png]]
- Manage interaction overlaps - when the first interaction's process is happening, there might be other inputs form the user - example keydown events when a user is filling up the form...
  ![A depiction of when tasks can overlap to produce long input delays. In this depiction, a click interaction overlaps with a keydown interaction to increase the input delay for the keydown interaction.](https://web.dev/static/articles/optimize-input-delay/image/a-depiction-when-tasks-8c6449133de24.png)

### Ways to minimize input delay

- Using [[Debouncing]]
- Using the abort controller - we can abort pending API calls

### Minimizing Script Evaluation and Long tasks

Script evaluation is necessary for running JS in the browser as the code is compiled just in time for execution

The script is parsed for errors , which are flagged, then it is compiled to byte code and then sent to execution. 

- The number of evaluation tasks that spin up are proportional to the number of scripts that get loaded on to the browser
- When bundlers combine all scripts into one huge script, this can be a problem as the script evaluation might take long
- Loading scripts using the dynamic `import()` rather than importing on top. - this helps with code splitting and reducing the number of scripts loaded before the application becomes interactive

Example of code splitting: 
```js
form.addEventListener("submit", 
	e => {  
		e.preventDefault();  
		import('library.moduleA')    
		// using the default export
		.then(module => module.default) 
		.then(() => someFunction())    
		.catch(handleError());
	});
	
const someFunction = () => {
	// uses moduleA ...
}
```

This way, module A is not  preLoaded during the initial script initialization, it is LazyLoaded only when the function needs to be executed. 

To further improve performance, some critical scripts can be `preLoaded`, this caches them in the browser. 

Delegating script loading and long running tasks to web workers instead of running them on the main thread. 

Further by implementing code splitting, will help us get better cache invalidation because whenever new code is added, only the chunk that was updated needs to get loaded, the other js code can still be fetched from cache.

