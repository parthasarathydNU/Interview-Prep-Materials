This should be the first step after understanding the system that we are designing. Further before we jump into this part, ,we need to discuss other aspects while we understand the system. 

Refer to [[Requirement_Gathering]] under the `Templates` folder of the `System Design` dir.

### Functional Requirements

**Shorten URL :** 
- Convert a long url into short unique identifiers

**Redirect to original URL :** 
- Redirect users to the original long url

**URL Expiration :** 
- Service should support setting expiration dates for shortened URLs

**User Account Management :** 
- Users can create accounts to manage their shortened URLs, view analytics and access additional features

**Custom Short URLs :** 
- Users should be able to create custom shortened URLs with specific key words only if the specified key word is unique

**Track usage stats :** 
- System should provide analytics of the shortened URLs such as number of clicks, location of users, and the referring platform

### Non Functional Requirements

How the system is supposed to behave.

**Highly Available :**
- The service should be highly available to ensure that shortened URLs are always accessible

**Security :**
- The system should prevent malicious or inappropriate content from being shortened, and protect against misuse like spamming or phishing
- Further the system should also support rate limiting so that no one clients hogs the server resources thereby preventing other clients from accessing the service

**Scalability :**
- The system should handle a large volume of URL shortening and redirection requests effectively

**Performance :**
- The system should provide fast redirection, with minimal latency between request being made and the redirect happening

#### CAP Theorem:

Here we have selected to go with high availability, what does it actually mean - how is that going to affect our system design ? 

Let's take the scenario - where we have servers across the world, we have a distributed system that spans across geographies and networks. 

Since we have a network partition, and we have chosen to go with high availability, we will presume that it is okay if a user closer to the east coast first creates a TinyURL , and sends it to a user on the west coast, but when that user tries to access it, they might not get redirected to the correct url, it might say invalid URL, but eventually, it will get rectified. Are we okay with this behavior ?

If we look at this fact, we realize that every decision that we make regarding the design comes with some sort of tradeoff. In this case, since we wanted the system to respond quickly and feel fast, we are okay to sacrifice consistency for a given period of time. But we have to think about how soon before data is propagated thoughout the system across all storages. So that all users can access this URL which was generated on the East Coast. While the system can quickly recover, we can satisfy most of the customers.

**What does the performance requirement tell us ?**
- The performance requirement also pushes us towards the direction of making the system feel quick and nimble. One question we can ask ourselves here is - what is the tradeoff that we will have to make to enable this behavior for the system. 
- Does consistency have to take a hit for this ?

I believe so - because if we want fast redirects , we might want to reduce the time to fetch the original URL, so we might have many distributed caches in place that are closer to the location of users, so the caches might have stale data. We can set an expiry time for the cached data, but say a URL is deleted or some sort of modification is made, it takes time for the change to get propagated across all the caches, so to provide very low latency of redirects, we sacrifice on the consistency aspect here , and we go with the eventual consistency model here.

Further Reading [[02 An aside on CAP theorem]]