# -*- coding: utf-8 -*-

import paramiko

class SFTP(object):

    def __init__(self, host, username, password, port=22):
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self._t = None


    def _get_conn(self):
        conn = paramiko.Transport((self._host, self._port))
        conn.connect(username=self._username, password=self._password)
        return conn

    # 从sftp下载文件
    def download_file(self, remotepath, localpath):
        """
            @param: localpath 本地临时文件地址
            @param: remotepath 远程文件地址 ***** 是文件路径 不是目标存放目录的路径
        """
        conn = self._get_conn()
        _sftp = paramiko.SFTPClient.from_transport(conn)
        _sftp.get(remotepath, localpath)
        conn.close()


    # 从本地上传文件到sftp
    def upload_file(self, localpath, remotepath):
        """
            @param: localpath 本地临时文件地址
            @param: remotepath 远程文件地址 ***** 是文件路径 不是目标存放目录的路径
        """
        conn = self._get_conn()
        _sftp = paramiko.SFTPClient.from_transport(conn)
        _sftp.put(localpath, remotepath)
        conn.close()



def test_upload_file(folder, local_path, file_name):
    """
        @param: folder
        @param: local_path  文件路径
        @param: file_name  文件名
    """
    sftp_ip = "47.101.48.198"
    sftp_user = "FTP_20201210"
    sftp_pwd = "67K7t8VC"
    sftp_port = 22
    sftp_dir = folder

    remote_path = sftp_dir + '/' + file_name



    sftp = SFTP(sftp_ip, sftp_user, sftp_pwd, sftp_port)
    sftp.upload_file(local_path, remote_path)
    return remote_path


if __name__ == '__main__':
    root = "/Send"
    
    local_path = "/Users/chenpeng/Desktop/禾赛ERP-JIT接口文档_V2.0.docx"
    file_name = "禾赛ERP-JIT接口文档_V2.0.docx"

    remote_path = test_upload_file("/Send", "/Users/chenpeng/Desktop/角度文件调查.xlsx", "角度文件调查.xlsx")

    print(remote_path)


