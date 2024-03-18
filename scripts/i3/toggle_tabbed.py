#!/usr/bin/env python

import i3ipc
import subprocess

ipc = i3ipc.Connection()


def main():
    subprocess.run('killall autotiling &> /dev/null', shell=True)
    focused = ipc.get_tree().find_focused()
    if focused and 'on' in focused.floating:
        ipc.command('focus mode_toggle')
    ipc.command('exec --no-startup-id i3-autolayout tabmode --file-layout /tmp/i3-autolayout-tabmode.save')
    subprocess.run('autotiling &', shell=True)


if __name__ == '__main__':
    main()
