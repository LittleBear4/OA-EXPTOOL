import sys
import os
#sys.path.append('')
#sys.path.append('main/YMoa')
#sys.path.append('/main/deal')
import rich
import time
import cmd2 as cmd
from rich.console import Console
import config_file as cfg_file
from os import altsep, read, system, name

import main
import main.deal
import main.mode

console = Console()
def loading():
    for i in range(0,105):
        time.sleep(0.005)
        print('-',end = "", file=sys.stdout, flush=True)
def index():
    if name=='nt':
        _ = system('cls')
        print('''
           ██████╗    █████╗         ███████╗ ██╗  ██╗ ██████╗ ████████╗  ██████╗     ██████╗   ██╗
         ██╝     ██╗ ██╔══██╗        ██╔════╝ ╚██╗██╔╝ ██╔══██╗╚══██╔══╝██╝     ██╗ ██╝     ██║ ██║
         ██      ██║ ███████║ █████╗ █████╗    ╚███╔╝  ██████╔╝   ██║   ██      ██║ ██      ██║ ██║
         ██      ██║ ██╔══██║ ╚════╝ ██╔══╝    ██╔██╗  ██╔═══╝    ██║   ██      ██║ ██      ██║ ██║
         ╚═██████╔═╝ ██║  ██║        ███████╗ ██╔╝ ██╗ ██║        ██║   ╚═██████╔═╝ ╚═██████╔═╝ ███████╗
           ╚═════╝   ╚═╝  ╚═╝        ╚══════╝ ╚═╝  ╚═╝ ╚═╝        ╚═╝     ╚═════╝     ╚═════╝   ╚══════╝
        使用时请先查看使用说明
                                   热门OA参数：
                                            zyscan:致远OA漏洞POC
                                            tdscan:通达OA漏洞POC
                                            yyscan:用友OA漏洞POC
                                            whscan:万户OA漏洞POC
                                            llscan:蓝凌OA漏洞POC
                                            fwscan:泛微OA漏洞POC
        _________________________________________________________________________________________________
        
        show:帮助和说明  clear:清屏  BABA:开启代理                                        作者:西瓜麻辣烫
        ''')  
    else:
        _ = system('clear')
        print('''
            ██████╗   █████╗         ███████╗██╗  ██╗██████╗ ████████╗  ██████╗    ██████╗  ██╗
          ██╝     ██╗██╔══██╗        ██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██╝     ██╗██╝     ██║██║
          ██      ██║███████║ █████╗ █████╗   ╚███╔╝ ██████╔╝   ██║   ██      ██║██      ██║██║
          ██      ██║██╔══██║ ╚════╝ ██╔══╝   ██╔██╗ ██╔═══╝    ██║   ██      ██║██      ██║██║
          ╚═██████╔═╝██║  ██║        ███████╗██╔╝ ██╗██║        ██║   ╚═██████╔═╝╚═██████╔═╝███████╗
            ╚═════╝  ╚═╝  ╚═╝        ╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝     ╚═════╝    ╚═════╝  ╚══════╝
          使用时请先查看使用说明
                                   命令帮助：
                                            zyscan:致远OA漏洞POC
                                            tdscan:通达OA漏洞POC
                                            yyscan:用友OA漏洞POC
                                            whscan:万户OA漏洞POC
                                            llscan:蓝凌OA漏洞POC
                                            fwscan:泛微OA漏洞POC
        ________________________________________________________________________________________________
        
        show:帮助和说明 ctrl+z:返回 clear:清屏                                           作者:西瓜麻辣烫
        ''')
        
