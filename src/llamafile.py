#!/usr/bin/env python3
import os
from langchain_community.llms.llamafile import Llamafile
from langchain_core.messages import HumanMessage, SystemMessage

url = os.getenv("LLAMAFILE_URL", "http://localhost:8080")

llm = Llamafile(base_url=url)

system_msg = SystemMessage('''
You are a helpful assistant that responds to user questions.
''')

prompt = HumanMessage("What is the capital of Germany?")

response = llm.invoke([system_msg, prompt])
print(response)
