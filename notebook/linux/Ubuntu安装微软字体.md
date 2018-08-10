# Ubuntu安装微软字体

### 1.获得字体包 (copy from windows, 后缀是 *.ttc || *.ttf || *.otf)
> windows 字体是 *.ttc  *.ttf

> mac 字体是 *.otf

### 2.创建目录 将字体文件copy到下面的路径

```sh
sudo mkdir /usr/share/fonts/truetype/windows-font
```

### 3.拷贝字体到wiondow-font目录下

```sh
sudo cp ./* /usr/share/fonts/truetype/windows-font

```

### 4.修改权限，并更新字体缓存

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


### 5.重启下系统吧！(maybe不reboot也是可以的, 这一步可以先pass)

```sh
sudo reboot
```
### 6.pdf使用字体说明, css设置 font-family

```css
/*
   宋体: simsun;
   微软雅黑: Microsoft YaHei;
   新細明體：PMingLiU 
   細明體：MingLiU 
   標楷體：DFKai-SB 
   黑体：SimHei 
   宋体：SimSun 
   新宋体：NSimSun 
   仿宋：FangSong 
   楷体：KaiTi 
   仿宋_GB2312：FangSong_GB2312 
   楷体_GB2312：KaiTi_GB2312 
   微軟正黑體：Microsoft JhengHei 
   微软雅黑体：Microsoft YaHei 
*/

.clazz {
    font-family:simsun;
}
```

### 7.查看已经安装的中文字体

```sh
    # 查看所有安装的中文字体
    fc-list :lang=zh
```

```
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Heavy,思源黑体 CN Heavy:style=Heavy,Bold
.苹方-繁,.蘋方-繁,.PingFang TC:style=细体,細體,Light
.苹方-港,.蘋方-港,.PingFang HK:style=细体,細體,Light
.苹方-简,.蘋方-簡,.PingFang SC:style=细体,細體,Light
Microsoft JhengHei,微軟正黑體,微軟正黑體 Light,Microsoft JhengHei Light:style=Light,Regular
文泉驿微米黑,文泉驛微米黑,WenQuanYi Micro Hei:style=Regular
Microsoft JhengHei UI:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
Microsoft JhengHei,微軟正黑體:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
微软雅黑,Microsoft YaHei,Microsoft YaHei Light,微软雅黑 Light:style=Light,Regular
文泉驿正黑,文泉驛正黑,WenQuanYi Zen Hei:style=Regular
文泉驿点阵正黑,文泉驛點陣正黑,WenQuanYi Zen Hei Sharp:style=Regular
楷体,KaiTi:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
宋体,SimSun:style=常规,Regular
.苹方-港,.蘋方-港,.PingFang HK:style=纤细体,纖細體,Thin
.苹方-简,.蘋方-簡,.PingFang SC:style=纤细体,纖細體,Thin
等线,DengXian:style=Regular
.苹方-繁,.蘋方-繁,.PingFang TC:style=纤细体,纖細體,Thin
Microsoft YaHei UI,Microsoft YaHei UI Light:style=Light,Regular
Microsoft YaHei UI:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
苹方-繁,蘋方-繁,PingFang TC:style=中粗体,中粗體,Semibold
苹方-简,蘋方-簡,PingFang SC:style=中粗体,中粗體,Semibold
苹方-港,蘋方-港,PingFang HK:style=中粗体,中粗體,Semibold
思源黑体 CN,Source Han Sans CN,Source Han Sans CN ExtraLight,思源黑体 CN ExtraLight:style=ExtraLight,Regular
苹方-简,蘋方-簡,PingFang SC:style=常规体,標準體,Regular
苹方-港,蘋方-港,PingFang HK:style=常规体,標準體,Regular
苹方-简,蘋方-簡,PingFang SC:style=极细体,極細體,Ultralight
苹方-港,蘋方-港,PingFang HK:style=极细体,極細體,Ultralight
Microsoft JhengHei UI,Microsoft JhengHei UI Light:style=Light,Regular
苹方-繁,蘋方-繁,PingFang TC:style=常规体,標準體,Regular
苹方-繁,蘋方-繁,PingFang TC:style=极细体,極細體,Ultralight
微软雅黑,Microsoft YaHei:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
仿宋,FangSong:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Regular,思源黑体 CN Regular:style=Regular
微软雅黑,Microsoft YaHei:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
.苹方-繁,.蘋方-繁,.PingFang TC:style=中黑体,中黑體,Medium
苹方-繁,蘋方-繁,PingFang TC:style=细体,細體,Light
等线,DengXian,DengXian Light,等线 Light:style=Light,Regular
.苹方-简,.蘋方-簡,.PingFang SC:style=中黑体,中黑體,Medium
.苹方-港,.蘋方-港,.PingFang HK:style=中黑体,中黑體,Medium
苹方-港,蘋方-港,PingFang HK:style=细体,細體,Light
苹方-简,蘋方-簡,PingFang SC:style=细体,細體,Light
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Medium,思源黑体 CN Medium:style=Medium,Regular
.苹方-繁,.蘋方-繁,.PingFang TC:style=中粗体,中粗體,Semibold
.苹方-简,.蘋方-簡,.PingFang SC:style=中粗体,中粗體,Semibold
.苹方-港,.蘋方-港,.PingFang HK:style=中粗体,中粗體,Semibold
文泉驿等宽正黑,文泉驛等寬正黑,WenQuanYi Zen Hei Mono:style=Regular
文泉驿等宽微米黑,文泉驛等寬微米黑,WenQuanYi Micro Hei Mono:style=Regular
苹方-繁,蘋方-繁,PingFang TC:style=中黑体,中黑體,Medium
等线,DengXian:style=Bold
苹方-简,蘋方-簡,PingFang SC:style=中黑体,中黑體,Medium
苹方-港,蘋方-港,PingFang HK:style=中黑体,中黑體,Medium
Microsoft JhengHei UI:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
新宋体,NSimSun:style=常规,Regular
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Light,思源黑体 CN Light:style=Light,Regular
Microsoft JhengHei,微軟正黑體:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
.苹方-简,.蘋方-簡,.PingFang SC:style=常规体,標準體,Regular
.苹方-港,.蘋方-港,.PingFang HK:style=常规体,標準體,Regular
.苹方-繁,.蘋方-繁,.PingFang TC:style=常规体,標準體,Regular
.苹方-简,.蘋方-簡,.PingFang SC:style=极细体,極細體,Ultralight
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Bold,思源黑体 CN Bold:style=Bold
.苹方-港,.蘋方-港,.PingFang HK:style=极细体,極細體,Ultralight
.苹方-繁,.蘋方-繁,.PingFang TC:style=极细体,極細體,Ultralight
Microsoft YaHei UI:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
苹方-港,蘋方-港,PingFang HK:style=纤细体,纖細體,Thin
苹方-简,蘋方-簡,PingFang SC:style=纤细体,纖細體,Thin
苹方-繁,蘋方-繁,PingFang TC:style=纤细体,纖細體,Thin
思源黑体 CN,Source Han Sans CN,Source Han Sans CN Normal,思源黑体 CN Normal:style=Normal,Regular

```