class hacktools(cmd.Cmd):
    prompt = time.strftime('\r\n\033[1;31mAction >>\033[32m')
     
    def do_install(self, line):
        main.main.install()
    def do_zyscan(self, line):
        #致远OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input('\033[1;31mzyscan >>\033[32m')
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.zypoc(xz, target_url)        
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.zypoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return
            
            
    def do_tdscan(self, line):
        #通达OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mtdscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.tdpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.tdpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return
            
            
    def do_yyscan(self, line):
        #用友OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31myyscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.yypoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.yypoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_whscan(self, line):
        #万户OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mwhscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.whpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.whpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_llscan(self, line):
        #蓝凌OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mllscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.llpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.llpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_fwscan(self, line):
        #泛微OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mfwscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.fwpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.fwpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return

    def do_frscan(self, line):
        #帆软OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mfrscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.frpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.frpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return  


    def do_htdlscan(self, line):
        #华天动力OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mHTdlscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.htdlpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.htdlpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return   



    def do_jdscan(self, line):
        #金蝶OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mjdscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.jdpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.jdpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    

  

    def do_hfscan(self, line):
        #红帆OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mhfscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.hfpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.hfpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    



    def do_qlscan(self, line):
        #启莱OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mqlscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.qlpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.qlpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    

    def do_zxscan(self, line):
        #志翔OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mzxscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.zxpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.zxpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    
            
        
   
             



    def do_zmscan(self, line):
        #智明OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mzmscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.zmpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.zmpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return               


    def do_xdscan(self, line):
        #新点OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mxdscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.xdpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.xdpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    

    def do_ymscan(self, line):
        #一米OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        
        xz = input("\033[1;31mymscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.ympoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.ympoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    

    def do_BABA(self, line): 
        print('''\033[33m
        开启代理，↑↑↓↓←←→→BABA我有三十条命
        ''')
        loading()
        print('''\033[33m
        http:HTTP代理
        socks4:SOCKS4代理
        socks5:SOCKS5代理
        debug:一建开启burp调试
        ''')
        xz = input("\033[1;31mproxy >>\033[32m")
        password=''
        if xz == 'http':
            url = input("\033[1;31m请输入代理地址：\033[32m")
            number = input("\033[1;31m请输入端口：\033[32m")
            username = input("\033[1;31m请输入账号(默认为空)：\033[32m")
            if username:
                password = input("\033[1;31m请输入密码：\033[32m")
            main.main.proxy(xz,url,number,username,password)
        
        if xz == 'socks4':
            url = input("\033[1;31m请输入代理地址：\033[32m")
            number = input("\033[1;31m请输入端口：\033[32m")
            username = input("\033[1;31m请输入账号(默认为空)：\033[32m")
            if username:
                password = input("\033[1;31m请输入密码：\033[32m")
            main.main.proxy(xz,url,number,username,password)
        
        if xz == 'socks5':
            url = input("\033[1;31m请输入代理地址：\033[32m")
            number = input("\033[1;31m请输入端口：\033[32m")
            username = input("\033[1;31m请输入账号(默认为空)：\033[32m")
            if username:
                password = input("\033[1;31m请输入密码：\033[32m")
            main.main.proxy(xz,url,number,username,password)
        
        if xz == 'debug':
            main.main.burp(xz)

    #def do_updata(self, line):
        
        
    def do_exit(self, line):
        try:
            sys.exit()
            os.system('cls')
            client = Client()
            client.cmdloop()
        except:
            exit()
            

    def do_clear(self, line):
        '''清屏'''
        _ = system('cls')
        index()
    
    def do_show(self, line):
        print('''
-----------------------------------------------------------------------------------------------
法律免责声明:未经事先双方同意攻击目标是非法的。
遵守所有适用的地方、州和联邦法律是最终用户的责任。
开发人员不承担任何责任，也不对本程序造成的任何误用或损害负责。
-----------------------------------------------------------------------------------------------''')
        list=['tdscan:通达OA漏洞POC','whscan:万户OA漏洞POC','frscan:帆软OA漏洞POC','ymscan:一米OA漏洞POC','hfscan:红帆OA漏洞POC','jdscan:金蝶OA漏洞POC','llscan:蓝凌OA漏洞POC','qlscan:启莱OA漏洞POC','zxscan:致翔OA漏洞POC','zxscan:致翔OA漏洞POC','zyscan:致远OA漏洞POC','zmscan:智明OA漏洞POC','fwscan:泛微OA漏洞POC','xdscan:新点OA漏洞POC','yyscan:用友OA漏洞POC','htdlscan:华天动力OA漏洞POC']
        print('''
使用说明:输入相对应的OA系统命令进入对应的模块
-----------------------------------------------------------------------------------------------
已收录的OA:
        ''')
        for i in list:
            print('''\033[33m       {}\033[37m'''.format(i))
            time.sleep(0.015)
            
        print(''' 
如果遇到问题请联系作者,作者会不断完善工具
-----------------------------------------------------------------------------------------------
致谢:感谢盆友的帮助，帮我优化代码提供意见''')

        
if __name__ == '__main__':
    loading()
    index()
    hacktools().cmdloop()
