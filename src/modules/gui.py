"""User friendly GUI to interact with Auto Maple."""

import time
import threading
import tkinter as tk
import pywinstyles
import ctypes
from tkinter import ttk
from src.common import config, settings
from src.gui import Menu, View, Edit, Settings


class GUI:
    DISPLAY_FRAME_RATE = 30
    RESOLUTIONS = {
        'DEFAULT': '780x860',
        'Edit': '1400x800'
    }

    def __init__(self):
        config.gui = self
        self.root = tk.Tk()

        appId = 'automaple.v2'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appId)

        self.root.title('Auto Maple v2')
        self.root.iconbitmap('assets/ico.ico')
        self.root.geometry(GUI.RESOLUTIONS['DEFAULT'])
        self.root.resizable(True, True)
        self.root.config(borderwidth=5)
        self.root.config(background='gray10')
        self.root.config(relief=tk.FLAT)
        self.root.config(cursor='diamond_cross')

        # Initialize GUI variables
        self.routine_var = tk.StringVar()

        # Build the GUI
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        style = ttk.Style()
        style.theme_use("default")

        # Notebook Style
        style.configure('TNotebook', background='gray13')
        style.configure('TNotebook.Tab', background='gray13', foreground='white')
        style.map('TNotebook.Tab',background=[("selected",'#0d98ba')])

        self.navigation = ttk.Notebook(self.root)

        self.view = View(self.navigation)
        self.edit = Edit(self.navigation)
        self.settings = Settings(self.navigation)

        self.navigation.pack(expand=True, fill='both')
        self.navigation.bind('<<NotebookTabChanged>>', self._resize_window)

        pywinstyles.change_header_color(self.root, color="#2f2c2c")  
        pywinstyles.change_title_color(self.root, color="#AFEEEE") 
        pywinstyles.change_border_color(self.root, color="#AFEEEE")

        self.root.focus()

    def set_routine(self, arr):
        self.routine_var.set(arr)

    def clear_routine_info(self):
        """
        Clears information in various GUI elements regarding the current routine.
        Does not clear Listboxes containing routine Components, as that is handled by Routine.
        """

        self.view.details.clear_info()
        self.view.status.set_routine('')

        self.edit.minimap.redraw()
        self.edit.routine.commands.clear_contents()
        self.edit.routine.commands.update_display()
        self.edit.editor.reset()

    def _resize_window(self, e):
        """Callback to resize entire Tkinter window every time a new Page is selected."""

        nav = e.widget
        curr_id = nav.select()
        nav.nametowidget(curr_id).focus()      # Focus the current Tab
        page = nav.tab(curr_id, 'text')
        if self.root.state() != 'zoomed':
            if page in GUI.RESOLUTIONS:
                self.root.geometry(GUI.RESOLUTIONS[page])
            else:
                self.root.geometry(GUI.RESOLUTIONS['DEFAULT'])

    def start(self):
        """Starts the GUI as well as any scheduled functions."""

        display_thread = threading.Thread(target=self._display_minimap)
        display_thread.daemon = True
        display_thread.start()

        layout_thread = threading.Thread(target=self._save_layout)
        layout_thread.daemon = True
        layout_thread.start()

        self.root.mainloop()

    def _display_minimap(self):
        delay = 1 / GUI.DISPLAY_FRAME_RATE
        while True:
            self.view.minimap.display_minimap()
            time.sleep(delay)

    def _save_layout(self):
        """Periodically saves the current Layout object."""

        while True:
            if config.layout is not None and settings.record_layout:
                config.layout.save()
            time.sleep(5)


if __name__ == '__main__':
    gui = GUI()
    gui.start()
