from ctypes import *
import threading
import time
import random, decimal

DD_CODE = {
    'left': 710,   # Arrow keys
    'up': 709,
    'right': 712,
    'down': 711,

    'backspace': 214,      # Special keys
    'tab': 300,
    'enter': 313,
    'shift': 500,
    'ctrl': 600,
    'alt': 602,
    'caps lock': 400,
    'esc': 100,
    'space': 603,
    'page up': 705,
    'page down': 708,
    'end': 707,
    'home': 704,
    'insert': 703,
    'delete': 706,

    '0': 210,      # Numbers
    '1': 201,
    '2': 202,
    '3': 203,
    '4': 204,
    '5': 205,
    '6': 206,
    '7': 207,
    '8': 208,
    '9': 209,

    'a': 401,      # Letters
    'b': 505,
    'c': 503,
    'd': 403,
    'e': 303,
    'f': 404,
    'g': 405,
    'h': 406,
    'i': 308,
    'j': 407,
    'k': 408,
    'l': 409,
    'm': 507,
    'n': 506,
    'o': 309,
    'p': 310,
    'q': 301,
    'r': 304,
    's': 402,
    't': 305,
    'u': 307,
    'v': 504,
    'w': 302,
    'x': 502,
    'y': 306,
    'z': 501,

    'f1': 101,     # Functional keys
    'f2': 102,
    'f3': 103,
    'f4': 104,
    'f5': 105,
    'f6': 106,
    'f7': 107,
    'f8': 108,
    'f9': 109,
    'f10': 110,
    'f11': 111,
    'f12': 112,
    'num lock': 810,
    'scroll lock': 701,

    ';': 410,      # Special characters
    '=': 212,
    ',': 508,
    '-': 211,
    '.': 509,
    '/': 510,
    '`': 200,
    '[': 311,
    '\\': 213,
    ']': 312,
    "'": 411
}

DD_DLL = windll.LoadLibrary('C:\\Users\\Garson\\Desktop\\auto-maple\\driver\\dd.32695\\dd32695.x64.dll')
st = DD_DLL.DD_btn(0) #DD Initialize
if st==1:
    print("OK Driver Loaded")
else:
    print("Driver Load Error")
    exit(101)

class DriverKey():
    def __init__(self):
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        self.start()
    
    def start(self):
        # Starts the DD thread
        print('\n[~] Started DriverKey')
        self.thread.start()
    
    def _main(self):
        self.driver = DD_DLL;
        self.key_down_queue = []
        self.key_up_queue = []
        while(True):
            for k in self.key_up_queue:
                self._key_up(k)
                self.key_up_queue.remove(k)
            for k in self.key_down_queue:
                self._key_down(k)
            time.sleep(0.03)
    
    def user_key_down(self, key):
        if not key in self.key_down_queue:
            self.key_down_queue.append(key)

    def user_key_up(self, key):
        if key in self.key_down_queue:
            self.key_down_queue.remove(key)
        self.key_up_queue.append(key)

    def _key_down(self, key):
        self.driver.DD_key(DD_CODE[key], 1) #1=down
        down_time = decimal.Decimal(random.random() / random.randint(1, 2))
        time.sleep(down_time);
        print(f"Down '{key}'")

    def _key_up(self, key): 
        self.driver.DD_key(DD_CODE[key], 2) #2=up
        print(f"Up '{key}'")
    
    #1==L.down, 2==L.up, 4==R.down, 8==R.up, 16==M.down, 32==M.up

    def _left_button_down(self):
        self.driver.DD_btn(1)

    def _left_button_up(self):
        self.driver.DD_btn(2)

    def _right_button_down(self):
        self.driver.DD_btn(4)

    def _right_button_up(self):
        self.driver.DD_btn(8)

    def _middle_button_down(self):
        self.driver.DD_btn(16)

    def _middle_button_up(self):
        self.driver.DD_btn(32)

    def _move_rel(self,x, y):
        self.driver.DD_movR(x, y)

    def _move_to(self,x, y):
        self.driver.DD_mov(x, y);

d_key = DriverKey();
d_key2 = DriverKey();
d_key._key_down('a');
d_key._key_up('a');

d_key._key_down('v');
d_key._key_up('v');