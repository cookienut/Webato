*******
Spammer
*******

Spammer is a fun cross-platform message spamming suite written in python using PyAutoGUI module. It provides CLI options to leverage GUI automation in order to send text messages to your friends, from a message file, over any web application.

``Spammer`` comes with a bunch of features. It provides CLI options for caliberating any web application for sending messages and an interactive platform in the form of confirmation and alert boxes. Besides, these caliberations are saved for future, so it's a one time affair. It leverages the features of ``PyAutoGUI`` to automate mouse clicks and key presses on keyboard in order to type in texts and send them over any web app.

Installation
------------

* For installation , create a virtual environment or directly use:
.. code-block:: text

    $ pip3 install -r requirements.txt

The ``PyAutoGUI`` module may have a few additional dependencies based on the platform it's being used on.

* For `Windows` there are no additional dependencies.
* For `Mac`, first install ``pyobjc-core`` and ``pyobjc`` modules:
.. code-block:: text

    $ pip3 install pyobjc-core
    $ pip3 install pyobjc

* For `Linux`, the only dependency is `python3-xlib` module.
.. code-block:: text

    $ pip3 install python3-xlib

Settings
--------

The parameters in ``settings.py`` are configurable. For example -

.. code-block:: text

    DEFAULT_APP = "whatsapp"        # Spammer uses caliberations of this default app, if no app is specified when Spammer is run
    INITIAL_SLEEP_SECS = 10         # Seconds given to switch to web app from terminal, after this spamming will start
    CALIBERATION_SLEEP_SECS = 10    # Seconds given to switch to web app from terminal, after this caliberation will start
    LINE_BY_LINE_MESSGAGING = True  # Send each line from the message file as separate text, for more annoyance

Fail-safe
---------

Since the mouse and keyboard controls are automated here, it may prove chaotic if something goes wrong.
To avoid such a situation we rely of ``Fail-Safe feature of PyAutoGUI``. To terminate the Spammer execution at any point of time, move the ``mouse cursor to any of the four corners of the screen``. This will trigger the fail-safe feature and execution will stop immediately.

Usage
-----

Follow the below steps to use Spammer:

* Log in to any web application and select a contact to sent automated messages to.
* Some web apps have been pre-caliberated. Each web app uses a message file which can be found under ``messages`` folder (check ``config.json`` for more details). To know more about how to caliberate apps or test caliberations use:
.. code-block:: python

    $ python spammer/caliberate.py --help           # For more usage details, if needed

* Testing caliberations: Before you use Spammer, make sure you've tested caliberations for your webapp on your setup once:
.. code-block:: python

    $ python spammer/caliberate.py -t -a whatsapp   # whatsapp should be replaced with app that you're testing
    
* Caliberating web apps: If you are trying to caliberate a new web app or the existing caliberations are off, use:
.. code-block:: python

    $ python spammer/caliberate.py -a myApp -f messages.txt   # It'll caliberate myApp & use messages.txt to read messages

* Make sure the message file for the web-app exists under ``messages`` folder before you start the Spammer. If not, create it. The messages will be read from this file.

* To run Spammer, use:
.. code-block:: python

    $ python spammer                    # Starts spammer for DEFAULT_APP set in settings.py
    or
    $ python spammer -a instagram       # Starts spammer for specific app i.e. instagram
    or
    $ python spammer --help             # For more options or help

* The above command will initiate the Spammer. Switch to the web app, don't move mouse cursor and after a few seconds Spammer will take over. Enjoy and don't forget to have fun !
