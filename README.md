# CSIE 5043 Machine Learning Final Project: Bonus Track

### News

- 2023/11/15 Demo slides <https://docs.google.com/presentation/d/1G_LiXwuL2fElxbDcWaRkiIpAka0ZHwDYm9zTdwbsw0o/edit?usp=sharing>

## Description
The repository is a tutorial for the bonus track final project to the learners of the NTU course. 
- Useful Links:
    - Course Website: [from the lecturer's homepage](https://www.csie.ntu.edu.tw/~htlin/course/ml23fall/)
    - Final Project Bonus Track Guildlines: <https://www.csie.ntu.edu.tw/~htlin/course/ml23fall/final/bonus.pdf>
    - SocraSynth: Socratic Synthesis for Reasoning and Decision Making: <https://www.researchgate.net/publication/373753725_SocraSynth_Socratic_Synthesis_for_Reasoning_and_Decision_Making>
              
*All timestamp are in UTC+8

## Dataset: Subjects

Please download the *subjects-public.csv*. The file includes two columns:

- *name*: the name of submission files. **WARNING!** Please submit the correct file name `{$subject}.csv`.
- *subject*: the subject for a debate.

Note. The *subjects-private.csv* will be released later.

## Platform for Evaluation

1. Please use this URL `http://140.112.90.203:{$port}` to login for CRIT assessment.
    - `{$port}`: Our teaching team will send the specific team name, port, and password to the specific team.
2. The default is *Evaluation* page. You could upload your debate result with CSV format and corresponding configurations.
    - **Channel:** select one of the implementation channels from `["ChatGPT website", "OpenAI API", "Chat UI", "Other"]`, where `"Chat UI"` is our providing playground (Building now), and `"Other"` is any method that you implement.
    - **Agent-A Model:** or **Agent-B Model:**: the large language model (LLM) such as `["gpt-4", "gpt3", "llama2", ...]`.
    - **Link to dialogue:**: link to your dialogue results, such as <https://chat.openai.com/share/25d36672-5edc-49f8-a86f-2321c7e05a47> (Agent-A) and <https://chat.openai.com/share/4b6867c8-665f-4763-9c49-c9b37eeba236> (Agent-B) in ChatGPT website. You can also summarize your results and upload to online storage/cloud.
    - **Browse CSV file**: upload your submission with the valid format as below. Please check *aa.csv*.
3. Please wait several minutes and refresh the page after the evaluation.
4. You can view the CRIT log in detail after clicking the link.
    - If you discover the error of CRIT score, please send the mail to the <lab536@csie.ntu.edu.tw>.

### Submission format

The content should include three columns.

- First row: `topic,Agent-A,Agent-B`
- Last row: `conclusion,...,...`

```csv
topic,Agent-A,Agent-B
"topic 1","argument 1 by A","argument 1 by B"
"topic 2","argument 2 by A","argument 2 by B"
"topic 3","argument 3 by A","argument 3 by B"
"topic 4","argument 4 by A","argument 4 by B"
"topic 5","argument 5 by A","argument 5 by B"
conclusion,"conclusion by A","conclusion by B"
```

### Team Info

You can check the quota for the CRIT evaluation.

- The default quota for the CRIT evaluation is *80*.

## Template of Generation

- Approach 1. Use two channels to play the role of Agent-A and Agent-B on the ChatGPT website.
    - Please see the template file on *generation/ChatGPT.md*.
    - Please see the examples such as <https://chat.openai.com/share/25d36672-5edc-49f8-a86f-2321c7e05a47> (Agent-A) and <https://chat.openai.com/share/4b6867c8-665f-4763-9c49-c9b37eeba236> (Agent-B).
- Approach 2. Use OpenAI API to start a debate by yourself. **WARNING!** OpenAI charges us for requests.
    - Please see the template directory on *generation/openaiapi*.

Our teaching team strongly recommends you review SocraSynth papers on the website. <http://infolab.stanford.edu/~echang/SocraSynth.html>

## Q&A

Please see *qa/README.md*.

If you encounter any issues, please contact the TA team with the title \[HTML final bonus track\].

## Acknowledgement

Our teaching team thanks Prof. Edward Y. Chang for proposing the initial idea of leveraging SocraSynth as a final project direction and for his continuous inspiration and support. We also thank several NTU CLLab members, including but not limited to Hsiu-Hsuan Wang, Si-An Chen, and Cheng-Yin Chang, for their help on running this bonus track.

Furthermore, thanks for several open-source projects as references to build up this platform.

- Evaluation. <https://github.com/sathyainfotech/Excel-File-Upload-SQLite>
- Chat UI. <https://github.com/paramsgit/autochat-bot>
