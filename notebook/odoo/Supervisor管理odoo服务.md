# Supervisor管理odoo服务

### 1.安装supervisor(python2.4+)
```sh
sudo easy_install supervisor

# 如果报错 sudo: easy_install: command not found，
# 请先使用下面命令安装python-setuptools
# sudo apt-get install python-setuptools
```
### 2.创建配置文件

> ##### 如果报权限问题, 直接 `echo_supervisord_conf` 把输出的文本复制到新建的`supervisord.conf`文件下

```
sudo mkdir -p /etc/supervisor/config.d
sudo touch /etc/supervisor/supervisord.conf
sudo echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

### 3.修改配置文件,最后两行

> ##### [include]前面的`;`也需要删掉

```
[include]
files = /etc/supervisor/config.d/*.ini
```

### 4.创建相关文件和目录

```
sudo mkdir /var/log/supervisor
sudo touch /var/log/supervisor/odoo.log
sudo touch /var/log/supervisor/odoo.error.log
```

### 5.创建进程管理文件(.ini)

```
sudo vim /etc/supervisor/config.d/odoo12.ini
```

> ##### 将下面的文本贴进去, command根据需要调整

- odoo

```bash
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

- odoo12

```bash
[program:odoo12]
command=/home/hesai/miniconda3/envs/py37/bin/python /home/odoo12/odoo12/odoo-bin -c /etc/odoo12.conf
stdout_logfile=/var/log/supervisor/odoo12.log
stderr_logfile=/var/log/supervisor/odoo12.error.log
user=odoo12
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
- 注意前面的`;`也要去掉

```
[inet_http_server]         ; inet (TCP) server disabled by default
port=0.0.0.0:9001          ; ip_address:port specifier, *:port for all iface
;username=user             ; default is no username (open server)
;password=123              ; default is no password (open server)
```
