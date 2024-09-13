First let's define what processing really means: 
- When Youtube users open some video, we want total views count for this video to be displayed immediately
- This means we need to calculate view counts on the fly, in real time
- Also when video owner opens statistics for the video, we want to be able to immediately show per hour statistics for the video
- So data processing means, whenever an event happens, we need to update several counters

> You are in front of the whiteboard and the interviewer is ready to capture your next steps.. Where do you go on from here ?

This is where we need to look back at our requirements of this system: 

These were the non functional requirements that we had defined earlier: 
- **Scalable:** We want to build a system that can handle 10s of 1000s of video views per second
- **Highly performant:** We want to retrieve the view statistics of total view counts of a video within 10s of milli seconds
- **Availability**: Data should be able to retrieved even if there is network or hardware failures

Here are some questions that we can ask ourselves: 
- How to scale ? 
- How to achieve **high throughput** ?
- How to **not lose data** when a processing node crashes ?
- What to do when **database** is **unavailable** or slow ?

Based on the past discussion in this document and other system design walk throughs, we know that: 
- When we want to scale data processing, we need to think about partitioning
- When we want to avoid data loss, we replicate data
- And when speed matters, we should keep things in memory and minimize disk reads

