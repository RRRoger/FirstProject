# Supervisor管理odoo服务

### 1.安装supervisor(python2.4+)
```sh
sudo easy_install supervisor
```
### 2.创建配置文件

```
sudo mkdir /etc/supervisor
sudo echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

### 3.修改配置文件,最后两行

```
[include]
files = /etc/supervisor/config.d/*.ini
```

### 4.创建相关文件和目录

```
sudo mkdir /var/log/supervisor
sudo touch /var/log/supervisor/odoo.log
sudo touch /var/log/supervisor/odoo.error.log
sudo mkdir /var/log/supervisor/config.d
```

### 5.创建进程管理文件(.ini)

```
sudo vim /var/log/supervisor/config.d/odoo.ini
```

- 将下面的文本贴进去, command可能需要调整

```
[program:odoo]
command=/usr/bin/odoo --config /etc/odoo/odoo.conf --logfile /var/log/odoo/odoo-server.log
stdout_logfile=/var/log/supervisor/odoo.log
stderr_logfile=/var/log/supervisor/odoo.error.log
user=odoo
autostart=true
autorestart=true
startsecs=5
priority=1
stopasgroup=true
killasgroup=true
```

### 6.启动supervisor服务

```
sudo supervisord -c /etc/supervisor/supervisord.conf
```

### 7.以上配置结束

- supervisor相关命令

```sh
sudo supervisorctl status  # 查看相关进程的状态
sudo supervisorctl stop odoo
sudo supervisorctl start odoo
sudo supervisorctl restart odoo
sudo supervisorctl reload # 当配supervisor.conf发生修改,需要执行此命令
sudo supervisorctl # 进入supervisorctl终端
tail -f /tmp/supervisord.log # supervisor日志
```

- 配置supervisor后台管理, 然后reload

```
[inet_http_server]         ; inet (TCP) server disabled by default
port=0.0.0.0:9001        ; ip_address:port specifier, *:port for all iface
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)
```
- 右击检查发现restart对应是一个url 那么我们可以用get请求去restart odoo的服务, 不用登录服务器, 直接在本地用命令就可以重启服务啦

```
wget "http://ip:9001/index.html?processname=odoo&action=restart"
```

- 此处可以参考下面链接, 双击执行脚本, 就可以很快捷的重启了
