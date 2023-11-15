import tkinter as tk
from src.gui.interfaces import *
from src.modules.listener import Listener


class Status(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Status', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.curr_cb = tk.StringVar()
        self.curr_cb_display = tk.StringVar()
        self.curr_routine = tk.StringVar()
        self.curr_routine_display = tk.StringVar()
        self.curr_st = tk.StringVar()
        self.curr_st.set('Start')

        self.cb_label = Label(self, text='Command Book:')
        self.cb_label.grid(row=0, column=1, padx=5, pady=(5, 0), sticky=tk.E)
        self.cb_entry = Entry(self, textvariable=self.curr_cb_display, state=tk.DISABLED)
        self.cb_entry.grid(row=0, column=2, padx=(0, 5), pady=(5, 0), sticky=tk.EW)

        self.r_label = Label(self, text='Routine:')
        self.r_label.grid(row=1, column=1, padx=5, pady=(0, 5), sticky=tk.E)
        self.r_entry = Entry(self, textvariable=self.curr_routine_display, state=tk.DISABLED)
        self.r_entry.grid(row=1, column=2, padx=(0, 5), pady=(0, 5), sticky=tk.EW)

        self.routine_enabled = False
        self.st_entry = Button(self, textvariable=self.curr_st, state='disabled', command=self.toggle)
        self.st_entry.config(background='pale turquoise', foreground='misty rose')
        self.st_entry.grid(row=2, column=2, padx=(0, 5), pady=(0, 5), sticky=tk.EW)
    
    def toggle(self):
        self.routine_enabled = not self.routine_enabled
        self.update_toggle_state()
        Listener.toggle_enabled()

    def set_cb(self, string):
        self.curr_cb.set(string)
        self.curr_cb_display.set('  ' + string)
        self.cb_label.config(foreground='lime green')
        print(self.curr_cb.get())
        self.update_toggle_state()

    def set_routine(self, string):
        self.curr_routine.set(string)
        self.curr_routine_display.set('  ' + string)
        self.cb_label.config(foreground='lime green')
        self.update_toggle_state()
    
    def update_toggle_state(self):
        if (len(self.curr_cb.get()) and len(self.curr_routine.get())):
            self.st_entry.config(state='normal', background='lime green', activebackground='gray30', activeforeground='misty rose')
        if (self.routine_enabled):
            self.curr_st.set('Stop')
            self.st_entry.config(state='active', background='indian red')
        else:
            self.curr_st.set('Start')
            self.st_entry.config(state='normal', background='lime green', activebackground='gray30', activeforeground='misty rose')
