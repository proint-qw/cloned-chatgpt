import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

def clear_chat_history():
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                   "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

st.title("💬 克隆ChatGPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    st.button("🔄 开启新会话", on_click=clear_chat_history)
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入OpenAI的API秘钥")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)