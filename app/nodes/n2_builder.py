import json
def build_node(state):
    rules = state['rules_text']
    data_json = json.dumps(state['diff_data'], ensure_ascii=False, indent=2)
    prompt = f"""你是一个专业的数据审计专家。请根据提供的 [校验规则] 对 [数据列表] 进行审核。
    
[校验规则]
{rules}

[数据列表]
{data_json}

[输出要求]
必须返回纯 JSON 格式，不得包含任何 Markdown 格式。
Key 为数据中的 ID (或第一列的值)，Value 为对象 {{"is_error": bool, "reason": "错误描述"}}。"""
    return {"final_prompt": prompt}