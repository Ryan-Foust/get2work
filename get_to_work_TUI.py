#!/usr/bin/python3
import json
import sys
import webbrowser
import subprocess
debug = False


def open_website(url):
    if debug:
        print("open_website called")
        print("url passed:", url)
    else:
        webbrowser.open(url)


def open_app(path):
    if debug:
        print("open_app called")
        print("path passed:", path)
    else:
        subprocess.Popen(path)


def main(args):
    if debug:
        print("Starting main")
        print(args)

    # open and convert json to python types
    options = json.loads(open(args[1]).read())

    if debug:
        print(options)

    i = 0
    print("In a comma-separated list, enter the numbers of what you want to open.")
    for option in options:
        print("For "+option["name"]+", use "+str(i))
        i += 1
    selected = input("Enter here: ")

    selected_ints = []
    selected_split = selected.split(',')
    for select in selected_split:
        if select[-1].isdigit():
            select = int(select[-1])
        selected_ints.append(select)
    if debug:
        print(selected_ints)

    for ints in selected_ints:
        print(options[ints]["name"])
        if options[ints]["is_website"]:
            open_website(options[ints]["url"])
        else:
            open_app(options[ints]["path"])


if __name__ == '__main__':
    main(sys.argv)
