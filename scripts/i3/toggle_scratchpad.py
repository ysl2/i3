#!/usr/bin/env python3

import i3ipc
import argparse
import pathlib
import subprocess
import time


parser = argparse.ArgumentParser()
parser.add_argument('scratchpad_class', type=str, nargs='?', default='spterm')
parser.add_argument('-r', '--reset', action='store_true')
parser.add_argument('-c', '--cwd', action='store_true')
args = parser.parse_args()

logdir = pathlib.Path().home() / '.vocal/.lock/i3'
logfile = logdir / args.scratchpad_class


def wait_spterm(ipc):
    while True:
        spterm = ipc.get_tree().find_focused()
        if spterm.window_class == args.scratchpad_class:
            return spterm


def show_spterm(ipc, spterm):
    # focused = ipc.get_tree().find_focused()
    # if focused.fullscreen_mode and (
    #     not spterm or spterm.window != focused.window
    # ):
    #     focused.command('fullscreen disable')

    def wait_resize_spterm():
        # 1. Fisrt, we search it in outside workspaces.
        spterm = wait_spterm(ipc)
        # 2. Then, we set the target size for spterm.
        mon = next((mon for mon in ipc.get_outputs() if mon.name == spterm.ipc_data['output']), None)
        width = mon.rect.width >> 1
        height = mon.rect.height >> 1
        # 3. Finally, we resize spterm and move it to center.
        while True:
            time.sleep(0.05)
            spterm.command(f'resize set {width} px {height} px')
            spterm = wait_spterm(ipc)
            if spterm.rect.width == width and spterm.rect.height == height:
                spterm.command('move position center')
                return

    if spterm:
        # 1. We first show spterm from scratchpad workspace to outside workspace.
        spterm.command('scratchpad show')
        # 2. Then, we wait and resize spterm.
        wait_resize_spterm()
        return

    # Create spterm
    terminal_cmd = f'alacritty -c {args.scratchpad_class}'
    if args.cwd:
        ipc.command(f'exec --no-startup-id cd "$(xcwd)" && exec {terminal_cmd}')
    else:
        ipc.command(f'exec --no-startup-id {terminal_cmd}')
    # Wait for spterm to appear, and resize it.
    wait_resize_spterm()
    # Log the spterm class.
    logdir.mkdir(parents=True, exist_ok=True)
    with open(logfile, 'w') as f:
        f.write('Alacritty')


def reset_spterm(ipc, spterm):
    # Release spterm's classname.
    if spterm:
        with open(logfile, 'r') as f:
            scratchpad_class = f.readline().strip()
        subprocess.run(['xdotool', 'set_window', '--class', scratchpad_class, str(spterm.window)])
    # Reset current focused window's classname to spterm.
    focused = ipc.get_tree().find_focused()
    with open(logfile, 'w') as f:
        f.write(focused.window_class)
    subprocess.run(['xdotool', 'set_window', '--class', args.scratchpad_class, str(focused.window)])
    # focused.command('move scratchpad')
    # show_spterm(ipc, focused)


def main():
    ipc = i3ipc.Connection()

    # If we get spterm in scratchpad, we should show it.
    if (
        spterm := ipc.get_tree()
        .scratchpad()
        .find_classed(args.scratchpad_class)
    ):
        spterm = spterm[0]
        if args.reset:
            reset_spterm(ipc, spterm)
        else:
            show_spterm(ipc, spterm)
        return
    # If we get spterm in outside windows, then:
    # Case 1: If in current workspace, we should hide it.
    # Case 2: If in other spaces, we should move it to current workspace.
    if spterm := ipc.get_tree().find_classed(args.scratchpad_class):
        spterm = spterm[0]
        if args.reset:
            reset_spterm(ipc, spterm)
            return
        # We first move spterm to scratchpad, whatever if it is in current workspace.
        spterm.command('move scratchpad')
        # If spterm not in current workspace, we should show it to current workspace.
        if spterm.workspace().name != ipc.get_tree().find_focused().workspace().name:
            show_spterm(ipc, spterm)
        return
    # If we cannot find spterm, we should open it.
    if args.reset:
        reset_spterm(ipc, None)
    else:
        show_spterm(ipc, None)


if __name__ == '__main__':
    main()
