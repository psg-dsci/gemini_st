# Basic Fake News Detection App using Gemini API
import streamlit as st 
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API Key
load_dotenv()

# Configuring the GEN-AI App
genai.configure(api_key = "AIzaSyChmrkzlnlX1Yh3uiNaFZfdnir_Ix-6n5U")

# User Defined prompt for the News Detection
prompt = """
Given a news item, your task is to analyze its credibility and content. If the news item is determined to be fake, your model should also generate a plausible true version of the news story. Consider the following steps:
Classify the news: Classify the News is true or not
(i) Analyze the Content: Evaluate the news item based on its content. Look for signs of manipulation, exaggeration, or misinformation. Consider the source's reputation and the context in which the news is presented.
(ii) Consider the Context: The credibility of a news item is often influenced by the context in which it is shared. Assess the social, political, and cultural background that might affect the perception of the news.
(iii) Evaluate Supporting Evidence: If the news item is found to be fake, consider what the true story might be. Look for any evidence that contradicts the false information and construct a plausible true version of the news.
(iv) Generate a True Version: If the news item is deemed fake, generate a true version of the news story. This should be a plausible narrative that aligns with the facts and addresses the misinformation presented in the original news item.
The News is given after the ending of this sentence. News is :
"""

# Gemini Response to get the Classification of the News
def get_gemini_response(prompt, news):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + news)
    return response.text

# Initializing the Strealit App
st.title("Detection of Fake News using NLP")
news = st.text_area("Enter the News you want to classify")
check = st.button("Click to get the Result")

if check:
    response_news = get_gemini_response(prompt, news)
    st.subheader("Detected Result is :")
    st.write(response_news)
