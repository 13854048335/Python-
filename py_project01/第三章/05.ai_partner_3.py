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

systme_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
规则:
1.每次只回1条消息
2.禁止任何场景或状态描述性文字
3.匹配用户的语言
4.回复简短，像微信聊天一样
5.有需要的话可以用6.用符合伴侣性格的方式对话
等emoji表情
7.回复的内容，要充分体现伴侣的性格特征伴侣
性格:
- %s
你必须严格遵守上述规则来回复用户。
"""
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 左侧侧边栏
with st.sidebar: # streamlit的上下文管理器
    st.title("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name =  nick_name
    # 性格输入框
    nature = st.text_area("性格", placeholder="请输入性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature =  nature

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
            {"role": "system", "content": systme_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
    )
    # 非流式输出解析方式
    # print("--------->大模型返回的结果",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 流式输出解析方式
    response_message = st.empty() # 创建一个空的组件，用于展示大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
