""" 專案在學習grid的編排 """
import tkinter as tk
from tkinter import ttk
import re
from PIL import Image , ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle =ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame',background='red')
        ttkStyle.configure('white.TFrame',background='white')
        ttkStyle.configure('yellow.TFrame',background='yellow')
        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', '16'),foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', '16'),foreground='#333333')

        mainFrame = ttk.Frame(self)
        #ttk.Label(mainFrame,text='BMI試算').pack()
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
    
        #上面的Frame
        topFrame = ttk.Frame(mainFrame,height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame,text="BMI試算",font=('Helvetica', '16')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True,fill=tk.BOTH)
        #下面的Frame的間格
        bottomFrame.columnconfigure(0,weight=3,pad=20)
        bottomFrame.columnconfigure(1,weight=5,pad=20)
        bottomFrame.rowconfigure(0,weight=1,pad=20)
        bottomFrame.rowconfigure(3, weight=1, pad=20)
        bottomFrame.rowconfigure(4, weight=1, pad=20)
        bottomFrame.rowconfigure(5, weight=1, pad=20)
        bottomFrame.rowconfigure(6, weight=1, pad=20)

        #定義Entry的textvariable
        self.nameStringVar = tk.StringVar()
        self.birthStringVar = tk.StringVar()
        self.heightIntVar = tk.IntVar()
        self.weightIntVar = tk.IntVar()
        #姓名欄位
        ttk.Label(bottomFrame,text="姓名:",style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E)
        self.nameEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry',textvariable=self.nameStringVar)
        self.nameEntry.grid(column=1,row=0,sticky=tk.W,padx=10)

        #出生年月日欄位
        ttk.Label(bottomFrame,text="出生年月日:",style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        ttk.Label(bottomFrame,text="(2000/03/01)",style='gridLabel.TLabel').grid(column=0,row=2,sticky=tk.E)
        self.birthEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry',textvariable=self.birthStringVar)
        self.birthEntry.grid(column=1, row=1, sticky=tk.W, rowspan=2, padx=10)

        #身高欄位
        ttk.Label(bottomFrame,text="身高(cm):",style='gridLabel.TLabel').grid(column=0,row=3,sticky=tk.E)
        self.heightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry',textvariable=self.heightIntVar)
        self.heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)

        #體重欄位
        ttk.Label(bottomFrame,text="體重(kg):",style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        self.weightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry',textvariable=self.weightIntVar)
        self.weightEntry.grid(column=1, row=4, sticky=tk.W, padx=10)

        #訊息顯示區域
        self.messageText = tk.Text(bottomFrame,height=5,width=35,state=tk.DISABLED)
        self.messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)
        #-------------commitFrame開始------------------------
        commitFrame =ttk.Button(bottomFrame)
        commitFrame.grid(column=0,row=6,columnspan=2)
        commitFrame.columnconfigure(0,pad=5)

        #計算鍵
        commitBtn = ttk.Button(commitFrame,text="計算BMI",command=self.check_value)
        commitBtn.grid(column=0,row=0)
        #清除鍵
        clearBtn = ttk.Button(commitFrame,text="清除欄位",command=self.clear_text)
        clearBtn.grid(column=1,row=0)
        #-------------commitFrame結束------------------------
        
    #印出訊息在訊息顯示區
    def print_message(self):
        message = f"{self.nameValue}您好:\n"
        message += f"出生年月日:{self.birthValue}\n"
        message += f"貴庚:"
        message += f"星座為:"
        message += "BMI:"

    #BMI計算
    def BMI(self,weight,height):
        bmi = weight // (height/100) ** 2
        if bmi < 18.5:
            message="太輕"
        elif bmi < 24:
            message="正常"
        elif bmi < 27:
            message="過重"
        elif bmi < 30:
            message="輕度肥胖"
        elif bmi < 35:
            message="中度肥胖"
        else:
            message="重度肥胖"
        return message
    #檢查輸入的值
    def check_value(self):
        dateRegex = re.compile(r"^\d\d\d\d/\d\d/\d\d$")
        self.nameValue = self.nameStringVar.get()
        self.birthValue = self.birthStringVar.get()
        birthMatch = re.match(dateRegex,self.birthValue)
        if  birthMatch is None:            
            self.birthValue = ""

        try:
            self.heightValue = self.heightIntVar.get()
        except:
            self.heightValue = 0

        try:
            self.weightValue = self.weightIntVar.get()
        except:
            self.weightValue =  0
        
        if self.nameValue == "" or self.birthValue == "" or self.heightValue == 0 or self.weightValue == 0 :            
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0",tk.END)
            self.messageText.insert(tk.END,"有欄位沒填或格式不正確")
            self.messageText.configure(state=tk.DISABLED)
        else:
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0",tk.END)
            self.messageText.insert(tk.END,"???" )
            self.messageText.configure(state=tk.DISABLED)
        
    #清除輸入的值
    def clear_text(self):
        self.nameStringVar.set("")
        self.birthStringVar.set("")
        self.heightIntVar.set(0)
        self.weightIntVar.set(0)
        self.messageText.configure(state=tk.NORMAL)        
        self.messageText.delete("1.0",tk.END)
        self.messageText.configure(state=tk.DISABLED)

def close_window(w):
    w.destroy()

def main():
    
    """ 這是執行點 """
    window = Window()
    window.title("BMI計算")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW",lambda:close_window(window))
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()