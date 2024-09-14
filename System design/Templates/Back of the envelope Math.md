#### Template 1
| Item           | Comment | Calculation | Value |
| -------------- | ------- | ----------- | ----- |
| MAU            |         |             |       |
| DAU            |         |             |       |
| Usage DAU      |         |             |       |
| Scaling Factor |         |             |       |
| Per second     |         |             |       |
| Simplifying    |         |             |       |

#### Template 2 for data storage:

| Item                         | Comment | Calculation | Value |
| ---------------------------- | ------- | ----------- | ----- |
| MAU                          |         |             | -     |
| DAU                          |         |             |       |
| % DAU that have this content |         |             |       |
| Content Sizes                |         |             |       |
| Data Replication Factor      |         |             |       |
| Time for storage             |         |             |       |
| Simplifying                  |         |             |       |

----------------------------------------------------------------------


Absolute calculation is not important, usually it is enough if we get within an order of magnitude or 2 of the actual numbers we are looking for.

#### Example:
If the math says that at scale our web service needs to handle `10^6` requests per second and our server can handle `10^4` requests per second. Then we can quickly ascertain that we will need about `100` servers within an auto scaling group fronted by a load balancer.

![Servers With Load Balancing](./Images/ServersWithLoadBalancing.png)
For Example:
If a database need to handle 10 queries per second at its peak, it means we can use a single database server for a while, we will not require sharding or caching for a while

### Most useful numbers to estimate

The most useful numbers to estimate are: 
- requests per second at the service level and 
- queries per second at the database level

#### Common inputs in a Requests per second calculation

Decide based on the system* The following are with a generalized assumption of how people might user twitter

**DAU** : Daily Active users
This number should be easy to obtain. Sometimes, the only number available will be monthly active users, in that case, we can estimate the DAU as a % of the MAU

**Usage Per DAU of the service we are designing for**
- For example not everyone will be active on twitter makes a post
- Only a percentage does that. So 10 to 25% seems reasonable
- Again this does not have to be exact
- Getting within an order of magnitude should be fine
- So here, we can probably use the 80-20 rule
- 80% of the traffic will come from 20% of the users
- But again here we want to serve 100% of the users, so we can take the percentage of usage to be from 30% of users

**Scaling Factor :**
- Usage rate for a service usually has peaks and valleys through out the day
- We need to estimate how much the traffic might peak in comparison to the average traffic
- This could inform us the peak requests per second where our system could potentially break
- For example, for a service like google maps, usage rate during commute hours could be 5x normal usage
- For a ride sharing service like Uber, weekends and nights might see 2x more usage than usual
#### Let's go over an example for the number of requests per second for a service like twitter

**MAU**: Let's assume twitter has `300 M` MAU
**DAU**: 50% of the MAU use twitter Daily so this comes to `150 M` DAU
**Usage per DAU**: We estimated that about 25% of DAU make tweets = 150 * 0.25 Tweets Daily
And each user on average makes two tweets per day = 150 * 0.25 * 2 Tweets Daily
**Scaling Factor**: Most people use twitter in the morning when the wake up, so let's spike it to 2X during the morning period = 150 * 0.25 * 2 Tweets Daily x 2 Per day
**Per Second** : 150 * 0.25 * 2 Tweets Daily x 2 Per day / 86400 seconds  / day


| Item           | Comment                                                                          | Calculation                                 | Value                                     |
| -------------- | -------------------------------------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| MAU            | Let's assume twitter has `300 M` MAU                                             | 300 * 10^6 DAU                              |                                           |
| DAU            | 50% of the MAU use twitter Daily                                                 | 300 *  10^6  * 0.5 DAU                      | 150 M DAU                                 |
| Usage DAU      | We estimated that about 25% of DAU make tweets and each one makes 2 tweets       | 150 x 10^6  DAU x 0.25 * 2                  | 150 x 10^6  DAU x 0.5 tweets              |
| Scaling Factor | Most people use twitter in the morning when the wake up, so let's spike it to 2X | 150 x 10^6  DAU x 0.5 tweets * 2            | 150 x 10^6  DAU tweets                    |
| Per second     |                                                                                  | 150 x 10^6  DAU tweets/ 86400 seconds / day | 150 x 10^6  DAU tweets/ 10^5seconds / day |
| Simplifying    | 1500  tweets / second                                                            |                                             |                                           |

Some handy conversions

| Number Unit | Memory Unit | Scientific Notation |
| ----------- | ----------- | ------------------- |
| Thousand    | KB          | 10^3                |
| Million     | MB          | 10^6                |
| Billion     | GB          | 10^9                |
| Trillion    | TB          | 10^12               |
| Quadrillion | PT          | 10^15               |

#### Let's estimate the file sizes required:

We have to estimate storage for pictures and videos
Pictures : one very 10 posts have a picture and a picture is 100KB
Videos: One every 100 videos and each video is 100 MB

| Item                         | Comment                                         | Calculation             | Value |
| ---------------------------- | ----------------------------------------------- | ----------------------- | ----- |
| MAU                          | -                                               | -                       | -     |
| DAU                          | We know that we have 150M DAU                   |                         |       |
| % DAU that have this content | We know that 1 in every 10 tweets have pictures | 150 x 10^6 x 0.1        |       |
| Content Sizes                | 100 KB per picture                              | 150 x 10^7 KB           |       |
| Data Replication Factor      | 3 copies                                        | 450 x 10^7 KB           |       |
| Time for storage             | 5 years * 400 days / year                       | 450 x 10^7 x 5 x 500 KB |       |
| Simplifying                  | 725 x 10^10 KB = 7.25 x 10^12                   | 7.5 PB                  |       |
Video size is 7.5 PB *  10^4 = 750 PB
