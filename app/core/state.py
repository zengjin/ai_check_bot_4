from typing import TypedDict, List, Dict, Any, Optional
class WorkflowState(TypedDict):
    file_path_v1: str
    file_path_v2: str
    rules_text: str
    diff_data: List[Dict[str, Any]]
    final_prompt: str
    llm_raw_response: Dict[str, Any]
    output_path: str