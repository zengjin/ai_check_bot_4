import os
import streamlit as st
from app.core.agent import create_workflow
from app.core.chatbot import ExcelChatBot
from app.utils.file_io import RuleFileManager

class WorkflowController:
    def __init__(self):
        self.workflow = create_workflow()
        self.rule_manager = RuleFileManager()
        self.chatbot = ExcelChatBot()
    def run_validation(self, f1, f2, scene_name):
        os.makedirs('data', exist_ok=True)
        p1, p2 = f"data/v1_{f1.name}", f"data/v2_{f2.name}"
        with open(p1, "wb") as f: f.write(f1.getbuffer())
        with open(p2, "wb") as f: f.write(f2.getbuffer())
        rules = self.rule_manager.read_rule(scene_name)
        inputs = {"file_path_v1": p1, "file_path_v2": p2, "rules_text": rules, "diff_data": [], "llm_raw_response": {}, "output_path": "data/output_marked.xlsx"}
        return self.workflow.invoke(inputs)