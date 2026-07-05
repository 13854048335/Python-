import datetime
import os
import streamlit as st
from openai import OpenAI
from streamlit.runtime.caching.cache_utils import get_session_id_or_throw
from streamlit.runtime.state import session_state
import json

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
# 兼容本地环境变量和云端 Secrets
def get_api_key():
    # 优先从 st.secrets 读取
    try:
        return st.secrets.get("DEEPSEEK_API_KEY")
    except:
        # 如果没有 secrets，从环境变量读取（本地开发用）
        return os.environ.get('DEEPSEEK_API_KEY')
# 保存会话信息的函数
def save_session():

    if st.session_state.current_session:
        session_data = {
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages,
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature
        }
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)
# 生成会话标识
def generate_session_id():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# 加载所有的会话列表
def load_session_list():
    session_list = []
    if os.path.exists("sessions"):
       filter_lsit = os.listdir("sessions")
       for filename in filter_lsit:
           if filename.endswith(".json"):
               session_list.append(filename[:-5:1])
       session_list.sort(reverse=True)
       return session_list
# 加载指定会话列表
def load_session(session_id):
    if os.path.exists(f"sessions/{session_id}.json"):
        try:
        # 读取会话数据
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.current_session = session_data["current_session"]
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
        except Exception as e:
            st.error(f"加载会话数据出错：{e}")
# 删除指定会话
def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            st.success("删除会话成功！")
            # 如果删除的是当前会话，更新当前的展示列表
            if session_id == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_id()
    except Exception as e:
        st.error(f"删除会话出错：{e}")

# 大标题
st.title("AI智能伴侣")
#Logo
#st.logo("./resources/logo.png")

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
# 会话标识
if "current_session" not in st.session_state:
    # 获取系统当前时间
    sysytem_date = generate_session_id()
    st.session_state.current_session = sysytem_date


# 展示聊天信息
st.text(f"会话的名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 左侧侧边栏
with st.sidebar: # streamlit的上下文管理器
    #会话信息
    st.subheader("AI控制面板")
    # 新建会话按钮
    if st.button("新建会话", width="stretch", icon="✏️"):
        save_session()
        # 创建新的会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.rerun()  # 重新运行当前页面
    # 会话历史
    st.text("历史会话")
    session_list = load_session_list()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            # 加载会话信息
            # 三元运算符: 如果条件为真, 则返回第一个表达式的值; 否则, 返回第二个表达式的值 --> 语法: 值1 if 条件 else 值2
            if st.button(session, width="stretch",icon="📝", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()

        with col2:
            # 删除指定会话
            if st.button("",width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
     # 分割线
    st.divider()
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
        api_key=get_api_key(),
        #api_key=os.environ.get('DEEPSEEK_API_KEY'),
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
    save_session()
