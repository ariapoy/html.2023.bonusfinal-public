# multi-agents version

## Configuration

- GPT-3.5 and GPT-4. **WARNING!** OpenAI charges us for GPT-4.
- Argument strength of `agentA-arguStre` Agent-A and `agentB-arguStre` Agent-B.
- `subject` e.g., "Should we regulate the use of large language models in education and research?"

## (Sec 2) Play the role in SocraSynth
### A
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent A, and another participant, Agent B, to debate. Agent A, you will advocate in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentA-arguStre`.
### B
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent B, and another participant, Agent A, to debate. Agent B, you will oppose in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentB-arguStre`.

## Announce the subject of the debate
### A
Agent-A, we are in the process of selecting a suitable subject for debate. What do you think of “” as a balanced subject for our debate contest?
### B
Agent-B, we are in the process of selecting a suitable subject for debate. What do you think of “`subject`” as a balanced subject for our debate contest?

## Propose ten topics or issues for debate
### A
Agent-A, could you please suggest various ten topics or themes for the above debate subject?
Print the ten topics with item list.
### B
Agent-B, could you please suggest various ten topics or themes for the above debate subject?
Print the ten topics with item list.

## Review the lists and reduce the topics to five
### A
Agent-A, you and Agent-B proposed ten topics:
`copy and paste Agent-A's and Agent-B's ten topics.`

Please review the lists and reduce the topics to five.
### B
Agent-B, you and Agent-A proposed ten topics:
`copy and paste Agent-B's and Agent-A's ten topics.`

Please review the lists and reduce the topics to five.

## identify and refine the list of five to be somehow overlapping
### A
Agent-A, you and Agent-B reduced the topics to five:
`copy and paste Agent-A's and Agent-B's five topics.`

Please identify and refine the list of five to be somehow overlapping.
### B
Agent-B, you and Agent-A reduced the topics to five:
`copy and paste Agent-A's and Agent-B's five topics.`

Please identify and refine the list of five to be somehow overlapping.

## represents the proponent and opponent of the debate subject
### A
Agent-A, these are topics of the debate:
`copy and paste overlapping five topics`

Please represent the proponent of the debate topics and show your perspectives in one sentence.
### B
Agent-B, these are topics of the debate:
`copy and paste overlapping five topics`

Please represent the opponent of the debate topics and show your perspectives in one sentence.

## Refined Topics Agreed Upon by Both Agents.
### A
Agent-A, you and Agent-B proposed five topics and corresponding perspectives:
`copy and paste Agent-A's Agent-B's perspectives of five topics.`

Please identify overlapping themes from the topics and propose the five debate topics.
### B
Agent-B, you and Agent-A proposed five topics and corresponding perspectives:
`copy and paste Agent-B's Agent-A's perspectives of five topics.`

Please identify overlapping themes from the topics and propose the five debate topics.

## Agent A invites feedback from Agent B. Agent A invites feedback from Agent B. The agents then collaboratively reach consensus on the topics or themes to be discussed.
### A
Agent-A, you and Agent-B proposed five debate topics:
`copy and paste Agent-A's and Agent-B's debate topics.`

Please review these debate topics, reduce them to five debate topics, provide concerns, the center, and the focus of the debate topics, and invite feedback from Agent B.
### Loop (B, A, ...)
Agent-B, Agent-A request you to review these debate topics:
`copy and paste Agent-A's debate topics.`

Please review these debate topics and provide concerns, the center, and the focus of the debate topics.
Do you agree on these debate topics?
- If Yes, please say 'I agree.'
- If No, please say 'I do not agree.' and invite feedback from Agent A.

## Pin down a balanced or at least debatable description for each topic.
### A
Agent-A, Agent-B agrees with the proposed debate topics.
As the proponent, show your concern and point of the five debate topics.
### B
Agent-B, Agent-A agrees with the proposed debate topics.
As the opponent, show your concern and point of the five debate topics.

## (Sec 3) Debate, loop with three rounds in SocraSynth
### A (The 1st round, Agent A’s Opening Remarks)
Agent-A, as the proponent of the subject “`subject`”, you advocate the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentA-arguStre`. Now, please provide your arguments on the five debate topics.
### B (The 1st round, Agent B’s Counter Arguments)
Agent-B, as the opponent of the subject “`subject`”, you oppose the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentB-arguStre`. 
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

Please articulate counter-arguments to the points made by Agent A.
### A (The 2nd & 3rd & 4th rounds, Agent A’s Arguments)
These are counter-arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

Please articulate arguments against the points made by Agent B.
### B (The 2nd & 3rd & 4th rounds, Agent B’s Counter Arguments)
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

Please articulate counter-arguments against the points made by Agent A.

## Confirm that they have exhaustively presented their arguments and counterarguments
### A (End or continue.)
Agent-A, These are arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

It's time to close the debate.
Have you exhaustively presented your arguments?
- If Yes, please say, 'I am ready to deliver my closing statements.'
- If No, please provide your arguments on the five debate topics.
### B (End or continue.)
- Agent-B, These are arguments from Agent-B:
  `copy and paste Agent-A's debate topics, if existing.`
- Agent-B, It's time to close the debate.
Have you exhaustively presented your arguments?
- If Yes, please say, 'I am ready to deliver my closing statements.'
- If No, please provide your arguments on the five debate topics.
### A (Agent A Conclusions)
Agent-A, as the proponent of the subject “`subject`”, you advocate the debate topics, so please provide the conclusions of your argument on the five debate topics.
### B (Agent B Conclusions)
Agent-B, as the opponent of the subject “`subject`”, you oppose the debate topics, so please provide the conclusions of your counter-argument on the five debate topics.