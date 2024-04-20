import streamlit as st
st.set_page_config(layout="wide")
tab1, tab2 = st.tabs(["Tab1", "Tab2"])    
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []
if "sum_history" not in st.session_state:
    st.session_state.sum_history = []
with tab1:
    qa_messages = st.container(height=500, border=False)
    prompt_tab1 = st.chat_input("Say something", key="tab1")
    if prompt_tab1:
        st.session_state.qa_history.append({"role": "user", "content": prompt_tab1})
        st.session_state.qa_history.append({"role": "assistant", "content": f'Echo: {prompt_tab1}'})
    for message in st.session_state.qa_history:
        qa_messages.chat_message(message["role"]).write(message["content"])

with tab2:
    sum_messages = st.container(height=500, border=False)
    prompt_tab2 = st.chat_input("Say something", key="tab2")
    if prompt_tab2:
        st.session_state.sum_history.append({"role": "user", "content": prompt_tab2})
        st.session_state.sum_history.append({"role": "assistant", "content": f'Echo: {prompt_tab2}'})
    for message in st.session_state.sum_history:
        sum_messages.chat_message(message["role"]).write(message["content"])