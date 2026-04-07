import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

class ExcelChatBot:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    def ask(self, query: str, context: str = ""):
        messages = [
            SystemMessage(content="你是一个 Excel 校验助手。"),
            HumanMessage(content=f"上下文: {context}\n\n问题: {query}")
        ]
        return self.llm.invoke(messages).content