#!/usr/bin/python3
"""
    This is  a script that adds all arguments to a Python
    list, and then save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv[1:]
lists = []

lists.extend(arguments)

save_to_json_file(lists, "add_item.json")

load_from_json_file("add_item.json")
