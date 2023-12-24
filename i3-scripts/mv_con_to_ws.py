#!/usr/bin/env python

import i3ipc
import subprocess

ipc = i3ipc.Connection()


def main():
    focused = ipc.get_tree().find_focused()
    result = subprocess.run("zenity --entry --title '' --text 'Move current container to workspace:'", shell=True, capture_output=True, text=True)
    result = result.stdout.strip()
    focused.command(f'move container to workspace "{result}"')


if __name__ == '__main__':
    main()
