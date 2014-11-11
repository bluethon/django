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

#--------------------------------------
#第四章
#--------------------------------------

#.py中使用模版 文件开头加入
from django.conf import settings
settings.configure()

#用两个大括号括起来的文字（例如 {{ person_name }} ）称为 变量(variable)

#给标签增加一个 reversed 使得该列表被反向迭代：
{% for athlete in athlete_list reversed %}
...
{% endfor %}

#检测列表为空,`` for`` 标签支持一个可选的`` {% empty %}`` 分句
{% for athlete in athlete_list %}
    <p>{{ athlete.name }}</p>
{% empty %}
    <p>There are no athletes. Only computer programmers.</p>
{% endfor %}

#locals() 。它返回的字典对所有局部变量的名称与值进行映射。
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
