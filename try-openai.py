#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "openai",
#     "dotenv"
# ]
# ///

from openai import OpenAI
from dotenv import load_dotenv
import os 

# make sure you have a .env file with 
# OPENAI_API_KEY and OPENAI_BASE_URL defined!
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

client = OpenAI(
    api_key =  OPENAI_API_KEY,
    base_url = OPENAI_BASE_URL
)

# List all available models
models = client.models.list()

# Sort the models by ID
sorted_model_names = sorted(models.data, key=lambda x: x.id)

# Print model IDs
print("Models available:")
for model in sorted_model_names:
    print(f"\t{model.id}")

question = "What are three pieces of advice you'd give to a college student for their first semester?"

print()
print(question)
print()

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": question}
    ]
)
print(response.choices[0].message.content)
