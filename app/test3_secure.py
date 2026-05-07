import subprocess
import hashlib
import yaml
import os

# SECURE - subprocess sans shell=True
def execute_command(command_list):
    result = subprocess.run(command_list, shell=False, capture_output=True, text=True)
    return result.stdout

# SECURE - hashlib SHA256 (pas MD5)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# SECURE - yaml.safe_load (pas yaml.load)
def parse_config(config_string):
    return yaml.safe_load(config_string)

# SECURE - os.path sans injection
def list_files(directory):
    safe_dir = os.path.abspath(directory)
    return os.listdir(safe_dir)

# SECURE - SQL avec paramètres (pas de concaténation)
def get_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    return cursor.fetchall()
