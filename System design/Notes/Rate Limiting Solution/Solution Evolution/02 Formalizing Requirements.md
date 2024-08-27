### Functional
- For a request the rate limiting service needs to return a value whether to `allowRequest` or not
### Non Functional
- Low Latency ( make decision as soon as possible )
- Accurate ( We do not want to throttle clients unless absolutely required )
- Scalable ( We need to be able to scale the rate limited along with the service )
- Ease of integration

If we need to add more service hosts to the service, this should not be a problem for the rate limiter. 

Consistency might not be a key factor for the rate limiting service, if we don't have enough information to decide whether to throttle or not, then don't throttle. 

But availability and performance must be high so that the Rate Limiter can quickly make the decision and also handle high load.

Ability to integrate with any kind of service. Since a rate limiter is a generic service, and many teams might want to make use of the service, it is also important to think about ease of integration. 

Let's start with a simple solution first [[03 Single Server Implementation]]