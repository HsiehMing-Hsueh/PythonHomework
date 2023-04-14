import tkinter as tk
from tkinter import Button,Frame

class Window(tk.Tk):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        
        top_frame = Frame(self,bg="#ffffff")
        Button(top_frame,text="按鈕1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(top_frame,text="按鈕2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(top_frame,text="按鈕3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        top_frame.pack(expand=True,fill=tk.BOTH)

        middle_frame = Frame(self,bg="#ffffff")
        Button(middle_frame,text="按鈕4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(middle_frame,text="按鈕5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(middle_frame,text="按鈕6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        middle_frame.pack(expand=True,fill=tk.BOTH)

        button_frame = Frame(self,bg="#ffffff")
        Button(button_frame,text="按鈕7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(button_frame,text="按鈕8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(button_frame,text="按鈕9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button_frame.pack(expand=True,fill=tk.BOTH)

def main():
    window = Window()
    window.title("這是作業11的視窗")
    window.geometry("400x400")
    window.mainloop()
    
if __name__ == "__main__":
    main()