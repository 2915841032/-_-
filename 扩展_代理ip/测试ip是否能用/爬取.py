import time
import random
import requests
import pandas as pd
from tqdm import trange


def get_table_data(index):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = f"https://www.89ip.cn/index_{index}.html"
    response = requests.get(url, headers=headers)
    df = pd.read_html(response.text)[0]
    return df
def get_proxy():
    with open('有效ip.csv', mode='r', encoding='utf-8-sig', newline='') as f:
        datas = f.readlines()
    ran_num = random.choice(datas)
    ip = ran_num.strip().split('/r')
    proxies = {'http://': 'http://' + ip[0]}
    return proxies
if __name__ == '__main__':
    df_list = []
    for i in trange(1,101):
        df = get_table_data(i)
        time.sleep(0.1)
        df_list.append(df)
    dfs = pd.concat(df_list)
    # dfs.drop('index', axis=1, inplace=True)
    dfs.drop_duplicates(inplace=True)
    dfs.reset_index(inplace=True)
    dfs['index']=[i for i in range(1,len(dfs)+1)]
    # index,IP,端口号,代理位置,运营商,录取时间
    dfs.columns=['序号','IP','端口','位置','运营商','时间']

    dfs['sucess']=dfs['IP'].astype(str)+':'+dfs['端口'].astype(str)
    dfs.to_csv(f"天气数据.csv", index=False,encoding='utf-8-sig',mode='a')
    print("成功爬取数据")







