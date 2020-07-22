"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)

This file serves as the entry point for trigerring spammer script through CLI.
Try ``spammer --help`` for more details.
"""

import time

import click
import pyautogui as gui

import settings
from spammer import Spammer

@click.command()
@click.option(
    '-a', '--app', default='', help='Provide the webapp name',
    required=False)
@click.option(
    '-f', '--file', default='', help='Provide the message file name',
    required=False)
def main(app, file):
    """
    Runs ``Spammer`` as CLI command.

    Accepts optional arguments ``--app`` and ``--file`` to specify
    webapp and the message file respectively. If not specifed, uses default
    values. For example:

    >> python spammer                           # Default webapp and msg file
    >> python spammer -a whatsapp               # Webapp and it's own msg file
    >> python spammer -a whatsapp -f msg.txt    # Webapp and specific msg file
    """

    spm = Spammer(app, file)

    gui.alert(''
        f'Please switch to the {spm.app_name.title()}\'s chat window and '
        'select a contact.')
    click.echo(
        f'Sleeping for {settings.INITIAL_SLEEP_SECS} seconds, switch '
        'to the web-app in the meantime...')
    time.sleep(settings.INITIAL_SLEEP_SECS)

    confirm = gui.confirm(
        'Make sure a contact is selected before proceeding. Try not to '
        'move the mouse cursor once you click or press \'OK\'. Continue ?')
    assert 'Cancel' not in confirm, "Spamming Aborted !"

    time.sleep(1.5)
    spm.initiate_spamming()


try:
    main()
except Exception as ex:
    click.echo(f'Error: {ex}')
