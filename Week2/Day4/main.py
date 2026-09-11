import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    model = ChatOpenAI(
        model="gpt-4.0-mini",
        temperature=0
    )

    prompt = "Explain RAG in one simple paragraph."

    response = model.invoke(prompt)

    print("Model Response:")
    print(response.content)


if __name__ == "__main__":
    main()