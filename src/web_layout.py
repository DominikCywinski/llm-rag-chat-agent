### Layout of web application ###

import streamlit as st


def create_layout():
    st.set_page_config(page_title="Agent", page_icon="🤖")

    st.markdown(
        '<h1 style="text-align: center;">Chat with Agent</h1>',
        unsafe_allow_html=True,
    )

    if "input" not in st.session_state:
        st.session_state.input = ""

    user_input = st.text_input(
        "Input Question: ",
        key="input",
        placeholder="Enter your question",
    )

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        submit_clicked = st.button("Ask the Question")

    return user_input, submit_clicked


def show_results(user_input, response):
    st.subheader("Your Question:")
    st.header(user_input)
    st.subheader("Result:")
    st.header(response)
    print("Result: ", response)
