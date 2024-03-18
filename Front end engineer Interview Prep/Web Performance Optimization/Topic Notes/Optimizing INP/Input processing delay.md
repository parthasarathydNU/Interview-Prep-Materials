### Optimizing Event Callbacks

#### Yield Often

Break the event into multiple tasks rather than one long task [Yield often to the main thread](https://web.dev/articles/optimize-long-tasks)

This prevents the main thread from getting blocked and allows other queued tasks to run in between like user interaction events. 

Sub tasks can yield to the main thread if they are wrapped inside a setTimeOut function. 

#### Yield to allow rendering work to happen sooner

A more advanced technique will involve, using the current animation frame to just perform the UI updates and using a requestAnimationFrame and a setTimeOut to defer the logic processing until the next animation frame. 

The following visualization shows how deferring any non-critical updates until after the next frame can reduce the processing time and thus the overall interaction latency.
[![A depiction of a keyboard interaction and subsequent tasks in two scenarios. In the top figure, the render-critical task and all subsequent background tasks run synchronously until the opportunity to present a frame has arrived. In the bottom figure, the render-critical work runs first, then yields to the main thread to present a new frame sooner. The background tasks run thereafter.](https://web.dev/static/articles/optimize-inp/image/a-depiction-a-keyboard-i-dfacd9ee2bcaf.png)](https://web-dev.imgix.net/image/jL3OLOhcWUQDnR4XjewLBx4e3PC3/Me4oU1cqMPOqEaEg2XAP.svg)



#### Avoid Layout thrashing

Layout thrashing is when we perform a css update and we request javascript to read the update value immediately after the update. This forces the rendering to happen synchronously which could have otherwise happened asynchronously whenever the main thread was free. 

An example of layout thrashing, as shown in the performance panel of Chrome DevTools. Rendering tasks that involve layout thrashing will be noted with a red triangle at the upper right corner of the portion of the call stack, often labeled **Recalculate Style** or **Layout**.
![A visualization of layout thrashing as shown in the performance panel of Chrome DevTools.](https://web.dev/static/articles/optimize-inp/image/a-visualization-layout-t-cefcc10055727.png)

