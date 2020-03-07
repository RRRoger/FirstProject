# Ubuntu源码安装Odoo10社区版


### 1、* (*pass 这步可以不做*) 更新Ubuntu服务器软件源
```bash
sudo apt-get update  #更新软件源  
sudo apt-get dist-upgrade -y  #更新软件包，自动查找依赖关系  
sudo shutdown -r now  #重启服务器，以更新改变的内容
```

### 2、新建系统用户用于运行Odoo程序
```bash
cat /etc/passwd  #查看是否已经存在odoo用户
sudo adduser --system --home=/home/odoo --group odoo  #新建系统用户odoo，指定home目录为/home/odoo
```

> 系统用户不能用于登录并且没有shell，但当需要以它的身份进行特定操作时，可以用su命令切换用户：

<div style="color:red">
	<ui>
		<li>sudo vim /etc/passwd</li>
		<li>odoo那一行改成如下;可以用 sudo su odoo 进入odoo用户</li>
		<li>/home/odoo:/bin/bash</li>
	</ui>
</div>

```bash
sudo su odoo  # 将当前终端登录切换到odoo用户, 命令失败参考上面操作
exit  #退出
```

> 命令运行后会自动从当前目录切换到odoo用户的home目录/home/odoo。操作完毕后输入exit命令，离开odoo用户的shell，回到登录所用的用户。

### 3、下载最新版Odoo10源码
```bash
sudo apt-get install -y git  # 安装git软件
sudo su odoo # 切换到odoo用户
git clone -b 10.0 https://github.com/odoo/odoo.git  # 下载Odoo10代码
mv odoo odoo10  # 修改文件夹名称为odoo10
exit #退出odoo用户  
sudo chmod -R 774 /home/odoo/odoo10 # 修改读取、写入、执行权限
```

```bash
sudo apt-get install -y git
sudo su odoo
git clone -b 10.0 https://github.com/odoo/odoo.git
mv odoo odoo10
exit
sudo chmod -R 774 /home/odoo/odoo10
```

### 4、安装和配置数据库服务器PostgreSQL
> 数据库默认用户名：postgres，没有密码

```bash
sudo apt-get install -y postgresql #安装PostgreSQL
sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt odoo #创建数据库用户odoo，输入两次密码odoo
```

```bash
sudo apt-get install -y postgresql
sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt odoo
```

### 4、安装Python运行库
> odoo源码目录下的 requirements.txt 文件里面列出了 odoo10 依赖的所有 Python lib。
因为lxml ldap psycopg2 需要使用gcc进行编译，所以需要先安装开发相关的库 libxml2, libxslt, libpq-dev, libldap2-dev, libsasl2-dev。

```bash
sudo apt-get install -y python-dev libxml2-dev libxml2 libxslt-dev libpq-dev libldap2-dev libsasl2-dev libevent-dev  #安装开发相关的库
sudo apt-get install -y libjpeg8-dev libpng12-dev libfreetype6-dev zlib1g-dev libwebp-dev libtiff5-dev libopenjpeg-dev libzip-dev  #安装Pillow依赖包
sudo apt-get install -y python-babel python-dateutil python-decorator python-docutils python-feedparser python-imaging
sudo apt-get install -y python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid
sudo apt-get install -y python-passlib python-psutil python-psycopg2 python-pychart python-pydot python-pyparsing
sudo apt-get install -y python-pypdf python-reportlab python-requests python-suds python-tz python-vatnumber python-vobject
sudo apt-get install -y python-werkzeug python-xlsxwriter python-xlwt python-yaml python-gevent
sudo apt-get install -y python-pip #安装pip，如果系统未安装
sudo pip install -r /home/odoo/odoo10/requirements.txt #使用 pip 安装 odoo-10 依赖的 Python 库
sudo apt-get -f install  #强制安装依赖
```

```bash
sudo apt-get install -y python-dev libxml2-dev libxml2 libxslt-dev libpq-dev libldap2-dev libsasl2-dev libevent-dev
sudo apt-get install -y libjpeg8-dev libpng12-dev libfreetype6-dev zlib1g-dev libwebp-dev libtiff5-dev libopenjpeg-dev libzip-dev
sudo apt-get install -y python-babel python-dateutil python-decorator python-docutils python-feedparser python-imaging
sudo apt-get install -y python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid
sudo apt-get install -y python-passlib python-psutil python-psycopg2 python-pychart python-pydot python-pyparsing
sudo apt-get install -y python-pypdf python-reportlab python-requests python-suds python-tz python-vatnumber python-vobject
sudo apt-get install -y python-werkzeug python-xlsxwriter python-xlwt python-yaml python-gevent
sudo apt-get install -y python-pip
sudo pip install -r /home/odoo/odoo10/requirements.txt
sudo apt-get -f install
```

