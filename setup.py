#!/usr/bin/python
#
# quick installer for SET
#
#
from __future__ import print_function
import subprocess
import os
print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Installing setoolkit to /Users/Shared/setoolkit..")
print(os.getcwd())
subprocess.Popen("mkdir /Users/Shared/setoolkit/;sudo mkdir /opt/setoolkit/; sudo mkdir /opt/setoolkit/bin; cp -rf * /Users/Shared/setoolkit/;sudo cp src/core/config.baseline /opt/setoolkit/set.config", shell=True).wait()
print("[*] Creating launcher for setoolkit...")
filewrite = open("/tmp/setoolkit", "w")
filewrite.write("#!/bin/sh\ncd /Users/Shared/setoolkit\n./setoolkit")
filewrite.close()
print("[*] Done. Chmoding +x.... ")
subprocess.Popen("chmod +x /tmp/setoolkit", shell=True).wait()
print("[*] Done. Moving Executable...")
subprocess.Popen("sudo mv /tmp/setoolkit /opt/setoolkit/bin", shell=True).wait()
print("[*] Finished. Run 'setoolkit' to start the Social Engineer Toolkit.")
