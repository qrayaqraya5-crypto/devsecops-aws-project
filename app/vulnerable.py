import subprocess
import hashlib
import pickle
import os

SECRET_PASSWORD = "admin123"
DB_PASSWORD = "mysql_root_password"

def search_user(username):
    cmd = "grep " + username + " /etc/passwd"
    result = subprocess.check_output(cmd, shell=True)
    return result

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def load_session(data):
    return pickle.loads(data)

def create_config():
    with open("/tmp/config.txt", "w") as f:
        f.write("password=" + SECRET_PASSWORD)
    os.chmod("/tmp/config.txt", 0o777)
