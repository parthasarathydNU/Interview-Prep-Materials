The next common situation that we would come across is providing the option of text based searching capabilities. 

**Elastic Search , Solr**
#### Examples

Suppose we have built a product like `Amazon` and sellers have posted information of their products there. We must now give users the ability to search for products based on text and keywords. 

This could be searching based on text available in the title and the description.

Similarly if we have built a product like `Netflix` we might want to be able to give users the ability to search movies based on movie name, movie title, cast, and genre.

Or if we have built something like `uber` or `google maps` where you might want to provide text searching capabilities or fuzzy search.

For all the above cases, we might have to provide a `Text Based Search Engine`

### Text Based Search Engine

The most popular text based search engines are Elastic Search and Solr and both of them are built on top of `Apache Lucene`. `Lucene` provides the text searching capabilities and both of them are then used by Elastic Search or Solr

### Elastic Search

### Solr

### Fuzzy Search

Suppose user searches for `Airprot` - so here this is Airport, but misspelt. So we need to be able to identify this and also return results related to `Airport` to the user.

This happens using the concept called `Edit Distance`.

So we can provide a level of fuzziness that the database has to support to provide good user experience.

—————————————————————————————————————————————————-

So wherever we need search capablities, we either use Elastic Search or Solr. And reiterating, these are not databases, but rather Search engines. 

> **The difference between a search engines and a database is that, whenever we write something in a database, it gives us a `guarantee` that the data would not be lost.**

Both of the data stores Elastic Search and Solr, do not give us any such guarantees. While it gives guarantees of availability and redundancy and all of that, potentially data could be lost. So we must not keep our data primarily in these text bases search engines as a primary source of truth.

The primary data can be somewhere else and we can load the data into this system to provide searching capabilities. 