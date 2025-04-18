from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
import streamlit as st

import os
from langchain.memory import ConversationKGMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key=st.secrets["OPENAI_API_KEY"],
                       openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input":prompt})
    return response ["response"]