### 6、安装wkhtmltopdf
> odoo源码目录下的 requirements.txt 文件里面列出了 odoo10 依赖的所有 Python lib。
因为lxml ldap psycopg2 需要使用gcc进行编译，所以需要先安装开发相关的库 libxml2, libxslt, libpq-dev, libldap2-dev, libsasl2-dev。

> 下载安装wkhtmltopdf(Odoo使用wkhtmltopdf来输出pdf)：


<div style="color:red">
	<ui>
		<li>如果安装出现问题参考此链接</li>
		<li><a>https://blog.csdn.net/tianlunshu/article/details/69946656</a></li>
	</ui>
</div>

```bash
sudo wget http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb #下载wkhtmltopdf，注意根据操作系统选择相应版本
sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb  #安装wkhtmltopdf  
sudo apt-get -f install  #强制修复出现的依赖关系错误，清理上面安装过程中遇到的错误
sudo cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf  #安装完成后将可执行文件复制到usr/bin中
sudo chown root:root /usr/bin/wkhtmltopdf  #更改所有者为root用户
sudo chmod +x /usr/bin/wkhtmltopdf  #并增加可执行属性
sudo apt-get install -y ttf-wqy-zenhei ttf-wqy-microhei  #安装中文字体
wkhtmltopdf www.baidu.com baidu.pdf  #打印一个网页到当前目录，如果成功生成pdf则表明安装成功
```

```bash
sudo wget http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb
sudo apt-get -f install
sudo cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf
sudo chown root:root /usr/bin/wkhtmltopdf
sudo chmod +x /usr/bin/wkhtmltopdf
sudo apt-get install -y ttf-wqy-zenhei ttf-wqy-microhei
wkhtmltopdf www.baidu.com baidu.pdf
```

### 7、安装nodejs、node-less

```bash
sudo apt-get install -y nodejs node-less npm
sudo npm install -g less-plugin-clean-css
```

### 8、配置Odoo的启动文件
> 用Ubuntu自带的nano编辑器在/etc/odoo/目录下创建odoo.conf文件。

```bash
sudo mkdir /etc/odoo
sudo vim /etc/odoo/odoo.conf
```
> 复制下面的内容到nano编辑器内

```
[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = odoo
db_password = odoo
addons_path = /home/odoo/odoo10/odoo/addons,/home/odoo/odoo10/addons
```

> 修改配置文件（/etc/odoo/odoo.conf）的权限

```bash
sudo chown odoo: /etc/odoo/odoo.conf
sudo chmod 640 /etc/odoo/odoo.conf
```

> 复制启动文件到/usr/bin/目录下，并尝试启动Odoo服务

```bash
sudo cp /home/odoo/odoo10/setup/odoo /usr/bin/odoo
sudo chown odoo: /usr/bin/odoo
sudo chmod 755 /usr/bin/odoo
cd /home/odoo/odoo10
python setup.py install
sudo su - odoo -s /bin/bash
/usr/bin/odoo -c /etc/odoo/odoo.conf
```

> 在浏览器输入http://ip:8069 检查

### 9、配置启动脚本
> 用Ubuntu自带的nano编辑器在/etc/init.d/目录下创建odoo启动脚本文件，然后把它改成可执行文件，赋给root用户。

```bash
sudo vim /etc/init.d/odoo
```
> 复制下面的内容到nano编辑器内

