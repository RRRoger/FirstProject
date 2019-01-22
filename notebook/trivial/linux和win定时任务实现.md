# linux和win定时任务实现

>  Author: Roger @2018-11-27 16:08:30

### 01.windows 定时执行步骤

> 这步骤和问题让人感觉很复杂

1. 搜索任务计划程序

2. 创建基本任务

3. 填写名称

4. 填写名称 "定时执行注册erp脚本"

5. 选择每天 下一步 下一步

6. 启动程序

7. C:\register2erp\pushERP.vbs

  - 用vbscript文件的目的是不让执行python脚本的时候弹框
  - 修改`pushERP.vbs`
  - 调用python的命令根据机器配置

8. 点完成

9. 然后点属性, 编辑时间间隔

10. 测试OK结束

### 02.ubuntu 开启定时任务(以下命令均用root用户执行)

> 相比于windows非常简单

1. 用root用户执行
```bash
vim /etc/crontab
```
2. 添加一行(参数配置见上面的描述)
```sh
*/1 * * * * hesai python PATH/register_erp.py "http://172.31.0.30:8069" "Demo-01" "Demo"
```
3. 重启cron
```bash
/etc/init.d/cron restart
```

