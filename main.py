import os
import requests
import json

pushplus_token = os.environ.get('pushplus_token')
topic = os.environ.get('topic')

text_url = "https://60s.viki.moe/60s?v2=1"

text_response = requests.get(text_url)
content = text_response.text
content = json.loads(content)
s = content['data']['news']
m = content['data']['tip']
c = ''
for i in range(len(s)):
    c += f'{i+1}、{s[i]}\n'
c += f'微语: {m}'

pushplus_url = "https://www.pushplus.plus//send"

pushplus_data = {
    "token": pushplus_token,
    "title": "每天60秒读懂世界",
    "content": "{}".format(c),
    # "topic": "群组ID",
    "template": "html"
}

requests.post(pushplus_url, json=pushplus_data)
