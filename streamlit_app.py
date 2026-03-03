import streamlit as st
import os
from app.core.pipeline import TalkSyncPipeline
from app.config import LANGUAGE_MAP

st.set_page_config(page_title="TalkSync", layout="wide")

st.title(" TalkSync - Real-Time Translation Solution")
st.markdown("Enable seamless communication between English and Hindi/Punjabi speakers during client calls.")

pipeline = TalkSyncPipeline()

# Sidebar Settings
st.sidebar.header("Language Settings")

source_language_name = st.sidebar.selectbox(
    "Source Language",
    options=list(LANGUAGE_MAP.keys())
)

target_language_name = st.sidebar.selectbox(
    "Target Language",
    options=list(LANGUAGE_MAP.keys())
)

source_lang = LANGUAGE_MAP[source_language_name]
target_lang = LANGUAGE_MAP[target_language_name]

st.subheader("Upload Client Audio (.wav)")
uploaded_file = st.file_uploader("Upload audio file", type=["wav"])

st.subheader("Or Use Demo Audio")

demo_files = {
    "Client Introduction": "demo_data/client_intro.wav",
    "Project Discussion": "demo_data/project_discussion.wav"
}

demo_choice = st.selectbox("Select Demo Audio", options=["None"] + list(demo_files.keys()))

audio_path = None

if uploaded_file:
    audio_path = f"temp_{uploaded_file.name}"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

elif demo_choice != "None":
    audio_path = demo_files[demo_choice]

if audio_path:
    if st.button(" Start Translation"):
        with st.spinner("Processing Translation..."):
            transcript, translation, audio_output = pipeline.process(
                audio_path,
                source_lang,
                target_lang
            )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(" Transcript")
            st.write(transcript)

        with col2:
            st.subheader(" Translated Output")
            st.write(translation)

        st.subheader(" Audio Playback")
        audio_file = open(audio_output, "rb")
        st.audio(audio_file.read(), format="audio/mp3")