# -*- coding: utf-8 -*-

from ftplib import FTP
from urllib import quote


def ftpconnect(host, username, password, port=21):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    print(ftp.getwelcome)
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



def test_upload_file(folder, local_path, file_name):
    """
        @param: folder
        @param: file_path  文件路径
        @param: file_name  文件名
        下载路径参考: ftp://chenpeng:QWE123@192.168.11.151:21/众像售后需求解决方案的副本.docx
    """
    ftp_ip = "47.101.48.198"
    ftp_user = "FTP_20201210"
    ftp_pwd = "67K7t8VC"
    ftp_port = 21
    ftp_dir = folder

    download_url = 'ftp://%s:%s@%s:%s/%s/%s' % (quote(ftp_user), quote(ftp_pwd), ftp_ip, ftp_port, ftp_dir, file_name)
    ftp = ftpconnect(ftp_ip, ftp_user, ftp_pwd, ftp_port)
    remote_path = ftp_dir + '/' + file_name
    upload_file(ftp, remote_path, file_path)

    return download_url


if __name__ = '__main__':
    root = "/Send"
    
    local_path = "/Users/chenpeng/Desktop/禾赛ERP-JIT接口文档_V2.0.docx"
    file_name = "禾赛ERP-JIT接口文档_V2.0.docx"

    remote_path = test_upload_file("/Send", "/Users/chenpeng/Desktop/禾赛ERP-JIT接口文档_V2.0.docx", "禾赛ERP-JIT接口文档_V2.0.docx")

    print(remote_path)


