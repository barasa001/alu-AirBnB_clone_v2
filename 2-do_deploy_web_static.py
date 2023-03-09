#!/usr/bin/python3
"""compress a folder"""
from datetime import datetime
from fabric.api import *
import os
import shlex

env.hosts = ['18.209.7.164', '54.211.25.155']
env.user = ['ubuntu']


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if archive_path is None or not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(archive_path))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(
            archive_path))
        run("rm /tmp/{}.tgz".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(archive_path))
        return True
    except BaseException:
        return False
