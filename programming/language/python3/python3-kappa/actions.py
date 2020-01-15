
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("PYTHONDONTWRITEBYTECODE", "1")
shelltools.export("LC_ALL", "en_US.UTF-8")

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")