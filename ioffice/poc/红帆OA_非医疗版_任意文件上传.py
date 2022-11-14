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


def main(url):
    target_url1 = url + "/ioffice/prg/set/Report/ioRepPicAdd.aspx"
    data='{ioffice}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-type": "application/x-www-form-urlencoded"
    }
    console.print(now_time() + " [INFO]     正在检测红帆任意文件上传漏洞", style='bold blue')
    try:
        urllib3.disable_warnings()
        res1 = requests.post(url=target_url1, headers=headers, data=data,verify=False)
        if res1.status_code == 200:
            console.print(now_time() + " [SUCCESS]     暂无exp，存在红帆任意文件上传:{}".format(target_url1), style='bold green')
        else:
            console.print(now_time() + " [WARNING]  不存在红帆任意文件上传", style='bold red')
    except Exception as e:
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