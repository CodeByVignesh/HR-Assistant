import streamlit as st

from src.main import answer_user_query


st.set_page_config(
    page_title="HR Assistant",
    page_icon="HR",
    layout="centered"
)

st.title("HR Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, ask me anything about the HR policy document.",
        }
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_query = st.chat_input("Ask about leave policy, benefits, attendance...")

if user_query:
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Searching the HR policy document..."):
            try:
                answer = answer_user_query(user_query)
            except Exception as error:
                answer = (
                    "I could not process that question. Please check your API keys, "
                    "Pinecone index, and stored document embeddings."
                )
                st.exception(error)

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )