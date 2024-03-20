#!/usr/bin/env python3

import i3ipc

i3 = i3ipc.Connection()


def on_window_new(i3, event):
    focused = i3.get_tree().find_focused()

    if focused.fullscreen_mode:
        focused.command('fullscreen disable')
    event.container.command('focus')


if __name__ == '__main__':
    i3.on(i3ipc.Event.WINDOW_NEW, on_window_new)
    i3.main()
