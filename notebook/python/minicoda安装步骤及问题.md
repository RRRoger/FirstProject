# MiniCoda安装步骤及问题

> 众所周知，python是世界上最好的两门语言。
>
> conda用于python项目做多版本环境创建与切换的
>
> 有效的进行版本之间的隔离

## 1、下载安装文件

- `For Mac OS`
```bash
cd ~
wget https://repo.continuum.io/miniconda/miniconda3-latest-MacOSX-x86_64.sh
```

- `FOr Linux`
```bash
cd ~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

## 2、安装

- `For MacOSX`

```bash
cd ~
bash miniconda3-latest-MacOSX-x86_64.sh
# 根据提示完成安装
```

- `For Linux`

```bash
cd ~
bash Miniconda3-latest-Linux-x86_64.sh
# 根据提示完成安装
```

## 3、手动生效环境变量

```bash
source ~/.bash_profile
```

## 4、验证安装成功

```bash
conda -h

# 出现如下信息表示成功

usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

...
```

## 5、升级conda以及pip version

```bash
conda upgrade conda
pip install --upgrade pip
```

## 6、查看env list

```bash
conda-env list

# conda environments:
#
base                  *  /Users/chenpeng/miniconda3
```

## 7、创建虚拟环境

> 创建一个名叫pj_odoo12的py3.6环境

```bash
conda create -n pj_odoo12 python=3.6 -y
conda create -n py38 python=3.8 -y

```

- 创建完毕提示

```bash
# To activate this environment, use
#
#     $ conda activate pj_odoo12
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

- 虚拟环境地址

```bash
# environment location: /Users/chenpeng/miniconda3/envs/pj_odoo12

/Users/xxxx/miniconda3/envs/pj_odoo12
```

## 8、激活和退出虚拟环境

```bash
# 激活
conda activate py38

# 退出
conda deactivate
```

## 9、卸载`miniconda`

> - 去掉~/.bash_profile环境变量配置
> - 删除`miniconda`目录
> - 删除隐藏的配置文件

```bash
# 删除相关的环境变量配置  不是添加是删除哦!!!!!
# export PATH="/Users/chenpeng/miniconda3/bin:$PATH"

# 删除miniconda
rm -rf ~/miniconda3

# 删除相关隐藏文件
rm -rf ~/.condarc
rm -rf ~/.conda
rm -rf ~/.continuum
```

## 10、常用命令

### 查看当前存在哪些虚拟环境

```bash
# 标记*的代表当前所处的虚拟环境
conda env list
conda info -e
```

### 创建python虚拟环境

```bash
conda create -n your_env_name python=X.X（2.7、3.6等)
```

### 激活虚拟环境

```bash
conda activate your_env_name
```

### 虚拟环境中安装额外的包

```bash
conda install -n your_env_name [package]
```

### 关闭虚拟环境

```bash
conda deactivate
```

### 删除虚拟环境

```bash
conda remove -n your_env_name(虚拟环境名称) --all

# or

conda env remove -n ENV_NAME
```

### 删除环境中的某个包

```bash
conda remove --name your_env_name  package_name
```

## 11、换源

### 1、Miniconda3及pip换源

> **清华源地址：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/**

- 添加命令

```bash
# 清华大学
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

# 中科大
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

# 上海交大
conda config --add channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

- 删除命令

```bash
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/


conda config --remove channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/
conda config --remove channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge/

conda config --remove channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --remove channels https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/

```

- pip永久换源
- 修改或者添加**~/.pip/pip.conf**

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## 12、注意事项

### 1、解决pyenv 和 conda 冲突

- 切换至系统的py环境

```bash
pyenv global system
```

### 2、关闭虚拟环境问题

> `source deactivate`已经弃用
>
> 请使用`conda deactivate`

- 关闭遇到`No such file or directory`

```bash
DeprecationWarning: 'source deactivate' is deprecated. Use 'conda deactivate'.
```

