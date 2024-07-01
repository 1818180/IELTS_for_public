import openai
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# load_dotenv(dotenv_path='.env.local')
# DS_API_KEY = os.getenv('DEEPSEEK_KRY')

DS_API_KEY = st.secrets['DEEPSEEK_KRY']

client = OpenAI(api_key=DS_API_KEY, base_url="https://api.deepseek.com")

def get_ds_1answer(question):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "assistant", "content": "一个非常专业的雅思老师"},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except openai.error.APIConnectionError:
        return None


if __name__ == "__main__":
    test_question = "雅思写作的评判标准有哪些呢？帮我简要概述一下"
    test_answer = get_ds_1answer(test_question)
    print(test_answer.choices[0].message.content)
