#!/usr/bin/python3
"""generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack."""
from time import strftime
from fabric.api import local


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
