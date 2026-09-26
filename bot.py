
import streamlit as st
import ollama

st.title("My AI chatboat")
st.subheader("welcome!Ask something to AI and it will respond to you")


prompt=st.text_input("Ask AI something",
                     placeholder="Type your prompt here ....")


if st.button("generate"):
    if prompt:
        st.success("your prompt is:" +prompt)

    else:
        st.error("please enter a prompt to get response")
    response=ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    st.write(response['message']['content'])