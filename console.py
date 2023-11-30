#!/usr/bin/python3
"""Module for HBNBCommand class"""
import cmd
import re
import json
from models.base_model import BaseModel
from models import storage
from models.employer import Employer
from models.job_application import JobApplication
from models.job_seeker import JobSeeker
from models.job_seeker_interactions import Message,Review
from models.job import Job


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "ajira.project "

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on empty line (just press ENTER)"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
