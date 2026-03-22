# import streamlit as st
# import os

# from transcription import transcribe_audio
# from summarizer import summarize_text, extract_action_items
# from report_generator import generate_report
# from email_sender import send_email

# st.set_page_config(page_title="AI Meeting Assistant")

# st.title("🤖 AI Smart Meeting Assistant")

# uploaded_file = st.file_uploader("Upload Meeting Audio", type=["wav","mp3","m4a","aac"])

# email = st.text_input("Enter customer email (optional)")

# if uploaded_file:

#     os.makedirs("uploads", exist_ok=True)
#     os.makedirs("reports", exist_ok=True)

#     file_path = os.path.join("uploads", uploaded_file.name)

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.success("Audio uploaded successfully ✅")

#     if st.button("Process Meeting"):

#         with st.spinner("Processing... ⏳"):

#             transcript = transcribe_audio(file_path)

#             summary = summarize_text(transcript)

#             actions = extract_action_items(transcript)

#             report_path = "reports/meeting_report.pdf"

#             generate_report(summary, actions, report_path)

#         st.subheader("📄 Summary")
#         st.write(summary)

#         st.subheader("✅ Action Items")
#         st.write(actions)

#         with open(report_path, "rb") as f:
#             st.download_button(
#                 "⬇ Download Report",
#                 f,
#                 file_name="meeting_report.pdf"
#             )

#         if email:
#             try:
#                 send_email(email, report_path)
#                 st.success("📧 Report sent successfully")
#             except Exception as e:
#                 st.error(f"Email failed: {e}")

# import streamlit as st
# import os
# from pathlib import Path

# from transcription import transcribe_audio
# from summarizer import summarize_text, extract_action_items
# from report_generator import generate_report
# from email_sender import send_email

# # ------------------ CONFIG ------------------
# st.set_page_config(page_title="AI Meeting Assistant", layout="centered")

# st.title("🤖 AI Smart Meeting Assistant")

# # ------------------ INPUT ------------------
# uploaded_file = st.file_uploader(
#     "Upload Meeting Audio",
#     type=["wav", "mp3", "m4a", "aac"]
# )

# email = st.text_input("Enter customer email (optional)")

# # ------------------ MAIN LOGIC ------------------
# if uploaded_file is not None:

#     try:
#         # Create folders safely
#         upload_dir = Path("uploads")
#         report_dir = Path("reports")

#         upload_dir.mkdir(exist_ok=True)
#         report_dir.mkdir(exist_ok=True)

#         # Safe filename (important fix)
#         safe_filename = uploaded_file.name.replace(" ", "_")

#         file_path = upload_dir / safe_filename

#         # Save file
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         st.success("✅ Audio uploaded successfully")

#         # Debug (important for your issue)
#         st.info(f"📂 File path: {file_path}")

#     except Exception as e:
#         st.error(f"❌ File upload failed: {e}")
#         st.stop()

#     # ------------------ PROCESS BUTTON ------------------
#     if st.button("🚀 Process Meeting"):

#         with st.spinner("Processing... ⏳"):

#             try:
#                 # ---------------- TRANSCRIPTION ----------------
#                 transcript = transcribe_audio(str(file_path))

#                 if not transcript or "Error" in transcript:
#                     st.error("❌ Transcription failed")
#                     st.stop()

#                 # ---------------- SUMMARY ----------------
#                 summary = summarize_text(transcript)

#                 # ---------------- ACTION ITEMS ----------------
#                 actions = extract_action_items(transcript)

#                 # ---------------- REPORT ----------------
#                 report_path = report_dir / "meeting_report.pdf"
#                 generate_report(summary, actions, str(report_path))

#             except Exception as e:
#                 st.error(f"❌ Processing error: {e}")
#                 st.stop()

#         # ------------------ OUTPUT ------------------
#         st.subheader("📄 Summary")
#         st.write(summary)

#         st.subheader("✅ Action Items")
#         st.write(actions)

#         # Download button
#         try:
#             with open(report_path, "rb") as f:
#                 st.download_button(
#                     "⬇ Download Report",
#                     f,
#                     file_name="meeting_report.pdf"
#                 )
#         except:
#             st.error("❌ Report file not found")

#         # ------------------ EMAIL ------------------
#         if email:
#             try:
#                 send_email(email, str(report_path))
#                 st.success("📧 Report sent successfully")
#             except Exception as e:
#                 st.error(f"❌ Email failed: {e}")

import streamlit as st
from pathlib import Path

from transcription import transcribe_audio
from summarizer import summarize_text, extract_action_items
from report_generator import generate_report
from email_sender import send_email

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Meeting Assistant", layout="centered")
st.title("🤖 AI Smart Meeting Assistant")

# ---------------- INPUT ----------------
uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["wav", "mp3", "m4a", "aac"]
)

email = st.text_input("Enter customer email (optional)")

# ---------------- MAIN ----------------
if uploaded_file is not None:

    upload_dir = Path("uploads")
    report_dir = Path("reports")

    upload_dir.mkdir(exist_ok=True)
    report_dir.mkdir(exist_ok=True)

    safe_filename = uploaded_file.name.replace(" ", "_")
    file_path = upload_dir / safe_filename

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio uploaded successfully")

    if st.button("🚀 Process Meeting"):

        with st.spinner("Processing... ⏳"):

            try:
                # 🔹 Transcription
                transcript = transcribe_audio(str(file_path))

                # if not transcript or "Error" in transcript:
                #     st.error("Transcription failed")
                #     st.stop()
                if not transcript or "Error" in transcript:
                      st.error(f"Transcription failed: {transcript}")
                      print("DEBUG ERROR:", transcript)
                      st.stop()

                # 🔹 Summary
                summary = summarize_text(transcript)

                # 🔹 Actions
                actions = extract_action_items(transcript)

                # 🔹 Report
                report_path = report_dir / "meeting_report.pdf"
                generate_report(summary, actions, str(report_path))

            except Exception as e:
                st.error(f"Processing error: {e}")
                st.stop()

        # ---------------- OUTPUT ----------------
        st.subheader("Summary")
        st.write(summary)

        st.subheader("Action Items")
        st.write(actions)

        # Download
        with open(report_path, "rb") as f:
            st.download_button(
                "⬇ Download Report",
                f,
                file_name="meeting_report.pdf"
            )

        # Email
        if email:
            try:
                send_email(email, str(report_path))
                st.success("Report sent successfully")
            except Exception as e:
                st.error(f"Email failed: {e}")
