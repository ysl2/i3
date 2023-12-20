#!/usr/bin/env python3

import i3ipc
import argparse


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
        spterm.command('scratchpad show, resize set 50 ppt 50 ppt, move position center')
        return
    # If we get spterm in outside windows, we should hide it.
    if spterm := ipc.get_tree().find_classed(args.scratchpad_class):
        spterm = spterm[0]
        spterm.command('move scratchpad')
        return
    # If we cannot find spterm, we should open it.
    ipc.command(f'exec alacritty -c {args.scratchpad_class}')


if __name__ == '__main__':
    main()
