#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import *
import os

env.hosts = ['18.209.7.164', '54.211.25.155']

def do_pack():
    """Packs the contents of web_static into a tar archive"""
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except:
        return None

def do_deploy(archive_path):
    """Deploys the web_static archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = os.path.basename(archive_path)
        dir_name = "/data/web_static/releases/" + file_name[:-4]
        run("mkdir -p {}".format(dir_name))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(dir_name, dir_name))
        run("rm -rf {}/web_static".format(dir_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_name))
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
