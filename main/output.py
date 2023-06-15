def exception(flag):
    if flag=='1':
        print("\033[31m[-]\033[0m 参数错误，type仅支持file/url类型")
    elif flag=="2":
        print("\033[31m[-]\033[0m 缺少重要的参数，请重新输入")
    elif flag=="3":
        print("\033[31m[-]\033[0m 目标可能出错了，请检查需要配置的目标")
    elif flag=="4":
        print("\033[31m[-]\033[0m 未找到相关POC，请检查配置")
    elif flag=="5":
        print("\033[31m[-]\033[0m 未找到POC序列号，请先show")
    elif flag=="6":
        print("\033[31m[-]\033[0m POC的name定义错误，请重新set")

    elif flag=="7":
        print("    \033[33m[*]\033[0m 请求发生错误，可能连接超时")

def result(flag,name):
    if flag=='1':
        print('''    \033[32m[*]\033[0m 存在:{} 漏洞'''
        .format(name))

    
    elif flag=='2':
        print('''    \033[31m[-]\033[0m 不存在:{} 漏洞'''.format(name))

def load(url):
    print(
    '''
    \033[34m[*]\033[0m 正在检测:{} 请稍等...........'''.format(url))



