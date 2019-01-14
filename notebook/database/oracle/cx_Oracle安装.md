# cx_Oracle安装

### 1.下载两个文件

```sh
instantclient-basic-linux.x64-12.2.0.1.0.zip
instantclient-sdk-linux.x64-12.2.0.1.0.zip
instantclient-sqlplus-linux.x64-12.0.1.0.zip
```

### 2.将这三个文件放在同一目录下，并解压

```sh
//顺序
instantclient-basic-linux.x64-12.2.0.1.0.zip，
instantclient-sdk-linux.x64-12.2.0.1.0.zip，
instantclient-sqlplus-linux.x64-12.0.1.0.zip
```

### 3.设置环境变量.我修改的是root用户的文件，.profile

```sh
export ORACLE_HOME=/opt/oracle/instantclient_12_1
export DYLD_LIBRARY_PATH=$ORACLE_HOME
export LD_LIBRARY_PATH=$ORACLE_HOME
```

> 让环境变量生效

```sh
source /etc/profile
source $HOME/.bash_profile
```

### 4.我解压后的文件路径是/opt/oracle/instantclient_12_2/,cd到该路径下，执行
```sh
ln -s libclntsh.so.12.1 libclntsh.so
ln -s libclntsh.so.12.1 libclntsh.so
```

5.执行

```sh
pip install cx_Oracle
```

6.执行

```sh
pip install DBUtils
```
