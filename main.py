import requests
import json
url = 'https://api.jun.la/60s.php?format=imgapi'
text = requests.get(url)
content = json.loads(text.text)
pushplus_token = '48abcdf31042406bb4dfd244df0bb34e'
image_url = content['imageBaidu']
pushplus_url = "https://www.pushplus.plus//send"
pushplus_data = {
"token": pushplus_token,
"title": "每日60s新闻",
"content": "<br/><img src='{}' alt=""/>".format(image_url),
# "topic": "群组ID",
"template": "html"
}

requests.post(pushplus_url, json=pushplus_data)
