import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import re


def create_new_folder(name):
    """
    Create a new folder with the given name or do nothing if folder with
    the given name exists.
    :param name: file name for the webpage
    """
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


def check_valid_domain_name(website):
    """
    Checks if the domain name given by the user is valid
    :param website: website name
    :return: true if website name matches with regular expression, else false
    """
    return re.search("(https:\/\/)*.*\..*\.\w{2,}", website)


def create_webpage_file(url, current_folder, file_name):
    """
    Creates a new file named after the domain name and writes content from certain html tags into the file
    :param url: webpage address
    :param current_folder: the folder where the user wants the webpage to be stored
    :param file_name: name of the file
    """
    r = requests.get(url)
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        tags = ['p', 'a', 'ul', 'ol', 'li']
        web_page = []
        for tag in tags:
            web_page.extend(soup.find_all(tag))
        with open("./{}/{}".format(current_folder, file_name), "w") \
                as f:
            for el in web_page:
                if el.name == 'a':
                    print(Fore.BLUE + el.text)
                    print(Style.RESET_ALL)
                else:
                    print(el.text)
                f.write(el.text.strip())
    else:
        print("Error: Unknown URL")


def get_domain_name(website):
    """
    :param website: website name
    :return: the domain name
    """
    m = re.match("(https:\/\/)*.*\.(.*)\.\w{2,}", website)
    return m.group(2)


stack = []
current_page = ""

while True:
    user_input = input("Enter a URL: ")
    folder = "tb_tabs"
    if "dir" in user_input:
        user_input = get_domain_name(user_input.split()[1])
        create_new_folder(user_input)
        folder = user_input
    else:
        create_new_folder(folder)
    if "dir" not in user_input and check_valid_domain_name(user_input):
        if "https://" not in user_input:
            user_input = "https://" + user_input
        if current_page == "":
            current_page = user_input
        else:
            stack.append(current_page)
            current_page = user_input
        website_name = get_domain_name(user_input)
        create_webpage_file(user_input, folder, website_name)
    elif user_input == "back":
        if len(stack) > 0:
            print(stack.pop())
    elif user_input == "exit":
        break
    else:
        print("Error: Invalid URL")
