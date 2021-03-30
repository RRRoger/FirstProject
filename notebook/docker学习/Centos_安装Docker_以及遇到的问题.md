# Centos 安装Docker 以及遇到的问题

> 参考链接1: https://www.jianshu.com/p/1f6b64d72e40
>
> 参考链接2: https://www.jianshu.com/p/b038f63fe929

## 一、卸载老版本

```bash
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

## 二、安装docker 基础包

```bash
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

## 三、设置稳定仓库

```bash
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm  
sudo yum install containerd.io-1.2.6-3.3.el7.x86_64.rpm #安装containerd.io
#再次重新安装docker
sudo yum install docker-ce docker-ce-cli containerd.io
```

## 四、启动与测试

```bash
sudo systemctl start docker  # 启动docker
sudo docker run hello-world  #测试

sudo systemctl enable docker # 设置开机自启
# Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.
```

## 五、启动docker服务远程允许访问

#### 1、编辑服务器上的docker.service文件

```bash
sudo vi /usr/lib/systemd/system/docker.service

# 大约 在 13行 原来的值 进行替换
# ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

# 替换为

ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock
```

#### 2、保存修改退出，重启docker

```bash
sudo systemctl daemon-reload

sudo service docker restart
```

#### 3、测试远程连接是否正常 输出下面的内容 如果出现以下内容则能正常连接：

```bash
curl http://localhost:2375/version

# 输出
{"Platform":{"Name":"Docker Engine - Community"},"Components":[{"Name":"Engine","Version":"20.10.5","Details":{"ApiVersion":"1.41","Arch":"amd64","BuildTime":"2021-03-02T20:15:27.000000000+00:00","Experimental":"false","GitCommit":"363e9a8","GoVersion":"go1.13.15","KernelVersion":"4.18.0-240.15.1.el8_3.x86_64","MinAPIVersion":"1.12","Os":"linux"}},{"Name":"containerd","Version":"1.4.4","Details":{"GitCommit":"05f951a3781f4f2c1911b05e61c160e9c30eaa8e"}},{"Name":"runc","Version":"1.0.0-rc93","Details":{"GitCommit":"12644e614e25b05da6fd08a38ffa0cfe1903fdec"}},{"Name":"docker-init","Version":"0.19.0","Details":{"GitCommit":"de40ad0"}}],"Version":"20.10.5","ApiVersion":"1.41","MinAPIVersion":"1.12","GitCommit":"363e9a8","GoVersion":"go1.13.15","Os":"linux","Arch":"amd64","KernelVersion":"4.18.0-240.15.1.el8_3.x86_64","BuildTime":"2021-03-02T20:15:27.000000000+00:00"}
```

#### 4、开放端口

> 需要将2375端口进行开放才能被远程连接，
>
> 如果是阿里云主机的话，可以直接登录阿里云去进行开放
>
> 如果是虚拟机的话，可以用以下命令进行开放：

```bash
firewall-cmd --zone=public --add-port=2375/tcp --permanent
```

#### ...

## 问题一、problem with installed package podman...

> Problem 1: problem with installed package podman-2.2.1-7.module_el8.3.0+699+d61d9c41.x86_64
>
> https://github.com/docker/containerd-packaging/issues/210#issuecomment-756773930

```bash
sudo yum remove runc
sudo yum install docker-ce docker-ce-cli containerd.io
```

