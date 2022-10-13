# making use the vertical and horizontal Scrollbars
import tkinter as tk

class ScrollBar:
    def __init__(self):
        # setup the root window
        self.root = tk.Tk()
        
        # set-up the outer frame
        self.outer_frame = tk.Frame()
        # inner frame nested in the outer frame
        self.inner_frame = tk.Frame(self.outer_frame)
        
        # pack the frames
        self.outer_frame.pack(padx=20, pady=20)
        self.inner_frame.pack()
        
        # Create the listbox in the inner frame, with the vertical scrollbar
        self.listbox = tk.Listbox(self.inner_frame)
        self.listbox.pack(side='left')
        
        # Populate the listbox
        items = ['He is going to school', 'I am learning GUI programming',
                 'I want to become a frontend Engineer',
                 'There are plenty fishes in the sea']
        for item in items:
            self.listbox.insert(tk.END, item)
            
        # Create the vertical scrollbar
        self.yscrollbar = tk.Scrollbar(self.inner_frame, orient="vertical")
        self.yscrollbar.pack(side="left", fill="y")
        # Configure yscrollbar to work with listbox
        self.yscrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.yscrollbar.set)
        
        # Create the horizontaal scrollbar
        self.xscrollbar = tk.Scrollbar(self.outer_frame, orient="horizontal", troughcolor='red', relief=
                                       'raised')
        self.xscrollbar.pack(side="bottom", fill="x")
        # Configure xscrollbar to work with listbox
        self.xscrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.xscrollbar.set)
        
        
        
        
        tk.mainloop()
        
if __name__=="__main__":
    myscrollbar = ScrollBar()