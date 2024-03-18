In this technique, instead of generating a random tinu url, we first generate a md5 hash for the given long url. 

MD5 is a 128 bit hash value, that can be represented by 32 hexadecimal digits. 

Example: `ec55d3e698d289f2afd663725127bace` 

In hexadecimal, each character represents 4 bits, so 32 characters represent 126 bits.

So assuming we want to generate 62^7 unique urls, we observed, that we need 42 bits for that. 

So from the md5 hash we pick the first 42 bits - these set of 42 bits will always be unique for a given long url.  - guess the first 11 characters from the md5 hash.

First 11 characters: `ec55d3e698d`

From these first 42 bits, we convert them to base 62 to get the first 7 characters of the tiny url.

Example of base conversion from base 16 to base 32:
We see that the input number got converted to the result
![[Pasted image 20231001012840.png]]


First convert Base 16 to decimal:

(ec55d3e698d)16 = (14 × 1610) + (12 × 169) + (5 × 168) + (5 × 167) + (13 × 166) + (3 × 165) + (14 × 164) + (6 × 163) + (9 × 162) + (8 × 161) + (13 × 160) = (16240835717517)10

Decimal to base 36 calculation:

Divide by the base to get the digits from the remainders:

|Division|Quotient|Remainder<br><br>(Digit)|Digit #|
|---|---|---|---|
|16240835717517/36|451134325486|21|0|
|451134325486/36|12531509041|10|1|
|12531509041/36|348097473|13|2|
|348097473/36|9669374|9|3|
|9669374/36|268593|26|4|
|268593/36|7460|33|5|
|7460/36|207|8|6|
|207/36|5|27|7|
|5/36|0|5|8|

= (5R8XQ9DAL) base 36

**Like the above exaple, we convert it to base 62**

This was we get the unique 7 character tiny URL.

