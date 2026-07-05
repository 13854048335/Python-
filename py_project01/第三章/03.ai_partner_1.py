import os
import streamlit as st
from openai import OpenAI
# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")
#Logo
st.logo("./resources/logo.png")

import streamlit as st
systme_prompt = "你是一个AI助理，请使用正式的语气回答客户的问题"
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


# 输入框
prompt = st.chat_input("请输入你要问的问题：")
if prompt:  # 字符串自动转换为布尔值，如果字符串非空，则返回True
    st.chat_message("user").write(prompt)
    print(f"调用AI大模型，提示词：{prompt}")
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型
    # 创建与AI大模型交互的客户端
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")
    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": systme_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
    )
    print("--------->大模型返回的结果",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
