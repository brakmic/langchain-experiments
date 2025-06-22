#!/usr/bin/env python3

import os
from langchain_community.llms.llamafile import Llamafile
from pydantic import BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from typing import List

class Answer(BaseModel):
    '''A structured answer with exploration opportunities.'''
    answer: str
    '''The main answer to the question'''
    confidence: str
    '''High, Medium, or Low'''
    related_topics: List[str]
    '''Related topics to explore further'''
    follow_up_questions: List[str]
    '''Questions that naturally follow from this answer'''

url = os.getenv("LLAMAFILE_URL", "http://localhost:8080")

llm = Llamafile(base_url=url)

parser = JsonOutputParser(pydantic_object=Answer)

prompt = PromptTemplate(
    template="""You are a programming expert. Answer the question and provide exploration data.

{format_instructions}

Question: {question}

Provide:
- An answer in full sentences (minimum 1 sentence)
- Your confidence level (High/Medium/Low)
- 2-3 related topics
- 2-3 follow-up questions

JSON response:""",
    input_variables=["question"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

question = {"question": "Should goto be used in modern programming?"}

def display_answer(answer_dict):
    """Display the structured answer in a clean, formatted way."""
    print(f"💡 {answer_dict['answer']}")
    print(f"\n🎯 Confidence: {answer_dict['confidence']}")

    print(f"\n🔗 Related Topics:")
    for topic in answer_dict['related_topics']:
        print(f"   • {topic}")

    print(f"\n❓ Follow-up Questions:")
    for question_item in answer_dict['follow_up_questions']:
        print(f"   • {question_item}")

try:
    answer = chain.invoke(question)
    # print(answer) # raw JSON output
    display_answer(answer)

except Exception as e:
    print(f"An error occurred: {e}")
    chain_no_parser = prompt | llm
    raw_output = chain_no_parser.invoke(question)
    print(f"Raw output:\n\n{raw_output}")
