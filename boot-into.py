grub = open("/boot/grub/grub.cfg").read().strip().split("\n")

major = -1
minor = 0
in_sub = False
in_menu = False

entries = [(0, -1, "Default")]

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

choice = int(input("Choice: "))
if choice >= 0 and choice < len(entries):
    default = str(entries[choice][0])
    if entries[choice][1] != -1:
        default += ">" + str(entries[choice][1])
    if choice != 0:
        default = "\"%s\"" % default
    print("sudo sed 's/GRUB_DEFAULT=.*/GRUB_DEFAULT=%s/' /etc/default/grub && sudo update-grub" % default)
else:
    print("Invalid choice")
