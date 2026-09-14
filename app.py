import streamlit as st

st.set_page_config(page_title = "Project Phoenix Copilot")

st.title("Project Phoenix Delivery Copilot")
st.write("Ask a question about the project")

question= st.text_input("Your question")

if question:
    st.info("No answer engine yet - arriving soon")