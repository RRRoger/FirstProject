# minio使用docker部署

> 参考链接: 
>
> - https://blog.csdn.net/u011831527/article/details/103254723
> - https://docs.min.io/docs/minio-client-complete-guide.html

## 1. docker 构建容器

> /Users/roger/minio/data 是宿主机目录与容器内data目录绑定

```bash
docker run -p 9000:9000 \
  --name minio1 \
  -v /Users/roger/minio/data:/data \
  -e "MINIO_ROOT_USER=AKIAIOSFODNN7EXAMPLE" \
  -e "MINIO_ROOT_PASSWORD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
  minio/minio server /data
```

## 2. 登录

| 用户名                       | 密码                                     |
| ---------------------------- | ---------------------------------------- |
| AKIAIOSFODNN7EXAMPLE         | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY |
| **后期可以通过`mc`命令添加** | **后期可以通过`mc`命令添加**             |

- 在浏览器界面创建`Bucket`: `test`

## 3. 安装minio client管理文件服务器

```bash
docker pull minio/mc
docker run -it --entrypoint=/bin/sh minio/mc
```

## 4. 关联minio-server

> 使用上面的账号密码
>

```bash
mc config host add minio http://172.18.132.220:9000 AKIAIOSFODNN7EXAMPLE wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY --api s3v4
# Added `minio` successfully.

mc admin info server minio
```

## 5. 查看之前创建的bucket和上传的文件

> test 就是你创建的`Bucket`

```bash
mc ls minio
mc ls minio/test
```

## 6. 设置外联永久下载

> test 就是你创建的`Bucket`

```bash
mc  policy  set  public minio/test
# Access permission for `minio/test` is set to `public`
mc  policy  set  download minio/test
Access permission for `minio/test` is set to `download`
```

## 7. 分配用户

```bash
mc admin user add minio/ newuser newuser123
# Added user `newuser` successfully.

mc admin group add minio newgroup newuser
# Added members {newuser} to group newgroup successfully.

mc admin group info minio newgroup
# Group: newgroup
# Status: enabled
# Policy:
# Members: newuser

mc admin policy set minio readwrite group=newgroup
# Policy readwrite is set on group `newgroup`
```

### ***命令清单- 添加用户***

```bash
# 添加用户
mc admin user add minio/ newuser newuser123

# 禁用用户
mc admin user disable minio/ newuser

# 启用用户
mc admin user enable minio/ newuser

# 删除用户
mc admin user remove minio/ newuser

# 用户列表
mc admin user list --json minio/

# 某个用户详情
mc admin user info minio someuser
```

### ***命令清单- 创建用户组***

```bash
# 新建用户组
mc admin group add minio newgroup newuser

# 禁用用户组
mc admin group disable minio/ newgroup

# 启用用户组
mc admin group enable minio/ newgroup

# newuser从组中删除用户
mc admin group remove myminio newgroup newuser

# 删除用户组
mc admin group remove minio/ newgroup

# 用户组列表
mc admin group list --json minio/

# 用户组详情
mc admin group info minio newgroup
```

### ***命令清单- 赋予权限***

```bash
# 给某个用户赋予权限
mc admin policy set minio readwrite user=newuser

# 给某个用户组赋予权限
mc admin policy set minio readwrite group=newgroup
```

