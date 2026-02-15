
import streamlit as st
from persona_analyzer import build_persona
from message_generator import generate_message
from image_generator import generate_image

st.title("AI Business Growth Assistant")

product=st.text_input("Product")
audience=st.text_input("Audience")
platform=st.selectbox("Platform",["Instagram","Facebook","TikTok"])
tone=st.selectbox("Tone",["Friendly","Professional","Bold"])

style=st.selectbox("Image Style",["Realistic","Minimal","Bold","Custom"])
custom=""
if style=="Custom":
    custom=st.text_input("Custom style")

if st.button("Generate Persona"):
    st.write(build_persona(product,audience))

if st.button("Generate Message"):
    st.write(generate_message(product,audience,tone,platform))

if st.button("Generate Image"):
    img=generate_image(product,audience,style,custom)
    st.image(img)
