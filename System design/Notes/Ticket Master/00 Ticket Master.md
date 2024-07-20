Ticket masters is an online platform that allows users to purchase tickets for concerts, and other live entertainment. It has ~100M Daily Active users.

[ExcaliDraw Link](https://excalidraw.com/#json=OUAphWmB61tF0m4_aHCgc,Qc51SfCNO3dJFcRelJNC6g)

=====================================================
![[TicketMaster.excalidraw]]
=====================================================


![[Screenshot 2024-07-19 at 8.29.49 PM.png]]
### Functional Requirements
*Features of the system*
- Users should be able to book tickets
- Viewing an event
- Search for events

### Non- Functional Requirements
*Characteristics of the system* - the `ility key words`- quantify it
- CAP Theorem - Availability or consistency ?
- Strong consistency for booking tickets
- High availability for searching and viewing events
- Low Latency Search
- Read Write Ratio ?: More reads than writes
- Scalable such that it can handle surges during popular events

------------

Out of scope: 
- Fault tollerance
- GDPR Compliance
- etc...