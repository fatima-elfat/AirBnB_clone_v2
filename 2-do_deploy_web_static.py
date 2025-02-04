#!/usr/bin/python3
"""
distributes an archive to your web servers,
using the function do_deploy:
"""
from time import strftime
from fabric.api import env, put, run
import os.path

env.user = "ubuntu"
env.hosts = ["52.86.154.130", "34.207.120.70"]


def do_pack():
    """
    generates .tgz archive folder
    """
    try:
        local("mkdir -p versions")
        timefrmat = strftime("%Y%M%d%H%M%S")
        filenme = "versions/web_static_{}.tgz".format(timefrmat)
        local("tar -cvzf {} web_static/".format(filenme))
        return filenme
    except Exception:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filenme = archive_path.split("/")[-1]
        nme = filenme.split(".")[0]
        path_r = "/data/web_static/releases/{}/".format(nme)
        path_c = "/data/web_static/current"
        put(archive_path, "/tmp/{}".format(filenme))
        """put(archive_path, "/tmp/")"""
        run("mkdir -p {}".format(path_r))
        run("tar -xzf /tmp/{} -C {}".format(filenme, path_r))
        run("rm /tmp/{}".format(filenme))
        run("mv {}web_static/* {}".format(path_r, path_r))
        run("rm -rf {}web_static".format(path_r))
        run("rm -rf {}".format(path_c))
        run("ln -s {} {}".format(path_r, path_c))
        print('New version deployed!')
        return True
    except Exception:
        return False
