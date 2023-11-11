import tkinter as tk
from src.gui.interfaces import LabelFrame
from src.modules.listener import Listener


class Status(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Status', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.curr_cb = tk.StringVar()
        self.curr_routine = tk.StringVar()
        self.curr_st = tk.StringVar()
        self.curr_st.set('Start')

        self.cb_label = tk.Label(self, text='Command Book:')
        self.cb_label.grid(row=0, column=1, padx=5, pady=(5, 0), sticky=tk.E)
        self.cb_entry = tk.Entry(self, textvariable=self.curr_cb, state=tk.DISABLED)
        self.cb_entry.grid(row=0, column=2, padx=(0, 5), pady=(5, 0), sticky=tk.EW)

        self.r_label = tk.Label(self, text='Routine:')
        self.r_label.grid(row=1, column=1, padx=5, pady=(0, 5), sticky=tk.E)
        self.r_entry = tk.Entry(self, textvariable=self.curr_routine, state=tk.DISABLED)
        self.r_entry.grid(row=1, column=2, padx=(0, 5), pady=(0, 5), sticky=tk.EW)

        self.routine_enabled = False
        self.st_entry = tk.Button(self, textvariable=self.curr_st, state='disabled', command=self.toggle)
        self.st_entry.grid(row=2, column=2, padx=(0, 5), pady=(0, 5), sticky=tk.EW)
        print(self.curr_cb.get())
    
    def toggle(self):
        self.routine_enabled = not self.routine_enabled
        self.update_toggle_state()
        Listener.toggle_enabled()

    def set_cb(self, string):
        self.curr_cb.set(string)
        self.update_toggle_state()

    def set_routine(self, string):
        self.curr_routine.set(string)
        self.update_toggle_state()
    
    def update_toggle_state(self):
        if (len(self.curr_cb.get()) and len(self.curr_routine.get())):
            self.st_entry.config(state='normal')
        if (self.routine_enabled):
            self.curr_st.set('Stop')
            self.st_entry.config(state='active')
        else:
            self.curr_st.set('Start')
            self.st_entry.config(state='normal')
