# -*- coding: utf-8 -*-
import main.main
import main.deal
from rich.console import Console
#from pyfiglet import Figlet


console = Console()
def ympoc(xz, target):
    name=main.deal.ymoa
    #console.print(Figlet().renderText('YiMi OA-Exp'), style='bold blue')
    select(xz,target,name)
    
def yypoc(xz, target):
    name=main.deal.yyoa
    #console.print(Figlet(font='slant').renderText('YonYou OA-Exp'), style='bold blue')
    select(xz,target,name)
    
def zypoc(xz, target):
    name=main.deal.zyoa
    #console.print(Figlet(font='slant').renderText('SeeyouOAExp'), style='bold blue')
    select(xz,target,name)

def tdpoc(xz, target):
    name=main.deal.tdoa
    #console.print(Figlet(font='slant').renderText('Office Anywhere OA-Exp'), style='bold blue')
    select(xz,target,name)
    
def whpoc(xz, target):
    name=main.deal.whoa
    #console.print(Figlet(font='slant').renderText('EzOffice OA-Exp'), style='bold blue')
    select(xz,target,name)
    
def llpoc(xz, target):
    name=main.deal.whoa
    #console.print(Figlet(font='slant').renderText('Landray OA-Exp'), style='bold blue')
    select(xz,target,name)
        
def fwpoc(xz, target):
    name=main.deal.fwoa
    #console.print(Figlet(font='slant').renderText('weaver OA-Exp'), style='bold blue')
    select(xz,target,name)

def frpoc(xz, target):
    name=main.deal.froa
    #console.print(Figlet(font='slant').renderText('FineReport OA-Exp'), style='bold blue')
    select(xz,target,name)

def htdlpoc(xz, target):
    name=main.deal.htdloa
    #console.print(Figlet(font='slant').renderText('HtianDL OA-Exp'), style='bold blue')
    select(xz,target,name)   

def jdpoc(xz, target):
    name=main.deal.jdoa
    #console.print(Figlet(font='slant').renderText('Kingdee OA-Exp'), style='bold blue')
    select(xz,target,name)    
    
def hfpoc(xz, target):
    name=main.deal.hfoa
    #console.print(Figlet(font='slant').renderText('ioffice OA-Exp'), style='bold blue')
    select(xz,target,name)
    
def qlpoc(xz, target):
    name=main.deal.qloa
    #console.print(Figlet(font='slant').renderText('Rev OA-Exp'), style='bold blue')
    select(xz,target,name)


def zxpoc(xz, target):
    name=main.deal.zxoa
    #console.print(Figlet(font='slant').renderText('seefly OA-Exp'), style='bold blue')
    select(xz,target,name) 

def zmpoc(xz, target):
    name=main.deal.zmoa
    #console.print(Figlet(font='slant').renderText('smart OA-Exp'), style='bold blue')
    select(xz,target,name) 

def xdpoc(xz, target):
    name=main.deal.xdoa
    #console.print(Figlet(font='slant').renderText('Xindian OA-Exp'), style='bold blue')
    select(xz,target,name) 
    
        
def select(xz,target,name):
    if xz == 'action':
        main.main.urlDeal(target,name)
    if xz == 'actions':
        main.main.fileDeal(target,name)    
    

