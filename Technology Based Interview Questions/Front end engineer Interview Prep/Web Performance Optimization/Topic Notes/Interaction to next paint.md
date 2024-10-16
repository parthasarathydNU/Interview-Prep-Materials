https://web.dev/articles/optimize-inp?hl=en

[Interaction to Next Paint (INP)](https://web.dev/articles/inp) is a [pending](https://web.dev/articles/vitals#pending) Core Web Vital metric that assesses a page's overall responsiveness to user interactions by observing the latency of all [qualifying interactions](https://web.dev/articles/inp#whats_in_an_interaction) that occur throughout the lifespan of a user's visit to a page. The final INP value is the longest interaction observed (sometimes ignoring outliers).

This is crazyyy next level shit!!

This is crazyy, if I had learnt all this before, I would have done so much more!!, but I appreciate it now.

### Optimizing Interactions

Interactions can be broken down into three phases: 

1. **[[The input delay]]**, delay between the time a user provides an input and the time taken for the respective callback to to be fired
2. **[[Input processing delay]]** : The delay that happens due to the logic that has to run in order to process the input
3. **[[Reduce rendering delay]]** :  The time taken for the browser to present the next frame that contains the visual results of the interaction

The sum of these three phases is the total interaction latency. Every single phase of an interaction contributes some amount of time to total interaction latency, so it's important to know how you can optimize each part of the interaction so it runs for as little time as possible.

