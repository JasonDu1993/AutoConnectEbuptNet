# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 11:27
# @Author  : Jason
# @Email   : 1358681631@qq.com
# @File    : t.py
# @Software: PyCharm
import requests
from time import strftime
import time
import argparse
from tqdm import tqdm


def login(user, password):
    """login work"""

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Length': '97',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.1.1.7:8002',
        'Origin': 'http://10.1.1.7:8002',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://10.1.1.7:8002/index.php?zone=cpzone',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    s = requests.Session()
    s.headers = headers
    post_data = {'auth_user': user, 'auth_pass': password, 'redirurl': "http://www.ebupt.com/",
                 'accept': '登录'}
    r = s.post('http://10.1.1.7:8002/index.php?zone=cpzone', data=post_data)
    print(r.text)
    print("log in, status = %s" % r.status_code)
    with open("log.txt", "a") as f:
        f.write("run time:" + strftime("%Y_%m%d_%H%M%S") + r.text.encode(encoding="utf-8")[3:].decode(encoding="utf-8"))
        f.write("log in, status = %s" % r.status_code + "\n")
        f.write("---" * 20 + "\n")
        f.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", type=int, default=3600)
    parser.add_argument("-u", "--user", type=str, default="***")
    parser.add_argument("-p", "--password", type=str, default="***")
    parser.add_argument("-r", "--recurrent", default=True)
    args = parser.parse_args()
    internal = args.time
    user = args.user
    password = args.password
    recurrent = args.recurrent
    print(args)
    print("每隔", internal, "秒登录一次")
    login(user, password)
    while recurrent:
        for i in tqdm(range(internal)):
            time.sleep(1)
        login(user, password)
