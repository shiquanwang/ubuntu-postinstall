#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# My script for post installation of Ubuntu
#
# Syntax: # sudo ./ubuntu-postinstall.py
#
# Shiquan Wang <shiquan.wang@philips.com>
# http://shiquanwang.github.io
# Distributed under the LGPL version 3 license


__appname__ = "ubuntu-postinstall"
__version__ = "0.1"
__author__ = "Shiquan Wang <shiquanwang@gmail.com>"
__license__ = "LGPL v3"


"""
Post installation script for Ubuntu
"""


import argparse
import logging
import os
import sys


# Global variables

_FOR_UBUNTU = "saucy"
_DEBUG = 1
_LOG_FILE = "/tmp/%s.log" % __appname__
_CONF_FILE = "https://raw.github.com/shiquanwang/ubuntu-postinstall/master/ubuntu-13.10-unity-postinstall.cfg"


# Classes

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    ORANGE = '\033[93m'
    NO = '\033[0m'

    def disable(self):
        self.RED = ''
        self.GREEN = ''
        self.BLUE = ''
        self.ORANGE = ''
        self.NO = ''


# Functions

def isroot():
    """
    Check if the user is root.
    Return TRUE if user is root.
    """
    return (os.geteuid() == 0)


def showexec(description, command, exitonerror = 0, presskey = 0, waitmessage = "", user = "root"):
    """
    Execute a system command with a pretty status display (Running / OK / Warning / Error)
    By default (exitcode=0), the function did not exit if the command failed
    """

    if _DEBUG:
        logging.debug("%s" % description)
        logging.debug("%s" % command)

    # wait message
    if (waitmessage == ""):
        waitmessage = description

    # manage very long description
    if (len(waitmessage) > 65):
        waitmessage = waitmessage[0:65] + "..."
    if (len(description) > 65):
        description = description[0:65] + "..."

    # display the command
    if (presskey == 1):
        status = _("[ ENTER ]")
    else:
        status = _("[Running]")
    statuscolor = colors.BLUE
    sys.stdout.write(colors.NO + "%s" % waitmessage + statuscolor + "%s" % status.rjust(79-len(waitmessage)) + colors.NO)
    sys.stdout.flush()

    # wait keypressed (optional)
    if (presskey == 1):
        try:
            tmp_input = input()
        except:
            pass
        input()

    # run the command
    if (user == "root"):
        returncode = os.system("/bin/sh -c \"%s\" >> /dev/null 2>&1" % command)
    else:
        returncode = os.system("/bin/sh -c \"sudo -u {0} -H {1}\" >> /dev/null 2>&1".format(user, command))

    # display the result
    if ((returncode == 0) or (returncode == 25600)):
        status = "[  OK   ]"
        statuscolor = colors.GREEN
    else:
        if exitonerror == 0:
            status = "[Warning]"
            statuscolor = colors.ORANGE
        else:
            status = "[ Error ]"
            statuscolor = colors.RED

    sys.stdout.write(colors.NO + "\r%s" % description + statuscolor + "%s\n" % status.rjust(79-len(description)) + colors.NO)

    if _DEBUG:
        logging.debug(_("Returncode = %d") % retruncode)

    # stop the program if returncode and exitonerror != 0
    if ((returncode != 0) & (exitonerror != 0)):
        if _DEBUG:
            logging.debug(_("Forced to quit"))
        exit(exitonerror)


def main():
    """
    Utility for Ubuntu post installation.
    See more using ubuntu-postinstall.py --help
    """
    # create parser
    parser = argparse.ArgumentParser()
    # argument for configuration file
    parser.add_argument('-c', '--conf', type=str, required=True,
                        help='Ubuntu post installation configuration file.')
    # argument group for scene/module selection
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--scene', type=str,
                       help='The scene to be installed.')
    group.add_argument('-m', '--module', type=str, action='append',
                       help='The module to be installed.')
    # argument for version
    parser.add_argument('--version', action='version',
                        version='{0} Version {1}'.format(
                            __appname__, __version__))
    # parse args
    args = parser.parse_args()

# Main program

if __name__ == "__main__":
    sys.exit(main())
