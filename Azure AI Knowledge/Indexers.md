Azure AI Search utilizers indexers for automating the process of extracting, converting, and loading data from various data sources into it's search index.

### Why do we need indexers ? 

- Automation: Indexers automate the process of importing data into the search index saving time and reducing manual effort
- Data transformation: They can perform data transformations to make the data searchable and format it according to the search index schema
- Efficiency: Keeps the search index updates with the latest data ensuring that search results are current and relevant
- Simplification: They simplify the process of working with Diverse data sources, such as databases, blob storage and more and provide a consistent method to import data.

Data Enrichment and transformation; To enrich and transform data during the indexing process such as extracting text from images or PDFs....

### How to implement indexers: 
- Create a search index: This borrows concepts from elastic search, where we first define the search index and specify fields that will be searchable, filterable , sortable etc...
- Define a data source connection specifying how to connect to data
- Create an indexer by linking both the data source and the search index..
  Some validations can happen here to check if the fields to be indexed exist in the data source or not\
- Run the indexer: Chunk the data , vectorize it load into search index for retrieval
- Data can be now queried


