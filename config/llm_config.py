import os

from dotenv import load_dotenv

from crewai import LLM


load_dotenv()


groq_llm = LLM(

    model="groq/llama-3.1-70b-versatile",

    api_key=os.environ.get(
        "GROQ_API_KEY"
    ),

    temperature=0.3

)
