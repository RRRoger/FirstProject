# 提取视频音频


> 此脚本用户提取抖音视频中的音频, 并支持视频剪辑

## 1.安装需要用到的库


```sh
# sudo apt-get install libav-tools # ubuntu
brew install libav # macos
sudo pip install pydub # 安装需要的py库
```

## 2.安装工具 ffmpeg 
> ### [ffmpeg用法](https://www.jianshu.com/p/7ed3be01228b)

```sh
brew install ffmpeg # macos
ffmpeg -i source_path dest_path
```

## 3.脚本
> ### [cut_music.py](cut_music.py)

