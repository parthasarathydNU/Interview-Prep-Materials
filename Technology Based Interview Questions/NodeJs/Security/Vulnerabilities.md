https://www.youtube.com/watch?v=QSMbk2nLTBk&ab_channel=node.js
### Risky JS Traits
- Built in Memory Magement -----> Buffer Vulnerabilities
- Native serialization (qs, JSON) ----> Type Manipultations
- Naturally Scalable ( via EventLoop) ----> RegEx DoS
- Frequent Template / encoding use -----> Sandbox Escaping
- Npm Package Ecosystem ----> Vulnerable Packages

### NPM Usage Has Exploded

![[Screenshot 2024-10-07 at 10.44.41 AM.png]]

Most of your application's code comes from NPM, which means most of your application vulnerabilities come from NPM.

This not only stops at Node Applications but a lot of FrontEnd applications as well because a lot of front end applications these days use node based packages . 