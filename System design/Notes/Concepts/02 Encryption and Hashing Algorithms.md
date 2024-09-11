
Here's a table comparing various common encryption and hashing algorithms:

| Algorithm Type        | Name     | Key/Output Size            | Description                                                                                               |
| --------------------- | -------- | -------------------------- | --------------------------------------------------------------------------------------------------------- |
| Symmetric Encryption  | AES      | 128, 192, or 256 bits      | Advanced Encryption Standard, widely used and considered very secure[1][6]                                |
| Symmetric Encryption  | Blowfish | 32-448 bits                | Fast algorithm, freely available in public domain[2][6]                                                   |
| Symmetric Encryption  | Twofish  | Up to 256 bits             | Successor to Blowfish, also freely available[2][6]                                                        |
| Asymmetric Encryption | RSA      | Typically 1024-4096 bits   | Based on difficulty of prime factorization, widely used for secure data transmission[2][6]                |
| Asymmetric Encryption | ECC      | 160-512 bits               | Elliptic Curve Cryptography, offers same security as RSA with smaller keys[6]                             |
| Hashing               | MD5      | 128 bits                   | Message Digest algorithm, considered insecure but still used in some non-cryptographic applications[2][3] |
| Hashing               | SHA-1    | 160 bits                   | Secure Hash Algorithm 1, no longer considered cryptographically secure[3]                                 |
| Hashing               | SHA-2    | 224, 256, 384, or 512 bits | Family of hash functions including SHA-256 and SHA-512, widely used and considered secure[3]              |
| Hashing               | SHA-3    | 224, 256, 384, or 512 bits | Newest member of the SHA family, designed to be more resistant to attacks[3]                              |
| Hashing               | Argon2   | Configurable               | Modern password hashing algorithm, recommended for password storage[2]                                    |

This table provides an overview of some of the most common encryption and hashing algorithms. Encryption algorithms are divided into symmetric (using a single key) and asymmetric (using public and private keys) types. Hashing algorithms produce fixed-size outputs and are one-way functions, meaning the original input cannot be derived from the hash.

Citations:
[1] https://www.okta.com/identity-101/hashing-algorithms/
[2] https://www.loginradius.com/blog/engineering/encryption-and-hashing/
[3] https://en.wikipedia.org/wiki/Secure_Hash_Algorithms
[4] https://www.simplilearn.com/data-encryption-methods-article
[5] https://auth0.com/blog/encoding-encryption-hashing/
[6] https://www.splunk.com/en_us/blog/learn/data-encryption-methods-types.html
[7] https://www.pingidentity.com/en/resources/blog/post/encryption-vs-hashing-vs-salting.html
[8] https://www.encryptionconsulting.com/education-center/encryption-vs-hashing/


### Is SHA not an encryption algorithm ?

You are correct - SHA (Secure Hash Algorithm) is not an encryption algorithm. Here are the key points to understand:

1. SHA is a hashing algorithm, not an encryption algorithm[1][2]. Hashing and encryption are distinct cryptographic processes with different purposes and properties.

2. The main differences between hashing and encryption are:

   - Hashing is a one-way process, while encryption is reversible[1][2].
   - Hashing always produces a fixed-size output regardless of input size, while encryption output size varies based on input[1][2].
   - Hashing is used for data integrity and verification, while encryption is used for confidentiality[1][2].

3. SHA algorithms (like SHA-1, SHA-256, etc.) take an input and produce a fixed-size hash value, typically represented as a hexadecimal number[1][2].

4. The primary purposes of SHA algorithms include:
   
   - Verifying data integrity
   - Password storage (hashing passwords rather than storing them in plain text)
   - Digital signatures
   - Checking file authenticity

5. While SHA is not encryption, it is often used alongside encryption in various security protocols and applications[1][6].

6. It's important to note that some older SHA variants like SHA-1 are no longer considered cryptographically secure, and newer versions like SHA-256 or SHA-3 are recommended for current use[3].

In summary, SHA is a hashing algorithm used for data integrity and verification purposes, not an encryption algorithm used for securing data confidentiality.

Citations:
[1] https://www.securew2.com/blog/what-is-sha-encryption-sha-256-vs-sha-1
[2] https://www.sectigo.com/resource-library/what-is-sha-encryption
[3] https://en.wikipedia.org/wiki/Secure_Hash_Algorithms
[4] https://www.loginradius.com/blog/engineering/encryption-and-hashing/
[5] https://brilliant.org/wiki/secure-hashing-algorithms/
[6] https://www.n-able.com/it/blog/sha-256-encryption
[7] https://en.wikipedia.org/wiki/SHA-2
[8] https://www.geeksforgeeks.org/sha-1-hash-in-java/

### Does Base 64 encoding always produce the same length output ?

Base64 encoding does not always produce the same length of output. The output length depends on the input length. Here are the key points to understand:

1. Base64 encoding converts 3 bytes of input data into 4 characters of output[1].

2. If the input data length is not divisible by 3, padding is added to make it so. This padding uses the '=' character[1].

3. The formula to calculate the Base64 encoded length is:
   `4 * ceil(n / 3)`
   Where n is the length of the input data in bytes[2].

4. This formula ensures that the output length is always a multiple of 4 characters[1].

5. For example:
   - 1 byte of input produces 4 characters of Base64 output (with 2 padding characters)
   - 2 bytes of input produce 4 characters of Base64 output (with 1 padding character)
   - 3 bytes of input produce 4 characters of Base64 output (no padding)[2]

6. The encoding causes an overhead of 33-37% relative to the original data size[1].

7. For very short messages, the overhead can be much higher due to padding[1].

In summary, while Base64 encoding always produces output in multiples of 4 characters, the actual length varies based on the input length. Longer inputs will produce proportionally longer outputs, but the relationship is not strictly linear due to the padding mechanism.

Citations:
[1] https://en.wikipedia.org/wiki/Base64
[2] https://stackoverflow.com/questions/13378815/base64-length-calculation
[3] https://www.base64encode.org/enc/length/
[4] https://lioncoding.com/calculate-a-file-size-from-base64-string/
[5] https://news.ycombinator.com/item?id=37981939
[6] https://community.wappler.io/t/base64-max-accepted-length/45073
[7] https://en.wikipedia.org/wiki/SHA-2
[8] https://brilliant.org/wiki/secure-hashing-algorithms/