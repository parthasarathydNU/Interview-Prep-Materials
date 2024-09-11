We need to understand what exactly each of the above terms mean to be able to use them in the right context and meaning: 

[High Level Over View Youtube](https://youtu.be/PNbQ1Ix71Gc)

### **Encoding :**
- A technique to transform data from one form to another, so that it can be understood and consumed by different systems.. this is pretty vague
- Encoding has to do with information representation
- For example, the `name of the mineral that weakens superman`: 

We can represent it through Letters: [a-z] and using letters we read it as `kryptonite`
![[Encoding.png]]

This is a handy representation for humans, but not easy for  being manipulater by computers.  

What usually happens is the given sequence of characters is converted to a sequence of bits:
![[CharactersAndBits.png]]

- Both the characters and the bits represent the same information.
- The representation with the `base letters` is easily understood by humans
- The representation with the `base of bits` is commonly used when working with computers

> So here we can say that the same information has been encoded into a sequence of letters or a sequence of bits. Therefore encoding is just a transformation of data from one way of representation to another way of representation for the same information.
> 
> Information encoded in one format can be easily decoded and encoded into other formats
> 
> Encoding does not add any layer of security


For example, we can use the ASCII table, to convert the sequence of characters into a sequence of numbers using the ASCII Table and then convert it into a sequence of bits by using the decimal to binary conversion.

Other commonly available encoding tables are :
- Unicode Table that help with encoding more complex characters than letters
- Emojis encoding
- Base 64 encoding, that lets us encode binary representation of data as text
- And we have URL encoding, useful to represent data in a URL where some characters are reserved or cannot be used like colons, spaces and other special characters

Therefore:
- Encoding allows interoperability between systems
- Encoding allows different systems that use different modes of understand data to share information
- Encoding has no security purpose
- Anyone that has access to the conversion algorithm can encode and decode data
- Encoding is a reversible process
- We can transform data from one representation to the other and go back without any data loss

### Encryption:

This is a technique that makes data unreadable and hard to decode for an unauthorized party.

- Encryption transforms data to a different representation whilst ensuring that prying eyes cannot understand it.
- But when we present information as a form of bits, can't we decode the bits using the ascii table to get back the original word ? 
- In a way this is correct, encryption is a form of encoding, but to actually hide the information, data has to be converted to another form before being encoded. This way even if it is decoded, it does not represent the original information.
- The purpose of encryption is different from purpose of encoding.
- Encoding's purpose is to make data easily understandable across systems as much as possible
- While encryption tries to make the data undecipherable unless we have authorization for it 

The mail goal of encryption is data confidentially. But one quirky part of encryption is that, the data transformation is based on a sequence of letters and numbers called keys using well known encryption algorithms.

Encryption algorithms are designed such that the encrypted data can only decrypted using that specific key or using advanced computational powers. Encryption algorithms rely on the fact that, current state of the art computers cannot decrypt encrypted data within a reasonable span of time.

#### Families of Key Based Encryption Algorithms

**Symmetric Key Algorithms:** 
- They use the same key to encrypt and decrypt data like the AES algorithm

**Asymmetric Key Algorithms**:
- These algorithms use a pair of different keys to encrypt and decrypt data.
- The keys are bound by a complex mathematical relationship
- `RSA` and `SHA` are examples of algorithms in this family
- Like pure encoding, encryption is a reversible process as well, but only by authorized people
- Authorized people posses the key that helps with decrypting the data

An example of this is the public private key encryption while performing SSH access. 

Every system will have it's own private key internally, while making the public key and the algorithm publicly available. 

Every client that is sending a request to this server, will encrypt the data using the algorithm and the public key

This encrypted data can only be decrypted by this server, because only it contains the private key. This way it can be ensured that even if data is intercepted, unless the intercepting party has access to the private key, it cannot decrypt the data even if it knows how to implement the encryption algorithm.

#### Security Best Practices
- Key based encryption can be enhanced by developing better and more complex algorithms
- Constantly rotating the keys to ensure that even if old keys get leaked, newer keys can be used to ensure security
- And the most important, keeping the keys secret

## Hashing ?

Hashing is a technique to generate a fixed length string : a Hash that is strictly dependent on the input data.

Since this is strictly dependent on the input data, any change to the input data, no matter how small or big will result in a different hash

Suppose we have a piece of information, we can compare it with another piece of data to check if anything has changed by recomputing the hash.

Thus hashing ensures data integrity. And a hashing algorithm must have the following 5 characteristics:

1. The resulting hash has a fixed length
2. The same input always produces the same output
3. Multiple different inputs should not produce the same output
4. It must not be possible to obtain the input data from the output data
5. Any change to the data input implies in a different resulting hash

If we look at point num 3 : ` Multiple different inputs should not produce the same output `

However this cannot be guaranteed. And this is the points that is one of the key differentiator points for various hashing algorithms.

For example, the `MD5` algorithms, in 2008 was depricated due to issues related to collision detection. Similarly this happened to some early algorithms of the Secure Hashing Algorithms Family `SHA`. 

Further the 4th Point `It must not be possible to obtain input data from the output data` indicates that hashing is not a reversible process.


## Overview

Here are some misconceptions:
- Thinking that encryption of passwords is the best security practice is not actually true 
- Adobe engineers learnt this the hard way in the [user data breach of 2013](https://www.csoonline.com/article/540070/network-security-adobe-confirms-stolen-passwords-were-encrypted-not-hashed.html)
- Instead of using Hashing to store passwords, engineers used the concept of Encryption using symmetric keys to store the passwords
- Hackers were able to identify this secret key and decode all passwords using the algorithm

Attackers can also guess the password based on which the hash was generated. Also simply relying on hashing is not the best option. This was known from the Data Breach at [Yahoo where engineers stored passwords using the MD5 hashing algorithm](https://www.businessinsurance.com/yahoo-security-problems-md5-hashing-algorithm-outdated-2013/) and were still hacked.

The latest industry best practice in saving passwords is by using the `SHA-265` algorithm and hashing it with a `salt` that changes for every user


