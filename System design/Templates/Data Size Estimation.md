| Category             | Data Type                                                                               | Typical Size           | Notes                    |
| -------------------- | --------------------------------------------------------------------------------------- | ---------------------- | ------------------------ |
| **Text Data**        |                                                                                         |                        |                          |
|                      | URL                                                                                     | 60-100 bytes           | Max: 2048 bytes          |
|                      | Email address                                                                           | 20-40 bytes            | Max: 254 bytes           |
|                      | Plain text (English)                                                                    | 1 byte/character       | -                        |
|                      | UTF-8 text                                                                              | 1-4 bytes/character    | Varies by character      |
|                      | JSON                                                                                    | 100 bytes - several KB | Highly variable          |
| **Database Fields**  |                                                                                         |                        |                          |
|                      | Integer (32-bit)                                                                        | 4 bytes                | -                        |
|                      | Integer (64-bit)                                                                        | 8 bytes                | -                        |
|                      | Float                                                                                   | 4 bytes                | -                        |
|                      | Double                                                                                  | 8 bytes                | -                        |
|                      | [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Collisions) - Binary | 16 bytes               |                          |
|                      | UUID - as human readable - store as varchar                                             | 36 bytes               |                          |
|                      | Boolean                                                                                 | 1 byte                 | -                        |
|                      | Date/Time                                                                               | 4-8 bytes              | Depends on precision     |
| **Database Storage** |                                                                                         |                        |                          |
|                      | VARCHAR (MySQL)                                                                         | Up to 65,535 bytes     | Variable length          |
|                      | TEXT (MySQL)                                                                            | Up to 65,535 bytes     | -                        |
|                      | MEDIUMTEXT (MySQL)                                                                      | Up to 16 MB            | -                        |
|                      | LONGTEXT (MySQL)                                                                        | Up to 4 GB             | -                        |
| **Audio**            |                                                                                         |                        |                          |
|                      | MP3 (3 min)                                                                             | 3-5 MB                 | -                        |
|                      | Lossless audio (3 min)                                                                  | 30-40 MB               | -                        |
| **Video**            |                                                                                         |                        |                          |
|                      | SD (1 min)                                                                              | 20-50 MB               | -                        |
|                      | HD (1 min)                                                                              | 100-200 MB             | -                        |
|                      | 4K (1 min)                                                                              | 350-500 MB             | -                        |
| **Documents**        |                                                                                         |                        |                          |
|                      | PDF                                                                                     | 100 KB - several MB    | Varies widely            |
|                      | Word document                                                                           | 100 KB - several MB    | Varies widely            |
|                      | Spreadsheet                                                                             | 100 KB - several MB    | Varies widely            |
| **User Data**        |                                                                                         |                        |                          |
|                      | Username                                                                                | 20-50 bytes            | -                        |
|                      | Password hash                                                                           | 32-64 bytes            | Depends on algorithm     |
|                      | User profile                                                                            | Few KB - several MB    | Includes profile picture |

This grouped table should make it easier to look up data types within specific categories. Remember that these are general estimates and actual sizes may vary based on specific implementations and content.