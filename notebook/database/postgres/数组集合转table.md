# [unnest]数组集合转table

```sql
SELECT unnest(array[ '215', '216', '218']) product_code
```

```sql
SELECT p_code.product_code product_code,
       52 AS shop_id
FROM
  ( SELECT unnest(array[ '215', '216', '218']) product_code) p_code
```
