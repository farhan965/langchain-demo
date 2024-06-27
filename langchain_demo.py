# -*- coding: utf-8 -*-


## Integrate our code OpenAI API
import os
from langchain.llms import OpenAI

! pip install langchain_community

## OPENAI LLMS
llm=OpenAI(temperature=0.8, openai_api_key="")

! pip install openai

llm('What is capital Of India')

