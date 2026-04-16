import subprocess
import hashlib
import pickle
import os

# FAILLE 1 : mot de passe en dur dans le code
SECRET_PASSWORD = "admin123"
DB_PASSWORD = "mysql_root_password"

# FAILLE 2 : exécution de commande shell sans protection (injection possible)
def search_user(username):
    cmd = "grep " + username + " /etc/passwd"
    result = subprocess.check_output(cmd, shell=True)
    return result

# FAILLE 3 : hashage MD5 (algorithme trop faible)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# FAILLE 4 : désérialisation non sécurisée (permet exécution de code)
def load_session(data):
    return pickle.loads(data)

# FAILLE 5 : permissions trop larges sur un fichier
def create_config():
    with open("/tmp/config.txt", "w") as f:
        f.write("password=" + SECRET_PASSWORD)
    os.chmod("/tmp/config.txt", 0o777)
