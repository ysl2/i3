#!/usr/bin/env python3

import i3ipc
import argparse
import getpass
import pathlib
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('scratchpad_class', type=str, nargs='?', default='spterm')
parser.add_argument('-r', '--reset', action='store_true')
args = parser.parse_args()

user = getpass.getuser()
logdir = f'/home/{user}/.vocal/.lock/i3'
logdir = pathlib.Path(logdir)
logfile = logdir / args.scratchpad_class


def show_spterm(ipc, spterm):
    focused = ipc.get_tree().find_focused()
    if focused.fullscreen_mode and (
        not spterm or spterm.window != focused.window
    ):
        focused.command('fullscreen disable')
    if spterm:
        spterm.command('scratchpad show, resize set 50 ppt 50 ppt, move position center')
        return
    # Create spterm
    ipc.command(f'exec --no-startup-id alacritty -c {args.scratchpad_class}')
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
