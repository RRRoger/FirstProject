###   1. docker 系统命令

```sh
# 查看docker版本
docker version

# 显示docker系统的信息
docker info

# 日志信息
docker logs
docker logs -n 10 <容器名orID> # 显示最后10行日志
docker logs -f <容器名orID> # 实时显示日志

# 故障检查
service docker status

# 启动关闭docker
sudo service docker start|stop
```

### 2. 查看容器信息

```sh
# 查看当前`运行`的容器
docker ps

# 查看`全部`容器 a = all
docker ps -a

# `只`查看全部容器的id和信息
docker ps -a -q

# 查看全部容器占用的空间 s - size
docker ps -as

# 查看一个正在运行容器进程，支持 ps 命令参数  ????
docker top

# 查看容器的示例id 大写的I
sudo docker inspect -f  '{{.Id}}' [id]

# 检查镜像或者容器的参数，默认返回 JSON 格式
docker inspect <容器名orID>

# 返回 ubuntu:14.04  镜像的 docker 版本
docker inspect --format '{{.DockerVersion}}' ubuntu:14.04
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ubuntu:14.04
```

### 3. 创建删除容器

```sh
# 创建一个容器命名为 test 使用镜像daocloud.io/library/ubuntu
docker create -it --name test daocloud.io/library/ubuntu

# 创建并启动一个容器 名为 test 使用镜像daocloud.io/library/ubuntu
docker run --name test daocloud.io/library/ubuntu

# 创建并且启动一个容器 名为 my_centos3 适用镜像 centos:latest
docker run -it --name my_centos3 -d centos:latest /bin/bash

# 删除一个容器
docker rm [容器id]

# 删除所有容器
docker rm `docker ps -a -q`

# 根据Dockerfile 构建
docker build -t [image_name] [Dockerfile_path]
```

### 4. 启动停止容器等操作

```sh
# 启动/停止/重启
docker start|stop|restart [id]

# 暂停|恢复 某一容器的所有进程
docker pause|unpause [id]

# 杀死一个或多个指定容器进程
docker kill -s KILL [id]

# 停止全部运行的容器
docker stop `docker ps -q`

# 杀掉全部运行的容器
docker kill -s KILL `docker ps -q`
```

### 5. 交互式进入容器

> - 只用 `-i` 参数: 执行但是无结果
> - 只用 `-t` 参数: 显示console, 但是无法执行命令
> - 使用 `-it` 参数: 可以进入console执行命令
> - 使用 `-d` 参数，在后台执行一个进程。如果一个命令需要长时间进程，会很快返回

```sh
sudo docker exec -it {{containerName or containerID}} bash
sudo docker exec -i {{containerName or containerID}} bash
sudo docker exec -t {{containerName or containerID}} bash
sudo docker exec -d {{containerName or containerID}} bash

docker exec -it my_centos /bin/bash
```

### 6. 容器于宿主拷贝文件

```sh
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

# 本地文件上传到对应容器的目录
docker cp local.sh [CONTAINERid]:[TagPath]

docker cp ~/test.txt my_centos:/root # 宿主机 -> 容器
docker cp my_centos:/root/test.txt ~ # 容器 -> 宿主机
```

### 7. 查看容器的root用户密码

```sh
docker logs <容器名orID> 2>&1 | grep '^User: ' | tail -n1
```

### 8. 容器同步命令

```sh
# 保存对容器的修改
docker commit

# 保存某个容器成为一个镜像
docker commit -a "user" -m "commit info" [CONTAINER] [imageName]:[imageTag]
docker commit -a "roger" -m "centos with miniconda3" my_centos centos_conda:miniconda3

# 把一个正在运行的容器保存为镜像
docker commit <CONTAIN-ID> <IMAGE-NAME>

# 推送一个容器到中心仓库
docker login --username=[userName] --password=[pwd] [registryURL]

## 建议登录后查看 docker info
docker tag [imageID] [remoteURL]:[imageTag]
docker push [remoteURL]:[imageTag]

# 拉取提交的容器
docker pull [remoteURL]:[imageTag]

# 对比容器的改动
docker diff

# 附加到一个运行的容器上
docker attach
```

### 9. 容器资源限制参数

```sh
# 限制内存最大使用
-m 1024m --memory-swap=1024m
# 限制容器使用CPU
--cpuset-cpus="0,1"
```