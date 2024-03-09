#!/usr/bin/env python

import i3ipc
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--title', action='store_true')
args = parser.parse_args()

ipc = i3ipc.Connection()


def main():
    focused = ipc.get_tree().find_focused()
    if args.title:
        prompt = 'Rename current container title to:'
    else:
        prompt = 'Move current container to workspace:'
    result = subprocess.run(f"zenity --entry --title '' --text '{prompt}'", shell=True, capture_output=True, text=True)
    result = result.stdout.strip()
    if args.title:
        focused.command(f'title_format "{result}"')
    else:
        focused.command(f'move container to workspace "{result}"')
        ipc.command(f'workspace "{result}"')


if __name__ == '__main__':
    main()
