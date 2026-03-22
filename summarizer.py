# from transformers import pipeline
# import nltk

# try:
#     nltk.data.find('tokenizers/punkt')
# except LookupError:
#     nltk.download('punkt')

# from nltk.tokenize import sent_tokenize

# summarizer = pipeline(
#     "summarization",
#     model="sshleifer/distilbart-cnn-12-6"
# )

# def summarize_text(text):
#     chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

#     summary = ""
#     for chunk in chunks:
#         result = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
#         summary += result[0]['summary_text'] + " "

#     return summary

# def extract_action_items(text):
#     sentences = sent_tokenize(text)
#     keywords = ["should", "must", "need", "todo", "action"]

#     actions = []
#     for s in sentences:
#         if any(word in s.lower() for word in keywords):
#             actions.append(s)

#     return actions

from transformers import pipeline
import nltk

# download punkt once
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# 🔥 FIX: use supported task
summarizer = pipeline(
    "text2text-generation",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=100, min_length=30)
        summary += result[0]['generated_text'] + " "

    return summary

def extract_action_items(text):
    sentences = sent_tokenize(text)
    keywords = ["should", "must", "need", "todo", "action"]

    actions = []
    for s in sentences:
        if any(word in s.lower() for word in keywords):
            actions.append(s)

    return actions
