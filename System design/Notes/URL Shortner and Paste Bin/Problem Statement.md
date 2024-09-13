[Youtube Video](https://youtu.be/_TsJizByBvE)

Probably the most famous question in System Design Interviews. The thing with URL shortener is that, the system is pretty simple to explain, but it gets complex when implementing the minor details under the hood.
### Basics Steps of System Design Interviews:
- Functional and Non Functional Requirements
- Back of the envelope calculations
- System APIs
- Database Schema

 These are the 4 steps that you should definitely be doing for any System Design Interview in depth at the beginning. This sets the stage for the rest of the system design.
### What is URL Shortener ? 

It is a system that converts long urls to a shorter version or their aliases. Whenever users go to the shortened URL they need to be redirected to the longer url.

**Example:** 
`https://www.designgurus/course/grokking-the-system-design-interview`

needs to be converted to `https://tinyurl.com/vzet59pa`

It is the unique code `vzet59pa` that is formed at the end that is the key that points to the longer url. How can we generate it such that it is unique.

### Advantages: 

**Saving space**:
- When there are a lot of parameters in the URL it becomes messy to store and manage
- Ad campaigns for example, have many parameters present in the URL
- For systems like twitter where you can only post short content, you want to save on space
- Social media posts, or emails

**Tracking and Analytics**:
- We can create multiple tiny urls for the same URL and then post it on different platforms
- That way we can identify where does traffic come from

> `This adds another requiremnet to the system that we design. A different unique short URL has to be generated each time even if we pass in the same long URL multiple times`

**Link Customization** :
- Masking long URLs

**Prevent Line Breaking**:
- When we send long urls in emails, when the url gets broken into different lines it might no longer work
- Similarly it is easier to create QR codes with smaller URLs