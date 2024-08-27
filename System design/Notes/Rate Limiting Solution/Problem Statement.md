https://www.youtube.com/watch?v=FU4WlwfS3G0

Suppose we have an application and the application became highly popular. Everything was working fine until one particular client started sending requests at a higher frequency. 

This could happen due to various reason. 

- This client could be another popular web service that started getting high traffic
- This could be web developers doing a load test on the client
- Or this could be a malicious client who tried to DDoS our service

All these problems may lead to a situation called "noisy neighbor problem" where one client utilized too much resources on a service host like CPU, Memory, disk or network I/O. And because of this other clients, start to face higher latency for their requests or higher rate of failure.

One of the ways to solve this noisy neighbor problem is to introduce Rate Limiting also known as throttling.

Throttling helps limit the number of requests a client can submit in a given amount time. If the number of requests exceed this limit, the request is either rejected or its processing is delayed.