Since we are using base 64 encoding, for every character in the encoding, we have 64 possible combinations: 

| Number of characters | Possible combinations        | Possible unique combinations |
| :------------------- | :--------------------------- | ---------------------------- |
| 6                    | 64 ^ 6= 68719476736          | ~ 64.7 * 10^9 ( Billion )    |
| 7                    | 64 ^ 7 = 4_398_046_511_104   | ~ 4398 * 10^9 ( Billion )    |
| 8                    | 64 ^ 8 = 281_474_976_710_656 | ~ 281 * 10^12 ( Trillion )   |
In the [[03 Understanding Scale]] system, we estimated that we will need to store about `30 Billion` keys over the span of next 5 years. So 6 character codes should be sufficient.

- At the same rate of requests, this system can handle the requirements for the next 9 years. 
- However if we want to support for a longer point in time, we can increase the number of letters in the sequence to support after that point in time. 
- How can this be achieved ? 
- What will happen if we change 6 to 7, does this number play a role in the look up ?
- This will only affect new URLs that are generated..
- Old URLs will still be stored in the database.. 
- We will have to look at storage requirements and how they change.

