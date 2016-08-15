#!/usr/bin/env python3
# espeak indicator

# module of python3-gi (PyGI)
from gi.repository import Gtk
from gi.repository import AppIndicator3

import subprocess
import os
import signal
import re

def espeak_pause(w, arg):
    try:
        pid = subprocess.check_output(["pidof","espeak"])
        pid = int(pid)
        os.kill(pid, signal.SIGSTOP)
    except subprocess.CalledProcessError:
        print("No process found")

def espeak_continue(w, arg):
    try:
        pid = subprocess.check_output(["pidof","espeak"])
        pid = int(pid)
        os.kill(pid, signal.SIGCONT)
    except subprocess.CalledProcessError:
        print("No process found")

def espeak_kill(w, arg):
    try:
        pid = subprocess.check_output(["pidof","espeak"])
        pids = re.findall('\d+', str(pid)) # finds all numbers
        for pid in pids:
            pid = int(pid)
            print(pid)
            os.kill(pid, signal.SIGKILL)
    except subprocess.CalledProcessError:
        print("No process found")



ind = AppIndicator3.Indicator.new(
    "Stop/Cont espeak process",
    "emblem-cool", # icons at /usr/share/icons/Humanity/*/*/
    AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

menu = Gtk.Menu()
ind.set_menu(menu)

# Menu 1
mitem = Gtk.MenuItem("Continue espeak")
menu.append(mitem)
mitem.show()
mitem.connect("activate", espeak_continue, None)

# Menu 2
mitem = Gtk.MenuItem("Pause espeak")
menu.append(mitem)
mitem.show()
mitem.connect("activate", espeak_pause, None)

# Seperator
mitem = Gtk.SeparatorMenuItem()
menu.append(mitem)
mitem.show()

# Menu 3
mitem = Gtk.MenuItem("Kill espeak")
menu.append(mitem)
mitem.show()
mitem.connect("activate", espeak_kill, None)

# Seperator
mitem = Gtk.SeparatorMenuItem()
menu.append(mitem)
mitem.show()

mitem = Gtk.MenuItem("Exit")
menu.append(mitem)
mitem.show()
mitem.connect("activate", lambda w, arg: Gtk.main_quit(), None)

Gtk.main()
