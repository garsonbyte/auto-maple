"""A module for simulating low-level keyboard and mouse key presses."""

import time
from src.common import utils, driver_key

from random import random

d_key = driver_key.DriverKey()

#################################
#           Functions           #
#################################
@utils.run_if_enabled
def key_down(key):
    """
    Simulates a key-down action. Can be cancelled by Bot.toggle_enabled.
    :param key:     The key to press.
    :return:        None
    """

    key = key.lower()
    d_key._key_down(key)


def key_up(key):
    """
    Simulates a key-up action. Cannot be cancelled by Bot.toggle_enabled.
    This is to ensure no keys are left in the 'down' state when the program pauses.
    :param key:     The key to press.
    :return:        None
    """
    key = key.lower()
    d_key._key_up(key)


@utils.run_if_enabled
def press(key, n, down_time=0.05, up_time=0.1):
    """
    Presses KEY N times, holding it for DOWN_TIME seconds, and releasing for UP_TIME seconds.
    :param key:         The keyboard input to press.
    :param n:           Number of times to press KEY.
    :param down_time:   Duration of down-press (in seconds).
    :param up_time:     Duration of release (in seconds).
    :return:            None
    """

    for _ in range(n):
        key_down(key)
        time.sleep(down_time * (0.8 + 0.4 * random()))
        key_up(key)
        time.sleep(up_time * (0.8 + 0.4 * random()))


@utils.run_if_enabled
def click(position, button='left'):
    """
    Simulate a mouse click with BUTTON at POSITION.
    :param position:    The (x, y) position at which to click.
    :param button:      Either the left or right mouse button.
    :return:            None
    """

    if button not in ['left', 'right']:
        print(f"'{button}' is not a valid mouse button.")
    else:
        d_key._move_to(position[0], position[1])
        if button == 'left':
            d_key._left_button_down()
            time.sleep(0.2 * random())
            d_key._left_button_up()
        else:
            d_key._right_button_down()
            time.sleep(0.2 * random())
            d_key._right_button_up()
