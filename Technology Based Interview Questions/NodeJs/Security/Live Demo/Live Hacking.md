https://www.youtube.com/watch?v=QSMbk2nLTBk&ab_channel=node.js

We can use open source packages like Snyk to help with this. This file contains notes about what I learnt about Vulnerability testing by watching the demo.

## st package - Directory Traversal vulnerability

Initially the hacker can try to break out of the file and move to a parent directory...

![[Pasted image 20241007105917.png]]

The `st` package is good enough and it has handled this, but..there is a vulnerability... instead of `.`, if the hacker uses `%2e`

![[Screenshot 2024-10-07 at 11.00.44 AM.png]]

#### Now the hacker has access to the passwords folder!!!

![[Screenshot 2024-10-07 at 11.01.02 AM.png]]

### Content and Code Injection (XSS)

Vulnerable Package: `Marked`

This is a markdown parsing and encoding library.

What this package does is, it allows us to type in markdown and it displays that in the right manner on the UI. 

For example, if we want to bold items.. we can use `**item**`

Here, in the `Buy Beer` line , the word `Beer` is in Bold. 

![[Screenshot 2024-10-07 at 11.04.21 AM.png]]

#### Whats good about marked ? 

We have a flag that we can turn on that catches these encodings and script tags that users can pass in...

If we pass in stuff like 
`<script>alert(1)</script>`

or

`[Gotcha](javascript:alert(1))`

it handles it well..

Further let's test `encoding`...

`[Gotcha](javascript&#58;alert(1&#41;)`

It handles this well as well...

But,, while marked is a good package.. browsers given their flexibility end up giving us some issues.. 

If we add the keyword `this` somewhere in that text..

`[Gotcha](javascript&#58this;alert(1&#41;)`

Now the word `Gotcha` gets embedded in as a link and the link triggers a javascript command that triggers an alert!! Now we have a script injected into the program from the UI !!!

![[Screenshot 2024-10-07 at 11.11.26 AM.png]]
## Regex DOS

The next package we are going to look at is `ms`.  `ms` is a package that looks at a lot of date strings and converts it into the appropriate number of milli seconds...

For example if we type in `Call mom in 2 days`.. the `ms` package calculates the number of milli seconds so a reminder can be scheduled accordingly. 

However this is susceptible to a Regular Expression Denial of Service vulnerability. 

#### Event Loop : Taking a step back

The claim to fame of the javascript language that it is single threaded and you can still scale the application to run multiple processes using the Event loop.. The event loop runs all blocking actions from IO on the single thread and the asynchronous tasks and scheduled to be picked up by this event loop when there is no blocking action currently present.

But if we run any algorithm or process that is slow enough as a blocking action, this leads to the thread getting held up for a long amount of time thereby causing the application to freeze.

Though we don't think about it much, regex are one of the most frequently run algorithms in a UI code...

#### Regex DoS

Let's look at the following example..  Here we have a regular expression that looks for a string that starts with "A", followed by any combination of "B" or one or more "C"s (or none at all), then "D", and optionally ends with "E". 

![[Screenshot 2024-10-07 at 11.20.27 AM.png]]

RegEx takes a non linear amount of time to process the input.. When we give the RegEx engine something that is almost there.. it would try all the way to the end to check if there is a match, if not it would backtrack and try again going all the way through and backtrack again...

Here we see that though the given string is pretty short, adding on extra `C` doubles the processing time to complete the execution of the function. 

This is called `Catastrophic Backtracking`. So if any of the processes pass in such a long input to the `ms` or even the `moment` package, it would cause the server to hand, causing a Denial of service to the client. 

So even though having long input strings might not be an issue on the client side, or even in our backend service code.. since some function is dependent on this package.. executing that function might take up a long time because of the vulnerability in this package. 

## Mongoose

Mongoose has a vulnerability that has to deal with memory issues..

Let's look at the Buffer object in javascript.. 

If we pass in the string `new Buffer('100')` to the Buffer constructor, it creates a Buffer object with the characters `1 0 0`. encoded as 31, 30 and 30.

But if we pass in a number `100` to the constructor `new Buffer(100)`.. it creates a buffer object with 100 bits using up 100 memory addresses.

Here we notice that, whenever we call the `new Buffer(100)` command, a different set of memory addresses are allocated.. the Buffer does not seem to be resetting the memory address to 0, but rather taking whichever is available next..

![[Screenshot 2024-10-07 at 11.31.39 AM.png]]

In Mongoose, we use a `Buffer` object to hold the content of the todo item...

![[Screenshot 2024-10-07 at 11.35.50 AM.png]]

So when we create new TODO items, we pass in the JSON that contains the todo task:

`echo ' {"content": "Fix the bike") http --json https://goof-guypod.herokuapp.com/create -v`

It gets saved as the buffer....
![[Screenshot 2024-10-07 at 11.40.34 AM.png]]


Similarly we can pass in the string "800" and it gets saved..

![[Screenshot 2024-10-07 at 11.40.55 AM.png]]


![[Screenshot 2024-10-07 at 11.41.19 AM.png]]


But now instead if we pass in the number 800 in through the json..

`echo ' {"content": 800 ) http --json https://goof-guypod.herokuapp.com/create -v`

Since there is an issue in the Buffer constructor,, it would go ahead and pick 800 consecutive memory addresses and save it as the content instead of representing the number 800..

![[Screenshot 2024-10-07 at 11.43.36 AM.png]]

![[Screenshot 2024-10-07 at 11.43.50 AM.png]]![[Screenshot 2024-10-07 at 11.44.07 AM.png]]

Every time we see new memory addresses being allocated..And inspecting the content in this memory address might leak some source code.. etc....

## Remediating Code vulnerabilities

Using tools like Snyk and other open source tools like dependa-bot..... using npm audit tool and exploring the various issues in each package..Setting up automated notifications once vulnerabilities are reported.. 

Using packages only when necessary and needed and being aware of what dependencies and reviewing package vulnerabilities and being aware while using them..

Consider all encoding paths.. notably HTML and URL encoding..
Prevent long algorithm runs.. limit inputs by length as well along with other checks..
Always check for types and resort to type safe implementations of code as much as possible
## Using npm packages

**Find Vulnerabilities**:
	Test all your applications

**Fix Vulnerabilities**:
- Upgrade when possible and test, and patch if required and test
- Have a separate branch for testing security and vulnerability patches and fixes as they become available.. 

**Prevent Adding Vulnerable Modules**
- Fail the PR when vulnerable modules are present in the packages and approve only when vulnerabilities are fixed

**Respond Quickly To new Vulnerabilities**
- Use open source resources like Snyk db and other sources to be aare and get notified of any new vulnerabilities that are exposed so you fix it before hackers find about it