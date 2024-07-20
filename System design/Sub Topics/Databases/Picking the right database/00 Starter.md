This discussion is in context to the discussion of designing the database for the Ad Click Data Aggregator High Level Design problem : [[04 High Level Design]]

### Consideration
- The events database has to be optimized to handle a lot of writes. 
- `Cassandra` uses a storage structure that resembles `LSMs`, which is a `log like structure` called MemTables. These tables are `in-memory` so it enables `High Writes` and it flushes it at a cadence to disk into a file called an SS table.  