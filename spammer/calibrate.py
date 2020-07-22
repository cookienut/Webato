"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)

This file contains the Calibration class and its methods to caliberate the
on-screen position of text box in web applications, on different platforms.
"""

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
            open(Path.joinpath(self.base_path, 'config.json')))
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
        config = self.config["caliberations"]

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
        __config = self.config["caliberations"]
        __config[self.app_name] = __config.get(self.app_name) or {}
        __config[self.app_name][self.platform] = [self.width, self.height]

        self.config["filenames"][self.app_name] = self.msg_file

        # Dump the details to config.json
        with open(Path.joinpath(self.base_path, 'config.json'), 'w') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

    def test_caliberations(self, width_height=None, show_switch_prompt=False):
        """
        A method to non invasively test whether the caliberations are correct
        on the current platform and if it is safe to use ``spammer`` with these
        caliberations.

        Usage: The mouse cursor hovers over the area which is expected to be a
        textbox for inputing text. User needs to validate the caliberations by
        accepting them OR opt to abort and recaliberate later.
        """
        width, height = width_height or self.get_caliberation_config()

        prompt_message = (
            'Alright, %sOnce you press \'OK\' you should see the mouse '
            'cursor automatically hover over the textbox as caliberated.')

        if show_switch_prompt:
            prompt_message = prompt_message % (
            f'before you press \'OK\', switch to {self.app_name.title()}...\n')
        else:
            prompt_message = prompt_message % ('')

        gui.alert(prompt_message)
        time.sleep(1)

        for _ in range(4):
            gui.moveTo(width + 10, height, 0.3)
            gui.moveTo(width, height, 0.3)

        accept = gui.confirm(
            'Press \'OK\' to proceed with these caliberations, or press '
            '\'Cancel\' to exit.')
        assert 'Cancel' not in accept, 'Caliberation Test Failed !'

        click.echo('Caliberation test complete.')

    def caliberate_app(self):
        """
        Method to help caliberte position of textbox on user's machine based
        on provided user inputs.
        """
        start_caliberation = gui.confirm(
            f'Starting caliberation for \'{self.app_name.title()}\'... '
            f'Press \'OK\' to continue.')
        assert 'Cancel' not in start_caliberation, 'Caliberation Aborted !'

        gui.alert(
            f'Please switch to the \'{self.app_name.title()}\' app and select '
            'a contact. Move the mouse cursor on top of the text-box and then '
            'hold it still for a few seconds, until confirmation.')

        click.echo(
        f'\nSleeping for {settings.CALIBERATION_SLEEP_SECS} seconds for '
        'caliberation...')
        time.sleep(settings.CALIBERATION_SLEEP_SECS)

        self.width, self.height = gui.position()
        self.test_caliberations((self.width, self.height))

        click.echo('\nCaliberation complete ! Updating config file... ')
        self.update_caliberation_config()
        print(f'Config file updated, location: `config.json` under '
              f'`{self.base_path}`')


@click.command()
@click.option('-t', '--test-mode', help='Flag to test caliberation',
    is_flag=True)
@click.option('-f', '--file', default='', help='Provide msg file name to set',
    required=False)
@click.option('-a', '--app', default='', help='Provide webapp to caliberate',
    required=False)
def cli_caliberate(app, file, test_mode):
    """
    Caliberate or test caliberations of web applications and set their
    corresponding message filenames in ``config.json`` through CLI.

    The purpose of these caliberations is to identify the on-screen position of
    textbox in a webapp to be able to send messages through GUI automation.

    Accepts optional parameters ``--app`` and ``--file`` to specify the webApp
    to caliberate and filename to set against this app in ``config.json``. For
    example:

    >> python caliberate.py -t               # Test default app caliberation
    >> python caliberate.py -t -a abc        # Test app caliberation for abc
    >> python caliberate.py -a whatsapp      # Set caliberation for whatsapp
    >> python caliberate.py -a abc -f m.txt  # Set webapp caliberation and msg
    .                                        # file for some webapp abc
    """

    try:
        cb = Calibration(app, file)
        if test_mode:
            click.echo(f'Testing caliberation for {cb.app_name}...')
            cb.test_caliberations(show_switch_prompt=True)
        else:
            cb.caliberate_app()

    except Exception as ex:
        click.echo(f'Error: {ex}')


if __name__ == '__main__':
    cli_caliberate()
