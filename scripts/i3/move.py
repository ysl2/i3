#!/usr/bin/env python3

import i3ipc
import sys


def main():
    direction = sys.argv[1]
    ipc = i3ipc.Connection()

    focused = ipc.get_tree().find_focused()
    focused_id = focused.id
    focused.command(f'move {direction}')

    focused = ipc.get_tree().find_by_id(focused_id)
    focused.command('focus')


if __name__ == '__main__':
    main()
