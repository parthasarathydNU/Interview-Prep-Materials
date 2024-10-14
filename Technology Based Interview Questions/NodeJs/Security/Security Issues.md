
### Issues with JWT

While including cookies in HTTP Request, use HTTPOnly cookies. This will prevent cookies from being accessed by Javascript. This will mean that while the cookies cannot be accessed from the terminal, they are still passed around using the HTTP Headers.. This way no one can manipulate the cookies. 

Next, to ensure JWT Tokens are secure, always ensure that the tokens are signed. Unsigned tokens cannot be verified by the backend. This will help prevent manipulation of JWTs.

Further be as specific as possible with algorithms that can be used to sign and decrypt JWTs and always whitelist valid authors so that can act as an additional check.


#### Cross Domain Requests

Cross Domain Access Controlls: 

This prevents un authorized domains from sending request to our domain using certain checks.

Website URL: https://google.com: 80
Requesting URL : https://google.com:80

In the above example.. we see that the protocol (https), Domain ( google.com ) and the Port (80) are the same, so the request is accepted..


##### Now lets look at Cross Site Request Forgery Attacks (CSRF)

One domain is forging request to another in order to modify a value. 

Suppose you have a website `vulnerable.com` and users can create account there.. then one day one user saw a link called `cat.com` on this website... and they clicked on it,, and boom, their account got deleted on `vulnerable.com`... Tears...

How did this happen  ? 

**Flow of CSRF Attacks**

Say we logged into vulnerable.com and we have cookies saved in the browser. 

Suppose there is a `delete_my_account` end point in `vulnerable.com`. So when the user clicks on it, their account get's deleted. But in this case what happened is, when user clicked on `cat.com` the same request was made to `vulnerable.com`.. 

How is this possible ? Because we only accept requests from `vulnerable.com` ??
![[Screenshot 2024-10-07 at 12.41.50 PM.png]]

#### What happened here ? 

Whenever our website makes a request , the cookies are automatically sent to the receiving server regardless of the domain .. 

One possible fix is using Randomized Tokens ( Anti CSRF Tokens )

![[Screenshot 2024-10-07 at 12.45.16 PM.png]]

#### But what happened in Cat.com

Here we see that the cat.com has a form that calls the delete end point on vulnerable.com... and it uses a script to automatically submit that request without any user interaction..

![[Screenshot 2024-10-07 at 12.46.14 PM.png]]
### Issues with submitting data with forms

Say suppose we have an input form from which we accept user input and allow them to submit data to an end point..

![[Screenshot 2024-10-07 at 12.27.10 PM.png]]

Here the user has submitted `**Hi** JSConf Iceland` to the end point..

This is ground for Cross Site Request Forgery Attack.. let's see how this can happen.

