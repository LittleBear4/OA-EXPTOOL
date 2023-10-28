import multiprocessing

from urllib import parse

from main import output
from main import request
from main import yaml


def POC_select(poc,filenames):
    if poc not in filenames and poc !="None":
        flag="6"
        output.exception(flag)
        return
    if poc == "None":
        return True
    return False



def Type_deal(value, type):

    if type=="file":
        #处理文件
        result=[]

        try:
            with open(value,'r',encoding ="utf-8") as file_object:
                lines = file_object.readlines()
        except:
            flag="3"
            output.exception(flag)
            return None
        pool = multiprocessing.Pool(1)
        for url in lines:
            url=url.strip('\n')
            result.append(Request_head_deal(url))
        #print(result)
        return result
        pool.close()
        pool.join()

    elif type=="url":
        #处理用户输入的目标url
        if value is None:
            return None
        try:
            result = []
            target = Request_head_deal(value)
            result.append(target)
            return result
        except:
            return None
        return target

    else:
        flag='1'
        output.exception(flag)






#请求协议处理：采用http还是https请求
def Request_head_deal(target): 
    try:
        if target is None:
            raise ValueError("target is None")
        if not target.startswith("http://") and not target.startswith("https://"):
            target = "http://" + target
        elif ":443" in target and "://" not in target:
            target = "https://" + target
        #print(target)
        parse1 = parse.urlparse(target)
        #print(parse1)
        port = str(parse1.port) 
        if not parse1.port:
            if parse1.scheme == 'http':
                port = '80'
            elif parse1.scheme == 'https':
                port = '443'
        item = {
            'host': parse1.hostname,
            'port': port,
            'scheme': parse1.scheme,
            'path':parse1.path,
        }
        target=item['scheme'].strip()+':'+'//'+item['host'].strip()+':'+item['port'].strip()
        #print(target)
        return target
    except ValueError as e:
        return None

        




