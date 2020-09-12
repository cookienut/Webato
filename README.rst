***********************************
Spammer: A PyAutoGUI Sample Project
***********************************

A simple automation suite written in python 3 using PyAutoGUI library, for sending automated text messages over any web application. The aim of the project is to learn the basics of PyAutoGUI and create a simple yet fun project out of it.

``Spammer`` provides CLI options (using basics of ``click``) to leverage GUI automation to send text messages over any web application, from a message file. Apart from sending automated text messages, Spammer also provides CLI options to configure or calibrate a new web-app as well as to test these calibrations at any point of time.

Installation
------------

* For installation , create a virtual environment first, and then run :
.. code-block:: text

    $ pip3 install -r requirements.txt


Settings
--------

The parameters in ``settings.py`` are configurable. For example -

.. code-block:: text

    DEFAULT_APP = "whatsapp"        # If no app name is specified while running Spammer, it runs for this default app
    INITIAL_SLEEP_SECS = 10         # Seconds given to switch to web app from terminal, after this spamming starts
    CALIBERATION_SLEEP_SECS = 10    # Seconds given to switch to web app from terminal, after this calibration starts
    LINE_BY_LINE_MESSGAGING = True  # Send each line from the message file as separate text, for more annoyance

Fail-safe
---------

Since both the mouse and keyboard are taken over, losing control may prove problematic, if configred improperly.
To avoid such a situation we rely of ``Fail-Safe feature of PyAutoGUI``. To terminate the Spammer execution at any point of time, move the ``mouse cursor to any of the four corners of the screen``. This will trigger the fail-safe feature and execution will stop immediately.

Usage
-----

* Log in to any web application and select a contact. Whatsapp and Instagram web-apps are pre-configured, you may add more, if needed.

* To run Spammer, use either of the following:
.. code-block:: python

    $ py spammer                             # Starts Spammer for DEFAULT_APP set in settings.py
    or
    $ py spammer -a instagram                # Starts Spammer for specific app i.e. instagram
    or
    $ py spammer -a instagram -f msg.txt     # Starts Spammer for specific app and uses specified msg file


* Calibrating web apps: If you are calibering a new web app or the existing calibrations are incorrect, use:
.. code-block:: python

    $ py spammer -c -a whatsapp -f msg.txt   # It'll caliberate whatsapp & set msg.txt as the message file

** ``NOTE - Make sure the specified message file already exists under 'messages' folder before you start the Spammer. If not, create it. The messages will be read from this file.``

* Testing calibration: Before you use Spammer, make sure you test calibrations for a web-app on your setup atleast once, just to be sure:
.. code-block:: python

    $ py spammer -t -a whatsapp   # whatsapp should be replaced with app that you're testing

* For more help, use:
.. code-block:: python

    $ py spammer --help           # For more usage details, if needed

* There you have it. Automate, learn and don't forget to have fun !
