
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
import os

stack = []
current_page = ""

while True:
    user_input = input()
    if "dir" in user_input:
        dirName = user_input.split()[1]
        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            pass
    else:
        try:
            # Create target Directory
            os.mkdir("tb_tabs")
        except FileExistsError:
            pass
    if user_input.count(".") > 0:
        if user_input.rstrip(".com") == "bloomberg":
            if current_page == "":
                current_page = bloomberg_com
            else:
                stack.append(current_page)
                current_page = bloomberg_com
            with open("./tb_tabs/" + user_input.rstrip(".com"), "w") as f:
                print(bloomberg_com)
                f.write(bloomberg_com)
        elif user_input.rstrip(".com") == "nytimes":
            if current_page == "":
                current_page = nytimes_com
            else:
                stack.append(current_page)
                current_page = nytimes_com
            with open("./tb_tabs/" + user_input.rstrip(".com"), "w") as f:
                print(nytimes_com)
                f.write(nytimes_com)
        else:
            print("Error: Unknown URL")
    elif user_input == "back":
        if len(stack) > 0:
            print(stack.pop())
    elif user_input == "exit":
        break
    else:
        print("Error: Invalid URL")
