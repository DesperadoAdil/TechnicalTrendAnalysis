# -*- coding: UTF-8 -*-
import requests
import json
from urllib.parse import quote
import pickle

TITLELIST = [
    "人工智能",
    "自动驾驶",
    "区块链",
    "计算机视觉",
    "数据挖掘",
    "数据建模",
    "深度学习",
    "图数据库",
    "物联网"
]


session = requests.Session()
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.122 Safari/537.36'

def get_trend_data(field):
    headers = {'User-Agent': USER_AGENT, 'Referer': 'http://trend.aminer.cn/topic/trend?query='+quote(field), 'Origin': 'http://trend.aminer.cn', 'Content-Type': 'Content-Type:application/json'}
    url = 'https://apiv2.aminer.cn/magic?a=getTrend__trend.GenTrend___'
    data = [{"action": "trend.GenTrend", "parameters": {"query": field, "size": 11, "searchType": "all", "advquery": {"texts": [{"source": "start_year", "text": "2000"}, {"source": "end_year", "text": "2017"},{"source": "isReload", "text": "false"}]}}, "schema": {"person": ["id", "name", "profile.org"]}}]
    res = session.post(url, data=json.dumps(data), headers=headers)
    term_freq = json.loads(res.text)['data'][0]['items'][0]['data']['term_freq_by_year']
    return term_freq

if __name__ == '__main__':
    data = {}
    ##提取本地数据##
    with open("./cache", "rb") as f:
        data = pickle.load(f)

    for item in TITLELIST:
        if item not in data:
            data[item] = get_trend_data(item)
        print ("finish " + item)

    with open("./cache", "wb") as f:
        pickle.dump(data, f)

    '''heat = {}
    for key,value in cache.items():
        list = []
        list.extend(value.values())
        sum = 0
        for num in list:
            sum += num
        heat[key] = (sum, list)

    heat = sorted(heat.items(), key = lambda v : v[1][0], reverse = True)'''
