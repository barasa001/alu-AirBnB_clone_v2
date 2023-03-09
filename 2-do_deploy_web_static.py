#!/usr/bin/python3
"""compress a folder"""
from datetime import datetime
from fabric.api import *
import os
import shlex

env.hosts = ['18.209.7.164', '54.211.25.155']
env.user = ['ubuntu']

def do_deploy(archive_path):
