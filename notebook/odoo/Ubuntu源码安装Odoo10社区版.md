# Ubuntu源码安装Odoo10社区版

> 一些问题可以在下面的问题列表里找到
>
> 1. 报错: error: 'ascii' codec can't encode characters in position 18-20: ordinal not in range(128)
> 2. Rsync使用帮助
> 3. chown 更改目录的所有者
> 4. 数据库操作指令
> 5. pip 换源
> 6. apt 换源


### 1、* (*pass 这步可以不做*) 更新Ubuntu服务器软件源
```bash
# 更新软件源 
sudo apt-get update 
# 更新软件包，自动查找依赖关系  
sudo apt-get dist-upgrade -y
# 重启服务器，以更新改变的内容
sudo shutdown -r now
```

### 2、新建系统用户用于运行Odoo程序
```bash
# 查看是否已经存在odoo用户
cat /etc/passwd
# 新建系统用户odoo，指定home目录为/home/odoo
sudo adduser --system --home=/home/odoo --group odoo
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

<div style="color:red">
	<ui>
		<li>由于源码下载龟速, 请直接用根目录的"odoo10.zip"压缩包解压</li>
	</ui>
</div>


```bash
# 安装git软件
sudo apt-get install -y git

# 切换到odoo用户
sudo su odoo

# 下载Odoo10代码
git clone -b 10.0 https://github.com/odoo/odoo.git

# 修改文件夹名称为odoo10
mv odoo odoo10

#退出odoo用户  
exit

# 修改读取、写入、执行权限
sudo chmod -R 774 /home/odoo/odoo10
```

### 4、安装和配置数据库服务器PostgreSQL
> 数据库默认用户名：postgres，没有密码

```bash
#安装PostgreSQL
sudo apt-get install -y postgresql

#创建数据库用户odoo，输入两次密码odoo
sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt odoo
```

### 5、安装Python运行库和wkhtmltopdf

<div style="color:red">
	<ui>
		<li>由于源码下载龟速, 请直接用根目录的压缩包"wkhtmltopdf.zip"解压</li>
	</ui>
</div>

> odoo源码目录下的 requirements.txt 文件里面列出了 odoo10 依赖的所有 Python lib。
因为lxml ldap psycopg2 需要使用gcc进行编译，所以需要先安装开发相关的库 libxml2, libxslt, libpq-dev, libldap2-dev, libsasl2-dev。

```bash
# 安装开发相关的库
sudo apt-get install -y python-dev libxml2-dev libxml2 libxslt-dev libpq-dev libldap2-dev libsasl2-dev libevent-dev

# 安装Pillow依赖包
sudo apt-get install -y libjpeg8-dev libpng12-dev libfreetype6-dev zlib1g-dev libwebp-dev libtiff5-dev libopenjpeg-dev libzip-dev

sudo apt-get install -y python-babel python-dateutil python-decorator python-docutils python-feedparser python-imaging

sudo apt-get install -y python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid

sudo apt-get install -y python-passlib python-psutil python-psycopg2 python-pychart python-pydot python-pyparsing

sudo apt-get install -y python-pypdf python-reportlab python-requests python-suds python-tz python-vatnumber python-vobject

sudo apt-get install -y python-werkzeug python-xlsxwriter python-xlwt python-yaml python-gevent

# 安装pip，如果系统未安装
sudo apt-get install -y python-pip

# 使用 pip 安装 odoo-10 依赖的 Python 库
sudo pip install -r /home/odoo/odoo10/requirements.txt

# 强制安装依赖
sudo apt-get -f install
```

> 下载安装wkhtmltopdf(Odoo使用wkhtmltopdf来输出pdf)：


<div style="color:red">
	<ui>
		<li>如果安装出现问题参考此链接</li>
		<li><a>https://blog.csdn.net/tianlunshu/article/details/69946656</a></li>
	</ui>
</div>

```bash
# 下载wkhtmltopdf，注意根据操作系统选择相应版本
sudo wget http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb

# 安装wkhtmltopdf  
sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb

# 强制修复出现的依赖关系错误，清理上面安装过程中遇到的错误
sudo apt-get -f install

# 安装完成后将可执行文件复制到usr/bin中
sudo cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf

# 更改所有者为root用户
sudo chown root:root /usr/bin/wkhtmltopdf

# 并增加可执行属性
sudo chmod +x /usr/bin/wkhtmltopdf

# 安装中文字体
sudo apt-get install -y ttf-wqy-zenhei ttf-wqy-microhei

# 打印一个网页到当前目录，如果成功生成pdf则表明安装成功
wkhtmltopdf www.baidu.com baidu.pdf
```

### 6、安装nodejs、node-less

```bash
sudo apt-get install -y nodejs node-less npm
sudo npm install -g less-plugin-clean-css
```

### 7、配置Odoo的启动文件
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
sudo chown odoo:odoo /etc/odoo/odoo.conf
sudo chmod 640 /etc/odoo/odoo.conf
```

> 复制启动文件到/usr/bin/目录下，并尝试启动Odoo服务

