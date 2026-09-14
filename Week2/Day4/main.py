import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

prompt = "Explain RAG in one simple paragraph."

response = model.invoke(prompt)

print("Model Response:")
print(response.content)

