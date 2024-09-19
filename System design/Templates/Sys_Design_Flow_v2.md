# Revised System Design Interview Flow with Earlier Diagramming

| Time (min) | Task                                                               | Key Actions                                                                                                                                                        |
| ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0-2        | Introduction and problem clarification                             | - Introduce yourself briefly<br>- Clarify the problem statement<br>- Ask initial high-level questions                                                              |
| 2-5        | Quick requirements gathering                                       | - List key functional requirements<br>- Note critical non-functional requirements<br>- Clarify major constraints                                                   |
| 5-8        | Brief user/data flow overview                                      | - Outline main user interactions or data flow<br>- Identify key touch points                                                                                       |
|            | Ask interviewer which parts he wants to focus on and discuss those |                                                                                                                                                                    |
| 8-15       | Initial high-level design (Start box diagram)                      | - Draw initial system components<br>- Show main data flow between components<br>- Discuss high-level API structure                                                 |
| 15-20      | Dive into critical components                                      | - Elaborate on key components<br>- Discuss data model and storage decisions<br>- Address main scalability concerns                                                 |
| 20-25      | Refine design and handle edge cases                                | - Refine the diagram based on discussion<br>- Address potential bottlenecks<br>- Discuss failure modes and mitigation                                              |
| 25-30      | Performance and scalability deep-dive                              | - Estimate load and throughput<br>- Discuss caching and optimization strategies<br>- Consider read/write patterns                                                  |
| 30-35      | Operational considerations                                         | - Briefly cover monitoring, deployment, security<br>- Discuss any geo-distribution needs<br>- Probably mention offline support / Low bandwidth support if required |
| 35-40      | Review and improvements                                            | - Summarize the design<br>- Discuss limitations and trade-offs<br>- Suggest future improvements                                                                    |

## Key Points:

1. Start diagramming early: Begin your box diagram around the 8-minute mark. This allows you to visualize the system quickly and gives the interviewer a chance to guide you if needed.

2. Iterative approach: Start with a basic diagram and refine it as you go deeper into the discussion. Add more details or components as you discuss specific aspects of the system.

3. Use the diagram as a reference: Continuously refer back to your diagram as you discuss different aspects of the system. This helps maintain clarity and consistency in your explanation.

4. Be prepared to redraw: If you realize a major change is needed, don't hesitate to redraw parts of your diagram. This shows flexibility and willingness to adapt your design.

5. Engage the interviewer: Ask for feedback on your diagram periodically. This demonstrates good communication and ensures you're on the right track.

6. Balance breadth and depth: Start with a broad overview, then dive deeper into critical components based on the interviewer's interest or the problem's requirements.

7. Discuss trade-offs: For each major design decision, briefly mention alternatives and your reasoning for the chosen approach.

8. Keep user/data flow in mind: Even as you diagram and discuss technical details, regularly tie your design decisions back to how they serve the user needs or optimize the data flow.

Remember, this flow is a guideline. Be prepared to adapt based on the specific problem and the interviewer's style or focus. The key is to demonstrate your thought process, technical knowledge, and ability to design scalable, reliable systems that meet user needs.