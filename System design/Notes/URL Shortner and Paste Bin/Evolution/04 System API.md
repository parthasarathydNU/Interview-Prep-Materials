This satisfies the functional requirements of the system - this is a good place to revisit the functional requirements. [[Technologies Interview Prep/System design/Notes/URL Shortner and Paste Bin/Evolution/01 Requirements Gathering]]

### External APIs

**Shorten URL :** 
- Convert a long url into short unique identifiers
- `POST shortenUrl(url: string) -> Promise<String> | 201 | 4xx`

**Redirect to original URL :** 
- Redirect users to the original long url
- `GET getRedirectFor(shortUrl: string) -> Promise<string> | 302 Redirect | 4xx` 

**URL Expiration :** 
- Service should support setting expiration dates for shortened URLs
- `POST shortenUrl(url: string, [validUntilEpoch | validForDuration | validUntilDate]) -> Promise<String> | 201 | 4xx`

**User Account Management :** 
- Users can create accounts to manage their shortened URLs, view analytics and access additional features
- `POST createUser(UserMetadata: Object) | 201 | 4xx `

**Custom Short URLs :** 
- Users should be able to create custom shortened URLs with specific key words only if the specified key word is unique
- `POST shortenUrl(url: string, [validUntilEpoch | validForDuration | validUntilDate], [customKeys]) -> Promise<String> | 201 | 4xx`

**Track usage stats :** 
- System should provide analytics of the shortened URLs such as number of clicks, location of users, and the referring platform
- `GET urlStats(shortUrl: string, startTime: timeStampEpoch, endTime: timeStampEpoch, [optionalFilters]) -> Promise<ResultsObject
- | 200 | 4xx`

**Delete Short URLs :**
- `DELETE delete(shortUrl: string) -> 201 | 4xx`

-------------------------------------------------

### Internal APIs

**Save events on urls**
- To provide users with analytics, we will need to store and aggregate event information associated with URLs
- Users might want to see details like, how many times their links were clicked over time
- What are the best performing demographies
- Whats are the top K platforms on which the link is being viewed from
- What are the device types on which the links are being viewed the most etc
- `POST processEvent(eventObject: EventObject) -> 201 | 4xx`


Go To [[05 Database Schema]]