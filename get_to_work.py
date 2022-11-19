#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import sys
import subprocess
import webbrowser
import button_creator
debug = True


def main(argv):
    if debug:
        print("Starting main")
        print("args received:", argv)

        # grab token to access task manager app
        with open(argv[1]) as TDI_Token:
            token = TDI_Token.read()
            api = TodoistAPI(token)

        # open and convert json to python types
        a_n_w_temp = open(argv[2])
        to_load = a_n_w_temp.read()
        apps_and_websites = json.loads(to_load)

        # check that json data made it
        if debug:
            print(apps_and_websites)
            print(type(apps_and_websites))

        for app in apps_and_websites:
            if debug:
                print(app)
            button_creator.createCheckbutton(app_data=app)


if __name__ == '__main__':
    main(sys.argv)
