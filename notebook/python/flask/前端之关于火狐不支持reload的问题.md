# 前端之 关于火狐不支持reload的问题

> https://blog.csdn.net/x_i_a_o_b_a_i/java/article/details/96609472

开发过程中遇到一个很奇怪的问题，火狐浏览器关闭iframe时关闭7,8次才能关闭上；但是其他浏览器这个功能是好的；

一顿分析和搜索后发现，我在关闭iframe之后（实际上是设置iframe的display为none），刷新了父页面，使用的方法是window.location.reload(); 而火狐由于他自己的缓存机制（没验证，看别的资料看来的）导致window.location.reload();不生效，还是把iframe刷出来了。

解决方式：将window.location.reload(); 改写成window.location.href = window.location.href; 然后就可以了。


