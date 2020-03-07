# [迁移]pg数据库迁移, 步骤

> postgresql数据库改变data目录 文档
> 例:把目录改变至/data中

## 0.准备工作停掉 pg server

```sh
service postgresql stop 
```

## 1.修改配置文件/etc/postgresql/9.3/main/postgresql.conf (记得备份)

```sh
data_directory = '/data/postgresql/9.3/main'
```

## 2.把默认数据目录的东西拷贝过来

```sh
cd /data
mkdir postgresql
cp -r /var/lib/postgresql/* /data/postgresql/
```

## 3.修改data_directory的所有者

> (记得 -R )

```sh
chown -R postgres:postgres /data
```

## 4.根据提示修改数据目录权限

```sh
chmod 700 /data
```
