#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "fonts"

def install():
    pisitools.dodir("/usr/share/fonts/default/ghostscript")
    pisitools.insinto("/usr/share/fonts/default/ghostscript", "*")

    # Remove fonts.* files as they will be generated by xorg-app pakhandler
    for f in ["scale", "dir"]:
        pisitools.remove("/usr/share/fonts/default/ghostscript/fonts.%s" % f)

    docs = ["COPYING", "ChangeLog", "README", "README.tweaks", "TODO"]

    for f in docs:
        pisitools.remove("/usr/share/fonts/default/ghostscript/%s" % f)
        pisitools.dodoc(f)
