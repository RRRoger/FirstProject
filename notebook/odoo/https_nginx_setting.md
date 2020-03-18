# Nginx https odoo 配置

```nginx
upstream odoo {
    server IP:8069; # 反向代理端口
}

upstream odoochat {
    server IP:8072;
}

server{
    listen 80;
    server_name www.domain.com;

    add_header Strict-Transport-Security max-age=2592000;
    #把http的域名请求转成https
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl; 
    server_name www.domain.com; 

    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;

    # Add Headers for odoo proxy mode
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    # SSL parameters
    ssl on;
    ssl_certificate 1_www.domain.com_bundle.crt; 
    ssl_certificate_key 2_www.domain.com.key; 
    ssl_session_timeout 20m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
    ssl_prefer_server_ciphers on;

    # log
    access_log /var/log/nginx/odoo.access.log;
    error_log /var/log/nginx/odoo.error.log;

    # Redirect longpoll requests to odoo longpolling port
    location /longpolling {
        proxy_set_header Host $host;
        proxy_pass http://odoochat;
    }

    # Redirect requests to odoo backend server
    location / {
        proxy_redirect off;
        proxy_pass http://odoo;
    }

    location ^~ /[\/]+/static/ {
        proxy_cache_valid 200 60m;
        proxy_buffering    on;
        expires 864000;
        proxy_pass http://odoo;
    }



    gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
    gzip on;

 }
```

