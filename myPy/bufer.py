import pyperclip

clipboard_content = pyperclip.paste()

def get_bufer():
    try:
        if clipboard_content:
            with open("bufer.txt", "w") as b:
                b.write(clipboard_content)
        else:
            with open("bufer.txt", "w") as b:
                b.write("bufer is empty")
    except:
        pass