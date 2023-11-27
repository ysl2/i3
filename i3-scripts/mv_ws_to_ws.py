import subprocess
import json
import sys


# Get input
command = '/usr/bin/zenity --entry --text "Rename workspace to workspace (seprate by space):"'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
process.wait()
output = process.stdout.read().decode()
output = output.strip()
if not output:
    sys.exit()
output = output.split(' ')

# Check input
if len(output) % 2 != 0:

    wss = subprocess.getoutput('i3-msg -t get_workspaces')
    wss = json.loads(wss)
    for ws in wss:
        if ws['focused']:
            ws_cur = ws['name']

    output.insert(0, ws_cur)

# Rename workspaces
for i in range(0, len(output), 2):
    command = f'i3-msg rename workspace \'"{output[i]}"\' to temp\\; rename workspace \'"{output[i+1]}"\' to "{output[i]}"\\; rename workspace temp to \'"{output[i+1]}"\''
    subprocess.Popen(command, shell=True)
