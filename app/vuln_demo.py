import subprocess
import os

def execute(cmd):
    subprocess.call(cmd, shell=True)

def list_dir(path):
    os.system("ls " + path)
