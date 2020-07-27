# 解决Can‘t locate revision identified by**

> https://blog.csdn.net/BigData_Mining/article/details/107125665

删除 migration 文件夹，并删除数据库中的`alembic_version`表中的数据

```bash
rm -rf migration
delete from alembic_version;
```

重新初始化（init, migrate, upgrade）即可，保留原来数据

