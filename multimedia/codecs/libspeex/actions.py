
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--enable-ogg \
                         --enable-sse \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS")
