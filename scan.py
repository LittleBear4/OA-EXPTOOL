import sys
import rich
import time
import main
import main.main
import cmd2 as cmd 
from rich.console import Console
from os import altsep, read, system, name


console = Console()
def loading():
    for i in range(0,105):
        time.sleep(0.005)
        sys.stdout.write('-')
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
        
        show:帮助和说明  exit:退出  clear:清屏                                            作者:西瓜麻辣烫
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
    prompt = time.strftime('\033[1;31mAction >>\033[32m')
     
    def do_install(self, line):
        main.main.install()
    def do_zyscan(self, line):
        #致远OA漏洞POC
        print('''\033[33m
        1.致远漏洞综合扫描
        2.致远漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.zypoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.zypoc(xz, target_url)
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
        1.通达漏洞综合扫描
        2.通达漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.tdpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.tdpoc(xz, target_url)
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
        1.用友漏洞综合扫描
        2.用友漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.yypoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.yypoc(xz, target_url)
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
        1.万户漏洞综合扫描
        2.万户漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.whpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.whpoc(xz, target_url)
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
        1.蓝凌漏洞综合扫描
        2.蓝凌漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.llpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.llpoc(xz, target_url)
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
        1.泛微漏洞综合扫描
        2.泛微漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.fwpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.fwpoc(xz, target_url)
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
        1.帆软漏洞综合扫描
        2.帆软漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.frpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.frpoc(xz, target_url)
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
        1.华天动力漏洞综合扫描
        2.华天动力漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.htdlpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.htdlpoc(xz, target_url)
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
        1.金蝶漏洞综合扫描
        2.金蝶漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.jdpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.jdpoc(xz, target_url)
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
        1.红帆漏洞综合扫描
        2.红帆漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.hfpoc(xz, target_url)
        elif xz == '2':
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
        1.启莱漏洞综合扫描
        2.启莱漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.qlpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.qlpoc(xz, target_url)
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
        1.志翔漏洞综合扫描
        2.志翔漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.zxpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.zx8poc(xz, target_url)
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
        1.智明漏洞综合扫描
        2.智明漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.zmpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.zmpoc(xz, target_url)
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
        1.新点漏洞综合扫描
        2.新点漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.xdpoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.xdpoc(xz, target_url)
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
        1.一米漏洞综合扫描
        2.一米漏洞综合批量扫描
        ''')
        xz = input("\033[1;31m请输入你的选项：\033[32m")
        if xz == '1':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.main.ympoc(xz, target_url)
        elif xz == '2':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.main.ympoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return    

            
    def do_exit(self, line):
        sys.exit()
            

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
如果遇到问题请联系作者,作者会不断完善工具，你的支持就是我最大的动力
-----------------------------------------------------------------------------------------------
致谢:感谢盆友的帮助，帮我优化代码提供意见''')
        
if __name__ == '__main__':
    loading()
    index()
    hacktools().cmdloop()
