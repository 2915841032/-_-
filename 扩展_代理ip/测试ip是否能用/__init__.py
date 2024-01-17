import csv
from multiprocessing.pool import ThreadPool

import pandas as pd
import requests

def validate(ip):
    IP = {'http': ip}  # 指定对应的 IP 进行访问网址
    # print(IP)
    try:
        r = requests.get('https://www.duitang.com/', proxies=IP,
                         timeout=3)  # proxies 设定对应的代理 IP 进行访问， timeout 设定相应的时间之后停止等待响应
        if r.status_code == 200:
            print("成功:{}".format(ip))
            alive_ip.append(ip)  # 有效的 IP 则添加进去
    except:
        print("无效:{}".format(ip))

def save(writer):
    for ip in alive_ip:
        writer.writerow([ip])
    print("成功保存所有有效 ip ")
def check(writer):
    lines=pd.read_csv('天气数据.csv')['sucess'].tolist()
    ips = list(map(lambda x: x.strip(), [line for line in lines]))  # strip() 方法用于移除字符串头尾指定的字符，默认就是空格或换行符。
    pool = ThreadPool(20)  # 多线程 设置并发数量！
    pool.map(validate, ips)  # 用 map 简捷实现 Python 程序并行化
    save(writer)  # 保存能用的 IP




if __name__ == '__main__':
    alive_ip=[]
    csv_file = open('有效ip.csv', 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['ip'])
    check(writer)
    csv_file.close()
