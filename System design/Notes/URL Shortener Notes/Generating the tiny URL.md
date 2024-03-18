Now let's look at the crux of the problem - this is given a long url how do we come up with a unique short URL, what are the constraints that we have in this system.

Let's assume we will be going ahead with the following characters to come up with the shortened URL: 

| Character Type | Count |
| -------------- | ----- |
| A - Z          | 26    |
| a - z          | 26    |
| 0 - 9          | 10    |
| **Total**          | 62    |

We have a total of 62 characters and let's assume that we have to generate a URL shortener that delivers shortened URL with 7 characters each.
- So for 7 characters, we have 62 options for the first character, 62 for the second and so on
- $62*62*62*26*62*62*62$ = $62^7$ = 3.5 trillion combinations
- So we have set up a system that can deliver us 3.5 trillion short URLs in total. 

Now, let's assume the rate of requests to this service.
- Assuming we can serve around 1000 requests / second, it would take around ~ 111 years to exhaust all the possible combinations. 

So it is a safe bet to assume that we can work with a 7 character url.

And for us to be able to store 62^7 unique urls, we will need log(62^7) base 2 bits.

Which is 42 bits. 

And for the table schema, we will need to store the tinyUrl and the long URL.
	The tinyurl will be the key and the long url will be the value

[[Techniques to generate and store random Tiny Urls]]

[[Generating a tiny URL using the md5 hash]]

