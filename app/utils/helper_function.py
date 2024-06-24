from langchain_core.prompts import PromptTemplate

def generate_question_prompt(jobdesc: str = "Hello world", jobtitle: str = "Hello world"):
    template = """
    You are a professional HR that can give a professional and related question to the candidate. He want to apply for the {jobtitle} position.
    Based on the job description below, please give them 5 questions that you think are relevant to the job description.
    Only give related questions to the job description response without opening or something else like "Here are five interview question...".
    Make sure your answer is formated like this: ["question 1", "question 2", "question 3", "question 4", "question 5"]
    
    Job Description:
    {jobdesc}
    """
    final_prompt = PromptTemplate.from_template(template)
    return final_prompt

def generate_feedback_prompt(candidate_answer: str = "Hello world", question: str = "Hello world"):
    template = """
    You are a professional HR that can give a professional and related feedback to the candidate. You ask the candidate {question}.
    Based on the candidate answer, please give them feedback for this question below. Make sure the feedback is objective, critical, and related to the question and the candidate answer.
    Please answer to the point and make sure the feedback is constructive, and give them score from 1-100 (make sure the score on string format).
    Make sure your answer is formated like this: ["feedback", "score"]
    
    Candidate answer:
    {candidate_answer}
    """
    final_prompt = PromptTemplate.from_template(template)
    return final_prompt