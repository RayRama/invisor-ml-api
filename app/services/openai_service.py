from langchain_openai import ChatOpenAI
from app.utils.helper_function import generate_question_prompt, generate_feedback_prompt
import os

OPENAI_API_KEY = os.getenv('OPENAI_KEY')
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.2, api_key=OPENAI_API_KEY)

def generate_question_jobdesc(jobdesc: str = "Hello world"):
    llm_chain = generate_question_prompt(jobdesc) | llm

    return llm_chain.invoke(jobdesc)