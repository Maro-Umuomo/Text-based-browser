import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
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


def create_directory(name):
    # Check if the directory already exists
    if os.path.exists(directory_name):
        # print(f"The directory '{name}' already exists.")
        return
    else:
        # If the directory does not exist, create it
        try:
            os.makedirs(name)
            # print(f"The directory '{name}' has been created.")
        except OSError as e:
            # Handle any errors that occur during directory creation
            print(f"Failed to create the directory '{name}': {e}")


args = sys.argv
directory_name = args[1]

create_directory(directory_name)
os.chdir(directory_name)


def process_user_input(user_input):
    match user_input:
        case "nytimes.com":
            create_web_file("nytimes", nytimes_com)
            print(nytimes_com)
        case "bloomberg.com":
            create_web_file("bloomberg", bloomberg_com)
            print(bloomberg_com)
        case "exit":
            quit()
        case _:
            print("Invalid URL\n")


def create_web_file(name: str, content: str):
    if not os.path.exists(name):
        with open(name, 'w') as f:
            f.write(content)


# write your code here
while True:
    query = input()
    process_user_input(query)
