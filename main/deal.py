import sys
import os
import main
import main.main
import datetime
import time
import config_file as cfg_file
from rich.console import Console

from main.YMoa import 一米OA_beifenAction_任意文件读取

from main.yonyou import nc_beanshell_rce,nc_upload_rce,nc_erp_sql,nc_u8_test_sql,nc_erp_directory

from main.yonyou import 用友畅捷通T_updata_任意文件上传,nc_U8_getSessionList,fe_oa_directiry, nc_readfile_everything,nc_xbr_rce,用友_U8_f5_sql,用友GRP_u8_upload_data,yongyou_KSOA_imageupload

from main.seeyou import 致远OA_A6_createMysql_数据库敏感信息泄露, 致远OA_A6_DownExcelBeanServlet_用户敏感信息下载, 致远OA_A6_initDataAssess_用户敏感信息泄露, \
    致远OA_A6_setextno_SQL注入Getshell, 致远OA_A6_test_SQL注入Getshell, 致远OA_A8_htmlofficeservlet_RCE, \
    致远OA_getSessionList_Session泄漏, 致远OA_ajax_登录绕过_任意文件上传, 致远OA_webmail_任意文件下载, 致远OA_Session泄露_任意文件上传, 致远OA_Fastjson_反序列化,致远OA_A6_config_jsp敏感信息泄露,致远OA_A8_status_jsp敏感信息泄露


from main.Anywhere import (通达OA_v11_5_swfupload_sql, 通达OA_v11_5_任意用户登录, 通达OA_v11_6_insert_sql, 通达OA_v11_6_report_bi_sql, 通达OA_v11_6_任意文件删除_RCE, 通达OA_v11_7_后台sql注入,通达OA_v11_7_在线用户登录, 通达OA_v11_8_api_任意文件上传, 通达OA_v11_8_getway_远程文件包含, 通达OA_v2014_get_contactlist, 通达OA_v2017_action_upload,通达OA_v2017_任意用户登录,通达OA_v11_8_logincheck,通达OA_v11_8_后台包含xss,通达OA_v11_9_getdata)

from main.ezoffice import (万户OA_download_ftp, 万户OA_download_http, 万户OA_download_old, 万户OA_fileupload_controller,万户OA_office_任意文件上传,万户OA_document_sql,万户OA_smart_upload_文件上传,万户OA_download_servelet)

from main.Landray import (蓝凌OA_任意文件写入, 蓝凌OA_treeXml_远程命令执行, 蓝凌OA_datajson_命令执行, 蓝凌OA_custom_任意文件读取)

from main.weaver import Bsh_RCE,E_Bridge_Arbitrary_File_Read,E_Cology_Database_Leak,E_Cology_V8_Sql,E_Cology_WorkflowServiceXml_RCE
from main.weaver import Weaver_Common_Ctrl_Upload,WorkflowCenterTreeData_Sql,Weaver_V9_uploadOperation,Weaver_oa_infiledonload
from main.weaver import Weaver_e_office_userlogin,E_office_upload,Weaver_e_officeserver_readfile,E_office_group_xml_sql,E_Cology_user_data,E_Cology_LoginsSSo_sql,E_Cology_getData_sql,泛微OA_hrmcareerApply_sql,泛微OA_jquery_filetree,泛微OA_Verify_QuickLogin,泛微OA_mysql_config数据库信息泄漏,泛微OA_signnature_任意文件访问,泛微OA_uploader_OPerate,泛微OA_V10_前台sql,泛微OA_doexcel,泛微OA_ktree_upload,泛微OA_v10_upload,泛微OA_eoffice8_upload,泛微OA_moblie_v6_sql

from main.FineReport import (帆软_v8_get_json_任意文件读取, 帆软_v9_design_文件覆盖上传,帆软_2012_信息泄露)

from main.HtianDL import ( 华天动力OA_8000版_sql)

from main.kingdee import (金蝶OA_server_file_目录遍历, 金蝶OA_path_任意文件下载, 金蝶OA_Apusic应用服务器_目录遍历)

from main.ioffice import (红帆OA_IOFILE_任意文件读取, 红帆OA_医疗云sql注入,红帆OA_非医疗版_任意文件上传,红帆OA_前台sql注入)

from main.Rev import (启莱OA_treelist_sql, 启莱OA_messageurl_sql, 启莱OA_treelist_sql)

from main.smart import (智明OA_EmailDownload_任意文件下载)

from main.XinDian import 新点OA_Excel_敏感信息泄露

console = Console() 
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


class Logger(object):
    def __init__(self, filename='default.log', add_flag=True, stream=sys.stdout):
        self.terminal = stream
        print("filename:", filename)
        self.filename = filename
        self.add_flag = add_flag
        self.log = open(filename, 'a+')

    def write(self, message):
    	if self.add_flag:
	        with open(self.filename, 'a+') as log:
	            self.terminal.write(message)
	            log.write(message)


    def flush(self):
        pass
        
def logPath():        
    sys.stdout = Logger("report.log", sys.stdout)
    
def Deal(target_url): 
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    console.print(now_time() + " [INFO]     正在检测:{}".format(target_url)+'\n', style='bold yellow')
   
def ymoa(target_url):
    Deal(target_url)
    logPath()
    list = ['一米OA_beifenAction_任意文件读取']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
        
