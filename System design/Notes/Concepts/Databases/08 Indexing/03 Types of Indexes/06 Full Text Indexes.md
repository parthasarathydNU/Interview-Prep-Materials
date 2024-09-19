Allows us to search text more efficiently.

It takes all the words in the field and separates it into tokens and it allows us to search for those words right from the **`beginning of each word`.** 

For example if we have "Richard Banner SQL Solutions Group" in a field. We can search for ["Solutions", "Sol%", "Gro%"] --> all these would be found. 

But ["ard"] won't be found, because it is the end of the word "Richard".

If we must do a search on large text files, then we must do `Full Text Indexes`. 

This is an `asynchronous` update and takes time for the data to get indexes.