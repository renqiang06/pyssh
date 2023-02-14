# -*- coding: utf-8 -*-
__author__ = 'Ren Qiang'
# %% SSH

import paramiko
import json


class Getinfo:
    # 获取用户名、密码
    def getIDPW(filename):
        with open(filename) as f:
            dictinfo = json.load(f)
        return dictinfo


class SSHConnection:
    # 初始化连接创建Transport通道
    def __init__(self, host='127.0.0.1', port=22, user='root', pwd='root'):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.__transport = paramiko.Transport((self.host, self.port))
        self.__transport.connect(username=self.user, password=self.pwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.__transport)

    # 关闭通道
    def close(self):
        self.sftp.close()
        self.__transport.close()

    # 上传文件到远程主机
    def upload(self, local_path, remote_path):
        self.sftp.put(local_path, remote_path)

    # 从远程主机下载文件到本地
    def download(self, local_path, remote_path):
        self.sftp.get(remote_path, local_path)

    # 在远程主机上创建目录
    def mkdir(self, target_path, mode='0777'):
        self.sftp.mkdir(target_path, int(mode))

    # 删除远程主机上的目录
    def rmdir(self, target_path):
        self.sftp.rmdir(target_path)

    # 查看目录下文件以及子目录（如果需要更加细粒度的文件信息建议使用listdir_attr）
    def listdir(self, target_path):
        return self.sftp.listdir(target_path)

    # 删除文件
    def remove(self, target_path):
        self.sftp.remove(target_path)

    # 查看目录下文件以及子目录的详细信息（包含内容和参考os.stat返回一个FSTPAttributes对象，对象的具体属性请用__dict__查看）
    def listdirattr(self, target_path):
        try:
            _list = self.sftp.listdir_attr(target_path)
        except BaseException as e:
            print(e)
            _list = []
        return _list

    # 获取文件详情
    def stat(self, remote_path):
        return self.sftp.stat(remote_path)

    # SSHClient输入命令远程操作主机
    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh._transport = self.__transport
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        print(result)
        return result


if __name__ == '__main__':
    info = Getinfo.getIDPW(filename='config.json')
    sc2ec2kk = SSHConnection(
        host=info['host'], port=info['port'], user=info['user'], pwd=info['pw'])
    #
    # termux-battery-status
    battinfo = sc2ec2kk.cmd("termux-battery-status")
    batjson = json.loads(battinfo)
    pass
    sc2ec2kk.close()

# %%
