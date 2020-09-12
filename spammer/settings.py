"""
Author: dev.sagarbhat@gmail.com (Sagar Bhat)
Github: @cookienut

This file contains the settings used by the application.
These settings can be updated to modify the behavior of application as needed.
"""

# Default webApp to run, if not explicitly specified
DEFAULT_APP = "whatsapp"

# Seconds for which the Spammer will wait before sending messages,
# in order to give user some time to switch to the webApp.
INITIAL_SLEEP_SECS = 7

# Seconds for which the Spammer will wait before starting calibration,
# in order to give user some time to switch to the webApp.
CALIBERATION_SLEEP_SECS = 7

# Send each line from the message file, as a separate
# text message (set to `True` for more annoyance ! )
LINE_BY_LINE_MESSGAGING = True
