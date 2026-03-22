# import whisper
# from pydub import AudioSegment
# import os

# # Load model (better accuracy than tiny)
# model = whisper.load_model("base")

# def convert_audio(input_path):
#     try:
#         if input_path.endswith(".aac") or input_path.endswith(".m4a"):
#             output_path = input_path + ".wav"
#             audio = AudioSegment.from_file(input_path)
#             audio.export(output_path, format="wav")
#             return output_path
#         return input_path
#     except Exception as e:
#         print("Conversion error:", e)
#         return input_path

# def transcribe_audio(audio_path):
#     try:
#         audio_path = convert_audio(audio_path)

#         # ✅ FIX: pass file path directly
#         result = model.transcribe(audio_path)

#         return result["text"]

#     except Exception as e:
#         return f"Error: {str(e)}"

# import whisper


# model = whisper.load_model("base")

# def transcribe_audio(audio_path):
#     try:
#         print("Processing file:", audio_path)

#         # 🔥 FORCE Whisper to handle everything
#         result = model.transcribe(audio_path)

#         print("Transcription success")

#         return result["text"]

#     except Exception as e:
#         print("TRANSCRIPTION ERROR:", e)
#         return f"Error: {str(e)}"

import whisper
import os
# load model once
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    try:
        print("Processing:", audio_path)

        result = model.transcribe(audio_path)

        print("Done")

        return result["text"]

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"
