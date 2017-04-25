# -*- coding:utf-8 -*-

from fabric.api import *

path = __file__.rsplit('/', 1)[0] + '/config'
host_path = path + '/host.conf'
config_path = path + '/shadowsocks.json'


host = [i.split('#')[0] for i in [i.strip() for i in open(host_path, 'r').readlines()]]
password = [i.split('#')[1] for i in [i.strip() for i in open(host_path, 'r').readlines()]]

env.hosts = host
env.password = password


def centos_install():
    run("sudo yum update")
    run("sudo yum install python-setuptools && easy_install pip")
    run("sudo pip install shadowsocks")
    pass


def config():
    put(config_path, "/etc")
    run("sudo ssserver -c /etc/shadowsocks.json -d start")
    pass