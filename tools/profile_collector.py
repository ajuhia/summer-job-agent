def collect_user_profile() -> str:
    name = input("What is your name? ")
    age = input("How old are you? ")
    grade = input("What grade are you in? ")
    interests = input("What are your interests or favorite school subjects? ")
    skills = input("What skills do you have (e.g., communication, teamwork)? ")
    experience = input("Have you had any work/volunteer experience? Describe briefly. ")
    availability = input("What dates or hours are you available this summer? ")
    job_type = input("What kind of job are you looking for? (e.g., camp counselor, cashier, office assistant) ")

    return f"""
Name: {name}
Age: {age}
Grade: {grade}
Interests: {interests}
Skills: {skills}
Experience: {experience}
Availability: {availability}
Job Preference: {job_type}
"""