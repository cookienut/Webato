"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file contains the Spammer class and its methods to initiate sending
text messages from a message file over any web application.
"""

import time

import click
import pyautogui as gui

import settings
from .calibrate import Calibration
from .reader import FileReader


class Spammer():
    """
    Class for sending text messages over a web app using GUI automation.
    """

    def __init__(self, app_name=None, msg_file=None):
        # WebApp name
        self.app_name = app_name or settings.DEFAULT_APP
        # Calibration details for webApp
        clb = Calibration()
        self.window_width, self.window_height = clb.get_caliberation_config(
            self.app_name)
        # Read and parse messages from message file
        self.msg_file = msg_file or clb.config['filenames'][self.app_name]
        fr = FileReader(self.msg_file)
        self.messages = fr.parse_file_content(fr.read_file())

    def send_message(self, text):
        """
        Automates GUI to type-in the provided ``text`` string on the keyboard
        and press the ``enter key`` to forward the very text.
        """
        gui.moveTo(self.window_width, self.window_height)
        gui.click()
        gui.typewrite(['end'])
        gui.typewrite(text)
        gui.typewrite(['enter'])

    def send_messages(self):
        """
        Automates GUI to type-in and send all the lines of text messages saved
        as a list in ``self.messages``, over the selected webapp.
        """
        click.echo(f'\nSending messages...\n')
        for text in self.messages:
            click.echo(text)
            time.sleep(0.01)
            self.send_message(text)
