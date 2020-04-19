# ubuntu搭建内网穿透服务Ngrok

> 原文地址： https://cloud.tencent.com/developer/article/1048272

## 1. 安装git 和Golang

```bash
sudo apt-get install build-essential golang mercurial git
```

## 2. 获取 Ngrok 源码

> 此处使用非官方地址，修复了部分包无法获取

```
git clone https://github.com/tutumcloud/ngrok.git ngrok
```

## 3. 生成自签名证书

```bash
cd ngrok
NGROK_DOMAIN="ngrok.roger.city"
openssl genrsa -out base.key 2048
openssl req -new -x509 -nodes -key base.key -days 10000 -subj "/CN=$NGROK_DOMAIN" -out base.pem
openssl genrsa -out server.key 2048
openssl req -new -key server.key -subj "/CN=$NGROK_DOMAIN" -out server.csr
openssl x509 -req -in server.csr -CA base.pem -CAkey base.key -CAcreateserial -days 10000 -out server.crt
```

- 执行完后

```bash
ll

ubuntu@VM-0-9-ubuntu:~/ngrok$ ll
total 76
drwxrwxr-x  7 ubuntu ubuntu 4096 Mar 31 11:10 ./
drwxr-xr-x 10 ubuntu ubuntu 4096 Mar 31 11:09 ../
drwxrwxr-x  4 ubuntu ubuntu 4096 Mar 31 11:04 assets/
-rw-rw-r--  1 ubuntu ubuntu 1679 Mar 31 11:09 base.key
-rw-rw-r--  1 ubuntu ubuntu 1115 Mar 31 11:10 base.pem
-rw-rw-r--  1 ubuntu ubuntu   17 Mar 31 11:10 base.srl
drwxrwxr-x  2 ubuntu ubuntu 4096 Mar 31 11:04 contrib/
-rw-rw-r--  1 ubuntu ubuntu  199 Mar 31 11:04 CONTRIBUTORS
drwxrwxr-x  2 ubuntu ubuntu 4096 Mar 31 11:04 docs/
drwxrwxr-x  8 ubuntu ubuntu 4096 Mar 31 11:04 .git/
-rw-rw-r--  1 ubuntu ubuntu  150 Mar 31 11:04 .gitignore
-rw-rw-r--  1 ubuntu ubuntu  551 Mar 31 11:04 LICENSE
-rw-rw-r--  1 ubuntu ubuntu 1433 Mar 31 11:04 Makefile
-rw-rw-r--  1 ubuntu ubuntu 1904 Mar 31 11:04 README.md
-rw-rw-r--  1 ubuntu ubuntu  997 Mar 31 11:10 server.crt
-rw-rw-r--  1 ubuntu ubuntu  899 Mar 31 11:10 server.csr
-rw-rw-r--  1 ubuntu ubuntu 1675 Mar 31 11:10 server.key
drwxrwxr-x  3 ubuntu ubuntu 4096 Mar 31 11:04 src/
-rw-rw-r--  1 ubuntu ubuntu  156 Mar 31 11:04 .travis.yml
```

```bash
# 替换
cp base.pem assets/client/tls/ngrokroot.crt
```

## 4. 编译

> 这一步骤等待时间较长，成功编译后，会在bin目录下找到ngrokd和ngrok这两个文件。

```bash
sudo make release-server release-client
```

## 5. 启动服务端

> 前面生成的 ngrokd 就是服务端程序了，指定证书、域名和端口启动它（证书就是前面生成的，注意修改域名）

```bash
sudo ./bin/ngrokd -tlsKey=server.key -tlsCrt=server.crt -domain="ngrok.roger.city" -httpAddr=":8081" -httpsAddr=":8082"
```

> 到这一步，ngrok 服务已经跑起来了，可以通过屏幕上显示的日志查看更多信息。httpAddr、httpsAddr 分别是 ngrok 用来转发 http、https 服务的端口，可以随意指定。ngrokd 还会开一个 4443 端口用来跟客户端通讯（可通过 -tunnelAddr=”:xxx” 指定），如果你配置了 iptables 规则，需要放行这三个端口上的 TCP 协议。
>
> 
>
> 现在，通过 `http://ngrok.mdzz2333.cn:8081` 和  `http://ngrok.mdzz2333.cn:8082`就可以访问到 ngrok 提供的转发服务。为了使用方便，建议把域名泛解析到 VPS 上，这样能方便地使用不同子域转发不同的本地服务。
>
> 
>
> 访问后看到提示：
>
> ```
> Tunnel pub.imququ.com:8081 not found
> ```
>
> 这说明万事俱备，只差客户端来连了。

