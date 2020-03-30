# Ubuntu源码安装Odoo12社区版

### 1、* (*pass 这步可以不做*) 更新Ubuntu服务器软件源
```bash
# 更新软件源
sudo apt-get update  

# 更新软件包，自动查找依赖关系
sudo apt-get dist-upgrade -y
```

### 2、新建系统用户用于运行Odoo12程序
```bash
# 查看是否已经存在odoo12用户
cat /etc/passwd

# 新建系统用户odoo12，指定home目录为/home/odoo12
sudo adduser --system --home=/home/odoo12 --group odoo12
```

> 系统用户不能用于登录并且没有shell，但当需要以它的身份进行特定操作时，可以用su命令切换用户

```bash
# odoo那一行改成如下;可以用 sudo su odoo12 进入odoo12用户
# 修改odoo那一行 /home/odoo12:/bin/bash
sudo vim /etc/passwd

sudo su odoo12 # 测试一下是否成功
exit # 退出
```

### 3、安装 Git ， Pip ， Node.js 和构建Odoo依赖项所需的工具

```bash
sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less
```

### 4、下载最新版Odoo12源码

<div style="color:red">
    <ui>
        <li>由于源码下载龟速, 请直接用根目录的"odoo10.zip"压缩包解压</li>
    </ui>
</div>

```bash
sudo apt-get install -y git
sudo su odoo12
git clone https://www.github.com/odoo/odoo --depth 1 --branch 12.0 /home/odoo12/odoo
mv odoo odoo12
exit
sudo chown -R odoo12:odoo12 /home/odoo12/odoo12
sudo chmod -R 774 /home/odoo12/odoo12
```

### 5、安装和配置数据库服务器PostgreSQL
> 数据库默认用户名：postgres，没有密码

```bash
# 安装PostgreSQL
sudo apt-get install -y postgresql

# 创建数据库用户odoo12，输入两次密码odoo12
sudo -u postgres createuser --createdb --no-createrole --no-superuser --pwprompt odoo12
```

### 6、安装Wkhtmltopdf

<div style="color:red">
    <ui>
        <li>由于源码下载龟速, 请直接用根目录的"wkhtmltopdf.zip"压缩包解压</li>
    </ui>
</div>

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

### 7、安装和配置Odoo

```bash
#更改为用户“odoo12”
sudo su - odoo12

#进入home目录
cd

# 为Odoo 12安装创建一个新的Python虚拟环境
python3 -m venv odoo-venv

# 激活环境
source odoo-venv/bin/activate
```

<div style="color:red">
    <ui>
        <li>-------------pip换源步骤开始-------------</li>
        <li>-------------pip原默认是国外的，建议更换到国内的-------------</li>
    </ui>
</div>


> `http://mirrors.aliyun.com/pypi/simple` 阿里云 <br/>
> `https://pypi.mirrors.ustc.edu.cn/simple` 中国科技大学 <br/>
> `http://pypi.douban.com/simple` 豆瓣(douban) <br/>
> `https://pypi.tuna.tsinghua.edu.cn/simple` 清华大学 <br/>
> `http://pypi.mirrors.ustc.edu.cn/simple` 中国科学技术大学 <br/>

```bash
# 创建编辑配置文件
mkdir ~/.pip
vim ~/.pip/pip.conf
```

- 输入以下文本保存退出

```bash
[global]
index-url = http://mirrors.aliyun.com/pypi/simple
```

<div style="color:red">
  <ui>
    <li>-------------pip换源步骤结束-------------</li>
    <li>-------------END-------------</li>
  </ui>
</div>


- 进入虚拟环境后(可能需要换源pip换源)

```bash
pip3 install wheel
pip3 install -r odoo12/requirements.txt
```

​    ***如果在安装过程中遇到任何编译错误，请确保安装了“开始之前”节中列出的所有必需依赖项。***

- 使用以下命令停用环境

```bash
deactivate
```

- 为自定义插件创建新目录

```
mkdir /home/odoo12/odoo-custom-addons
```

- 切换回您的sudo用户

```bash
exit
```

- 编辑配置文件

`sudo vim /etc/odoo12.conf`

- 粘贴以下内容

```bash
[options]
; This is the password that allows database operations:
admin_passwd = my_admin_passwd
db_host = False
db_port = False
db_user = odoo12
db_password = odoo12
addons_path = /home/odoo12/odoo12/addons,/home/odoo12/odoo12/odoo/addons,/home/odoo12/odoo-custom-addons
data_dir = /var/lib/odoo12
log_level = info
logfile = /var/log/odoo12/odoo12-server.log
logrotate = True
;xmlrpc_port = 8069
;db_filter = ^vivi$
```

- 创建log目录

```bash
sudo mkdir /var/log/odoo12
sudo chown -R odoo12:odoo12 /var/log/odoo12
```

- 创建odoo12的静态目录

```bash
sudo mkdir /var/lib/odoo12
sudo chown -R odoo12:odoo12 /var/lib/odoo12
```


- 保存退出, 修改权限

```bash
sudo chmod 774 /etc/odoo12.conf
```

  

### 8、创建systemd服务文件

- 创建文件

```bash
sudo cp /etc/systemd/system/odoo12.service /etc/systemd/system/odoo12.service.bak
sudo vim /etc/systemd/system/odoo12.service
```
- 创建文件

```bash
[Unit]
Description=Odoo12
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo12
PermissionsStartOnly=true
User=odoo12
Group=odoo12
ExecStart=/home/odoo12/odoo-venv/bin/python3 /home/odoo12/odoo12/odoo-bin -c /etc/odoo12.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
```

- 执行

```bash
sudo systemctl daemon-reload
sudo systemctl start odoo12
```

- 运行

```bash
sudo systemctl status odoo12
```

- ***部分命令***

```bash
# 启用Odoo
sudo systemctl enable odoo12

# 查看Odoo服务记录
sudo journalctl -u odoo12

# 启动服务
sudo systemctl start odoo12

# 重启服务
sudo systemctl daemon-reload
sudo systemctl restart odoo12

# 停止服务
sudo systemctl stop odoo12
```

### 9、添加自动备份数据库

#### 1. 添加脚本

```
mkdir ~/db-backups
chmod 777 ~/db-backups
sudo su postgres
cd
vim pgbackup.sh
```

 - 粘贴以下文本

```bash
#!/bin/bash
db_name="hesai_portal"
file_name="/home/hesai/db-backups/"

pg_dump --format=c $db_name -U postgres > "$file_name$db_name-`date '+%y%m%d%H%M'`.dump"
```

  - 修改文件权限

```
chmod 744 pgbackup.sh
exit
```

#### 2. 创建定时任务

```
sudo vim /etc/crontab
```

- 在最后一行添加(每周执行一次)

```bash
0 0 * * 0 postgres /var/lib/postgresql/pgbackup.sh
```

- [crontab执行时间计算- 在线工具](https://tool.lu/crontab/)

| name       | code        |
| ---------- | ----------- |
| 每5min执行 | */5 * * * * |
| 每小时执行 | 0 * * * *   |
| 每天执行   | 0 0 * * *   |
| 每周执行   | 0 0 * * 0   |
| 每月执行   | 0 0 1 * *   |
| 每年执行   | 0 0 1 1 *   |
