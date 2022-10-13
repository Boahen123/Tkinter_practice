import tkinter as tk

class ListboxExample:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        
        # frames to keep the first listbox and second Listbox
        self.left_frame = tk.Frame(self.root)
        self.right_frame = tk.Frame()
        
        # Create a Listbox widget
        self.listbox = tk.Listbox(self.left_frame, activestyle='underline', height=0, width=0, \
            selectmode=tk.EXTENDED)
        self.listbox.pack_configure(padx=10, pady=10)
        
        # Populate the Listbox with the data
        self.listbox.insert(0,'Monday')
        self.listbox.insert(1,'Tuesday')
        self.listbox.insert(2,'Wednesday')
        self.listbox.insert(3,'Thursday')
        self.listbox.insert(4,'Friday')
        self.listbox.insert(5,'Saturday')
        self.listbox.insert(tk.END,'Sunday')
        
        # Populate the second listbox using loops
        self.listbox2 = tk.Listbox(self.right_frame, height=0, width=0)
        # self.listbox2.pack(side='left')
        
        days = ('Monday', 'Tuesday', 'Wednesday', 'Friday', \
            'Saturday', 'Sunday')
        for day in days:
            self.listbox.insert(tk.END, day)
        
        # style the first line
        self.listbox.itemconfig(0, background='white', foreground='red', selectbackground='blue')
        # Line selected
        self.listbox.activate(3)
        
        # Pack the frames
        self.left_frame.pack(side='left')
        self.right_frame.pack()
        
        # Start the mainloop
        tk.mainloop()
        
    # Instantiate a ListboxExample class
if __name__=='__main__':
    listbox_example = ListboxExample()
        
        
        