import cmd
from tabulate import tabulate

from main import deal
from main import output
from main import yaml
from main import request

class MyCmd(cmd.Cmd):
    prompt = '> '
    def do_set(self,line):
        name = line.split()
        path=str(name).replace('[\'','').replace('\']','')+self.prompt
        Entrance(path).cmdloop()

    def do_zyscan(self, line):
        path="zyscan "+self.prompt
        Entrance(path).cmdloop()

    def do_tdscan(self, line):
        path="tdscan "+self.prompt
        Entrance(path).cmdloop()

    def do_yyscan(self, line):
        path="yyscan "+self.prompt
        Entrance(path).cmdloop()

    def do_whscan(self, line):
        path="whscan "+self.prompt
        Entrance(path).cmdloop()

    def do_llscan(self, line):
        path="llscan "+self.prompt
        Entrance(path).cmdloop()

    def do_fwscan(self, line):
        path="fwscan "+self.prompt
        Entrance(path).cmdloop()

    def do_frscan(self, line):
        path="frscan "+self.prompt
        Entrance(path).cmdloop()

    def do_htdlscan(self, line):
        path="htdlscan "+self.prompt
        Entrance(path).cmdloop()

class Entrance(cmd.Cmd):
        
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt
        self.value = None
        self.type = "url"
        self.poc = "None"
        self.proxy = "Null"
        self.num = []
        self.Yaml=yaml.Yaml_deal(self.prompt)
        self.Yaml.Open_Yaml()
    
        
    
    def do_option(self,line):
        print(
        '''
        name         Command description                            Current Setting  
        ----         -------------------                            ---------------
        type:        指定的类型扫描的内容是文件还是IP               {}
        value:       指定目标，可以是IP或者文件                     {}
        poc          单独指定poc，如果为空或者默认则执行全部        {}
        proxy        请求时所用的代理和端口默认为系统默认的端口     {}
        '''.format(self.type,self.value,self.poc,self.proxy))
        

    def do_set(self,line):
        try:
            name,value = line.split()
            setattr(self, name, value)
            print('{} ==> {}'.format(name,value))
        except ValueError:
            flag="2"
            output.exception(flag)
        except Exception as e:
            print('Error: {}'.format(e))


    def do_show(self,line):
        table=[]
        pocid=self.Yaml.id
        poctime=self.Yaml.time
        pocexplain=self.Yaml.explain
        tabulate.PRESERVE_WHITESPACE = False
        #print(pocid,poctime,pocexplain)
        print('''\n\rPOC LIST''')
        print('''\r========''')
        headers= ["#","Name", "time", "description","Reference"]
        for i in range(len(self.Yaml.filenames)):
            table.append([i,pocid[i],poctime[i],pocexplain[i]])

        #print(tabulate(table, headers=headers, tablefmt="rounded_grid", maxcolwidths=[2, 20, 20, 70]))
        print(tabulate(table, headers=headers, tablefmt="rounded_grid", maxcolwidths=[2, 20, 20, 70], numalign="center", stralign="center"))
        print("\n")




    def do_use(self,line):
        self.num=line.split()
        filenames=self.Yaml.id
        if len(filenames) > int(self.num[0]):
            filename=filenames[int(self.num[0])] #修改为使用整数索引
            print('POC ==> {}'.format(filename))
        else:
            flag="5"
            output.exception(flag)
            return
        setattr(self,'poc',filename)        

    def completedefault(self, text, line, begidx, endidx):
        commands = ['type','value','poc','proxy']
        options = [i for i in commands if i.startswith(text)]
        return options

    
    def do_help(self,line):
        print(
        '''
        Command details：
            set       用来设置参数
            show      显示可选漏洞名称
            run       运行
            q         退出到主页
            option    显示设定的参数

        Option parameter：
            type      类型 支持参数为url或者文件(url/file)
            poc       名称 仅支持show提供的poc名称,默认为None扫描所有poc
            value     名称 支持目标名称,如果不带端口或者头默认为http(80)
            proxy     名称 默认为ip:端口

        #支持用tab命令补全

        ''')

    def do_q(self, line):
        """
        输入q或quer退出
        """
        return True

    def do_run(self,line):
        target=deal.Type_deal(self.value,self.type)
        if target==None:
            flag="3"
            output.exception(flag)
            return
        result=deal.POC_select(self.poc,self.Yaml.id)
        req=request.Request(target,self.Yaml.method,self.Yaml.url,self.Yaml.match_condition,self.Yaml.match,self.proxy,self.Yaml.body,self.Yaml.Rheader,self.Yaml.Gheader,self.Yaml.id,self.Yaml.extractors)
        #print(target,result,self.Yaml.method,self.Yaml.url,self.Yaml.match_condition,self.Yaml.match,self.proxy,self.num)
        if result:
            req.all_poc(self.Yaml.filenames)
        elif not result:
            req.specify_poc(int(self.num[0]))









