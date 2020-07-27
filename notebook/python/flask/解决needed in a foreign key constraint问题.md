# 解决`needed in a foreign key constraint`问题

> 字面意思是，mysql不能drop掉索引 ‘primary’，在外键约束上被需要。就是说，主键上是有名为`primary`的索引的，并且关联了外键，这个时候是无法对这个被参照的对象进行修改(删除)的。

## 需要先删除外键

- 查看数据表`keyMap`的外键信息

```sql
show create table keyMap;

/*
  CONSTRAINT `keymap_ibfk_1` FOREIGN KEY (`modelName`) REFERENCES `model` (`modelName`),
  CONSTRAINT `keymap_ibfk_2` FOREIGN KEY (`customName`) REFERENCES `custom` (`customName`)
*/

```

- 删除相关的外键

```sql
alter table keyMap drop foreign key keymap_ibfk_1;
alter table keyMap drop foreign key keymap_ibfk_2;
```

