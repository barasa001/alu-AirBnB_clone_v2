#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generate a .tgz archive from the contents
    of the web_static folder."""
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(now)
    local('mkdir -p versions')
    result = local('tar -cvzf {} web_static'.format(file_path))
    if result.failed:
        return None
    return file_path
