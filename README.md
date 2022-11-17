# OA - EXPTOOL OA综合利用工具(11-14号更新)

### 通知
最近小伙伴反应出现bug无法使用的问题

一个问题系统报错：请看修复第一条
请修改环境变量：

以python的环境变量运行 python3 否则会报错

python运行python2的话会出现中文乱码从而报错

建议安装python3.7以上版本

再次声明 ！！！！

遇到问题请联系我 出现问题不一定是我bug 但一定是我的问题

### 使用

- 第一次使用脚本请运行pip3 install -r requirements.txt
- 然后使用show查看命令合集
- 主要针对的是OA产品的漏洞检测
- 产生的攻击行为和后果与本人无关
- 本工具无毒无后门，因为含有冰蝎木马文件原因请下载时关闭防护软件
- 存在问题请联系我
- 本人第一款工具，因为有很多不完善的地方 发出来希望各位前辈在使用的同时提供建议和测试，暂定版本为0.5
- 后续的设想是增加指纹识别，当然扫描结果保存的功能暂时没有加，后续也会增加
#



####更新记录11月14号
----

增加帆软2017敏感信息泄露poc

增加泛微OA_hrmcareerApply_sql poc,泛微OA_mysql_config数据库信息泄漏,泛微OA_jquery_filetree,泛微OA_Verify_QuickLogin
泛微OA_signnature_任意文件访问,泛微OA_uploader_OPerate_2022,泛微OA_V10_前台sql

增加红帆OA_非医疗版_任意文件上传

增加万户OA_document_sql，万户OA DownloadServlet 任意文件读取漏洞

增加nc_xbr_rce，用友_U8_f5_sql，用友GRP_u8_upload_data

优化优化泛微OA的检测，对检测增加内容判断，提高准确性，优化红帆漏洞poc增加payload，优化蓝凌oa poc的准确性 去掉部分exp，优化通达后台xxs包含漏洞的线程问题，优化万户模块下的poc提高准确性
## 主界面

----
![cmd](readme/cmd.jpg)


### 安装教程
> python scan.py  （python3 请注意变量 这是python的问题 当然也是我的问题）
> 
> install # 安装第三方库
> 


如果有任何建议可以找作者联系。欢迎各位提供改进方案
## 作者：西瓜麻辣烫

联系方式/问题群聊：
 
![vx](readme/vx.jpg) ![ql](readme/ql.jpg)

