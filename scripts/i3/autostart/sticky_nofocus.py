#!/usr/bin/env python3

import i3ipc

i3 = i3ipc.Connection()


def on_workspace_focus(change, old):
    focused = i3.get_tree().find_focused()

    if focused and focused.sticky:
        i3.command('focus mode_toggle')


if __name__ == '__main__':
    i3.on(i3ipc.Event.WORKSPACE_FOCUS, on_workspace_focus)
    i3.main()
