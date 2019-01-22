# 安装rabbitmq

### 1.官网下载rabbitmq-server-3.6.3

> 地址 http://www.rabbitmq.com/install-standalone-mac.html

### 2.解压

```sh
tar -zxvf rabbitmq-server-mac-standalone-3.6.6.tar.xz
```

### 3、添加主机名

```sh
vim /etc/hosts, 添加
127.0.0.1  你的主机名称
```

### 4、启动rabbitMQ。

```sh
cd rabbitmq_server-3.6.3/sbin， 
./rabbitmq-server
# 或者后台启动./rabbitmq-server -detached
```

### 5、开启 Web 界面管理。

#### 1.把插件复制到plugins里面

```
# 卸载 命令
./rabbitmq-plugins disable rabbitmq_delayed_message_exchange

# 安装 命令
./rabbitmq-plugins enable rabbitmq_delayed_message_exchange
./rabbitmq-plugins enable rabbitmq_management

# 之后可以通过http://localhost:15672来访问，默认账号密码guest/guest。
```

### 6、其他命令。

```
./rabbitmqctl stop
./rabbitmqctl status
```

## someQ:

```
sudo scutil --set HostName localhost   # 修改自己的主机名
sudo scutil --set ComputerName MacBookPro  # 修改共享名称
```

## 正常的安装方式:
#### 1. 安装：

```
brew install rabbitmq
brew uninstall rabbitmq
```

#### 2. 安装插件rabbitmq_delayed_message_exchange

> 从 https://www.rabbitmq.com/blog/2015/04/16/scheduling-messages-with-rabbitmq/ 下载 rabbitmq_delayed_message_exchange 插件
复制ez文件到 /usr/local/Cellar/rabbitmq/3.6.1/plugins/ 目录（3.6.1替换为实际的版本号）

> 执行下列脚本启用此plugin：

```
/usr/local/sbin/rabbitmq-plugins enable rabbitmq_delayed_message_exchange
./rabbitmq-plugins enable rabbitmq_delayed_message_exchange
```

#### 3. 启动

```
/usr/local/sbin/rabbitmq-server start &
```

#### 4. 登陆管理界面

> http://localhost:15672/
默认账号是 guest/guest

#### 5. 安装python依赖包
```
sudo pip install pika
```

> 其中会遇到一些问题，比如说更新homebrew
直接安装homebrew就好了，安装命令行：

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```
# 一些帮助的命令：
brew help 查看帮助命令的
brew update 用来更新homebrew的
ps -ef|grep rabb 查看进程的
kill －9 xxx 用来杀某条进程的
brew outdated 查看你的系统安装的系统的包的版本
```