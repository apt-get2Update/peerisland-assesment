# llm.py
from langchain_openai import ChatOpenAI
from app.config import MAX_TOKENS

llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-3.5-turbo-16k",
    max_tokens=MAX_TOKENS
)