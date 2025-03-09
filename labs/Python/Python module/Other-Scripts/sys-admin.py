"""
Use os.system() to run a Bash command
Use subprocess.run() to run Bash commands
"""

import os
import subprocess

os.system("ls")

print("\n")
subprocess.run(["ls"])

print("\n")
subprocess.run(["ls","-l"])

print("\n")
subprocess.run(["ls","-l","README.md"])

print("\n")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print("\n")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])