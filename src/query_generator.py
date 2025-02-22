from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # make sure to have your OPENAI API key saved in the .env file

OPENAI_model = "gpt-4"
openai = OpenAI()   

system_prompt = """
    You are an assistant which takes an input a query written in natural language
    and converts this into a well structured SQL query.
    Do not provide or explaination of the query, just the query.
"""

# Formatting the user prompt
def user_prompt_for(nlp_query):
    user_prompt = f"Convert the following request into an SQL query: {nlp_query}"
    return user_prompt

# Generates an SQL query from natural language input using above defined model
def generate_sql(nlp_query):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(nlp_query)}
    ]

    # Call OpenAI
    response = openai.chat.completions.create(
        model=OPENAI_model, messages=messages, temperature=0.1
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    user_query = "Show me all customers from Canada."
    sql_query = generate_sql(user_query)
    print(sql_query)