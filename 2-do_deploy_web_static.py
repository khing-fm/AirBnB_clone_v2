#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import local, env, run, put
import os

env.user = "ubuntu"
env.hosts = ["3.229.113.226", "44.200.142.76"]


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
