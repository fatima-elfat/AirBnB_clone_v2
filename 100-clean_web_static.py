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
    do_pack generates folder
    """
    try:
        local("mkdir -p versions")
        timefrmat = strftime("%Y%M%d%H%M%S")
        filenme = "versions/web_static_{}.tgz".format(timefrmat)
        local("tar -cvzf {} web_static/".format(filenme))
        return filenme
    except Exception:
        return None


def do_deploy(arch):
    """
    do_deploy archive
    """
    if os.path.isfile(arch) is False:
        return False
    filenme = arch.split("/")[-1]
    nme = filenme.split(".")[0]
    try:
        path_r = "/data/web_static/releases/{}/".format(nme)
        path_c = "/data/web_static/current"
        put(arch, "/tmp/{}".format(filenme))
        run("mkdir -p {}".format(path_r))
        run("tar -xzf /tmp/{} -C {}".format(filenme, path_r))
        run("rm /tmp/{}".format(filenme))
        run("mv {}web_static/* {}".format(path_r, path_r))
        run("rm -rf {}web_static".format(path_r))
        run("rm -rf {}".format(path_c))
        run("ln -s {} {}".format(path_r, path_c))
        return True
    except Exception:
        return False


def deploy():
    """
    deploy creates and distributes
    """
    arch = do_pack()
    if arch is None:
        return False
    r = do_deploy(arch)
    return r


def do_clean(number=0):
    """
    deletes out-of-date archives, using the function do_clean

    Args:
        number (int, optional): the number of the archives.
            Defaults to 0.
    """
    if number == 0:
        number = 1
    with lcd('./versions/'):
        local("sudo ls -t | tail -n +{} | xargs rm -rf".format(number))
    with cd('/data/web_static/releases/'):
        run("sudo ls -t | tail -n +{} | xargs rm -rf".format(number))
