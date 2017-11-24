# -*- coding: utf-8 -*-
import time
import tarfile
import os
from ftplib import FTP


def ftpconnect(host, username, password, port=21):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


# 从ftp下载文件
def download_file(ftp, remotepath, localpath, buffersize=1024):
    """
        @param: ftp 连接实例
        @param: remotepath 远程文件地址 ***** 是文件路径 不是目标存放目录的路径
        @param: localpath 本地临时文件地址
        @param: buffersize
    """
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, buffersize)
    ftp.set_debuglevel(0)
    fp.close()


# 从本地上传文件到ftp
def upload_file(ftp, remotepath, localpath, buffersize=1024):
    """
        @param: ftp 连接实例
        @param: remotepath 远程文件地址 ***** 是文件路径 不是目标存放目录的路径
        @param: localpath 本地临时文件地址
        @param: buffersize
    """
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, buffersize)
    ftp.set_debuglevel(0)
    fp.close()


def xx():
    with open('bx1.txt', 'w+') as input_file:
        for j in range(1, 7):
            input_str = '\t'.join([str(r) for r in range(1, 6)])
            input_file.writelines(input_str)
            input_file.write('\n')

# if __name__ == "__main__":
#     ftp = ftpconnect("113.105.139.xxx", "ftp***", "Guest***")
#     download_file(ftp, "Faint.mp4", "C:/Users/Administrator/Desktop/test.mp4")
#     # 调用本地播放器播放下载的视频
#     os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
#     upload_file(ftp, "C:/Users/Administrator/Desktop/test.mp4", "test.mp4")
#     ftp.quit()
