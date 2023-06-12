import os
import json
import yaml




class Yaml_deal:
    def __init__(self, prompt):
        self.prompt = prompt.replace('>', '').strip()
        self.path = "book/" + self.Get_module_value() #调用类内的方法，获取模块对应的目录
        self.filenames=self.Get_folder_filename()      #调用类内的方法，获取模块对应的文件名
        self.time=[]                                    #漏洞纰漏的时间
        self.id=[]                                      #漏洞名称
        self.explain=[]                                 #漏洞说明
        self.method=[]                                  #请求方式
        self.url=[]                                     #漏洞的url
        self.Gheader=[]                                 #GET请求所需要的头
        self.body=[]                                    #post请求内容
        self.Rheader=[]                                 #post请求所需要的头
        self.content=[]                                 #post的内容
        self.match_condition=[]                         #匹配的规则
        self.match=[]                                   #匹配的内容
        self.Reference=[]                               #参考链接
        self.extractors=[]                              #初始化提取器

    #这里主要编辑的是模块的键值 例如zyscan对应目录为seeyou
    def Get_module_value(self):
        with open(f"bin/module.json", "r") as f:
            value=[]
            data = json.load(f)
            try:
                value = ((data['employees'])[0])[self.prompt]
                return value
            except KeyError:
                value = (self.prompt).replace('[\'','')  
                value=value.replace('\']','')          
                return value



    def Get_folder_filename(self):
        filenames = []
        for filename in os.listdir(self.path):
            filenames.append(filename)        
        return filenames
        


    def Open_Yaml(self):
        for filename in self.filenames:
            try:
                #打开yaml文件内容
                with open(os.path.join(self.path, filename), 'r', encoding='utf-8') as f:
                    data = f.read()
                    yaml_data = yaml.safe_load(data)
                    #print(yaml_data)
                    self.id.append(yaml_data['id'])                         #漏洞的名称
                    #自已定的yaml数据主要是用来展示漏洞来源
                    if 'info' in yaml_data and 'description' in yaml_data['info'] and yaml_data['info']['description'] != None:
                        self.explain.append(yaml_data['info']['description'])
                    else: 
                        self.explain.append("未定义") # Add "未定义" to the list

                        
                    if 'time' in yaml_data:
                        self.time.append(yaml_data['time'])                 #漏洞的纰漏时间
                    else:
                        self.time.append("未定义")
                    
                    if 'body' in (yaml_data['http'])[0]:
                        self.body.append(((yaml_data['http'])[0])['body'])
                        #print(self.body)
                    else:
                        self.body.append("占位符2")

                    if 'Rheader' in (yaml_data['http'])[0]:
                        self.Rheader.append(((yaml_data['http'])[0])['Rheader'])
                        #print(self.Rheader)
                    else:
                        self.Rheader.append("None") #占位符

                    if 'Gheader' in (yaml_data['http'])[0]:
                        self.Gheader.append(((yaml_data['http'])[0])['Gheader'])
                    else:
                        self.Gheader.append("None") #占位符

                    if 'extractors' in (yaml_data['http'])[0]:
                        self.extractors.append(((yaml_data['http'])[0])['extractors'])
                    else:
                        self.extractors.append("None") #占位符    

                    self.method.append(((yaml_data['http'])[0])['method'])  #请求方式GET/POST
                    self.url.append(((yaml_data['http'])[0])['path'])       #漏洞的url
                    self.match_condition.append(((yaml_data['http'])[0])['matchers-condition']) #匹配条件
                    #匹配内容
                    self.match.append((((yaml_data['http'])[0])['matchers']))
            except Exception as e:
                print(f"错误的打开文件 {filename}: {e}")





        
 







