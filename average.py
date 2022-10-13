# A program GUI to calculate the average of three test scores
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        # create the root window
        self.root = tk.Tk()
        
        # Create 5 frames to store the widgets
        self.test_frame1 = tk.Frame()
        self.test_frame2 = tk.Frame()
        self.test_frame3 = tk.Frame()
        self.avg_frame = tk.Frame()
        self.button_frame = tk.Frame()
        
        # variable to store the average value
        self.test_avg = tk.StringVar()
        
        # set the labels for frame 1
        self.label1 = tk.Label(self.test_frame1, text='Enter the score for test1: ')
        self.entry1 = tk.Entry(self.test_frame1, width=10)
        
        # pack the labels for frame 1
        self.label1.pack(side='left')
        self.entry1.pack(side='left')
        
        # set the labels for frame 2
        self.label2 = tk.Label(self.test_frame2, text='Enter the score for test2: ')
        self.entry2 = tk.Entry(self.test_frame2, width=10)
        
        # pack the labels for frame 2
        self.label2.pack(side='left')
        self.entry2.pack(side='left')
        
        # set the labels for frame 3
        self.label3 = tk.Label(self.test_frame3, text='Enter the score for test3: ')
        self.entry3 = tk.Entry(self.test_frame3, width=10)
        
        # pack the labels for frame 3
        self.label3.pack(side='left')
        self.entry3.pack(side='left')
        
        # set the labels for frame 4
        self.label4 = tk.Label(self.avg_frame, text='Average Value:')
        self.label5 = tk.Label(self.avg_frame, textvariable=self.test_avg, width=10, background='white')
        
        # pack the labels for frame 4
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        
        # set the labels for frame 5
        self.avg = tk.Button(self.button_frame, text='Average', command=self.average)
        self.quit = tk.Button(self.button_frame, text='Quit', command=self.root.destroy)
        
        # pack the labes for frame 5
        self.avg.pack(side='left')
        self.quit.pack(side='left')
        
        # pack all the frames
        self.test_frame1.pack()
        self.test_frame2.pack()
        self.test_frame3.pack()
        self.avg_frame.pack()
        self.button_frame.pack()
        
        self.root.title('Calculate Average')
        
        tk.mainloop()
        
    def average(self):
        ''' calculate the average '''
        try:
            if self.entry1.get() and self.entry2.get():
                if self.entry3.get():
                    summation = float(self.entry1.get()) + float(self.entry2.get()) + float(self.entry3.get())
                
                    # compute the average
                    avg = f'{summation/3.0:.3f}'
                    self.test_avg.set(avg)
                else:
                    messagebox.showerror('Empty Field','All or some of the input fields are empty')
            else:
                messagebox.showerror('Emptpy Field','All or some of the input fields are empty')
            
        except ValueError:
            messagebox.showerror('Invalid Input','Please enter the number in digits ONLY!')
        
if __name__=='__main__':
    mygui = MyGUI()
        
        
        
        
