from openai import OpenAI
import openai

openai.api_key = OPENAI_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message["content"])


