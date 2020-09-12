"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file contains methods to perform the following actions through CLI:
1. Trigger spammer script
2. Calibrate spammer for a web application
3. Test calibrations for a web application
"""

import sys
import time

import click
import pyautogui as gui

import settings
from .calibrate import Calibration
from .spammer import Spammer


@click.command('main', short_help='Run or calibrate spammer for webapps.')
@click.option(
    '-f', '--mfile', default='', help='Name of message file', required=False
)
@click.option(
    '-a', '--app', default='', help='Name of webapp to use', required=False
)
@click.option(
    '-t', '--test-mode', default=False, help='Calibration mode flag', is_flag=True
)
@click.option(
    '-c', '--calibrate', default=False, help='Flag for calibration mode', is_flag=True
)
def main(calibrate, test_mode, app, mfile):
    """
    Runs ``Spammer`` as CLI command.

    Accepts optional arguments ``--app`` and ``--file`` to specify
    webapp and the message file respectively. If not specifed, uses default
    values. For example:

    Running spammer:
    >> py spammer                           # Default webapp and msg file
    >> py spammer -a whatsapp               # Webapp and it's own msg file
    >> py spammer -a whatsapp -f msg.txt    # Webapp and specific msg file

    Calibrating Web Apps:
    >> py spammer -c                         # Default webapp and msg file
    >> py spammer -c -a whatsapp             # Calibrate app, old msg file
    >> py spammer -c -a whatsapp -f msg.txt  # Webapp and set new msg file

    Testing Calibration:
    >> py spammer -t                         # Test default webapp
    >> py spammer -t -a whatsapp             # Test specific webapp
    """

    if test_mode:
        # Test calibrations and exit gracefully
        cb = Calibration(app, mfile)
        click.echo(f'Testing calibration for {cb.app_name.title()}...')
        cb.test_calibration(show_switch_prompt=True)
        sys.exit(0)

    if calibrate:
        # Calibrate web app and exit gracefully
        cb = Calibration(app, mfile)
        click.echo(f'Calibrating {cb.app_name.title()}...')
        cb.calibrate()
        sys.exit(0)

    # Spammer object
    spm = Spammer(app, mfile)
    gui.alert(
        f'Please switch to {spm.app_name.title()}\'s chat window and '
        'select a contact.')
    click.echo(
        f'Sleeping for {settings.INITIAL_SLEEP_SECS} seconds, switch '
        'to the web-app in the meantime...')
    time.sleep(settings.INITIAL_SLEEP_SECS)

    confirm = gui.confirm(
        'Make sure a contact is selected before proceeding.\nTry not to '
        'move the mouse cursor once you confirm. \nContinue ?')
    assert 'Cancel' not in confirm, "Spamming Aborted !"

    time.sleep(1.5)
    spm.send_messages()
