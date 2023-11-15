import tkinter as tk

from src.common import settings
from src.gui.interfaces import *
from src.routine import components
from src.common.interfaces import Configurable


class InGame(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'In-game Settings', **kwargs)

        user_settings_row = Frame(self)
        user_settings_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)

        self.auto_maple_settings = InGameSettings('auto-maple')
        self.auto_change_channel = tk.BooleanVar(value=self.auto_maple_settings.get('auto_change_channel'))
        self.checkbox = Checkbutton(
            user_settings_row,
            variable=self.auto_change_channel,
            text='Auto Change Channel',
            command=self._on_check
        )
        self.checkbox.on_check(self.auto_change_channel)
        self.checkbox.pack()
    
    def _on_check(self):
        self.checkbox.on_check(self.auto_change_channel, self._on_change)

    def _on_change(self):
        self.auto_maple_settings.set('auto_change_channel', self.auto_change_channel.get())
        self.auto_maple_settings.save_config()

class InGameSettings(Configurable):
    DEFAULT_CONFIG = {
        'auto_change_channel': False,
    }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        assert key in self.config
        self.config[key] = value