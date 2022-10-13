# Trying to draw nigeria's flag and Ghana's flag
import tkinter as tk

class Flags:
    ''' Ghana and Nigeria's flag '''
    # root window
    def __init__(self):
        
        self.root = tk.Tk()
        self.nigeria_frame = tk.Frame(self.root)
        self.ghana_frame = tk.Frame(self.root)
        
        self.canvas = tk.Canvas(self.nigeria_frame, width=320, height=270) 
        
        # Starting with Nigeria's flag, create first green rectangle
        self.canvas.create_rectangle(2,2,320,90, fill='#1B7339')
        # Create the second white rectangle
        self.canvas.create_rectangle(2,90,320,180, fill='white')
        # Create the third green rectangle
        self.canvas.create_rectangle(2,180,320,270, fill='#1B7339')
        
        self.ghana_canvas = tk.Canvas(self.ghana_frame, width=320, height=270) 
        
        # Then to the Ghana flag, create first red rectangle
        self.ghana_canvas.create_rectangle(2,2,320,90, fill='#EF3340')
        # Create the second white rectangle
        self.ghana_canvas.create_rectangle(2,90,320,180, fill='#FFD100')
        # Create the third green rectangle
        self.ghana_canvas.create_rectangle(2,180,320,270, fill='#009739')
        # create the black star
        points = [160, 90, 126, 180, 160, 150, 192, 180, 160, 90]
        self.ghana_canvas.create_polygon(points)
        points2 = [100,120,222,120,160,150]
        self.ghana_canvas.create_polygon(points2)
        
        
        
        
        
        
        self.canvas.pack()
        self.nigeria_frame.pack(side='bottom')
        self.ghana_frame.pack(side='top')
        self.ghana_canvas.pack()
        
        
        self.root.title('Nigerian and Ghana flags')
        tk.mainloop()
    
if __name__=='__main__':
    flag = Flags()