import os
import sys
import datetime
import multiprocessing
import socket, socks
from rich.console import Console
import config_file as cfg_file

console = Console()

def fileDeal(target,name):
    file_object = open(target,'r')
    try:
        lines = file_object.readlines()
        pool = multiprocessing.Pool()
        for url in lines:
            pool.apply(name, args=(url.strip('\n'),))
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
    finally:
        file_object.close()

def urlDeal(target,name):
    try:
        name(target)
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')
        
def proxy(xz,url,number,username,password): 
    number=int(number)
    if xz == 'http':
        socks.set_default_proxy(socks.HTTP,addr=url,port=number,username=username,password=password)
    if xz == 'socks4':
        socks.set_default_proxy(socks.SOCKS4,addr=url,port=number,username=username,password=password)
    if xz == 'socks5':
        socks.set_default_proxy(socks.SOCKS5,addr=url,port=number,username=username,password=password)   
    socket.socket = socks.socksocket
    print('''\033[33m
    已配置全局代理，启用成功！！！
    ''')
    
def burp(xz):
    if xz == 'debug':
        socks.set_default_proxy(socks.HTTP,addr="127.0.0.1",port=8080)    
    socket.socket = socks.socksocket
    print('''\033[33m
    burp代理已开启，默认IP为127.0.0.1 端口8080，如若更改请使用http代理
    ''')
    



    

    