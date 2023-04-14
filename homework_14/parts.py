from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk

class TopFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #去除線條
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('TLabelframe',borderwidth=0)
        #建立花的圖
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        self.canvas = tk.Canvas(self, width=173, height=200)
        self.canvas.pack()
        self.canvas.create_image(0, 5, image=self.flowerPhoto1, anchor='nw')
        self.canvas.create_text(0, 200, text='Flower', fill='yellow',font=('verdana', 36), anchor='sw')
        #建立鑽石圖
        daimondImage1 = Image.open("./images/diamond.png")
        self.daimondPhoto1 = ImageTk.PhotoImage(daimondImage1)
        self.canvas.create_image(175, 5, image=self.daimondPhoto1, anchor='nw')
        #建立原子圖
        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        self.canvas.create_image(280, 5, image=self.atomPhoto1, anchor='nw')
        #建立scrollbar捲動軸
        self.scrollbar = ttk.Scrollbar(self,orient='horizontal',command=self.canvas.xview)
        self.scrollbar.pack(side='bottom',fill='x')
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=(0,0,500,200))

class MedianFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #換選項的圖示
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        #去除線條
        ttkStyle.configure('TLabelframe', borderwidth=0)
        #建立與window的連結(重要!!!)
        self.w = master
        #----------建立一個Frame(多選一選項)開始---------------
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT)
        #設一個字串的Var
        self.radioStringVar = tk.StringVar()
        #設radio的按鈕(多選一選項)
        self.radiobutton1 = ttk.Radiobutton(
            radionFrame, text='Option 1', variable=self.radioStringVar, value='red',command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(
            radionFrame, text='Option 2', variable=self.radioStringVar, value='green', command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(
            radionFrame, text='Option 3', variable=self.radioStringVar, value='blue', command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(
            radionFrame, text='Option 4', variable=self.radioStringVar, value='yellow', command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set('red')
        # ----------建立一個Frame(多選一選項)結束---------------
        #-----------------建立多選開始-------------------
        checkFrames = ttk.LabelFrame(self, text='Check Buttons')
        checkFrames.pack(side=tk.RIGHT, padx=10, pady=10)

        self.checkStringVar1 = tk.StringVar()
        self.checkStringVar2 = tk.StringVar()
        self.checkStringVar3 = tk.StringVar()
        self.checkStringVar4 = tk.StringVar()
        self.checkbutton1 = ttk.Checkbutton(
            checkFrames, text='Option 1', variable=self.checkStringVar1, command=self.checkEvent, onvalue='op1check',offvalue='1off')
        self.checkbutton1.pack()
        self.checkbutton2 = ttk.Checkbutton(
            checkFrames, text='Option 2', variable=self.checkStringVar2, command=self.checkEvent, onvalue='op2check', offvalue='2off')
        self.checkbutton2.pack()
        self.checkbutton3 = ttk.Checkbutton(
            checkFrames, text='Option 3', variable=self.checkStringVar3, command=self.checkEvent, onvalue='op3check', offvalue='3off')
        self.checkbutton3.pack()
        self.checkbutton4 = ttk.Checkbutton(
            checkFrames, text='Option 4', variable=self.checkStringVar4, command=self.checkEvent, onvalue='op4check', offvalue='4off')
        self.checkbutton4.pack()
        #------------------建立多選結束---------------------
    # 建立(多選一選項)的事件
    def radioEvent(self):
        self.w.radioButtonEventOfMedianFrame(self.radioStringVar.get())
    #建立(多選)的事件
    def checkEvent(self):
        print(self.checkStringVar1.get())
        print(self.checkStringVar2.get())
        print(self.checkStringVar3.get())
        print(self.checkStringVar4.get())

class BottomFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #新增w跟window做連結
        self.w = master
        listFrame = ttk.LabelFrame(self,text="List Box")
        listFrame.pack(side=tk.LEFT,padx=10,pady=10)
        list= tk.Listbox(listFrame,height=6,width=10)
        list.pack(side=tk.LEFT)
        #做month的list
        self.data = []
        for month in range(1,13):
            self.data.append(f"{month}月")
        for item in self.data:
            list.insert(tk.END,item)
        #做scrollBar放在listFrame
        scrollBar =ttk.Scrollbar(listFrame,command=list.yview)
        scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
        list.configure(yscrollcommand=scrollBar.set)

        list.bind('<<ListboxSelect>>',self.items_selected)
        #建立ComboBox的frame
        comboBoxFrame = ttk.LabelFrame(self,text="Combo Box")
        comboBoxFrame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.comboBoxValues = ('請選擇月份','January','February','March','April','May','June','July','August','September','October','November','December')
        #---------------建立ComboBox開始-----------------
        comboBox = ttk.Combobox(comboBoxFrame,state="readonly",width= 8)
        comboBox.pack()
        #combo box的
        comboBox['values'] =self.comboBoxValues
        comboBox.current(0)
        comboBox.bind('<<ComboboxSelected>>',self.month_changed)
        #----------------建立comboBox結束----------------

    #收集月份的data與window連結
    def items_selected(self,event):
        listbox = event.widget
        (selctedIndex,) = listbox.curselection()
        selectedValue = self.data[selctedIndex]
        self.w.listBoxEventOfBottomFrame(selectedValue)
    #收集value與window連結
    def month_changed(self,event):
        combobox = event.widget
        selectedIndex = combobox.current()
        selectedValue = self.comboBoxValues[selectedIndex]
        self.w.comboBoxEventOfBottomFrame(selectedValue)

        