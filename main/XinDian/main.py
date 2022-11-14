# -*- coding: utf-8 -*-
import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
import sys
import os
#sys.path.append(os.path.abspath('main')) 
#from creatlogtext import text_create
from poc import (新点OA_Excel_敏感信息泄露)

console = Console() 
file_name='xindian'
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() + " [INFO]     正在检测:{}".format(target_url)+'\n', style='bold yellow')
    list = ['新点OA_Excel_敏感信息泄露']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)

    
if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('Xindian OA-Exp'), style='bold blue')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                console.print(now_time() + " [INFO]     正在检测:{}".format(url)+'\n', style='bold yellow')
                pool.apply(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            main(args.url)
        else:
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
