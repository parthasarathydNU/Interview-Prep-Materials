**Remember to focus on the client-side architecture**, not the backend.

The High Level Diagram usually ends up with a few rectangular boxes with arrows between them to demonstrate the flow of data

**Components that are commonly found**:

**Server**: This is a backbox as far as front end system designs are concerned

**View**: This represents what the user sees, and it usually contains smaller sub views within it, can contain client- side only state

**Controller** : This module which responds to user interactions and processes the data from the store in a format the view expects. 

**Model/Client Store** : Where data lives on the client side. Stores contain data which will be presented to the user via views and stores tend to be app-wide for an interview context.

**Separation of Concerns:** Components are meant to be modular and serve to encapsulate a set of functionality and data. Consider the purpose / functionality of each component, what data it should contain and how it can service the rest of the system.

**Where should computation happen**: Should it be done on the client side or on the server side ? What are the tradeoffs to each approach .

Example Diagram: 

![Example architecture diagram](https://www.greatfrontend.com/img/questions/news-feed-facebook/news-feed-architecture.png)

