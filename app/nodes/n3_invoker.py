import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

def invoke_node(state):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    response = llm.invoke([HumanMessage(content=state['final_prompt'])])
    content = response.content.strip()
    if content.startswith("```json"):
        content = content.split("```json")[1].split("```")[0].strip()
    elif content.startswith("```"):
        content = content.split("```")[1].split("```")[0].strip()
    return {"llm_raw_response": json.loads(content)}