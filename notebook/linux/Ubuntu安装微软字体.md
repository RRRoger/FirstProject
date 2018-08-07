# Ubuntu安装微软字体

### 1.获得字体包 (copy from windows, 后缀是 *.ttc || *.ttf)

### 2.创建目录 将字体文件copy到下面的路径

```sh
sudo mkdir /usr/share/fonts/truetype/windows-font
```

### 3.拷贝字体到wiondow-font目录下

```sh
sudo cp ./*.ttf /usr/share/fonts/truetype/windows-font
sudo cp ./*.ttc /usr/share/fonts/truetype/windows-font

```

### 4.修改权限，并更新字体缓存

```sh
sudo chmod -R 777  /usr/share/fonts/truetype/windows-font
cd /usr/share/fonts/truetype/windows-font
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```

### 5.修改权限，并更新字体缓存

```sh
sudo chmod -R 777  /usr/share/fonts/truetype/windows-font
cd /usr/share/fonts/truetype/windows-font
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```


```sh
# 如果出现 mkfontscale: command not found 错, 则执行以下命令, 否则跳过
sudo apt-get install ttf-mscorefonts-installer
```


### 6.重启下系统吧！(maybe不reboot也是可以的, 这一步可以先pass)

```sh
sudo reboot
```
### 7.pdf使用字体说明, css设置 font-family

```css
/*
   simsun: 宋体;
   Microsoft YaHei: 微软雅黑;
*/
.clazz {
    font-family:simsun;
}
```

