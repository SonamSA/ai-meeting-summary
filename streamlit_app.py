import streamlit as st
from datetime import datetime

# --- APP TITLE ---
st.title("🎙 AI Meeting Summary Assistant")
st.write("Upload a meeting audio file to generate a summary and action items.")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')
    
    # --- FAKE TRANSCRIPTION (Mock Output) ---
    st.subheader("📜 Transcript (sample)")
    transcript = """Today we discussed the Q3 roadmap. 
    John will finalize the marketing plan by next week. 
    The AI team will deliver the prototype by the next sprint. 
    Sarah suggested adding an FAQ bot feature."""
    st.write(transcript)
    
    # --- FAKE AI SUMMARY (Mock Output) ---
    st.subheader("📝 AI-Generated Summary")
    summary = """The team reviewed the Q3 roadmap, confirming timelines for marketing and AI feature delivery. 
    Key agreements were made on the prototype demo and feature prioritization."""
    st.success(summary)
    
    # --- FAKE ACTION ITEMS ---
    st.subheader("✅ Action Items")
    action_items = [
        "John: Finalize marketing plan by July 31",
        "AI Team: Deliver prototype by Sprint 3",
        "Sarah: Draft FAQ bot feature proposal"
    ]
    for item in action_items:
        st.checkbox(item, value=False)
    
    # --- FOOTER ---
    st.markdown("---")
    st.caption(f"Demo generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | AI Scrum Master Portfolio Project")
