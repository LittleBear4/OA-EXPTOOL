import os
import sys
import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
import telnetlib
import argparse
import threading


lock=threading.Lock()


def install():
    os.system("pip3 install -r main/requirements.txt --user")

#致远
def zypoc(xz, target_url):
    if xz == '1':
        os.system("python main/seeyou/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/seeyou/main.py -f " + target_url)

#通达       
def tdpoc(xz, target_url):
    if xz == '1':
        os.system("python main/Anywhere/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/Anywhere/main.py -f " + target_url)

#泛微
def fwpoc(xz, target_url):
    if xz == '1':
        os.system("python main/weaver/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/weaver/main.py -f " + target_url)

#用友         
def yypoc(xz, target_url):
    if xz == '1':
        os.system("python main/yonyou/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/yonyou/main.py -f " + target_url)

#万户        
def whpoc(xz, target_url):
    if xz == '1':
        os.system("python main/ezoffice/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/ezoffice/main.py -f " + target_url)
        
#帆软        
def frpoc(xz, target_url):
    if xz == '1':
        os.system("python main/FineReport/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/FineReport/main.py -f " + target_url)
        
#华天动力
def htdlpoc(xz, target_url):
    if xz == '1':
        os.system("python main/HtianDL/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/HtianDL/main.py -f " + target_url)

#红帆        
def hfpoc(xz, target_url):
    if xz == '1':
        os.system("python main/ioffice/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/ioffice/main.py -f " + target_url)
     
#金蝶        
def jdpoc(xz, target_url):
    if xz == '1':
        os.system("python main/kingdee/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/kingdee/main.py -f " + target_url)
     
#蓝凌        
def llpoc(xz, target_url):
    if xz == '1':
        os.system("python main/Landray/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/Landray/main.py -f " + target_url)
        
#启莱        
def qlpoc(xz, target_url):
    if xz == '1':
        os.system("python main/Rev/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/Rev/main.py -f " + target_url)
        
#致翔        
def zxpoc(xz, target_url):
    if xz == '1':
        os.system("python main/seefly/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/seefly/main.py -f " + target_url)
        
#智明        
def zmpoc(xz, target_url):
    if xz == '1':
        os.system("python main/smart/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/smart/main.py -f " + target_url)
     
#新点        
def xdpoc(xz, target_url):
    if xz == '1':
        os.system("python main/XinDian/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/XinDian/main.py -f " + target_url)
        
#一米        
def ympoc(xz, target_url):
    if xz == '1':
        os.system("python main/YMoa/main.py -u " + target_url)
    if xz == '2':
        os.system("python main/YMoa/main.py -f " + target_url)
