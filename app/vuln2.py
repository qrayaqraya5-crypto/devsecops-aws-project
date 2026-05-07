import subprocess
import os
import pickle
import yaml

# HIGH - B602: subprocess with shell=True (Command Injection)
def execute_command(user_input):
    subprocess.call("ping " + user_input, shell=True)

# HIGH - B605: os.system shell injection
def list_files(directory):
    os.system("ls -la " + directory)

# HIGH - B301: pickle.loads (Arbitrary code execution)
def load_data(serialized_data):
    return pickle.loads(serialized_data)

# HIGH - B506: yaml.load without Loader (Code execution)
def parse_config(config_string):
    return yaml.load(config_string)

# HIGH - B603: subprocess without shell check
def run_process(cmd):
    subprocess.Popen(cmd, shell=True)
