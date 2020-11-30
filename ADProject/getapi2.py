import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst?"

service_key = 'aGseaS0o0EdPAsk5d2Ocp83rdLts9s84zfCq8yryY16S0ldRaKfN5qLtgwfeTLaMEaDXTpRuS3Gc3kJGj5PQhQ%3D%3D'

today = datetime.datetime.today()
base_date = today.strftime("%Y%m%d") # "20200214" == 기준 날짜
base_time = "0600" # 날씨 값
stnId = "133"

payload = "serviceKey=" + service_key + "&" +\
    "dataType=json" + "&" +\
    "stnId=" + stnId + "&" +\
    "tmFc=" + base_date + base_time

data = ['POP', 'TMN', 'TMX', 'SKY']
# 값 요청
res = requests.get(vilage_weather_url + payload)
items = res.json().get('response').get('body').get('items')
for i in items['item']:
    # if i['category'] in data:
    #    print(i)
     print(i)

#print(items['item'][0])
#{'item': [{'baseDate': '20200214',
#   'baseTime': '0500',
#   'category': 'POP',
#   'fcstDate': '20200214',
#   'fcstTime': '0900',
#   'fcstValue': '0',
#   'nx': 60,
#   'ny': 128},
#  {'baseDate': '20200214',
#   'baseTime': '0500',
#   'category': 'PTY',
#   'fcstDate': '20200214',
#   'fcstTime': '0900',
#   'fcstValue': '0',
#   'nx': 60,
#   'ny': 128},
#      'ny': 128},
#     {'baseDate': '20200214'