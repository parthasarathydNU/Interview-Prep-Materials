# Distributed Rate Limiter Service

## Overview

This project implements a distributed rate limiter service designed for high scalability, performance, and accuracy. It's suitable for managing request rates across a cluster of servers, with self-service tools for rule management and efficient communication between hosts.

## Project Structure

```
.
├── Problem Statement.md
└── Solution Evolution
    ├── 01 Requirements Clarification.md
    ├── 02 Formalizing Requirements.md
    ├── 03 Single Server Implementation.md
    ├── 04 The Rate Limiter Algorithm.md
    ├── 05 Token Bucket Algorithm Code.md
    ├── 06 Object Oriented Design.md
    ├── 07 Making this a Distributed Service.md
    ├── 08 Communication Between Hosts.md
    ├── 09 Integrating with the service.md
    ├── 10 What else can be discussed ?.md
    ├── 11 Summary.md
    └── images
```

## Key Components

1. **Rules Management**: Self-service tools for service owners to manage rate limiting rules.
2. **Database**: Stores the rate limiting rules.
3. **Rules Retriever**: Caches rules locally on each service host.
4. **Rate Limiter Client**: Builds client identifiers and communicates with the rate limiter.
5. **Rate Limiter**: Makes decisions based on rules and current request rates.
6. **Message Broadcaster**: Facilitates communication between hosts in the cluster.

## Non-Functional Requirements

- High Scalability
- Fast Performance
- Accuracy

## Communication Method

The service uses Gossip communication over UDP for inter-host communication in the cluster. This method is efficient for clusters with:
- Less than several thousand nodes
- Fewer than 10,000 active buckets per node

For larger clusters (10,000+ nodes), a distributed cache option may be more suitable, though it increases latency and operational costs.

## Scalability Considerations

The effectiveness of the solution depends on:
- Number of hosts in the cluster
- Number of rules
- Request rate

## Further Reading

For a detailed evolution of the solution, refer to the markdown files in the "Solution Evolution" directory. These files provide step-by-step insights into the design process, from initial requirements to the final distributed architecture.