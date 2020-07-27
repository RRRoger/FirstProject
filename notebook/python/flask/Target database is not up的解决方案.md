# Target database is not up的解决方案

> https://www.shuzhiduo.com/A/VGzlPx0xzb/

#### 在flask中进行数据库迁移时报错，报错信息为"Target database is not up"，解决方案如下

- 找到alembic的最新版本号，找到文件夹migrate下的最新版本，文件名即为最新版本号（去掉末尾的_）
- 然后更新数据库表alembic_version里version_num的字段，将该字段的值改为最新版本号
- 再次迁移即可成功

还有一种方法（如果你的数据不重要的话）：***删除数据文件和migrate文件，重新初始化数据库。***

