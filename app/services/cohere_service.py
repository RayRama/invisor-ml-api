from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from app.utils.helper_function import generate_question_prompt, generate_feedback_prompt
import os

COHERE_API_KEY = os.getenv('COHERE_KEY')
llm = ChatCohere(cohere_api_key=COHERE_API_KEY, max_tokens=128, temperature=0.2)

def generate_question_jobdesc(jobdesc: str = "Hello world", jobtitle: str = "Hello world"):
    prompt = generate_question_prompt(jobdesc, jobtitle)
    llm_chain = prompt | llm

    return llm_chain.invoke({
        "jobdesc": jobdesc,
        "jobtitle": jobtitle
    })

def generate_feedback_answer(candidate_answer: str = "Hello world", question: str = "Hello world"):
    prompt = generate_feedback_prompt(candidate_answer, question)
    llm_chain = prompt | llm

    return llm_chain.invoke({"candidate_answer": candidate_answer, "question": question})