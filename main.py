import os
import requests

pushplus_token = os.environ.get('pushplus_token')
topic = os.environ.get('topic')

image_url = "https://60s.viki.moe/bing?e=image"

text_url = "https://60s.viki.moe/bing?e=text"

text_response = requests.get(text_url)
content = text_response.text

pushplus_url = "https://www.pushplus.plus//send"

pushplus_data = {
    "token": pushplus_token,
    "title": "每天60秒读懂世界",
    "content": "{}<br/><img src='{}' />".format(content,image_url),
    # "topic": "群组ID",
    "template": "html"
}

requests.post(pushplus_url, json=pushplus_data)
