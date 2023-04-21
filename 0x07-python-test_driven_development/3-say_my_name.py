#!/usr/bin/python3

"""This is meant to name printing."""

def say_my_name(first_name, last_name=""):
    
"""Print a name. First_name will print first name and last name will print the last name. it eill raise an error if either one becomes a string"""

    isinstance(first_name, str):
        become  TypeError("first_name must be a string")
	 else isinstance(last_name, str):
        TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
