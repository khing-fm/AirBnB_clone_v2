#!/usr/bin/python3
"""script defines deploy funcrion that screates and distributes an
archive to your web servers"""
import os
from fabric.api import local, env, run, put
from datetime import datetime

env.user = "ubuntu"
env.hosts = ["3.229.113.226", "44.200.142.76"]


def do_pack():
    """generates archive from web static folder contents"""
    try:
        local("sudo mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(now)
        local("sudo tar -czvf {} web_static/".format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """Function that deploys archive to web_servers"""
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file = archive_path.split("/")[-1]
        archive_folder = "/data/web_static/releases/{}".\
            format(file.split(".")[0])
        run("sudo mkdir -p {}".format(archive_folder))
        run("sudo tar -xvzf /tmp/{} -C {}".format(file, archive_folder))
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {}/web_static/* {}/".
            format(archive_folder, archive_folder))
        run("sudo rm -rf {}/web_static/".format(archive_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(archive_folder))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
