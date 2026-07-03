# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
# 与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个AI助理，可以帮我进行写作"},
        {"role": "user", "content": "这是一个示例： "},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)