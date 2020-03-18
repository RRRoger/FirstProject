# ubuntu/MacOS 换源信息整合

## 0x01 brew换源

### 1、替换默认源

> https://mirrors.ustc.edu.cn/brew.git 中科大 <br/>
> https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git 清华大学

```bash
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
```

### 2、替换homebrew-core.git

> https://mirrors.ustc.edu.cn/homebrew-core.git 中科大 <br/>
> https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git 清华大学

```bash
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
```

### 3、替换homebrew-bottles:

> https://mirrors.ustc.edu.cn/homebrew-bottles 中科大 <br/>
> https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles 清华大学

```bash
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile
```

### 4、应用生效:

```bash
brew update
```

## 0x02 pip换源

### 1、修改 ~/.pip/pip.conf 

> (没有就创建一个)

> `http://mirrors.aliyun.com/pypi/simple/` 阿里云 <br/>
> `https://pypi.mirrors.ustc.edu.cn/simple/` 中国科技大学 <br/>
> `http://pypi.douban.com/simple/` 豆瓣(douban) <br/>
> `https://pypi.tuna.tsinghua.edu.cn/simple/` 清华大学 <br/>
> `http://pypi.mirrors.ustc.edu.cn/simple/` 中国科学技术大学 <br/>


```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2、 windows下设置

> 直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## 0x03 docker

> `https://registry.docker-cn.com` Docker中国官方 <br/>
> `http://hub-mirror.c.163.com` 网易 <br/>
> `https://docker.mirrors.ustc.edu.cn` 中国科技大学 <br/>
> `https://pee6w651.mirror.aliyuncs.com` 阿里云 <br/>

### 1、mac 如图

![](https://ae01.alicdn.com/kf/HTB1SbrYaN_rK1RkHFqDq6yJAFXa1.jpg)

### 2、Ubuntu

#### 1）修改daemon.json

> 在/etc/docker/目录下新建daemon.json文件，如果有就修改

```bash
sudo vim /etc/docker/daemon.json
```

```json
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

#### 2）重启docker

```bash
sudo service docker restart
```

## 0x04 ubuntu系统更换源

### 1、进入/etc/apt/

```bash
cd /etc/apt
```

### 2、备份sources.list文件

```bash
sudo cp sources.list sources.list.bak
```

### 3、修改sources.list文件

```bash
sudo vim sources.list
```

***Ubuntu 14.04***

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

***Ubuntu 16.04.3***

```
#aliyun
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
```

```
#tsinghua.edu
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse
```

```
#neu.edu
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial main restricted #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security multiverse
```

### 4、更新列表

```
sudo apt-get update
```

## 0x05 npm 换源

### Way1

```bash
# 淘宝镜像: `http://registry.npm.taobao.org/`

npm config set registry https://registry.npm.taobao.org
# 配置后可通过下面方式来验证是否成功

npm config get registry
# 或npm info express
```

### Way2: 通过cnpm

```bash
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install -g electron
# 等待安装完成，成功后使用electron -v查看electron版本
```

### Way3: 编辑 ~/.npmrc

```bash
vim ~/.npmrc
```

- 添加如下配置

```
registry=https://registry.npm.taobao.org
sass_binary_site=https://npm.taobao.org/mirrors/node-sass/
phantomjs_cdnurl=http://npm.taobao.org/mirrors/phantomjs
electron_mirror=http://npm.taobao.org/mirrors/electron/
```

## 0x06 Miniconda3及pip换源

> **清华源地址：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/**

### 添加命令

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

### 删除命令

```bash
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```