"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file contains the Calibration class and its methods to caliberate the
on-screen position of text box in web applications, on different platforms.
"""

import os
import sys
import json
import time

from pathlib import Path

import click
import pyautogui as gui

import settings

class Calibration():
    """
    Class for caliberating on-screen position of text boxes for writing and
    sending messages over any web application.
    """

    def __init__(self, app_name=None, msg_file=None):
        self.base_path = Path(__file__).resolve().parent
        self.config = json.load(
            open(Path.joinpath(self.base_path, '..','config.json')))
        self.app_name = app_name or settings.DEFAULT_APP
        self.msg_file = msg_file or self.config["filenames"][self.app_name]
        self.platform = self.get_system_platform()

    def get_system_platform(self):
        """
        Returns the generalized system platform name on which current app is
        being run. For example - linux, windows etc.
        """
        platform = sys.platform.lower()
        if 'win' in platform:
            platform = 'windows'
        elif 'linux' in platform:
            platform = 'linux'
        elif 'darwin' in platform:
            platform = 'mac'
        return platform

    def get_caliberation_config(self, app_name=None):
        """
        Retrieves caliberation configuration for the provided ``app_name``.
        Default value of ``app_name is ``None``. By default, retrieves
        caliberations of the default web-app.
        """
        app_name = app_name or self.app_name
        config = self.config["calibrations"]

        if app_name not in config:
            click.echo(
                f'Error: App config missing for \'{app_name}\'. '
                'Please check \'config.json\' or recaliberate.')
            sys.exit(1)
        elif self.platform not in config[app_name]:
            click.echo(
                f'Error: App config missing for platform: \'{self.platform}\'. '
                'Please check \'config.json\' or recaliberate.')
            sys.exit(1)
        return config[app_name][self.platform]

    def update_caliberation_config(self):
        """
        Updates callibration config file with position (width and height)
        of text box on screen, for the calibrated webApp.
        """
        __config = self.config["calibrations"]
        __config[self.app_name] = __config.get(self.app_name) or {}
        __config[self.app_name][self.platform] = [self.width, self.height]

        self.config["filenames"][self.app_name] = self.msg_file

        # Dump the details to config.json
        with open(Path.joinpath(self.base_path, 'config.json'), 'w') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

    def test_calibration(self, width_height=None, show_switch_prompt=False):
        """
        A method to non invasively test whether the app calibrations are correct
        on the current platform and if it is safe to use ``spammer`` with these
        calibrations or not.

        Usage: The mouse cursor hovers over the area which is expected to be a
        textbox for inputing text. User needs to validate the calibrations and
        accept them for saving OR user may opt to abort and recalibrate later.
        """
        # Check if the message file exists for the web-app
        file_ = Path.joinpath(self.base_path, '..', 'messages', self.msg_file)
        assert os.path.exists(file_) and os.path.isfile(file_), (
            f'Message file {self.msg_file}, does not exist.')

        # Check if text-box is calibrated properly
        width, height = width_height or self.get_caliberation_config()

        prompt_message = (
            'Hello, %sOnce you press \'OK\' the mouse cursor will automatically '
            'hover over the screen where a textbox is expected to be.')
        if show_switch_prompt:
            prompt_message = prompt_message % (
            f'before you press \'OK\', switch to {self.app_name.title()} and '
             'make sure a contact is selected.\n\n')
        else:
            prompt_message = prompt_message % ('')
        gui.alert(prompt_message)

        time.sleep(1)
        # Hover over expected area
        for _ in range(4):
            gui.moveTo(width + 10, height, 0.3)
            gui.moveTo(width, height, 0.3)

        accept = gui.confirm(
            'Press \'OK\' if the cursor was correctly positioned over textbox, '
            'or press \'Cancel\' to exit')
        assert 'Cancel' not in accept, (
            'Caliberation Test Failed ! Please re-calibrate the web app.')
        click.echo('Caliberation test complete.')

    def calibrate(self):
        """
        Method to help caliberte position of textbox on user's machine based
        on provided user inputs.
        """
        start_caliberation = gui.confirm(
            f'Starting calibration for \'{self.app_name.title()}\' !!! '
            f'\n\nPress \'OK\' to continue or \'Cancel\' to abort.')
        assert 'Cancel' not in start_caliberation, 'Caliberation Aborted !'

        gui.alert(
            f'Please switch to the \'{self.app_name.title()}\' app and select '
            'a contact after pressing \'Ok\'. Move the mouse cursor over the '
            'text-box and then hold it still for a few seconds, until '
            'confirmation.')

        click.echo(
        f'\nSleeping for {settings.CALIBERATION_SLEEP_SECS} seconds for '
        'caliberation...')
        time.sleep(settings.CALIBERATION_SLEEP_SECS)

        self.width, self.height = gui.position()
        self.test_calibration((self.width, self.height))

        click.echo('\nUpdating config file... ')
        self.update_caliberation_config()
        conf_file_path = Path(__file__).resolve().parent.parent
        conf_file_path = Path.joinpath(conf_file_path, 'config.json')
        click.echo('Caliberation complete !')
        click.echo(f'Config file location: {conf_file_path}')
