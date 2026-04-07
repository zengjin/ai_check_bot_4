from langgraph.graph import StateGraph, END
from app.core.state import WorkflowState
from app.nodes.n1_extractor import extract_node
from app.nodes.n2_builder import build_node
from app.nodes.n3_invoker import invoke_node
from app.nodes.n4_editor import edit_node

def create_workflow():
    workflow = StateGraph(WorkflowState)
    workflow.add_node("n1", extract_node)
    workflow.add_node("n2", build_node)
    workflow.add_node("n3", invoke_node)
    workflow.add_node("n4", edit_node)
    workflow.set_entry_point("n1")
    workflow.add_edge("n1", "n2")
    workflow.add_edge("n2", "n3")
    workflow.add_edge("n3", "n4")
    workflow.add_edge("n4", END)
    return workflow.compile()