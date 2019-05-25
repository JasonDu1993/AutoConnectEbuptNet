[win]
每6个小时自动连接东信北邮网络，其中可以通过修改set INTERVAL= 21600参数来修改自动连接的时间，单位为秒

1，auto_connect_network.py文件修改自己的账号密码，第29行auth_user后面参数改为自己的用户名，auth_pass修改为每周的密码，
密码每周会换，后续优化是如何通过远程自动修改为每周更新的密码，发送post请求后的数据会存储在log.txt
2，双击运行run.bat文件，不能关闭该窗口
4，（可选）运行background_run.vbs后台运行文件，我没有测试不知道行不行
[linux]
1,可以后台直接运行script.py脚本
环境需要：
python3、request、tdqm、argparse、time
使用方式
nohup python3 script.py -u zhoud -p qeff31sa &
-t 表示每隔多少秒连接一次网络，默认为3600秒
-r 与-t联合使用，默认为True,即循环调用post请求连接网络
-u 用户名（改成自己的）
-p 密码（每周记得修改）

[优化]
1，让run.bat脚本跟随电脑重启时自动启动脚本，防止win10自动更新
https://jingyan.baidu.com/article/9989c746fafee2f648ecfe2c.html Win10如何将程序加入启动项 程序怎么随系统启动
    （1）windows键+r进行命令行窗口，然后输入shell:startup会跳转到一个文件夹，
        如：C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    （2）然后右键run.bat->发送到->桌面快捷方式，可以改一下名称，随意吧
    （3）然后把桌面上的这个快捷方式拖到刚才那个文件即可

https://blog.csdn.net/baidu_35679960/article/details/79400093 win7如何使程序开机自启(开机自动启动应用程序)


2，还可以通过在系统中直接设置 每1小时自动执行执行python脚本
    linux下比较方便，直接设置 crontab即可。
    windows下可以设置机器的自动任务计划，具体步骤如下：
    https://www.cnblogs.com/mousachi2007/p/10194695.html windows下 Python脚本自动执行
    （1）开始->所有工具->windows管理工具->任务计划程序
    （2）创建任务
        （2.1）常规 ——填写程序名称（随意）
        （2.2）触发器 ——新建，设置为每天固定时间开始执行，每隔一个小时重复一次
        （2.3）操作 ——新建，设置为执行python脚本或者run.bat脚本都可以，且设置正确的命令行参数 （包括python脚本路径和参数5）