def yyoa(target_url):
    Deal(target_url)
    nc_erp_sql.POC_1(target_url)
    list = ['nc_beanshell_rce','nc_upload_rce','nc_u8_test_sql','nc_erp_directory',
            '用友畅捷通T_updata_任意文件上传','nc_U8_getSessionList','fe_oa_directiry','nc_readfile_everything','nc_xbr_rce','用友_U8_f5_sql','用友GRP_u8_upload_data','yongyou_KSOA_imageupload']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def zyoa(target_url):
    Deal(target_url)    
    list = ['致远OA_A6_createMysql_数据库敏感信息泄露', '致远OA_A6_DownExcelBeanServlet_用户敏感信息下载', '致远OA_A6_initDataAssess_用户敏感信息泄露',
            '致远OA_A6_setextno_SQL注入Getshell', '致远OA_A6_test_SQL注入Getshell','致远OA_A8_htmlofficeservlet_RCE',
            '致远OA_getSessionList_Session泄漏', '致远OA_ajax_登录绕过_任意文件上传', '致远OA_webmail_任意文件下载',
            '致远OA_Session泄露_任意文件上传','致远OA_A6_config_jsp敏感信息泄露','致远OA_A8_status_jsp敏感信息泄露',
            '致远OA_Fastjson_反序列化']
    for i in list:
        eval(i+".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
        
def tdoa(target_url):
    Deal(target_url) 
    list = ['通达OA_v11_5_swfupload_sql', '通达OA_v11_5_任意用户登录','通达OA_v11_6_insert_sql',
            '通达OA_v11_6_report_bi_sql', '通达OA_v11_6_任意文件删除_RCE', '通达OA_v11_7_后台sql注入',
            '通达OA_v11_7_在线用户登录', '通达OA_v11_8_api_任意文件上传', '通达OA_v11_8_getway_远程文件包含',
            '通达OA_v2014_get_contactlist', '通达OA_v2017_action_upload', '通达OA_v2017_任意用户登录','通达OA_v11_8_logincheck','通达OA_v11_8_后台包含xss','通达OA_v11_9_getdata']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def whoa(target_url):
    Deal(target_url)     
    list = ['万户OA_download_ftp', '万户OA_download_http', '万户OA_download_old',
            '万户OA_fileupload_controller', '万户OA_office_任意文件上传','万户OA_document_sql','万户OA_smart_upload_文件上传','万户OA_download_servelet']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')

def lloa(target_url):
    Deal(target_url) 
    list = ['蓝凌OA_任意文件写入', '蓝凌OA_treeXml_远程命令执行','蓝凌OA_datajson_命令执行','蓝凌OA_custom_任意文件读取']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.015)
    print('\n')

def fwoa(target_url):
    Deal(target_url)
    list1 = ['Bsh_RCE','E_Bridge_Arbitrary_File_Read']
    list2 = ['E_Cology_Database_Leak','E_Cology_V8_Sql','E_Cology_WorkflowServiceXml_RCE',
             'Weaver_Common_Ctrl_Upload','WorkflowCenterTreeData_Sql','Weaver_V9_uploadOperation',
             'Weaver_oa_infiledonload','Weaver_e_office_userlogin','E_office_upload',
             'Weaver_e_officeserver_readfile','E_office_group_xml_sql','E_Cology_user_data',
             'E_Cology_LoginsSSo_sql','E_Cology_getData_sql','泛微OA_hrmcareerApply_sql','泛微OA_jquery_filetree','泛微OA_Verify_QuickLogin','泛微OA_mysql_config数据库信息泄漏','泛微OA_signnature_任意文件访问','泛微OA_uploader_OPerate','泛微OA_V10_前台sql','泛微OA_doexcel','泛微OA_ktree_upload','泛微OA_v10_upload','泛微OA_eoffice8_upload','泛微OA_moblie_v6_sql']
    for a in list1:
        eval(a + ".check(target_url)")
        time.sleep(0.01)
    for i in list2:
        eval(i + ".main(target_url)")
        time.sleep(0.01)
    print('\n') 
    
def froa(target_url):
    Deal(target_url)
    list = ['帆软_v8_get_json_任意文件读取', '帆软_v9_design_文件覆盖上传','帆软_2012_信息泄露']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')

def HtianDLoa(target_url): 
    Deal(target_url)
    list = [ '华天动力OA_8000版_sql']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def jdoa(target_url): 
    Deal(target_url)        
    list = ['金蝶OA_server_file_目录遍历', '金蝶OA_path_任意文件下载','金蝶OA_Apusic应用服务器_目录遍历']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def hfoa(target_url): 
    Deal(target_url)        
    list = ['红帆OA_IOFILE_任意文件读取', '红帆OA_医疗云sql注入','红帆OA_非医疗版_任意文件上传','红帆OA_前台sql注入']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def qloa(target_url): 
    Deal(target_url)        
    list = ['启莱OA_treelist_sql', '启莱OA_messageurl_sql','启莱OA_treelist_sql']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')

def zxoa(target_url):
    Deal(target_url)    
    list = ['致翔OA_msglog_sql']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def zmoa(target_url):  
    Deal(target_url) 
    list = ['智明OA_EmailDownload_任意文件下载']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
    
def xdoa(target_url):  
    Deal(target_url) 
    list = ['新点OA_Excel_敏感信息泄露']
    for i in list:
        eval(i + ".main(target_url)")
        time.sleep(0.2)
    print('\n')