```bash
#!/bin/bash
### BEGIN INIT INFO
# Provides:          odoo
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start odoo daemon at boot time
# Description:       Enable service provided by daemon.
# X-Interactive:     true
### END INIT INFO
## more info: http://wiki.debian.org/LSBInitScripts

. /lib/lsb/init-functions

PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin
DAEMON=/usr/bin/odoo
NAME=odoo
DESC=odoo
CONFIG=/etc/odoo/odoo.conf
LOGFILE=/var/log/odoo/odoo-server.log
PIDFILE=/var/run/${NAME}.pid
USER=odoo
export LOGNAME=$USER

test -x $DAEMON || exit 0
set -e

function _start() {
    start-stop-daemon --start --quiet --pidfile $PIDFILE --chuid $USER:$USER --background --make-pidfile --exec $DAEMON -- --config $CONFIG --logfile $LOGFILE
}

function _stop() {
    start-stop-daemon --stop --quiet --pidfile $PIDFILE --oknodo --retry 3
    rm -f $PIDFILE
}

function _status() {
    start-stop-daemon --status --quiet --pidfile $PIDFILE
    return $?
}


case "$1" in
        start)
                echo -n "Starting $DESC: "
                _start
                echo "ok"
                ;;
        stop)
                echo -n "Stopping $DESC: "
                _stop
                echo "ok"
                ;;
        restart|force-reload)
                echo -n "Restarting $DESC: "
                _stop
                sleep 1
                _start
                echo "ok"
                ;;
        status)
                echo -n "Status of $DESC: "
                _status && echo "running" || echo "stopped"
                ;;
        *)
                N=/etc/init.d/$NAME
                echo "Usage: $N {start|stop|restart|force-reload|status}" >&2
                exit 1
                ;;
esac

exit 0
```

>接下来修改odoo文件的权限。

```sh
sudo chown root: /etc/init.d/odoo
sudo chmod 755 /etc/init.d/odoo
```
> 增加配置文件的参数，修改/etc/odoo/odoo.conf文件

```sh
sudo vim /etc/odoo/odoo.conf
```
> 复制下面的内容到odoo.conf文件内

```
data_dir = /var/lib/odoo
log_level = info
logfile = /var/log/odoo/odoo-server.log
logrotate = True
;xmlrpc_port = 8069
```

> 配置文件里指定了日志文件和附件的存储位置，因此要创建这个目录，同时还得让它能被odoo用户读写：

<!--
```bash
sudo mkdir /var/lib/odoo  #新建附件存储目录
sudo chown odoo: /var/lib/odoo  #修改所有者为odoo用户
sudo chmod 774 /var/lib/odoo  #修改为odoo用户读取和写入
sudo mkdir /var/log/odoo  #新建日志存储目录
sudo chown odoo:root /var/log/odoo  #修改所有者为odoo用户
```
-->

```bash
sudo mkdir /var/lib/odoo
sudo chown odoo: /var/lib/odoo
sudo chmod 774 /var/lib/odoo
sudo mkdir /var/log/odoo
sudo chown odoo:root /var/log/odoo
```

> 启动odoo服务


<div style="color:red;">
	<ui>
		<li>如果`service odoo start`报错;Failed to start odoo.service: Unit odoo.service not found.</li>
		<li>执行</li>
		<li>sudo systemctl unmask odoo.service</li>
	</ui>
</div>


```bash
sudo service odoo start
```

> 查看odoo的日志判断是否启动成功

```bash
tail -f /var/log/odoo/odoo-server.log
```

> 检查odoo服务器是否可以被正常停止：

```bash
sudo service odoo stop
```

### 10、将Odoo设为开机自启动 (可以不做)
> 让启动脚本随着Ubuntu服务器的开、关机而自动启动、关闭Odoo服务。

```bash
sudo update-rc.d odoo defaults
```

> 现在就可以重启你的服务器，当你再次登录服务器，Odoo应该已经在运行了。输入以下命令查看Odoo是否已在运行。

```bash
ps -ef|grep odoo
```

### 11、*用nginx代理odoo
```bash
sudo apt-get  install nginx
```
> 在/etc/nginx/sites-enabled 中增加一个可用的server

```
server{
　　listen 80;
　　server_name odoo10;
　　location / {
　　　　proxy_set_header Host $host;
　　　　proxy_set_header X-Real-IP $remote_addr;
　　　　proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
　　　　proxy_pass http://0.0.0.0:8069;
　　}
}
```

> 把 /etc/nginx/sites-enabled/default 里面80注释或者改成其他端口


# ps:

### 报错: error: 'ascii' codec can't encode characters in position 18-20: ordinal not in range(128)
 <div style="color:red;">
	<ui>
		<li>实际在代码里可以避免; 中文字符前加u可以避免; 如果不想改代码, 可以参考</li>
	</ui>
</div>

* 看原先的编码

> 进python2.7

```python
import sys
print sys.getdefaultencoding()
```

* 先看下site-packages目录的位置

```python
import sys
print sys.path
# */site-packages 目录下
```

* 到该目录下新建文件 sitecustomize.py, 写入以下内容, 重启python解释器

```python
# encoding=utf8 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```



