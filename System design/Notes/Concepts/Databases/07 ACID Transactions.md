### ACID Properties and Transactions: 

[Reading](https://en.wikipedia.org/wiki/ACID#Atomicity)

ACID is a set of properties of database transactions intended to guarantee data validity despite errors, power failures and other mishaps.

In the context of databases, a `sequence of database operations` that `satisfy the ACID properties` are called as a `transaction`.

ACID is not the property of the database, the power of the database is that it provides the feature of transactions that satisfy the ACID properties. So whenever any system has a problem that requires the power of ACID, go with RDBMS.

#### Atomicity:
- Atomicity is the guarantee that `a series of operations` in an `atomic transaction` will either all occur or none will occur.
- These series of operations cannot be separated with only some of them being excuted, which makes the series of operations “indivisible” - hence seen as an `Atom`
- A guarantee of atomocity prevents updates to the database from happening only partially, which can cause greater problems than rejecting the while series outright. 
- Example: Money transactions : this consists of two operations, withdrawing money from `account A` and depositing it into `account B`. Performing these operations in an `atomic transaction` ensures that the database remains in a `consistent state`, the money is neither debited or credited if any one of these operations fail

Atomic systems guarantee atomicity in each and every situations including power failures, errors and crashes. 

One consequence of Atomic Transaction is that the transaction cannot be observed to be in progress by another database client unless it has been committed. When the other client started processing it’s transaction, the database was at it’s initial state, but by the time this transaction was completed, the database changed, this will cause the second transaction to fail in case there are conflicts. This is the behavior of the system that we will need to be aware of when using Databases that support ACID transactions.
#### Consistency

This demands that data must meet all validation rules. Consistency ensures that a transaction can only bring the database from one state to another as long as every state preserves the defined rules, constraints, cascades, triggers and any combination thereof. This prevents database corruption by an illegal transaction.

For example, if we have a requirement that A + B = 100. In a transaction that attempts to subtract 10 from A will fail, unless there is also a step in the transaction that adds this 10 to B. The entire transaction will be cancelled and the affected rows will be rolled back to their previous state. 

Similarly if there had been other constraints, triggers, or cascades, every single change operation would have been checked in the same way as above before the entire transaction is committed to the database. This way even if there is one step that fails in a a transaction that has a 100 steps, the transaction will be rolled back.

### Isolation:

Transactions are often executed concurrently in a database. Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. This is the main goal of concurrency control mechanisms in RDBMs

Need to read about : Pessimistic concurrency control and optimistic concurrency control mechanisms

### Durability:

Durability guarantees that once a transaction has been committed, it will remain committed even if there is an issue with system failure, power outage or crashes. This usually means that completed transactions and their effects are recorded in non-volatile memory. Database Write Logs.

The database system writes all successful operations to write logs, so that even if there is some transaction that has not been committed in the `disk buffer` that was lost due to power outage or failure, the system can be brought back to the state by sequentially running through the events in the Write Logs of the database. 