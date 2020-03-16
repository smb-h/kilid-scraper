import requests
from bs4 import BeautifulSoup
import json
import lxml


url = "https://api.kilid.com/api/listing/search/portal/v2.0?page=4&sort=kilid,DESC"

# payload = "{\"locations\":[{\"type\":\"city\",\"locationId\":\"2301021576\"}],\"subType\":\"buy\",\"type\":\"listing\",\"page\":\"4\",\"sort\":\"kilid,DESC\"}"
payload = '{"locations":[{"type":"city","locationId":"2301021576"}],"subType":"buy","type":"listing","page":"100","sort":"kilid,DESC"}'
headers = {
  'Content-Type': 'application/json',
  'origin': 'https://kilid.com',
  'referer': 'https://kilid.com/buy/tehran?locations=c_2301021576&subType=buy&type=listing&sort=kilid,DESC',
}

response = requests.request("POST", url, headers=headers, data = payload)
contents = response.get("content", False)


# print(response.text.encode('utf8'))
print(response.text.encode('utf8'))



