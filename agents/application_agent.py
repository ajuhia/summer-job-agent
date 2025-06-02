from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
import streamlit as st

def run_application_agent_with_inputs(name, email, phone, age, grade, interests, skills, experience, availability, job_type):
    user_info = f"""Name: {name}
Email: {email}
Phone: {phone}
Age: {age}
Grade: {grade}
Interests: {interests}
Skills: {skills}
Experience: {experience}
Availability: {availability}
Job Preference: {job_type}"""

    llm = ChatGroq(api_key=st.secrets["GROQ_API_KEY"], temperature=0.3, model_name="llama3-70b-8192")

    resume_prompt = ChatPromptTemplate.from_template("""
You are a resume writer assistant.

Using the following user information, generate a professional resume suitable for a high school student applying for a summer job.

IMPORTANT: Output only the resume content. Do not include any preamble, explanation, or headings outside of the resume sections. Do not hallucinate or make up any information.

{user_info}

Format the resume as following sections:
1. Name and Contact Info
2. Objective
3. Education
4. Skills
5. Work/Volunteer Experience
6. Availability
""")

    cover_letter_prompt = ChatPromptTemplate.from_template("""
You are a cover letter assistant.

Using the following user profile, generate a short, personalized, and sincere cover letter for a summer job.

IMPORTANT: Output only the letter. Do not include any preamble or explanation.

{user_info}

Tone: Friendly, responsible, and motivated.
Keep the letter under 200 words.
Start directly with the letter content.
""")

    resume = llm.invoke(resume_prompt.format_messages(user_info=user_info))
    cover_letter = llm.invoke(cover_letter_prompt.format_messages(user_info=user_info))

    return {
        "resume": resume.content,
        "cover_letter": cover_letter.content
    }
