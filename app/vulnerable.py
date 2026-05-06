import subprocess
import os

# HIGH - Command injection B602
def run_cmd(user_input):
    os.system("ls " + user_input)

# HIGH - Shell injection B603
def execute(cmd):
    subprocess.call(cmd, shell=True)

# HIGH - SQL Injection B608
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query
