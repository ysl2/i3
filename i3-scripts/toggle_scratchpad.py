#!/usr/bin/env python3

import i3ipc
import argparse


def show_spterm(spterm):
    spterm.command('scratchpad show, resize set 50 ppt 50 ppt, move position center')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scratchpad_class', type=str, nargs='?', default='spterm')
    args = parser.parse_args()

    ipc = i3ipc.Connection()

    # If we get spterm in scratchpad, we should show it.
    if (
        spterm := ipc.get_tree()
        .scratchpad()
        .find_classed(args.scratchpad_class)
    ):
        spterm = spterm[0]
        show_spterm(spterm)
        return
    # If we get spterm in outside windows, then:
    # Case 1: If in current workspace, we should hide it.
    # Case 2: If in other spaces, we should move it to current workspace.
    if spterm := ipc.get_tree().find_classed(args.scratchpad_class):
        spterm = spterm[0]
        # We first move spterm to scratchpad, whatever if it is in current workspace.
        spterm.command('move scratchpad')
        # If spterm not in current workspace, we should show it to current workspace.
        if spterm.workspace().name != ipc.get_tree().find_focused().workspace().name:
            show_spterm(spterm)
        return
    # If we cannot find spterm, we should open it.
    ipc.command(f'exec alacritty -c {args.scratchpad_class}')


if __name__ == '__main__':
    main()
