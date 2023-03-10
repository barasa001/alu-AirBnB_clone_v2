#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""compress a folder"""
from datetime import datetime
from fabric.api import *
import os
import shlex

env.hosts = ['34.229.149.26', '54.224.98.80']


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if archive_path is None or not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        file_no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, file_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(
            file, path, file_no_ext))
        run("rm /tmp/{}".format(file))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, file_no_ext))
        run("rm -rf {}{}/web_static".format(path, file_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".
            format(path, file_no_ext))
        return True
    except:
        return False
