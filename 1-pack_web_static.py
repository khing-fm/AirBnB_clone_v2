#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import env, local
from datetime import datetime


def do_pack():
    """generates archive from web static folder contents"""
    try:
        local("sudo mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}".format(now)
        local("sudo tar -czvf {}.tgz web_static/".format(path))
        return path
    except Exception:
        return None
