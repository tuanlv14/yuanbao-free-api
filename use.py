import base64
import requests
from openai import OpenAI

base_url = "http://localhost:8000/v1/"

hy_source = "web"
hy_user = "19f7bcca0e134402976a6ae79f9d648c"    # 替换为你的用户ID
hy_token = "knxxrda/pVbgxQFkZO83VDod9tMGPOlZMBGp9ThSRB8RyfWQYi9nGGT9k/CtgHMCFsDFVdiKkhPkOZoFM0KpIw=="  # 替换为你的token

agent_id = "naQivTmsDa"
chat_id = ""    # 可选，如果不提供会自动创建

# pure text chat only
multimedia = []  # no file uploads, empty list for text chat

# chat
client = OpenAI(base_url=base_url, api_key=hy_token)

response = client.chat.completions.create(
    model="deepseek-v3",
    messages=[{"role": "user", "content": "hello, who are you?"}],
    stream=True,
    extra_body={
        "hy_source": hy_source,
        "hy_user": hy_user,
        "agent_id": agent_id,
        "chat_id": chat_id,
        "should_remove_conversation": False,
        "multimedia": multimedia,
    },
)

accumulated = ""
for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        accumulated += content
print(accumulated.replace('[text]', ''))

#https://github.com/chenwr727/yuanbao-free-api?tab=readme-ov-f