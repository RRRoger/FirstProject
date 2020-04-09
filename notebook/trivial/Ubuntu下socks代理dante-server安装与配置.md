# Ubuntu下socks代理dante-server

## 1. 安装

```
sudo apt-get install dante-server
```

## 2. 配置

- 首先备份/etc/danted.conf

```bash
sudo mv /etc/danted.conf /etc/danted.conf.bak
```

- 然后将其内容替换为:

```
logoutput: /var/log/danted.log
internal: 0.0.0.0 port = 1080
# 这里external为代理服务器上访问外网的网卡的IP. ifconfig查看
external: 172.16.5.90
method: username none
user.privileged: proxy
user.notprivileged: nobody
user.libwrap: nobody
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: connect disconnect
}
pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0 port gt 1023
    command: bind
    log: connect disconnect
}
pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    command: connect udpassociate
    log: connect disconnect
}
block {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: connect error
}
```

## 3. 创建log目录

```bash
sudo mkdir /var/log/sockd
```

## 4. 启动

```bash
sudo /etc/init.d/danted start
```

## 5. 检测是否启动成功

```
netstat -lnp | grep 1080
```

## 6. 用户连接后查看连接情况

```
netstat -anp | grep 1080
```
