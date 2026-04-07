import streamlit as st
from web.controller import WorkflowController
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="AI Assistant", layout="wide")
if "ctl" not in st.session_state: st.session_state.ctl = WorkflowController()
ctl = st.session_state.ctl
def main():
    st.sidebar.title("🛠️ 管理面板")
    scenes = ctl.rule_manager.get_scenes()
    selected_scene = st.sidebar.selectbox("当前业务场景", scenes)
    t1, t2, t3 = st.tabs(["📊 自动校验", "💬 AI 问答", "⚙️ 规则维护"])
    with t1:
        u1 = st.file_uploader("V1", type="xlsx", key="u1")
        u2 = st.file_uploader("V2", type="xlsx", key="u2")
        if st.button("🚀 开始校验") and u1 and u2:
            res = ctl.run_validation(u1, u2, selected_scene)
            st.session_state.last_res = str(res['llm_raw_response'])
            st.success("分析完成！")
            with open("data/output_marked.xlsx", "rb") as f:
                st.download_button("📥 下载结果", f, file_name="report.xlsx")
    with t2:
        if "msgs" not in st.session_state: st.session_state.msgs = []
        for m in st.session_state.msgs: st.chat_message(m['role']).write(m['content'])
        if p := st.chat_input("询问更多细节..."):
            st.session_state.msgs.append({"role": "user", "content": p})
            ans = ctl.chatbot.ask(p, st.session_state.get("last_res", ""))
            st.session_state.msgs.append({"role": "assistant", "content": ans})
            st.rerun()
    with t3:
        txt = ctl.rule_manager.read_rule(selected_scene)
        new = st.text_area("编辑规则", value=txt, height=300)
        if st.button("保存"): ctl.rule_manager.save_rule(selected_scene, new); st.success("已保存")
if __name__ == "__main__": main()