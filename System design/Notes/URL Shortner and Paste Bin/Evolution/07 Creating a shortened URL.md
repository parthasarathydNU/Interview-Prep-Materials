The following process is one approach to create a shortened URL
1. Clean the input url, to remove extra '/' at the end and check if this is a valid URL
2. Hash the given long url using MD5 or SHA 256 algorithm
3. Encode that value to a more readable form using base36, 62 or base64 encoding

`https://www.designgurus.com/courses.grokking-the-system-design-interview/` -> Apply MD5 Hashing algorithm
-> `3c48c3223d7bbf0d5d0f02902eb0f305
-> Apply base 64 encoding to convert it to Readable Form
-> `PEjDlj17vw1dDwKQLrDzBQ+P`

**What is the purpose of doing it this way ?** :
- First every URL is unique, therefore by Hashing it, we ensure that we generate a unique representation of each url of a fixed length irrespective of how long the input is
- This constraining of length is the first advantage that we get in the hashing process
- Next to make it easily consumable, it is encoded to a base 64 representation that has letters that is closer to human representation
#### Elaborate more on the URL shortening process: 

Let's break down the process of hashing with SHA-256 and then encoding with Base64, and how it affects the output length:

1. SHA-256 Hashing:
   - SHA-256 always produces a 256-bit (32-byte) output, regardless of input size.
   - This 32-byte output is typically represented as a 64-character hexadecimal string.

2. Base64 Encoding:
   - Base64 encoding takes 3 bytes of input and converts them to 4 characters of output.
   - If the input length is not divisible by 3, padding ('=') is added to make it so.

Here's how the transformation occurs:

1. Original URL -> SHA-256 hash:
   - Output: 32 bytes (256 bits) or 64 hexadecimal characters

2. SHA-256 hash -> Base64 encoding:
   - Input: 32 bytes
   - Output: 44 characters (including padding)

The formula for Base64 encoded length is:
`4 * ceil(n / 3)` where n is the input length in bytes.

For a SHA-256 hash (32 bytes):
`4 * ceil(32 / 3) = 4 * 11 = 44 characters`

So, if you hash a URL with SHA-256 and then Base64 encode it, you'll always get a 44-character string, regardless of the original URL length.

For URL shortening:
1. This method (SHA-256 + Base64) will always produce a 44-character result, which might not be short enough for your needs.
2. It's not reversible, so you can't retrieve the original URL from the shortened version.

A better approach for URL shortening might be:
1. Generate a unique identifier (e.g., incremental ID or random string).
2. Store the mapping between this identifier and the full URL in a database.
3. Encode the identifier using a Base62 or Base64 encoding to create a short URL.

This way, you can control the length of the shortened URL and still maintain the ability to retrieve the original URL.

Citations:
[1] https://www.lifewire.com/base64-encoding-overview-1166412
[2] https://stackoverflow.com/questions/201479/what-is-base-64-encoding-used-for
[3] https://bunny.net/academy/http/what-is-base64-encoding-and-decoding/
[4] https://en.wikipedia.org/wiki/Base64
[5] https://www.base64encoder.io/learn/
[6] https://www.base64encode.org
[7] https://www.freecodecamp.org/news/what-is-base64-encoding/
[8] https://www.base64encode.org/enc/length/


Now that we have hashed and encoded it, we can be sure that this representation will be unique to the given input URL. 

To further shorten the data that we store, we can take the first 6 or 7 characters based on the configuration.

Now if we store this shortened URL in the database, whenever we get a new Long URL, if it resolved to the same short URL in the database, then we can either throw an error saying this URL already exists, or drop the request as this URL is already present in it's shortened form and just return the value. 

However one of our requirement is that, we will need to return a unique short url every time the same URL is sent to the system.

