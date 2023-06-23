import subprocess

def install_samba_package():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'samba'])

def set_samba_permissions():
    subprocess.run(['sudo', 'groupadd', 'sambashare'])
    subprocess.run(['sudo', 'usermod', '-aG', 'sambashare', 'YOUR_USERNAME'])
    subprocess.run(['sudo', 'chown', '-R', 'root:sambashare', '/path/to/shared/folder'])
    subprocess.run(['sudo', 'chmod', '1775', '/path/to/shared/folder'])

def restart_samba_service():
    subprocess.run(['sudo', 'systemctl', 'restart', 'smbd.service'])

if __name__ == '__main__':
    install_samba_package()
    set_samba_permissions()
    restart_samba_service()
