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
    if not path.exists(archive_path):
        return False
    file_name = path.basename(archive_path)
    folder_name = file_name.replace('.tgz', '')
    remote_path = '/tmp/{}'.format(file_name)
    put(archive_path, remote_path)
    run('mkdir -p /data/web_static/releases/{}'.format(folder_name))
    run('tar -xzf {} -C /data/web_static/releases/{}'.format
            (remote_path, folder_name))
    run('rm {}'.format(remote_path))
    run('mv /data/web_static/releases/{}/web_static/* 
            /data/web_static/releases/{}/'.format
            (folder_name, folder_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format
            (folder_name))
    return True
