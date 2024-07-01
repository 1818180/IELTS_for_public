import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env.local')

http_proxy = os.getenv('HTTP_PROXY')
https_proxy = os.getenv('HTTPS_PROXY')
API_KEY = os.getenv('API_KEY')

# http_proxy = st.secrets['HTTP_PROXY']
# https_proxy = st.secrets['HTTPS_PROXY']
# API_KEY = st.secrets['API_KEY']

genai.configure(api_key=API_KEY)

def modle_names():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

# models/gemini-1.0-pro
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest       
# models/gemini-1.0-pro-vision-latest
# models/gemini-1.5-flash
# models/gemini-1.5-flash-001        
# models/gemini-1.5-flash-latest     
# models/gemini-1.5-pro
# models/gemini-1.5-pro-001
# models/gemini-1.5-pro-latest       
# models/gemini-pro
# models/gemini-pro-vision

def get_gm_1answer(question, ai_model):
    model = genai.GenerativeModel(ai_model)
    raw_response = model.generate_content(question)
    response = raw_response.text
    return response


if __name__ == "__main__":
    # test_question = "雅思写作的评判标准有哪些呢？帮我简要概述一下"
    # test_answer = get_gm_1answer(test_question)
    # print(test_answer)
    modle_names()