#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import sys
import subprocess
import webbrowser
debug = False


def main(argv):
    if debug:
        print("Starting main")
        print("args received:", argv)


if __name__ == '__main__':
    main(sys.argv)
