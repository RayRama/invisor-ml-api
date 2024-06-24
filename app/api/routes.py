import json
import os
from . import api_blueprint
from flask import request, jsonify
# from app.services.openai_service import generate_question_jobdesc
from app.services.cohere_service import generate_question_jobdesc, generate_feedback_answer

@api_blueprint.route('/api/test', methods=['GET'])
def test():
    return jsonify({"response": "Hello World"})

@api_blueprint.route('/api/generate-question', methods=['POST'])
def generate_question():
    body = request.json
    jobtitle = body.get('job_title')
    jobdesc = body.get('job_description')

    # Read Authorization type "API Key" header from postman
    access_key = request.headers.get('Authorization').split(" ")[1] if request.headers.get('Authorization') else None

    if access_key is None or access_key != os.getenv('ACCESS_KEY'):
        return jsonify({"error": "Unauthorized"}), 401

    # Error handling
    if jobtitle is None or jobtitle == "":
        return jsonify({"error": "job_title is required"}), 400
    if jobdesc is None or jobdesc == "":
        return jsonify({"error": "job_description is required"}), 400

    try:
        questions = generate_question_jobdesc(jobdesc, jobtitle)
        response = dict({
            "message": "Success",
            "error": False,
            "data": {
                "job_title": jobtitle,
                "job_description": jobdesc,
                "questions": [
                    {
                        "question": question
                    } for question in json.loads(questions.content)
                ]
            }
        })
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/api/user-answer', methods=['POST'])
def generate_feedback():
    # args = request.args
    # candidate_answer = args.get('candidate_answer', default="Hello world")
    # question = args.get('question', default="Hello world")
    # response = generate_feedback_answer(candidate_answer, question)
    # return jsonify({"response": response.content})
    interviews = request.json.get('interviews')
    job_title = request.json.get('job_title')
    job_description = request.json.get('job_description')

    # Read
    access_key = request.headers.get('Authorization').split(" ")[1] if request.headers.get('Authorization') else None

    if access_key is None or access_key != os.getenv('ACCESS_KEY'):
        return jsonify({"error": "Unauthorized"}), 401

    if interviews is None or len(interviews) == 0:
        return jsonify({"error": "interviews is required"}), 400

    try:
        response = []
        for interview in interviews:
            question = interview.get('question')
            answer = interview.get('answer')

            feedbacks = generate_feedback_answer(candidate_answer=answer, question=question)

            response.append({
                "question": question,
                "answer": answer,
                "feedback": json.loads(feedbacks.content)[0],
                "score": json.loads(feedbacks.content)[1]
            })

        final_response = {
            "message": "Success",
            "error": False,
            "data": {
                "job_title": job_title,
                "job_description": job_description,
                "feedbacks": response
            }
        }
        return jsonify(final_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
