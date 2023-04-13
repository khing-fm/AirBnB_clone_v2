#!/usr/bin/python3
"""fabric script that deletes out-of-date archives,
using the function do_clean"""
from fabric.api import local, env, run, put
from datetime import datetime

env.hosts = ['3.229.113.226', '44.200.142.76']
env.user = "ubuntu"


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
