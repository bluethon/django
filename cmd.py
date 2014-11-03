#--------------
#第二章
#---------------
#init
django-admin.py startproject [mysite]
#运行开发服务器
python manage.py runserver [port]
#允许非本地连接访问 0.0.0.0代表侦听任意网络接口
python manage.py runserver 0.0.0.0:8000

#--------------
#第三章
#---------------
#urls注解
#代表当前目录且优先查找
'',
#引号内为正则表达式 ^代表开头 $代表结尾
    ('^hello/$', hello),
#任何位置 插入如下语句触发出错页 来debug
assert False
