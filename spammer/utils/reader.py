"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file contains the Reader class and methods to read as well as parsed the
contents of message files as needed.
"""

import sys

from pathlib import Path

import settings


class FileReader():
    """
    Reader class for reading and parsing text from the message files.
    """

    def __init__(self, file_name):
        __base_path = Path(__file__).resolve().parent
        self.file_path = Path.joinpath(__base_path, '..', 'messages', file_name)
        self.line_by_line_messaging = settings.LINE_BY_LINE_MESSGAGING

    def read_file(self, file_path=None):
        """
        Reads text line by line from message file and returns it as a list of
        strings.
        """
        file_path = file_path or self.file_path
        try:
            with open(file_path, 'r') as fh:
                return fh.readlines()
        except FileNotFoundError:
            print(f'\nError: File "{file_path}" not found...')
            sys.exit(0)

    def parse_file_content(self, content):
        """
        Parses the provided list of text strings and returns the parsed list.
        """
        parsed = list()

        # Update the following code as required, for any additional processing
        parsed = [_line.rstrip('\n') for _line in content]

        if not self.line_by_line_messaging:
            parsed = [' '.join(parsed)]
        return parsed
