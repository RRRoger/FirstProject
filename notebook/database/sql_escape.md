# SQL语句转义字符

> ***写在前面： SQL语句中转义字符是单引号（`'`）***

> ##### 参考链接：
>
> - [How to Escape Single Quotes in SQL?](https://www.databasestar.com/sql-escape-single-quote/)
>   - https://www.databasestar.com/sql-escape-single-quote/
>
> - [SQL 的转义字符是：'（单引号）](https://blog.csdn.net/xuaner8786/article/details/79215339)
>   - https://blog.csdn.net/xuaner8786/article/details/79215339


## 1、先聊聊单引号双引号的作用

### 1）单引号

> 一般表示一个字符串

```sql
update company set name = 'Nike';
```

### 2）双引号

> 一般表示一个变量：如：表名，字段名等

```sql
update "company" set "name" = 'Nike';
```

- 双引号特殊场景


```sql
-- 在一些系统中“不得不”对某一字段命名成一个数字：如：123456

-- 错误写法
select 123456 from table1;

-- 正确写法
select "123456" from table1;
```

## 2、转义字符（`'`）的使用

> 首先定义一张表`公司`（`company`）；
>
> 仅有一个字段`名称`（`name`）

### 1) 添加一个叫“Nike”的公司。

```sql
insert into company (name) values ('Nike');
```

### 2) 添加一个叫“`O'Reilly`”的公司

- ***注意***： 此时名称中有单引号， 而在sql语句里单引号是`表示一个字符串`

- ***错误写法***

  - ```sql
    insert into company (name) values ('O'Reilly');
    ```

- ***正确写法***

  - ```sql
    -- 使用单引号进行转义
    insert into company (name) values ('O''Reilly');
    ```

### 3）练习：添加一个叫“`''''''`”的记录

- 这条记录的名称是6个单引号

- 每个单引号需要一个单引号转义，得到（12个单引号）：`''''''''''''`

- 最后还要用两个单引号表示字符串

- 所以最终的sql语句是（总计：14个单引号）

  - ```sql
    insert into company (name) values ('''''''''''''');
    ```



---

## ***需要转义的字符***

```bash
'
"
:
;
(
)
[
]
|
\
@
.............
```



## 其他写法

```sql
-- 使用字符串拼接的方式 CHR(39) 即单引号
insert into company (name) values ('O' || || CHR(39) || 'Reilly');
```

