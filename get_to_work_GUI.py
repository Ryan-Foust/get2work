#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import sys
import subprocess
import webbrowser
import button_creator
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

def main(argv):
    if debug:
        print("Starting main")
        print("args received:", argv)

    # grab token to access task manager app
    # with open(argv[1]) as TDI_Token:
    #     token = TDI_Token.read()
    #     api = TodoistAPI(token)

    # open and convert json to python types
    a_n_w_temp = open(argv[1])
    to_load = a_n_w_temp.read()
    apps_and_websites = json.loads(to_load)

    # check that json data made it
    if debug:
        print(apps_and_websites)
        print(type(apps_and_websites))

    maker = None
    obj_list = []
    # all JSON stuff is passed to class
    for app in apps_and_websites:
        maker = button_creator.createCheckbutton(app_data=app)
        obj_list.append(maker)
        maker.button.pack()
    maker.start_GUI()

    # for each button made
    for obj in obj_list:

        # if box was checked (meaning, open app or website)
        if obj.ctrl.get() == 1:
            if obj.apps['is_website']:
                open_website(obj.apps['url'])
            else:
                open_app(obj.apps['path'])


if __name__ == '__main__':
    main(sys.argv)
