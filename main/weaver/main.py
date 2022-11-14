import time
import argparse
import multiprocessing
from pyfiglet import Figlet
from rich.console import Console
from poc import Bsh_RCE,E_Bridge_Arbitrary_File_Read,E_Cology_Database_Leak,E_Cology_V8_Sql,E_Cology_WorkflowServiceXml_RCE
from poc import Weaver_Common_Ctrl_Upload,WorkflowCenterTreeData_Sql,Weaver_V9_uploadOperation,Weaver_oa_infiledonload
from poc import Weaver_e_office_userlogin,E_office_upload,Weaver_e_officeserver_readfile,E_office_group_xml_sql,E_Cology_user_data,E_Cology_LoginsSSo_sql,E_Cology_getData_sql,泛微OA_hrmcareerApply_sql,泛微OA_jquery_filetree,泛微OA_Verify_QuickLogin,泛微OA_mysql_config数据库信息泄漏,泛微OA_signnature_任意文件访问,泛微OA_uploader_OPerate,泛微OA_V10_前台sql

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    list1 = ['Bsh_RCE','E_Bridge_Arbitrary_File_Read']
    list2 = ['E_Cology_Database_Leak','E_Cology_V8_Sql','E_Cology_WorkflowServiceXml_RCE',
             'Weaver_Common_Ctrl_Upload','WorkflowCenterTreeData_Sql','Weaver_V9_uploadOperation',
             'Weaver_oa_infiledonload','Weaver_e_office_userlogin','E_office_upload',
             'Weaver_e_officeserver_readfile','E_office_group_xml_sql','E_Cology_user_data',
             'E_Cology_LoginsSSo_sql','E_Cology_getData_sql','泛微OA_hrmcareerApply_sql','泛微OA_jquery_filetree','泛微OA_Verify_QuickLogin','泛微OA_mysql_config数据库信息泄漏','泛微OA_signnature_任意文件访问','泛微OA_uploader_OPerate','泛微OA_V10_前台sql']
    for a in list1:
        eval(a + ".check(target_url)")
        time.sleep(0.01)
    for i in list2:
        eval(i + ".main(target_url)")
        time.sleep(0.01)
    

if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('weaver OA-Exp'), style='bold blue')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                console.print(now_time() + " [INFO]     正在检测:{}".format(url)+'\n', style='bold yellow')
                pool.apply(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            console.print(now_time() + " [INFO]     正在检测:{}".format(args.url)+'\n', style='bold yellow')
            main(args.url)
        else:
            console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.console.print('\nCTRL+C 退出', style='reverse bold red')