```bash
sudo cp /home/odoo/odoo10/setup/odoo /usr/bin/odoo
sudo chown odoo: /usr/bin/odoo
sudo chmod 755 /usr/bin/odoo
# 由于一些权限的问题, 此处可能需要注意
cd /home/{root}/odoo10
python setup.py install
sudo su - odoo -s /bin/bash
/usr/bin/odoo -c /etc/odoo/odoo.conf
```

> 在浏览器输入http://ip:8069 检查

### 8、配置启动脚本
> 用Ubuntu自带的nano编辑器在/etc/init.d/目录下创建odoo启动脚本文件，然后把它改成可执行文件，赋给root用户。

```bash
sudo vim /etc/init.d/odoo
```
> 复制下面的内容到编辑器内

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

```bash
sudo mkdir /var/lib/odoo  #新建附件存储目录
sudo chown odoo: /var/lib/odoo  #修改所有者为odoo用户
sudo chmod 774 /var/lib/odoo  #修改为odoo用户读取和写入
sudo mkdir /var/log/odoo  #新建日志存储目录
sudo chown odoo:root /var/log/odoo  #修改所有者为odoo用户
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

### 9、将Odoo设为开机自启动 (可以不做)
> 让启动脚本随着Ubuntu服务器的开、关机而自动启动、关闭Odoo服务。

```bash
sudo update-rc.d odoo defaults
```

> 现在就可以重启你的服务器，当你再次登录服务器，Odoo应该已经在运行了。输入以下命令查看Odoo是否已在运行。

```bash
ps -ef|grep odoo
```

### 10、*用nginx代理odoo (可以不做)
```bash
sudo apt-get  install nginx
```
> 在/etc/nginx/sites-enabled 中增加一个可用的server

```
server{
    listen 80;
    server_name odoo12;
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://0.0.0.0:8069;
    }
} 
```

> 把 /etc/nginx/sites-enabled/default 里面80注释或者改成其他端口

---

---


# ps:

### 1. 报错: error: 'ascii' codec can't encode characters in position 18-20: ordinal not in range(128)
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

### 2. Rsync使用帮助

```bash
# rsync

# 带端口
rsync -avzP -e "ssh -p 58729" hesai@hesai-erp.chinacloudapp.cn:/tmp/aaa.sql ~/Desktop

# 不带端口
rsync -avzP -e  root@172.18.10.147:/var/log/app_server/app-server.log.6.gz /Users/chenpeng/

# 排除一些文件
rsync -avzP -e "ssh -p 29722" --exclude ".git,*.pyc,.DS_Store" hesai@40.73.113.181:~/odoo10 ~/Desktop/odoo10

rsync -avzP ~/Desktop/odoo安装必备/odoo10.zip hesai@10.0.100.33:~/
rsync -avzP ~/Desktop/odoo安装必备/wkhtmltopdf.zip hesai@10.0.100.33:~/

```

### 3. chown 更改目录的所有者

```bash
sudo chown -R user:user /home/ubuntu/DIR
```

###  4. 数据库操作指令

- 1. 备份

```
pg_dump --format=c db_name > dest_path
```

- 2. 恢复

```bash
# 在终端直接执行
dropdb DB_name
createdb -T template0 DB_name
pg_restore -d DB_name /Users/chenpeng/Desktop/xxx.dmp ## 还原二进制文件

# 在postgres环境里执行
# 还原文本文件 先进入相应数据库, 在用\i命令
psql DB_name
\i /Users/chenpeng/Desktop/xxx.dmp
```

- 3. 修改用户

```
alter database DB_name owner to user_name;
```

- 4. 执行sql脚本

```
psql -d DB_name -f /mnt/source/bak/xxx.sql
```

- 5. 将执行结果输出到文件

```
# 分三步
\o path
select * from users;
\o
```

### 5. pip 换源

- 修改 ~/.pip/pip.conf (没有就创建一个)

  > `http://mirrors.aliyun.com/pypi/simple/` 阿里云 <br/>
  > `https://pypi.mirrors.ustc.edu.cn/simple/` 中国科技大学 <br/>
  > `http://pypi.douban.com/simple/` 豆瓣(douban) <br/>
  > `https://pypi.tuna.tsinghua.edu.cn/simple/` 清华大学 <br/>
  > `http://pypi.mirrors.ustc.edu.cn/simple/` 中国科学技术大学 <br/>

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 6. ubuntu系统更换源

##### 1. 进入/etc/apt/

```bash
cd /etc/apt
```

##### 2. 备份sources.list文件

```bash
sudo cp sources.list sources.list.bak
```

##### 3. 修改sources.list文件

```bash
sudo vim sources.list
```

##### ***Ubuntu 14.04***

```
sudo vim /etc/apt/sources.list #修改
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

##### ***Ubuntu 16.04.3***

```
#aliyun
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
```

```
#tsinghua.edu
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse
```

```
#neu.edu
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial main restricted #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security multiverse
```

##### 4. 更新列表

```
sudo apt-get update
```