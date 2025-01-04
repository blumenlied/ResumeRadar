import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
api_key = os.getenv("MY_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

header = {"Content-Type": "application/json"}


def grade(resume, job_description):
    prompt = f"""
    RESUME TEXT: {resume}
    JOB DESCRIPTION: {job_description}

    INSTRUCTIONS:

    Grade the provided resume based on the given job description. Give actionable feedback for each category. Consider the following criteria and provide scores out of 100 for each category, and an overall score which can be calculated using this formula:
    Overall = (Relevance score * 35) + (Experience * 35) + (Skill Demonstration * 15) + (Professionalism * 15).

    Relevance: (weight - 35)
    How well does the resume match the keywords and requirements of the job description?
    Does the resume effectively highlight the most relevant skills and experiences for this specific role?

    Experience: (weight - 35)
    Does the experience section clearly demonstrate relevant skills and accomplishments?
    Does the resume provide sufficient detail about past roles and responsibilities?

    Skill Demonstration: (weight - 15)
    Does the resume effectively use action verbs and quantify achievements? (e.g., "Increased sales by 15%", "Managed a team of 5", "Reduced costs by 10%")
    Does the resume provide specific examples of how the candidate has applied their skills in past roles?

    Professionalism: (weight - 15)
    Is the resume free of any spelling, grammar, or punctuation errors?
    Is the writing style professional, concise, and easy to read? (e.g., active voice, appropriate tone, ignore spacing between the lines.)

    Output the results in the following JSON format:

    {{
        "name": "<string>",
        "email": "<string>",
        "education": "<string>",
        "scores": {{
            "Relevance": {{
                "score": <int>,
                "feedback_title": "<string>",
                "feedback": "<string>"
            }},
            "Experience": {{
                "score": <int>,
                "feedback_title": "<string>",
                "feedback": "<string>"
            }},
            "Skill Demonstration": {{
                "score": <int>,
                "feedback_title": "<string>",
                "feedback": "<string>"
            }},
            "Professionalism": {{
                "score": <int>,
                "feedback_title": "<string>",
                "feedback": "<string>"
            }}
        }},
        "overall_comment": "<string>",
        "overall_score": <float>
    }}
    """

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, headers=header, data=json.dumps(payload))

    if response.status_code == 200:
        json_response = response.json()

        output_text = json_response["candidates"][0]["content"]["parts"][0]["text"]

        output_text = (
            output_text.strip("```").replace("json\n", "").replace("\n```", "")
        )
        try:
            return json.loads(output_text)

        except json.JSONDecodeError:
            return "Error: Failed to decode the JSON response."
    else:
        return f"Error {response.status_code}: {response.text}"

