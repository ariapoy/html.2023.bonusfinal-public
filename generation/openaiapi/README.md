# SocraSynth Lite OpenAI API

Lite version of SocraSynth System.

We reproduce critical functions in SocraSynth by OpenAI API for HTML 2023 Fall final project.

- [SocraSynth](https://socrasynth.com): SocraSynth orchestrates a symposium of GAI agents, facilitating investigative dialogues to reveal knowledge and insights previously elusive to humans.
- [OpenAI API](https://platform.openai.com/overview)
- [HTML](https://hsuantien.github.io)

## Getting Started

This is an example of how to set up SocraSynth-lite locally.

## Prerequisites

SocraSynth-lite is built on Python3 and OpenAI API.
To install the required packages, you can create virtual environment.

```shell
python3 -m venv socrasynthLite
```

after activate *socrasynthLite* environment, use pip to install required packages.

```shell
pip install -r requirements.txt
```

### OpenAI API accounts

Go to [OpenAI official website](https://openai.com/blog/openai-api) to get the API key.
It looks like this. `sk-...`


## Usage

### Knowledge generation

The generation phase aims to conduct a debate by setting up the configurations.

```shell
python socrasynth.py --subject "Could graffiti become as revered an art as classical painting?"
```

The socrasynth-lite system allows you to:
- Chat with two agent as a moderator
- Copy and past the agent's latest output with `[cp]` special token
    - You have to `save` the content before using `[cp]`

Note that `socrasynth.py` only provides a convenient interface to hold the debate.
You still have to copy the prompts from the *./OpenAIAPI.md*.