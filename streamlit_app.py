import streamlit as st
from agents.application_agent import run_application_agent_with_inputs

st.title(" Hi, your Summer Job Application Assistant is ready to assist you!! 🌞")

# Initialize session state
if "resume" not in st.session_state:
    st.session_state.resume = None
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = None

# Input Form
with st.form("job_app_form"):
    name = st.text_input("Your Name", "Emma Garcia")
    email = st.text_input("Email", "emma.garcia@example.com")
    phone = st.text_input("Phone Number", "(555) 123-4567")
    age = st.text_input("Age", "16")
    grade = st.text_input("Grade", "11th")
    interests = st.text_input("Interests", "Psychology, writing, social work")
    skills = st.text_input("Skills", "Communication, empathy, teamwork")
    experience = st.text_area("Work/Volunteer Experience", "Volunteered at a local library and babysat neighbors")
    availability = st.text_input("Availability", "June 5 to August 15, weekdays")
    job_type = st.text_input("Job Type", "Camp counselor")

    submitted = st.form_submit_button("Generate Application")

# Run agent after form submission
if submitted:
    with st.spinner("Generating your resume and cover letter..."):
        result = run_application_agent_with_inputs(
            name, email, phone, age, grade, interests, skills, experience, availability, job_type
        )
        st.session_state.resume = result["resume"]
        st.session_state.cover_letter = result["cover_letter"]
    st.success(" Application Documents Generated!")

# Display results and download buttons
if st.session_state.resume and st.session_state.cover_letter:
    st.subheader("📄 Resume")
    st.text(st.session_state.resume)

    st.subheader("✉️ Cover Letter")
    st.text(st.session_state.cover_letter)

    st.download_button("Download Resume", st.session_state.resume, file_name="resume.txt")
    st.download_button("Download Cover Letter", st.session_state.cover_letter, file_name="cover_letter.txt")

    if st.button("🔁 Reset Application"):
        st.session_state.resume = None
        st.session_state.cover_letter = None
        st.rerun()
