 
import requests
import random
import re

from main import output
#from main import extractors




class Request:
    def __init__(self,target,method,url,match_condition,match,proxy,body,Rheader,Gheader,name,Controls):
        self.target=target                      #类型列表 url
        self.method=method                      #列表   请求方式
        self.path=url                           #列表   POC路径
        self.match_condition=match_condition    #列表   匹配条件
        self.match=match                        #列表   匹配的内容初始化后待处理
        self.proxy=proxy                        #列表   代理
        self.body=body
        self.Rheader=Rheader                    #POST请求头
        self.Gheader=Gheader                    #GET 请求头       
        self.id=name
        self.ext=Controls
        






    def specify_poc(self,num):
        response = None
        
        method=self.method[num]
        ext=self.ext[num]
        
        #print(self.Rheader)
        #print(self.Gheader)
        #print(self.path)
        #print(self.body)
        #print(self.id)
        #print(ext)
        #print(method)

        
        for url in self.target:
            #设置POST_header一个计数器，每一次POST请求完毕则加一
            counter=0
            #设置GET_header一个计数器，每一次get请求完毕则加一
            count=0
            #一个请求计数器
            req_conunt=1
            output.load(url)
            for  number in range(len(self.path[num])):
                #print(method[number])
                #print(number)
                path =(self.path[num])[number]
                #print(path)
                path= path.replace('{{BaseURL}}', '')
                med=method[number] 

                if med == 'GET':     
                    RequestHeader=self.RequestHeader()
                    if self.Gheader[num]=="None":
                        count=0
                    else:
                        Gheader=(self.Gheader[num])[count]
                        Gheader=Gheader.split('&') 
                        for i in Gheader:
                            i = i.strip()
                            #print(i)
                            key, value =i.split(':')
                            RequestHeader[key] = value
                        count=count+1 
                    target=url+path
                    #print(target)
                    #print(RequestHeader)
                    #print('-------------------------------------')
                    try:
                        response = requests.get(target, headers=RequestHeader, verify=False, timeout=5.1, allow_redirects=False)
                        result=self.extractors(ext,response,req_conunt,num)
                    except:
                        flag='7'
                        output.exception(flag)  
                    #print('xxx')
                    req_conunt+=1
                    #self.verify_poc(response,num



                    #except:
                      #  flag='7'
                      #  output.exception(flag)                   
                    
                
                if med == 'POST':
                    #利用计数器来赋予body值
                    body = (self.body[num])[counter]
                    #print(body)
                    #获取并更新请求头
                    RequestHeader=self.RequestHeader()
                    if (self.Rheader[num])=="None":
                        counter=0
                    else:
                        Rheader=(self.Rheader[num])[counter] 
                        Rheader=Rheader.split('&')   
                        for i in Rheader:
                            i = i.strip()
                            key, value =i.split(':')
                            RequestHeader[key] = value
                        counter+= 1  
                    #try:
                    target=url+path
                    #print(target)
                    #print(RequestHeader)     
                            
                    #print('-------------------------------------')
                    try:       
                        response = requests.post(target, headers=RequestHeader,  data=body,verify=False, timeout=5.1, allow_redirects=False)
                        self.extractors(ext,response,req_conunt,num)
                    except:
                        flag='7'
                        output.exception(flag)
                    req_conunt+=1
                
            #请求结束后进行验证
            if response is not None:
                self.verify_poc(response,num)
            else:
                flag='2'
                output.result(flag,self.id[num])



    def all_poc(self,filenames):
        response = None
        for url in self.target:
            output.load(url)      
            #print()
            for num in range(len(filenames)):
                method=self.method[num]
                ext=self.ext[num]
                #print(url)
                counter=0
                count=0
                req_conunt=1
                for  number in range(len(self.path[num])):
                    #print(method[number])
                    #print(number)
                    path =(self.path[num])[number]
                    #print(path)
                    path= path.replace('{{BaseURL}}', '')
                    med=method[number] 

                    if med == 'GET':     
                        RequestHeader=self.RequestHeader()
                        #print(self.Gheader)
                        if self.Gheader[num]=="None":
                            count=0
                        else:
                            Gheader=(self.Gheader[num])[count]
                            Gheader=Gheader.split('&') 
                            for i in Gheader:
                                i = i.strip()
                                #print(i)
                                key, value =i.split(':')
                                RequestHeader[key] = value
                            count=count+1 
                        target=url+path
                        #print(target)
                        #print(RequestHeader)
                        #print('-------------------------------------')
                        try:
                            response = requests.get(target, headers=RequestHeader, verify=False, timeout=5.1, allow_redirects=False)
                            result=self.extractors(ext,response,req_conunt,num)
                        except:
                            flag='7'
                            output.exception(flag)  
                        #print('xxx')
                        req_conunt+=1



                        #except:
                        #  flag='7'
                        #  output.exception(flag)                   
                        
                    
                    if med == 'POST':
                        #利用计数器来赋予body值
                        body = (self.body[num])[counter]
                        #print(body)
                        #获取并更新请求头
                        RequestHeader=self.RequestHeader()
                        if (self.Rheader[num])=="None":
                            counter=0
                        else:
                            Rheader=(self.Rheader[num])[counter] 
                            Rheader=Rheader.split('&')   
                            for i in Rheader:
                                i = i.strip()
                                #print(i)
                                key, value =i.split(':')
                                RequestHeader[key] = value
                            counter+= 1  
                        #try:
                        target=url+path
                        #print(target)
                        #print(RequestHeader)     
                                
                        #print('-------------------------------------')
                        try:       
                            response = requests.post(target, headers=RequestHeader,  data=body,verify=False, timeout=5.1, allow_redirects=False)
                            self.extractors(ext,response,req_conunt,num)
                        except:
                            flag='7'
                            output.exception(flag)
                        req_conunt+=1
                
                #请求结束后进行验证
                if response is not None:
                    self.verify_poc(response,num)
                else:
                    flag='2'
                    output.result(flag,self.id[num])





    def extractors(self,ext,response,conunt,num):
        #print(ext,response,conunt,num)
        old_list=[]

        result = ''
        #如果ext中有None，直接返回
        #print(ext)
        if 'None' in ext:
            return 
        else:
            #遍历ext中的每一个元素
            for i in range(len(ext)):
                #print(i)
                time_index = None
                #遍历ext[i]中的time列表
                for j in range(len((ext[i])['time'])): 
                    if (ext[i])['time'][j] == conunt: 
                        time_index = j 
                        break
                #如果找到了time_index，继续执行代码
                if time_index is not None: 
                    regex = (ext[i])['regex'][time_index].split(',')   
                    #遍历regex列表
                    for j in range(len(regex)):
                        pattern = re.compile(regex[j])
                        #print(pattern)
                        part = ((ext[i])['part'])[j]
                        #print(part)
                        #如果part是Gheader或Rheader，就在response.headers中查找
                        if part=='Gheader' or part=='Rheader':
                            #print('header')
                            header_str = str(response.headers)
                            header_list = header_str.split('\n')
                            header_dict = {}
                            for header in header_list:
                                if ':' in header:
                                    key, value = header.split(':', 1)
                                    header_dict[key.strip()] = value.strip()
                            result = pattern.findall(str(header_dict))
                            result = result[0] if result else ''
                        else:
                            result = pattern.findall(response.text)
                            result = result[0] if result else ''



                        #如果part是列表，就遍历列表中的每一个元素，将其中的((ext[i])['name'])[j]替换为result
                        #if isinstance((getattr(self,part))[num], list):
                        old_list = getattr(self,part)
                        #print(old_list)
                        new_list = [] # create a new list to store the modified items
                        for item in (getattr(self,part))[num]: # iterate over the items in the original list
                            new_list.append(item.replace(((ext[i])['name'])[j], result)) # replace 'session' with '1' and add to the new list
                        old_list[num]=new_list
                        setattr(self, part, old_list) # set the attribute to the new list

  



    def verify_poc(self,response,num):
        verifier=[]                        #定义验证器 
        condition=self.match_condition
        match=self.match
        #取条件
        for data in match[num]:
            if 'part' in data.keys():
                if data['part']=="header":
                    #print('1')
                    #print(data)
                    if data['type']=='word':

                        for value in data['words']:
                            #print('2')
                            #print(value)
                            if value in response.headers:
                                verifier.append(True)
                            else:
                                verifier.append(False)

                
                elif data['part']=='body':
                    
                    if data['type']=='word':
                        for value in data['words']:
                            #print('3')
                            #print(value)
                            if value in response.text:
                                verifier.append(True)
                            else:
                                verifier.append(False)
                    else:
                        for value in data[data['type']]:
                            if value in response.text:
                                verifier.append(True)
                            else:
                                verifier.append(False)                     

            else:    
                #判断key的值，key的值作为索引
                if data['type']=='word':
                    for value in data['words']:
                        #print('4')
                        #print(value)
                        if value in response.text:
                            verifier.append(True)
                        else:
                            verifier.append(False)
                
                elif data['type']=='status':
                    #print('5')
                    #print(data['status'])
                   
                    for value in data['status']:
                        #print(value)
                        if response.status_code in data['status']:
                            verifier.append(True)
                        else:
                            verifier.append(False)
                
                #有待验证
                #有待验证
                else:
                    for i in data[data['type']]:
                        #print('6')
                        #print(value)
                        for value in i:
                            if value in response.text:
                                verifier.append(True)
                            else:
                                verifier.append(False)
        

        if self.match_condition[num]=="and":
            if False not in verifier:
                flag='1'
                output.result(flag,self.id[num])
            else:
                flag='2'
                output.result(flag,self.id[num])
        elif self.match_condition[num]=="or":
            if True in verifier:
                flag='1'
                output.result(flag,self.id[num])
            else:
                flag='2'
                output.result(flag,self.id[num])


    #一个默认的请求头
    def RequestHeader(self):
        random_ip = "10.0.{}.{}".format(random.randint(1, 254), random.randint(1, 254))
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Accept-Language": "en",
            "X-Forwarded-For": random_ip,
            "X-Real-IP" :random_ip,
        }
        return headers
