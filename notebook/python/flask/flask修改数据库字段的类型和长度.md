# flask修改数据库字段的类型和长度

> https://www.coder.work/article/2618329
>
> https://blog.csdn.net/weixin_30627381/article/details/101912802

 在将models中的字段的db.String(256)修改为db.String(1024)后，执行migrate和upgrade操作后，发现数据库并没有更新，网上查阅资料后，解决方法如下：

- 打开env.py文件（文件路径为：migrations/env.py）

- 找到run_migrations_online函数下的context.configure,在括号中添加两行配置项

   compare_type=True,

   compare_server_default=True

- 添加完成后再次迁移即可成功

