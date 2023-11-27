#!/usr/bin/env python3
import subprocess
import json
import sys


PROJECTOR = {
    'u': 'up',
    'd': 'down',
    'l': 'left',
    'r': 'right',
}


def get_input():
    command = 'zenity --entry --text "Rename workspace to workspace or monitor (sequence seprated by whitespace):"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
    process.wait()
    sequence = process.stdout.read().decode()
    sequence = sequence.strip()
    if not sequence:
        sys.exit()
    sequence = sequence.split(' ')
    return sequence


def insert_default(sequence):
    wss = subprocess.getoutput('i3-msg -t get_workspaces')
    wss = json.loads(wss)
    for ws in wss:
        if ws['focused']:
            ws_cur = ws['name']
    sequence.insert(0, ws_cur)


def rename_workspace(ws_from, ws_to):
    command = f'i3-msg rename workspace \'"{ws_from}"\' to temp\\; rename workspace \'"{ws_to}"\' to "{ws_from}"\\; rename workspace temp to \'"{ws_to}"\''
    subprocess.Popen(command, shell=True)


def move_workspace_to_monitor(ws, mon):
    command = f'i3-msg workspace {ws}\\; move workspace to output {mon}'
    subprocess.Popen(command, shell=True)


def is_monitor(arg):
    return arg in PROJECTOR.values()


def project_monitor(arg):
    return PROJECTOR.get(arg, arg)


def process(sequence):
    if len(sequence) % 2 != 0:
        insert_default(sequence)
    for i in range(0, len(sequence), 2):
        arg0 = project_monitor(sequence[i])
        arg1 = project_monitor(sequence[i + 1])
        if is_monitor(arg0) and is_monitor(arg1):
            continue
        arg0, arg1 = (arg1, arg0) if is_monitor(arg0) else (arg0, arg1)
        if is_monitor(arg1):
            move_workspace_to_monitor(arg0, arg1)
            continue
        rename_workspace(arg0, arg1)


def main():
    sequence = get_input()
    process(sequence)


if __name__ == '__main__':
    main()
