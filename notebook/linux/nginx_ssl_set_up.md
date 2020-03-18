# Nginx 服务器证书安装

#### 申请免费证书：

- https://console.cloud.tencent.com/ssl

#### 详细教程链接： 

- https://cloud.tencent.com/document/product/400/35244

#### 注意事项：

- 下载下来的证书文件，有用的只有以下两个

  - 1_www.domain.com_bundle.crt
  - 2_www.domain.com.key

- ubuntu里nginx默认的配置目录是

  - `/etc/nginx/`

- 把下载的两个文件移动到配置文件目录下

- ```nginx
  server {
       # SSL 访问端口号为 443
       listen 443 ssl; 
       # 填写绑定证书的域名
       server_name www.domain.com; 
       # 证书文件名称
       ssl_certificate 1_www.domain.com_bundle.crt; 
       # 私钥文件名称
       ssl_certificate_key 2_www.domain.com.key; 
       ssl_session_timeout 5m;
       # 请按照以下协议配置
       ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
       # 请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
       ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
       ssl_prefer_server_ciphers on;
       location / {
           # 网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
           root /var/www/www.domain.com; 
           index  index.html index.htm;
       }
   }
  
  server {
      listen 80;
      # 填写绑定证书的域名
      server_name www.domain.com; 
      # 把http的域名请求转成https
      return 301 https://$host$request_uri; 
  }
  ```