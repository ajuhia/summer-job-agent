# Summer Job Application Generator

This is a LangChain + Groq-powered application that helps generate professional resumes and cover letters tailored for high school students applying for summer jobs. It takes basic user input, processes it through an autonomous agent, and outputs clean application materials using a simple Streamlit interface.
#### Notes
- Ideal for helping students apply to internships or part-time roles during summer break.


## Project Structure

```
SummerJobAppAgent/
├── agents/
│   └── application_agent.py       # Defines LangChain-based agent to generate resume and cover letter
│
├── tools/
│   └── profile_collector.py       # Collects and manages user's input profile
│
├── streamlit_app.py               # Streamlit interface for interaction and display
├── requirements.txt               # Required Python packages
├── .streamlit/
│   └── secrets.toml               # Stores your Groq API key securely for Streamlit
├── README.md                      # Documentation
```

## Features

- Accepts structured input (name, age, experience, etc.) from high school students
- Automatically generates a personalized resume
- Creates a tailored and concise cover letter with appropriate tone
- Uses LangChain with Groq LLM (`llama3-70b-8192`) for generation
- User-friendly web interface via Streamlit

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SummerJobAppAgent.git
cd SummerJobAppAgent
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key in `secrets.toml`

In the `.streamlit/secrets.toml` file, add your Groq API key like this:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Streamlit will automatically make this accessible via `st.secrets["GROQ_API_KEY"]`.

### 5. Run the App

```bash
streamlit run streamlit_app.py
```

## Requirements

- Python 3.9 or later
- Packages listed in `requirements.txt`:
  - langchain
  - groq
  - python-dotenv (if `.env` fallback is needed)


