### 如何用好搜索引擎？

> 正确的使用搜索引擎，可以更高效的搜索到自己想要的内容。

> 以下是搜索引擎匹配规则以及适配的搜索引擎范围
>
> `G`: 适用于 Google:谷歌
>
> `B`: 适用于 Baidu:百度
>
> `M`: 适用于 Bing(MicroSoft):必应(微软)

| Command             | Description                | Scope |
| ------------------- | -------------------------- | ----- |
| "abc"               | 完全匹配搜索"abc"          | `GBM` |
| -abc                | 不包含"abc"                | `GM`  |
| a*c                 | "abc"也符合                | `GBM` |
| inurl:abc           | "abc"在url里               | `GB`  |
| allinurl:abc cdf    | 相当于inurl含多组关键词    | `G`   |
| inanchor:点击这里   | 点击这里在链接文字中出现   | `G`   |
| intitle:abc         | "abc"在标题中出现          | `GB`  |
| allintitle:abc cdf  | 相当于intitle含多组关键词  | `G`   |
| filetype:pdf python | 搜索特定文件格式`pdf`      | `GBM` |
| site:v2ex.com abc   | 指定网站v2ex.com下搜索     | `GBM` |
| related:taobao.com  | 搜索与taobao.com相关的网站 | `G`   |



**综上所述：**

- `Google` > `Baidu` > `Bing`

