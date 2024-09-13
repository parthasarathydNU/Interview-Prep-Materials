# URL Shortener and Paste Bin System Design

This repository contains a comprehensive study on the system design of a URL Shortener and Paste Bin service. It's structured to provide a step-by-step evolution of the system design, covering various aspects from initial requirements to the final architecture.

## Project Structure

```
.
├── Evolution/
│   ├── 01 Requirements Gathering.md
│   ├── 02 An aside on CAP theorem.md
│   ├── 03 Understanding Scale.md
│   ├── 04 System API.md
│   ├── 05 Database Schema.md
│   ├── 06 Fact Tables vs Dimension Tables.md
│   ├── 07 Creating a shortened URL.md
│   ├── 08 Handling Duplicate Inputs.md
│   ├── 09 What should be the length of the hash code ?.md
│   ├── 10 Other Strategies for Key Generation.md
│   ├── 11 Detailed Drawbacks of Auto-incrementing Keys for URL Shortening.md
│   ├── 12 URL Redirection Service.md
│   ├── 13 Caching.md
│   ├── 14 Purging or Data Clean UP.md
│   ├── 15 Data Partitioning.md
│   └── 16 Final Diagram.md
├── Images/
│   └── [Various diagram and illustration files]
└── Problem Statement.md
```

## Content Overview

### Evolution
This folder contains a series of markdown files that walk through the entire process of designing the system. Each file focuses on a specific aspect or challenge of the system design.

1. **Requirements Gathering**: Initial analysis of the project needs.
2. **CAP Theorem**: Discussion on the CAP theorem and its implications.
3. **Understanding Scale**: Analyzing the scale requirements of the system.
4. **System API**: Defining the API endpoints for the service.
5. **Database Schema**: Designing the database structure.
6. **Fact vs Dimension Tables**: Exploring different table structures.
7. **Creating Shortened URLs**: Core functionality implementation.
8. **Handling Duplicates**: Strategies for managing duplicate inputs.
9. **Hash Code Length**: Determining optimal hash length for shortened URLs.
10. **Key Generation Strategies**: Exploring various methods for generating unique keys.
11. **Drawbacks of Auto-incrementing Keys**: Analysis of potential issues.
12. **URL Redirection Service**: Designing the redirection mechanism.
13. **Caching**: Implementing caching for improved performance.
14. **Data Cleanup**: Strategies for managing and purging old data.
15. **Data Partitioning**: Scaling the database through partitioning.
16. **Final Diagram**: The complete system architecture.

### Images
This folder contains all the diagrams and illustrations referenced in the markdown files, providing visual aids to the concepts discussed.

### Problem Statement
The root-level "Problem Statement.md" file contains the initial project requirements and constraints.

## How to Use This Repository

1. Start with the "Problem Statement.md" to understand the project goals.
2. Follow the numbered files in the Evolution folder to see how the system design progresses.
3. Refer to the Images folder for visual representations of concepts discussed in the markdown files.

This repository serves as a comprehensive guide to designing a URL Shortener and Paste Bin service, covering various aspects of system design and addressing common challenges and considerations.