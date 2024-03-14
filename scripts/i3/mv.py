#!/usr/bin/env python3

import subprocess
import sys
import i3ipc
import argparse


MONS = {
    'u': 'up',
    'd': 'down',
    'l': 'left',
    'r': 'right',
}


def project(obj):
    return MONS.get(obj, obj)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--container', action='store_true')
    parser.add_argument('-g', '--goto', action='store_true')
    return parser.parse_args()


def get_input(args):
    if args.container:
        prompt = 'Move container to workspace or monitor'
    elif args.goto:
        prompt = 'Goto workspace'
    else:
        prompt = 'Rename workspace to workspace or monitor'

    command = (
        'GTK_THEME="$(cat ~/.config/gtk-3.0/settings.ini | grep gtk-theme-name | cut -d= -f2)" '
        f'zenity --entry --title "" --text "{prompt} (sequence seprated by whitespace):"'
    )
    sequence = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
    sequence = sequence.stdout.decode()
    sequence = sequence.strip()
    if not sequence:
        sys.exit()
    sequence = sequence.split(' ')
    return sequence


def insert_default(ipc, sequence, args):
    if args.container:
        sequence.insert(0, 'c')
    elif args.goto:
        sequence.insert(0, 'g')
    else:
        focused = ipc.get_tree().find_focused()
        ws_cur = focused.workspace().name
        sequence.insert(0, ws_cur)


def move_workspace_to_workspace(ipc, ws_from, ws_to):
    ipc.command(f'rename workspace "{ws_from}" to temp; rename workspace "{ws_to}" to "{ws_from}"; rename workspace temp to "{ws_to}"')


def move_workspace_to_monitor(ipc, ws, mon):
    ipc.command(f'workspace {ws}; move workspace to output {project(mon)}')


def move_container_to_workspace(ipc, ws):
    focused = ipc.get_tree().find_focused()
    focused.command(f'move to workspace "{ws}"')
    focused.command('focus')


def move_container_to_monitor(ipc, mon):
    focused = ipc.get_tree().find_focused()
    focused.command(f'move to output {project(mon)}')
    focused.command('focus')


def retitle_container(ipc, title):
    focused = ipc.get_tree().find_focused()
    focused.command(f'title_format "{title}"')


def goto_workspace(ipc, ws):
    ipc.command(f'workspace {ws}')


def goto_monitor(ipc, mon):
    ipc.command(f'focus {project(mon)}')


def is_monitor(obj):
    return obj in MONS or obj in MONS.values()


def is_container(obj):
    return obj == 'c'


def is_workspace(obj):
    return obj.isdigit()


def is_goto(obj):
    return obj == 'g'


def is_legal(obj):
    return is_monitor(obj) \
        or is_container(obj) \
        or is_workspace(obj) \
        or is_goto(obj)


def main():
    ipc = i3ipc.Connection()
    args = get_args()
    sequence = get_input(args)

    if len(sequence) % 2 != 0:
        insert_default(ipc, sequence, args)
    for i in range(0, len(sequence), 2):
        # obj_from can be a workspace, a container, or a goto
        obj_from = project(sequence[i])
        # obj_to can be a workspace, a monitor, or a container
        obj_to = project(sequence[i + 1])

        if not is_legal(obj_from):
            continue

        if not is_legal(obj_to):
            if is_container(obj_from):
                retitle_container(ipc, obj_to)
            continue

        if is_goto(obj_from) and is_workspace(obj_to):
            goto_workspace(ipc, obj_to)
            continue

        if is_goto(obj_from) and is_monitor(obj_to):
            goto_monitor(ipc, obj_to)
            continue

        if is_workspace(obj_from) and is_workspace(obj_to):
            move_workspace_to_workspace(ipc, obj_from, obj_to)
            continue

        if is_workspace(obj_from) and is_monitor(obj_to):
            move_workspace_to_monitor(ipc, obj_from, obj_to)
            continue

        if is_container(obj_from) and is_workspace(obj_to):
            move_container_to_workspace(ipc, obj_to)
            continue

        if is_container(obj_from) and is_monitor(obj_to):
            move_container_to_monitor(ipc, obj_to)
            continue


# def test_move_workspace_to_monitor():
#     ipc = i3ipc.Connection()
#     move_workspace_to_monitor(ipc, '1', 'u')
#
#
# def test_move_container_to_monitor():
#     ipc = i3ipc.Connection()
#     move_container_to_monitor(ipc, 'u')


if __name__ == '__main__':
    main()
