#!/usr/bin/env python3
import i3ipc
import sys


def get_workspace_bounds(i3):
    workspaces = i3.get_workspaces()
    nums = [w.num for w in workspaces]
    return min(nums), max(nums)


def move_to_workspace(i3, direction):
    current_workspace = i3.get_tree().find_focused().workspace().num
    min_workspace, max_workspace = get_workspace_bounds(i3)

    num_workspaces = max_workspace - min_workspace + 1

    if int(direction) < 0:
        target_workspace = (current_workspace - 1 - min_workspace) % num_workspaces + min_workspace
    elif int(direction) > 0:
        target_workspace = (current_workspace + 1 - min_workspace) % num_workspaces + min_workspace
    else:
        return

    i3.command(f"workspace number {target_workspace}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <direction>")
        sys.exit(1)

    direction = sys.argv[1]
    i3 = i3ipc.Connection()

    move_to_workspace(i3, direction)
