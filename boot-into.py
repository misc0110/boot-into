#!/usr/bin/env python

from subprocess import Popen, PIPE

grub = open("/boot/grub/grub.cfg").read().strip().split("\n")

major = -1
minor = 0
in_sub = False
in_menu = False

#entries = [(0, -1, "Default")]
entries = []

for gl in grub:
    if gl.strip() == "}":
        if in_menu:
            in_menu = False
        elif in_sub:
            in_sub = False
            minor = 0
    
    if "submenu " in gl:
        in_sub = True
        minor = -1
        major += 1

    if "menuentry " in gl:
        if in_sub:
            minor += 1
        else:
            major += 1
        in_menu = True        
        desc = gl.split("'")[1]
        entries.append((major, minor if in_sub else -1, desc))

for idx, e in enumerate(entries):
    print("[%2d] %s" % (idx, e[2]))
print("[ x] Quit")

while True:
    raw_choice = input("Choice: ")
    if raw_choice.strip() in ["x", "X", "q", "Q"]:
        break
    try:
        choice = int(raw_choice)
    except:
        print("Invalid choice!")
        continue

    if choice >= 0 and choice < len(entries):
        default = str(entries[choice][0])
        if entries[choice][1] != -1:
            default += ">" + str(entries[choice][1])
        cmd = ['grub-reboot', default]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))
        print(stderr.decode("utf-8"))
        process = Popen(['reboot', 'now'], stdout=PIPE,stderr=PIPE);
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))
        print(stderr.decode("utf-8"))
        break
    else:
        print("Invalid choice!")
