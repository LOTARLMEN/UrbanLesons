import requests
import fake_useragent
from bs4 import BeautifulSoup
import json

url = 'https://medreg.gov39.ru/rpc/er/login?cache=c380f2b1db917ad4e37be79d5b4e8a00a'
user = fake_useragent.UserAgent().random

header = {'User-Agent': user,
          }
data = {
  "fname": "Янушкевич",
  "polis_num": "3998799741000017"
        }
data = json.dumps(data)

responce = requests.post(url, verify=False, data=data, headers=header).text
# print(r.text)
print(responce)

