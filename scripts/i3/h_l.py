#!/usr/bin/env python3

import i3ipc
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--direction', type=str, required=True)
    parser.add_argument('-c', '--container', action='store_true')
    return parser.parse_args()


def main():
    args = get_args()

    ipc = i3ipc.Connection()
    ws_cur = ipc.get_tree().find_focused().workspace().num

    if args.direction == 'h':
        target = max(ws_cur - 1, 1)
    elif args.direction == 'l':
        target = ws_cur + 1

    if args.container:
        ipc.command(f'move container to workspace number {target}; workspace number {target}')
    else:
        ipc.command(f"workspace number {target}")


if __name__ == '__main__':
    main()
