from langchain_google_genai import ChatGoogleGenerativeAI

def model_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
    )
    return llm

