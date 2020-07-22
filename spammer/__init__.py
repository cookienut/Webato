import platform

import click


class SpammerException(Exception):
    """
    Exception class for Spammer related Exceptions
    """
    pass


def get_version():
    """
    Echoes the ``python version`` on platform as well as ``Spammer version``.
    """
    click.echo(
        f'Python {platform.python_version()}\n'
        f'Spammer {__version__}\n'
    )

version_option = click.Option(
    ["--version"],
    help="Show the Spammer version",
    expose_value=False,
    callback=get_version,
    is_flag=True
)

__version__ = "0.0.1.dev"
