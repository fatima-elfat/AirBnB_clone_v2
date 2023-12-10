#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy:
"""
from fabric.api import env, put, run, local
import os.path
from time import strftime

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
    filenme = archive_path.split("/")[-1]
    nme = filenme.split(".")[0]
    path_r = "/data/web_static/releases/{}/".format(nme)
    path_c = "/data/web_static/current"
    if put(archive_path, "/tmp/{}".format(filenme)).failed is True:
        return False
    """put(archive_path, "/tmp/")"""
    if run("mkdir -p {}".format(path_r)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C {}".format(filenme, path_r)).failed is True:
        return False
    if run("rm /tmp/{}".format(filenme)).failed is True:
        return False
    if run("mv {}web_static/* {}".format(path_r, path_r)).failed is True:
        return False
    if run("rm -rf {}web_static".format(path_r)).failed is True:
        return False
    if run("rm -rf {}".format(path_c)).failed is True:
        return False
    if run("ln -s {} {}".format(path_r, path_c)).failed is True:
        return False
    print('New version deployed!')
    return True


def deploy():
    """
    deploy creates and distributes
    """
    arch = do_pack()
    if arch is None:
        return False
    r = do_deploy(arch)
    return r
