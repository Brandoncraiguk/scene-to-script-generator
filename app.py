import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit configuration
st.set_page_config(page_title="Scene-to-Script Generator", layout="centered")

# Title and description
st.title("🎬 Scene-to-Script Generator")
st.markdown("Generate short screenplay scenes from a description using GPT-3.5.")

# Input fields
scene = st.text_area("Describe your scene",
                     placeholder="e.g. A foggy alley in 1940s Chicago")
tone = st.text_input("Tone/style (optional)",
                     placeholder="e.g. noir, cinematic, surreal", value="cinematic")

# Generate button
if st.button("Generate Script"):
    if not scene.strip():
        st.warning("Please enter a scene description.")
    else:
        with st.spinner("Generating script..."):
            prompt = (
                "You are a screenwriter. Based on the following scene description, "
                f"write a short script snippet (2-3 paragraphs) in a {tone} tone.\n\n"
                f"Scene: {scene}\n\nScript:"
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8
                )

                script_output = response.choices[0].message["content"].strip()
                st.subheader("Generated Script")
                st.text(script_output)

                filename = "scene_script_output.txt"
                with open(filename, "w") as f:
                    f.write(f"Scene Description: {scene}\n\n")
                    f.write(script_output)

                with open(filename, "r") as f:
                    st.download_button("Download Script", f,
                                       file_name=filename)

            except Exception as e:
                st.error(f"An error occurred: {e}")
