
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--prefix=/usr --disable-static")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    # Add the documentation
    pisitools.dodoc ("doc/*.css", "doc/*.png", "doc/*.html")
