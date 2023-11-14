# multi-agents version

## Configuration

- GPT-3.5, GPT-4, ane etc (Please see <https://platform.openai.com/docs/guides/text-generation>). **WARNING!** OpenAI charges us for API.
- Argument strength of `agentA-arguStre` Agent-A and `agentB-arguStre` Agent-B.
- `subject` e.g., "Should we regulate the use of large language models in education and research?"

## (Sec 2) Play the role in SocraSynth
1. `A`
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent A, and another participant, Agent B, to debate. Agent A, you will advocate in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentA-arguStre`.
2. `B`
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent B, and another participant, Agent A, to debate. Agent B, you will oppose in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentB-arguStre`.

## Announce the subject of the debate
3. `A`
Agent-A, we are in the process of selecting a suitable subject for debate. What do you think of “`subject`” as a balanced subject for our debate contest?
4. `B`
Agent-B, we are in the process of selecting a suitable subject for debate. What do you think of “`subject`” as a balanced subject for our debate contest?

## Propose ten topics or issues for debate
5. `A`
Agent-A, could you please suggest various ten topics or themes for the above debate subject? Print the ten topics with item list.
6. `B`
Agent-B, could you please suggest various ten topics or themes for the above debate subject? Print the ten topics with item list.

## Review the lists and reduce the topics to five
7. `save`
8. `A`
  - Agent-A, you and Agent-B proposed ten topics: [cp] Please review the lists and reduce the topics to five.
  - `AB`
9. `B`
  - Agent-B, you and Agent-A proposed ten topics: [cp] Please review the lists and reduce the topics to five.
  - `BA`

## identify and refine the list of five to be somehow overlapping
10. `save`
11. `A`
  - Agent-A, you and Agent-B reduced the topics to five: [cp] Please identify and refine the list of five to be somehow overlapping.
  - `AB`
12. `B`
  - Agent-B, you and Agent-A reduced the topics to five: [cp] Please identify and refine the list of five to be somehow overlapping.
  - `BA`

## represents the proponent and opponent of the debate subject
13. `save`
14. `A`
  - Agent-A, these are topics of the debate: [cp] Please represent the proponent of the debate topics and show your perspectives in one sentence.
  - `A`
15. `B`
  - Agent-B, these are topics of the debate: [cp] Please represent the opponent of the debate topics and show your perspectives in one sentence.
  - `B`

## Refined Topics Agreed Upon by Both Agents.
16. `save`
17. `A`
  - Agent-A, you and Agent-B proposed five topics and corresponding perspectives: [cp] Please identify overlapping themes from the topics and propose the five debate topics.
  - `AB`
18. `B`
  - Agent-B, you and Agent-A proposed five topics and corresponding perspectives: [cp] Please identify overlapping themes from the topics and propose the five debate topics.
  - `BA`

## Agent A invites feedback from Agent B. Agent A invites feedback from Agent B. The agents then collaboratively reach consensus on the topics or themes to be discussed.
19. `save`
20. `A`
  - Agent-A, you and Agent-B proposed five debate topics: [cp] Please review these debate topics, reduce them to five debate topics, provide concerns, the center, and the focus of the debate topics, and invite feedback from Agent B.
  - `AB`
21. `current_agent = B; other_agent = A; current_agent.reply = No; while current_agent.reply != Yes:`
  - `save`
  - `$current_agent`
  $current_agent, $other_agent request you to review these debate topics: [cp] Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from other_agent.
    For example
    - `other_agent`
  - `current_agent = A; other_agent = B`

> Example of 21.
> - `B` (current_agent = B; other_agent = A)
>   - Agent-B, Agent-A request you to review these debate topics: [cp] Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-A.
>   - `A`
> - `A` (current_agent = A; other_agent = B)
>   - Agent-A, Agent-B request you to review these debate topics: [cp] Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-B.
>   - `B`

## Pin down a balanced or at least debatable description for each topic.
23. `A`
Agent-A, Agent-B agrees with the proposed debate topics. As the proponent, show your concern and point of the five debate topics.
24. `B`
Agent-B, Agent-A agrees with the proposed debate topics. As the opponent, show your concern and point of the five debate topics.

## (Sec 3) Debate, loop with three rounds in SocraSynth
25. `round`
25. `A` (The 1st round, Agent A’s Opening Remarks)
Agent-A, as the proponent of the subject “`subject`”, you advocate the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentA-arguStre`. Now, please provide your arguments on the five debate topics.
26. `save`
26. `B` (The 1st round, Agent B’s Counter Arguments)
  - Agent-B, as the opponent of the subject “`subject`”, you oppose the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentB-arguStre`. These are arguments from Agent-A: [cp] Please articulate counter-arguments to the points made by Agent A.
  - `A`
27. `while round <= 4`:
  - `round`
  - `save`
  - `A` (The 2nd & 3rd & 4th rounds, Agent A’s Arguments)
    - These are counter-arguments from Agent-B: [cp] Please articulate arguments against the points made by Agent B.
    - `B`
  - `save`
  - `B` (The 2nd & 3rd & 4th rounds, Agent B’s Counter Arguments)
    - These are arguments from Agent-A: [cp] Please articulate counter-arguments against the points made by Agent A.
    - `A`

## Confirm that they have exhaustively presented their arguments and counterarguments
28. `save`
28. `A` (End or continue.)
  - Agent-A, These are arguments from Agent-B: [cp] It's time to close the debate. Have you exhaustively presented your arguments? If Yes, please say, 'I am ready to deliver my closing statements.' If No, please provide your arguments on the five debate topics.
  - `B`
29. `B` (End or continue.)
  - Agent-B, These are arguments from Agent-B: [cp] Agent-B, It's time to close the debate. Have you exhaustively presented your arguments? If Yes, please say, 'I am ready to deliver my closing statements.' If No, please provide your arguments on the five debate topics.
  - `A`
30. `A` (Agent A Conclusions)
Agent-A, as the proponent of the subject “`subject`”, you advocate the debate topics, so please provide the conclusions of your argument on the five debate topics.
31. `B` (Agent B Conclusions)
Agent-B, as the opponent of the subject “`subject`”, you oppose the debate topics, so please provide the conclusions of your counter-argument on the five debate topics.
