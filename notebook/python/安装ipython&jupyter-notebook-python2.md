# 安装 ipython & jupyter-notebook (python)


## 1.安装ipython
> 因为ipython对于python2 只支持到5.x

### 先输入下面命令, 找到最新的5.x版本

```bash
sudo pip install ipython==8888
```

### ipython (5.8.0)

```bash
sudo pip install ipython==5.8.0
```

## 2.安装jupyter

```bash
sudo pip install jupyter
```

> 等待安装成功

> jupyter notebook # 进入jupyter terminal 会有下面的log, 并用以下网址使用

```bash
➜  ~ jupyter-notebook
[TerminalIPythonApp] WARNING | Subcommand `ipython notebook` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter notebook` in the future
[I 10:46:46.865 NotebookApp] Serving notebooks from local directory: /Users/chenpeng
[I 10:46:46.866 NotebookApp] The Jupyter Notebook is running at:
[I 10:46:46.866 NotebookApp] http://localhost:8888/?token=9322dddf067380407a7cf3edb8fbd98f024cd970674c16e6
[I 10:46:46.866 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 10:46:46.867 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
http://localhost:8888/?token=9322dddf067380407a7cf3edb8fbd98f024cd970674c16e6
[I 10:46:47.061 NotebookApp] Accepting one-time-token-authenticated connection from ::1
```

## 3.服务器安装jupyter后可远程使用

### 1. 生成配置文件

```bash
jupyter notebook --generate-config
# vim ~/.jupyter/jupyter_notebook_config.py
```

> ps:
如果是 root 用户执行上面的命令，会发生一个问题：
jupyter notebook --generate-config --allow-config

### 2.设置密码 

jupyter notebook password # type twice

路径: ~/.jupyter/jupyter_notebook_config.json

### 3.复制密码
```bash
more ~/.jupyter/jupyter_notebook_config.json #
```

### 4.修改配置文件

```bash
vim ~/.jupyter/jupyter_notebook_config.py

# 修改配置, 请先 back up
c.NotebookApp.ip=‘*'
c.NotebookApp.password = u'sha:ce...刚才复制的那个密文’
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888  #可自行指定一个端口, 访问时使用该端口
```

### 5.启动 jupyter notebook 并使用

```bash
jupyter notebook
```

> 123 ; sha1:8d5df3123670:044e665e217abd4ec57ef67f78e5dc59e41433b8


## 后台启动并将日志写入指定文件

```
nohup jupyter notebook --allow-root > jnotebook.out 2>&1 &
```
