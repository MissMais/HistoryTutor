from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API = os.getenv("API_KEY")

user = st.text_input('Ask a question')

client = Groq(api_key=API)

st.title('How Can History Professor Helps You??')

if user:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a History Tutor. Give only historical information. When asked a question about some other subject, reply I don't know."},
            {"role": "user", "content": user}
        ],
        temperature=0.7)
    st.text(response.choices[0].message.content)


# import google.generativeai as genai

# genai.configure(api_key="AIzaSyBu83FKc8Rpo0CNpXFZjPc_uTUGWyVisT8")

# model = genai.GenerativeModel(
#     model_name='gemini-2.5-flash-lite',
#     system_instruction="""You are a History Tutor.
#                         - Provide general information only.
#                         - Reply in a paragraph format.""")


# response = model.generate_content("Who built the Taj Mahal")
# print(response.candidates[0].content.parts[0].text)

