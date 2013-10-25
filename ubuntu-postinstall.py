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
