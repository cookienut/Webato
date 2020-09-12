"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file serves as the entry point for trigerring spammer script through CLI.
Try ``spammer --help`` for more details.
"""

from utils import cli

try:
    cli.main()
except Exception as ex:
    print(f'Error: {ex}')
