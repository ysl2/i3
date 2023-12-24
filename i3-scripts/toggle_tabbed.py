#!/usr/bin/env python

import i3ipc

ipc = i3ipc.Connection()


def main():
    focused = ipc.get_tree().find_focused()
    if focused and 'on' in focused.floating:
        ipc.command('focus mode_toggle')
    ipc.command('exec --no-startup-id i3-autolayout tabmode --file-layout /tmp/i3-autolayout-tabmode.save')


if __name__ == '__main__':
    main()
