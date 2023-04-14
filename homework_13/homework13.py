""" 專案在學習grid的編排 """
import tkinter as tk
from tkinter import ttk
import re
from PIL import Image , ImageTk
import datetime

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle =ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('blue.TFrame',background='blue')
        ttkStyle.configure('white.TFrame',background='white')
        ttkStyle.configure('green.TFrame',background='green')
        ttkStyle.configure('lightblue.TLabel',background='lightblue')
        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', '16'),foreground='#666666',background='lightgreen')
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', '16'),foreground='#666666',)
        

        mainFrame = ttk.Frame(self)
        #ttk.Label(mainFrame,text='BMI試算').pack()
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
    
        #上面的Frame
        topFrame = ttk.Frame(mainFrame,height=100,style='blue.TFrame')
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame,text="BMI試算",font=('Helvetica', '16'),style='lightblue.TLabel').pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame,style='green.TFrame')
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
        self.messageText = tk.Text(bottomFrame,height=6,width=35,state=tk.DISABLED)
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

        #建立Logo
        logoImage = Image.open('./Image/BMI_Pic.png')
        resizeImage = logoImage.resize((50,50),Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(self,image=self.logoTkimage,width=50)
        logoLabel.place(x=40,y=40)
        

    #BMI計算
    def BMI_c(self):
        self.bmi = self.weightValue // (self.heightValue/100) ** 2
        if self.bmi < 18.5:
            return"太輕"
        elif 18.5 < self.bmi < 24:
            return"正常"
        elif 24 < self.bmi < 27:
            return"過重"
        elif 27< self.bmi < 30:
            return"輕度肥胖"
        elif 30< self.bmi < 35:
            return"中度肥胖"
        else:
            return"重度肥胖"
        
    #傳出訊息
    def print_message(self):
        message = f"{self.nameValue}您好:\n"
        message += f"出生年月日:{self.birthValue}\n"
        message += f"貴庚為:{self.age}歲\n"
        message += f"星座為:{self.star_sign}\n"
        message += f"BMI:{self.bmi}\n"
        message += f"你的BMI值是:{self.bmi_message}哦~\n"

    #檢查輸入的值
    def check_value(self):
        dateRegex = re.compile(r"^\d\d\d\d/\d\d/\d\d$")
        self.nameValue = self.nameStringVar.get()
        self.birthValue = self.birthStringVar.get()
        birthMatch = re.match(dateRegex,self.birthValue)
        #計算年齡
        Now = datetime.datetime.today().date()
        birthday = datetime.date(int(self.birthValue[0:4]), int(self.birthValue[5:7]), int(self.birthValue[8:]))
        age_delta = Now - birthday 
        age_date = datetime.date(1,1,1) + age_delta
        self.age = (int(age_date.isoformat()[:4])-1) 
        

        #判斷星座
        birth_mo_day = int(self.birthValue[5:7]), int(self.birthValue[8:])
        print(birth_mo_day)
        self.star_sign = ""
        if birth_mo_day[0] == 3 and birth_mo_day[1] <= 20:
            self.star_sign = "雙魚座（Pisces）02/20~3/20"
        if birth_mo_day[0] == 2 and birth_mo_day[1] >= 20:
            self.star_sign = "雙魚座（Pisces）02/20~3/20"
        if birth_mo_day[0] == 4 and birth_mo_day[1] <= 20:
            self.star_sign = "牡羊座（Aries）03/21 ~ 04/20"
        if birth_mo_day[0] == 3 and birth_mo_day[1] >= 21:
            self.star_sign = "牡羊座（Aries）03/21 ~ 04/20"
        if birth_mo_day[0] == 5 and birth_mo_day[1] <= 21:
            self.star_sign = "金牛座（Taurus）04/21 ~ 05/21"
        if birth_mo_day[0] == 4 and birth_mo_day[1] >= 21:
            self.star_sign = "金牛座（Taurus）04/21 ~ 05/21"
        if birth_mo_day[0] == 6 and birth_mo_day[1] <= 21:
            self.star_sign = "雙子座（Gemini）05/22 ~ 06/21"
        if birth_mo_day[0] == 5 and birth_mo_day[1] >= 22:
            self.star_sign = "雙子座（Gemini）05/22 ~ 06/21"
        if birth_mo_day[0] == 7 and birth_mo_day[1] <= 22:
            self.star_sign = "巨蟹座（Cancer）06/22 ~ 07/22"
        if birth_mo_day[0] == 6 and birth_mo_day[1] >= 22:
            self.star_sign = "巨蟹座（Cancer）06/22 ~ 07/22"
        if birth_mo_day[0] == 8 and birth_mo_day[1] <= 23:
            self.star_sign = "獅子座（Leo）07/23 ~ 08/23"
        if birth_mo_day[0] == 7 and birth_mo_day[1] <= 23:
            self.star_sign = "獅子座（Leo）07/23 ~ 08/23"
        if birth_mo_day[0] == 9 and birth_mo_day[1] <= 23:
            self.star_sign = "處女座（Virgo）8/24~09/23"
        if birth_mo_day[0] == 8 and birth_mo_day[1] >= 24:
            self.star_sign = "處女座（Virgo）8/24~09/23"
        if birth_mo_day[0] == 10 and birth_mo_day[1] <= 23:
            self.star_sign = "天秤座（Libra）09/24~10/23"
        if birth_mo_day[0] == 9 and birth_mo_day[1] >= 24:
            self.star_sign = "天秤座（Libra）09/24~10/23"
        if birth_mo_day[0] == 11 and birth_mo_day[1] <= 22:
            self.star_sign = "天蠍座（Scorpio）10/24~11/22"
        if birth_mo_day[0] == 10 and birth_mo_day[1] >= 24:
            self.star_sign = "天蠍座（Scorpio）10/24~11/22"
        if birth_mo_day[0] == 12 and birth_mo_day[1] <= 21:
            self.star_sign = "射手座（Sagittarius）11/23~12/21"
        if birth_mo_day[0] == 11 and birth_mo_day[1] >= 23:
            self.star_sign = "射手座（Sagittarius）11/23~12/21"
        if birth_mo_day[0] == 1 and birth_mo_day[1] <= 20:
            self.star_sign = "摩羯座（Capricorn）12/22~01/20"
        if birth_mo_day[0] == 12 and birth_mo_day[1] >= 22:
            self.star_sign = "摩羯座（Capricorn）12/22~01/20"
        if birth_mo_day[0] == 2 and birth_mo_day[1] <= 19:
            self.star_sign = "水瓶座（Aquarius）01/21~2/19"
        if birth_mo_day[0] == 1 and birth_mo_day[1] >= 21:
            self.star_sign = "水瓶座（Aquarius）01/21~2/19"
        
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
        
        # BMI計算
        self.bmi = self.weightValue // (self.heightValue/100) ** 2
        if self.bmi < 18.5:
            self.bmi_message = "太輕"
        if 18.5<self.bmi < 24:
            self.bmi_message = "正常"
        if self.bmi < 27:
            self.bmi_message = "過重"
        if self.bmi < 30:
            self.bmi_message = "輕度肥胖"
        if self.bmi < 35:
            self.bmi_message = "中度肥胖"
        if self.bmi >= 35:
            self.bmi_message = "重度肥胖"

        #檢查值是否有值，否則傳出訊息
        if self.nameValue == "" or self.birthValue == "" or self.heightValue == 0 or self.weightValue == 0 :            
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0",tk.END)
            self.messageText.insert(tk.END,"有欄位沒填或格式不正確")
            self.messageText.configure(state=tk.DISABLED)
        else:
            message = f"{self.nameValue}您好:\n"
            message += f"出生年月日:{self.birthValue}\n"
            message += f"貴庚為:{self.age}歲\n"
            message += f"星座為:{self.star_sign}\n"
            message += f"BMI:{self.bmi}\n"
            message += f"你的BMI值是:{self.bmi_message}哦~\n"

            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0",tk.END)
            self.messageText.insert(tk.END,message)
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
#關閉視窗能做甚麼事
def close_window(w):
    w.destroy()

def main():
    
    """ 這是執行點 """
    window = Window()
    window.title("BMI計算")
    #固定視窗
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW",lambda:close_window(window))
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()