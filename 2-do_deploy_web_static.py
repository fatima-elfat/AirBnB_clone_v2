#!/usr/bin/python3
"""
distributes an archive to your web servers,
using the function do_deploy:
"""
from fabric.api import env, put, run
import os.path

env.hosts = ["52.86.154.130", "34.207.120.70"]


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
        if put(archive_path, "/tmp/{}".format(filenme)).failed is True:
            return False
        """put(archive_path, "/tmp/")"""
        if run("mkdir -p {}".format(path_r))is True:
            return False
        if run("tar -xzf /tmp/{} -C {}".format(filenme, path_r))is True:
            return False
        if run("rm /tmp/{}".format(filenme))is True:
            return False
        if run("mv {}web_static/* {}".format(path_r, path_r))is True:
            return False
        if run("rm -rf {}web_static".format(path_r))is True:
            return False
        if run("rm -rf {}".format(path_c))is True:
            return False
        if run("ln -s {} {}".format(path_r, path_c))is True:
            return False
        return True
    except Exception:
        return False
