#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

# Avoid g-ir-scanner FTB/SV
shelltools.export ("HOME", get.installDIR())

# Circular deps  - woo
IgnoreAutodep = True

def setup():
    autotools.configure ("--libexecdir=/usr/lib \
                          --localstatedir=/var  \
                          --disable-manpages \
                          --sysconfdir=/etc \
                          --with-sysvinit-path=/etc/init.d \
                          --with-firmware-path=/lib/firmware \
                          --with-pamlibdir=/lib/security")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    # udev compatibility stuff
    pisitools.dosym ("/usr/bin/udevadm", "/sbin/udevadm")
    pisitools.dosym ("/usr/lib/systemd/systemd-udevd", "/lib/udev/udevd")
    pisitools.dosym ("/usr/lib/libudev.so", "/usr/lib/libudev.so.0")

    # Final tweaks ^^
    pisitools.dosym ("/usr/lib/systemd/systemd", "/bin/systemd")
    pisitools.dosym ("/usr/lib/systemd/systemd", "/sbin/init")

    # Make the journal directory
    pisitools.dodir ("/var/log/journal")

    # Install controll symlinks
    for control_item in ["reboot", "shutdown", "poweroff", "halt"]:
        pisitools.dosym ("/usr/bin/systemctl", "/sbin/%s" % control_item)

    # Remove unwanted rpm macro
    pisitools.removeDir ("/usr/lib/rpm")


    # Set defaults (enable readahead)
    pisitools.dosym("/usr/lib/systemd/system/systemd-readahead-collect.service",
                    "/usr/lib/systemd/system/default.target.wants/systemd-readahead-collect.service")

    # Set defaults (enable readahead)
    pisitools.dosym("/usr/lib/systemd/system/systemd-readahead-replay.service",
                    "/usr/lib/systemd/system/default.target.wants/systemd-readahead-replay.service")
