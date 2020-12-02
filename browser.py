import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore

def createNewFolder(name="tb_tabs"):
    """
    Create a new folder with the given name or do nothing if folder with
    the given name exists.
    """
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


stack = []
current_page = ""

while True:
    user_input = input()
    folder = "tb_tabs"
    if "dir" in user_input:
        createNewFolder(user_input.split()[1])
        folder = user_input.split()[1]
    else:
        createNewFolder()
    if user_input.count(".") > 0:
        if "https://" not in user_input:
            user_input = "https://" + user_input
        if current_page == "":
            current_page = user_input
        else:
            stack.append(current_page)
            current_page = user_input
        r = requests.get(user_input)
        if r:
            soup = BeautifulSoup(r.content, 'html.parser')
            tags = ['p', 'a', 'ul', 'ol', 'li']
            web_page = []
            for tag in tags:
                web_page.extend(soup.find_all(tag))
            websiteName = user_input[:len(user_input) - 4].lstrip("https://").lstrip("www.")
            with open("./{}/".format(folder) + websiteName, "w") \
                    as f:
                for el in web_page:
                    if el.name == 'a':
                        print(Fore.BLUE + el.text)
                    else:
                        print(el.text)
                    f.write(el.text)
        else:
            print("Error: Unknown URL")
    elif user_input == "back":
        if len(stack) > 0:
            print(stack.pop())
    elif user_input == "exit":
        break
    else:
        print("Error: Invalid URL")
