Give the interviewer enough time to ask follow up questions and dig your knowledge if they want to whilst also showing them that you can solve what they ask.

| Phase       | Step                                                                                                                  | Description                                                                                                                                                                                                                                                                              |     |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| 1 min       | Read and understand problem                                                                                           | <br>- [ ] Ask questions to understand requirements<br>- [ ] Confirm input/output format and constraints<br>- [ ] Discuss assumptions and edge cases<br><br>                                                                                                                              |     |
| 2 mins      | Make note of input size and ask about memory constraints                                                              | <br>- [ ] Consider input size and scale<br>- [ ] Inquire about memory usage and object manipulation<br><br>                                                                                                                                                                              |     |
| 5 mins      | Start explaining high level approach and get consensus                                                                | <br>- [ ] Explain approach<br>- [ ] Break problem into smaller components if required<br>- [ ] List down failure cases for the solution<br>                                                                                                                                              |     |
| 7 mins      | Start talking about edge cases and how you are going to handle it<br><br>Explain time and space complexity at the end | <br>- [ ] Explain space and time complexity of the approach <br>- [ ] Check Alignment and ask if we can start implementing<br>- [ ] ***Do not code until sure about complexity***                                                                                                        |     |
| 8th minute  | Code implementation                                                                                                   | <br>- [ ] Start with handling edge cases and base conditions<br>- [ ] Write code for happy path <br>- [ ] Discuss tradeoffs between different approaches if applicable<br>                                                                                                               |     |
| 12th minute | Start dry run for examples                                                                                            | - [ ] Dry Run for each scenario and scan for bugs<br>**Code clean up** <br>- [ ] Linting errors<br>- [ ] Spelling errors, variable names<br>- [ ] one off errors<br>- [ ] Boundary conditions and infinite loop errors                                                                   |     |
| 15th minute | Code execution                                                                                                        | <br>- [ ] Execute program  it for a few examples if possible to catch errors - debug quickly<br>- [ ] Ask interviewer if they have any questions<br><br><br>                                                                                                                             |     |
| 15          | Complexity Analysis                                                                                                   | <br>- [ ] Provide detailed time and space complexity analysis<br>- [ ] Show in code why complexity is as stated<br>- [ ] Ask interviewer their thoughts and if they have any questions<br>                                                                                               |     |
| 25 minutes  | Reflection and Improvement                                                                                            | <br>- [ ] Identify issues in current approach<br>- [ ] Consider real-life scale and variability<br>- [ ] Discuss approach changes for production scenarios<br>                                                                                                                           |     |
|             | Code Standards                                                                                                        | <br>- [ ] Ensure function documentation<br>- [ ] Revisit and improve variable names<br>- [ ] Remove unnecessary comments after walkthrough<br>- [ ] Ensure variable names are self-explanatory<br>- [ ] Refactor for explicitness if needed<br>- [ ] Only comment larger code chunks<br> |     |

#### Initial Phase

This is where we understand the problem: 
- Ask questions to understand the problem requirement fully
- Confirm input and output format and constraints
- Discuss any assumptions and edge cases
- Come up with test cases that cover various edge cases, failure conditions and happy cases

Analyze the scale and time requirements of the system
- Consider the size of the input and try to understand how quickly the system must compute
- Also ask questions about memory usage object manipulation and such
- Identify certain data structures and algorithms that would help with different aspects of the problem and discuss tradeoffs

Propose High level approach: 
- Outline initial thoughts on ho to solve the problem
- Discuss tradeoffs between different approaches if appilcable

#### Middle phase

Design the solution: 
- Break down the problem into smaller manageable components
- Sketch out the main functions or classes that we’ll need
- Decide conditions and checks for errors / base cases
- Discuss time and space complexity of the proposed solution

***Do not code unless we are sure about the time and space complexity***

Start coding:
- Implement logic to handle special cases or potential errors
- Discuss and show how your solution deals with invalid inputs
- And then discuss how your solution handles valid input and converges towards the final output

#### End Phase

Test your solution: 
- Walk through your code with a simple example to do a dry run
- Walk through some examples that show how code handles edge cases
- Write test suite and run test cases to check for failures

Analyze time and space complexity
- Provide a detailed analysis of time and space complexity and show in your code why it is so 

Reflect and improve: 
- Identify issues in current approach
- Think in terms of real life systems, the scale that is involved, how would you change your approach and what sorts of tests would you do to handle that scale and variability if this was in production

Code standards
- Ensure to have a function doc
- Revisit variable names and suggest better variable names and remove comments after code walk through
- Check if variable names directly mean what they are supposed to mean
- Be explicit and refactor if required
- Only have comments for larger chunks of code

--—————————-



Behavioral question Feedback:

What sort of questions will be asked in usual

- Response was very clear
- Described the situation, task action and result
- Practice different scenarios and different questions
- Communication was clear


