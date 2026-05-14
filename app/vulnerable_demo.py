import hashlib, pickle, subprocess, os

# FAILLE 1 HIGH : mot de passe en dur
SECRET_PASSWORD = "admin123"

# FAILLE 2 HIGH : injection shell
def search_user(username):
    cmd = "grep " + username + " /etc/passwd"
    return subprocess.check_output(cmd, shell=True)

# FAILLE 3 MEDIUM : MD5 casse depuis 2004
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# FAILLE 4 HIGH : deserialisation dangereuse
def load_session(data):
    return pickle.loads(data)

# FAILLE 5 MEDIUM : permissions trop larges
def create_config():
    os.chmod("/tmp/config.txt", 0o777)
