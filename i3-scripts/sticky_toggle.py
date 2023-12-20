#!/usr/bin/env python3
import i3ipc


def main():
    i3 = i3ipc.Connection()
    focused = i3.get_tree().find_focused()

    if focused.sticky:
        focused.command('sticky disable')
        return
    if focused.fullscreen_mode:
        focused.command('fullscreen disable')
    if 'off' in focused.floating:
        focused.command('floating enable')
        focused.command('resize set 50 ppt 50 ppt')
        focused.command('move position center')
    focused.command('sticky enable')


if __name__ == '__main__':
    main()
