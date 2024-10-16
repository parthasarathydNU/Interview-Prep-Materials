Here we describe the various data entities, the fields they contain and which component(s) they belong to .

There are two kinds of data on client applications: 

### Server-originated data

Data that originates from the server, and meant to be seen by multiple people / accessed from different devices. Common examples include user data and user generated data.

### Client-only Data

Also known as state, is data that only needs to live on the client and does not have to be sent to the server for writing into the database. 

When listing hte data fields, it'd be useful to identify what kind of data that field is, whether it's server originated data or client-only data.

#### Example Data Model:

A basic example of the data model for the various entities using the News Feed question.

| Source              | Entity - Map to Data Model | Belongs To Component (Owner) | Fields                                                                     |
| ------------------- | -------------------------- | ---------------------------- | -------------------------------------------------------------------------- |
| Server              | `Post`                     | Feed Post                    | `id`, `created_time`, `content`, `image`, `author` (a `User`), `reactions` |
| Server              | `Feed`                     | Feed UI                      | `posts` (list of `Post`s), `pagination` (pagination metadata)              |
| Server              | `User`                     | Client Store                 | `id`, `name`, `profile_photo_url`                                          |
| User input (client) | `NewPost`                  | Feed Composer UI             | `message`, `image`                                                         |

Write these fields near the components which own them in the architecture diagram.

