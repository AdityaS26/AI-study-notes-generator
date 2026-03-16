
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Study Notes Generator")

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

generator = load_model()

st.title("📚 AI Study Notes Generator")
st.write("Enter a study topic and generate notes, key points, summary, and exam questions using Generative AI.")

topic = st.text_input("Enter a topic (Example: Database Normalization, Operating System Scheduling)")

if st.button("Generate Notes"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        prompt = f"""Create study notes for the topic: {topic}.

        Give output in this format:
        1. Explanation
        2. Key Points (bullet list)
        3. Short Summary
        4. Five Important Exam Questions
        """

        with st.spinner("Generating notes..."):
            result = generator(prompt, max_length=300, do_sample=True)
            text = result[0]["generated_text"]

        st.subheader("Generated Study Notes")
        st.write(text)
