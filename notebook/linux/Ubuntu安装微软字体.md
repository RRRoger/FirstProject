> # *此操作需要reboot服务器*

## 1.获得字体包 (copy from windows, 后缀是*.ttv || *.ttf)

## 2.创建目录 将字体文件copy到下面的路径

```sh

sudo mkdir /usr/share/fonts/truetype/windows-font

```

## 3.拷贝字体到wiondow-font目录下

```sh

sudo cp ./*.ttf /usr/share/fonts/truetype/windows-font
sudo cp ./*.ttc /usr/share/fonts/truetype/windows-font

```

## 4.修改权限，并更新字体缓存

```sh

sudo chmod -R 777  /usr/share/fonts/truetype/windows-font
cd /usr/share/fonts/truetype/windows-font
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv

```

## 5.修改权限，并更新字体缓存

```sh

sudo chmod -R 777  /usr/share/fonts/truetype/windows-font
cd /usr/share/fonts/truetype/windows-font
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv

```

> if mkfontscale: command not found; then 

```sh
sudo apt-get install ttf-mscorefonts-installer
```


# 6.重启下系统吧！

```sh

sudo reboot

```

