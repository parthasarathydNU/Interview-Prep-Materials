Just like the call back queue, we also have a micro task queue in JS. The micro task queue has a higher priority than the callback queue. 

When the call stack is empty and there are tasks in the McTask queue, those are executed first before the Call back queue.  

#### Call backs from `fetch` calls , `promises`  and `Mutation Observer` are stored in the Micro Task queue

All other call backs are sent to the call back queue.

Mutation Observer is something that triggers events when there is any change in the DOM tree.

![[Pasted image 20231013222944.png]]
