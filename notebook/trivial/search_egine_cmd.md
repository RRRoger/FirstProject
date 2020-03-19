# 搜索引擎常用指令

> 搜索引擎常用指令
>
> 以及适配的搜索引擎

| Command                     | Description                           | Scope |
| --------------------------- | ------------------------------------- | ---------------- |
| "abc"                       | 完全匹配搜索"abc"                     | `Google` `Baidu` `Bing` |
| -abc                        | 不包含"abc"                           | `Google` `Bing`  |
| a*c                         | "abc"也符合                           | `Google` `Baidu` `Bing` |
| inurl:abc                   | in url： "abc"在url里                 | `Google` `Baidu` |
| allinurl:abc cdf            | 相当于`inurl`含多组关键词             | `Google`         |
| inanchor:点击这里           | in anchor：点击这里在链接锚文字中出现 | `Google`         |
| intitle:abc                 | in title："abc"在标题中出现           | `Google` `Baidu` |
| allintitle:abc cdf          | 相当于`intitle`含多组关键词           | `Google`         |
| filetype:pdf python学习笔记 | 搜索特定文件格式`pdf`                 | `Google` `Baidu` `Bing` |
| site:v2ex.com python        | 指定网站`v2ex.com`下搜索`python`      | `Google` `Baidu` `Bing` |
| related:taobao.com          | 搜索与`taobao.com`相关的网站 | `Google` |



综上所述：

- `Google` > `Baidu` > `Bing`

