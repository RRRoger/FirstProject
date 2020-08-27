# 1.脚本

## 1). 初始化

- 进入数据库

```bash
mysql -uroot -ppassword

mysql -h host db_name -uuser_name -ppassword
```

- 显示数据库

```bash
show databases;
```

- 使用数据库

```bash
use test_mysql_db;
```

- 创建数据库

```bash
CREATE DATABASE 数据库名 charset=utf8;
```

## 2). 查看命令

- 显示表数据

```bash
show tables; # 显示表
desc table_name; # 显示表结构
```

- 查看表索引

```sql
show index from TABLE_NAME;
show index from keyMap;
```

- 查看表所有结构

```
show create table keyMap;
```



## 3). 备份与还原

- 备份数据库

```bash
mysqldump -u USER -p PASSWORD --single-transaction --master-data=2 --flush-logs -B DATABASE_NAME > 123.sql
```

- 还原数据库

```bash
mysql -uroot -proot -Dtest_mysql_db < ~/Desktop/123.sql

mysql -uroot -phesai1588 -Droger_db < ~/Desktop/123.sql
```

## 4). DDL

- 创建表

```bash
CREATE TABLE table_name (column_name column_type);
```

## 5). SQL

