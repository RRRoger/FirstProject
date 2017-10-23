根据数据生成excel
1.数据形式必须是 [{},{}] json字符串
2.FULL_DIR 生成excel存放路劲
3.FIEL_NAME 生成excel内部sheet文件名
4.DATA_PATH json数据存放的文件名
5.HEADERS 表头信息, 
    — name 中文显示名称
    — alias json里面的key
    — seq 每个key在excel里面的排序
    — group 聚合函数: 
	— — sum 该key对应的数据求和
	— — avg 该key对应的数据求平均
6.可直接运行demo的数据演示