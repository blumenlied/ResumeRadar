import json
import os
import base64

from modules.pdf import parse, clean_text
from modules.gemini import grade
from modules.create_report import generate_resume_grade_pdf
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/process")
async def process_resume(
    resume: UploadFile = File(...), job_description: str = Form(...)
):
    try:
        resume_pdf_file = await resume.read()
        resume_text = parse(resume_pdf_file)
        job_description = clean_text(job_description)

        scores = grade(resume_text, job_description)

        if "error" in scores:
            return JSONResponse(content=scores, status_code=400)

        report_filename = (
            "/home/stephen/myrepo/resume/front/src/lib/pdf/ResumeRadarReport.pdf"
        )
        generate_resume_grade_pdf(scores, filename=report_filename)

        # Encode the PDF file content into Base64
        resume_base64 = base64.b64encode(resume_pdf_file).decode("utf-8")

        return {"scores": scores, "resume_pdf_file": resume_base64}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
