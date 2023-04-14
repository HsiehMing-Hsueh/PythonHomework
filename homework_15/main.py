import datasource
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.simpledialog import askinteger,askstring
from PIL import Image, ImageTk
from messageWindow import MapDisplay
from tkinter.simpledialog import Dialog

sbi_numbers = 3
bemp_numbers = 3
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立一個menu
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        #建立選項menu
        self.command_menu = tk.Menu(self.menubar)
        self.command_menu.add_command(label="設定",command=self.menu_setting_click)
        self.command_menu.add_command(label="離開", command=self.destroy)
        self.menubar.add_cascade(label="選項", menu=self.command_menu)
        #建立搜尋menu
        self.search_menu = tk.Menu(self.menubar)
        self.search_menu.add_command(label="搜尋",command=self.search_site_Total)
        self.menubar.add_cascade(label="搜尋站點",menu=self.search_menu)

        #建立mainFrame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30,pady=50)
        # ----------------建立logo--------------------
        logoImage = Image.open('./image/bicycle.png')
        resizeImage = logoImage.resize((100,100), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame, image=self.logoTkimage)
        logoLabel.pack(pady=(0,50))

        #建立top_wrapperFrame
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)
        # 建立行政區的topFrame
        topFrame = ttk.LabelFrame(top_wrapperFrame, text="台北市行政區")
        # 建立(多選一選項)的事件
        self.radioStringVar = tk.StringVar()
        # 取得行政區的名稱
        length = len(datasource.sarea_list)
        for i in range(length):
            cols = i % 3
            rows = i // 3
            ttk.Radiobutton(topFrame, text=datasource.sarea_list[i],value=datasource.sarea_list[i], variable=self.radioStringVar, command=self.radio_Event).grid(
                column=cols, row=rows, sticky=tk.W, padx=10, pady=10)
        topFrame.pack(side=tk.LEFT)
        # 預設選項選擇為信義區
        self.radioStringVar.set('信義區')
        self.area_data = datasource.getInfoFromArea('信義區')
        # 建立sbi_warningFrame開始-----------------------------
        self.sbi_warningFrame = ttk.LabelFrame(top_wrapperFrame, text="可借目前不足站點")
        columns = ('#1', '#2', '#3')
        self.sbi_tree = ttk.Treeview(self.sbi_warningFrame, columns=columns, show='headings')
        self.sbi_tree.heading('#1', text='站點')
        self.sbi_tree.column("#1", minwidth=0, width=200)
        self.sbi_tree.heading('#2', text='可借')
        self.sbi_tree.column("#2", minwidth=0, width=30)
        self.sbi_tree.heading('#3', text='可還')
        self.sbi_tree.column("#3", minwidth=0, width=30)
        self.sbi_tree.pack(side=tk.LEFT)
        self.sbi_warning_data = datasource.filter_sbi_warning_data(self.area_data, sbi_numbers)

        sbi_sites_numbers = len(self.sbi_warning_data)
        self.sbi_warningFrame.configure(text=f"可借不足站點數:{sbi_sites_numbers}")
        for item in self.sbi_warning_data:
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']],tags=item['sna'])
        self.sbi_warningFrame.pack(side=tk.LEFT)
        # 建立sbi_warningFrame結束-----------------------------

        # 建立bemp_warningFrame開始----------------------------
        self.bemp_warningFrame = ttk.LabelFrame(top_wrapperFrame, text="可還目前不足站點")
        columns = ('#1', '#2', '#3')
        self.bemp_tree = ttk.Treeview(self.bemp_warningFrame, columns=columns, show='headings')
        self.bemp_tree.heading('#1', text='站點')
        self.bemp_tree.column("#1", minwidth=0, width=200)
        self.bemp_tree.heading('#2', text='可借')
        self.bemp_tree.column("#2", minwidth=0, width=30)
        self.bemp_tree.heading('#3', text='可還')
        self.bemp_tree.column("#3", minwidth=0, width=30)
        self.bemp_tree.pack(side=tk.LEFT)
        self.bemp_warning_data = datasource.filter_bemp_warning_data(self.area_data, bemp_numbers)

        bemp_sites_numbers = len(self.bemp_warning_data)
        self.bemp_warningFrame.configure(text=f"可還不足站點數:{bemp_sites_numbers}")
        for item in self.bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']], tags=item['sna'])
        self.bemp_warningFrame.pack(side=tk.LEFT)
        # 建立bemp_warningFrame結束----------------------------

        # 建立bottomFrame裝Treeview-------------------
        now = datetime.datetime.now()
        #建立現在時刻
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame = ttk.LabelFrame(mainFrame, text=f"信義區-{nowString}")
        self.bottomFrame.pack()
        #建立Treeview
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
        self.tree = ttk.Treeview(self.bottomFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='站點')
        self.tree.column("#1", minwidth=0, width=200)
        self.tree.heading('#2', text='時間')
        self.tree.column("#2", minwidth=0, width=200)
        self.tree.heading('#3', text='總車數')
        self.tree.column("#3", minwidth=0, width=50)
        self.tree.heading('#4', text='可借')
        self.tree.column("#4", minwidth=0, width=30)
        self.tree.heading('#5', text='可還')
        self.tree.column("#5", minwidth=0, width=30)
        self.tree.heading('#6', text='地址')
        self.tree.column("#6", minwidth=0, width=250)
        self.tree.heading('#7', text='狀態')
        self.tree.column("#7", minwidth=0, width=30)
        self.tree.pack(side=tk.LEFT)
        #tree,addItem
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']],tags=item['sna'])
        # self.tree bind event
        self.tree.bind('<<TreeviewSelect>>', self.treeSelected)
        #幫treeview加scrollbar------------------------------------------------
        scrollbar = ttk.Scrollbar(self.bottomFrame, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
        #可借的卷軸
        sbi_scrollbar = ttk.Scrollbar(self.sbi_warningFrame, command=self.sbi_tree.yview)
        sbi_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sbi_tree.config(yscrollcommand=sbi_scrollbar.set)
        #可還的卷軸
        bemp_scrollbar = ttk.Scrollbar(self.bemp_warningFrame, command=self.bemp_tree.yview)
        bemp_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bemp_tree.config(yscrollcommand=bemp_scrollbar.set)
    #tree的event
    def treeSelected(self, event):
        selectedTree = event.widget
        if len(selectedTree.selection()) == 0: return
        itemTag = selectedTree.selection()[0]
        itemDic = selectedTree.item(itemTag)
        siteName = itemDic['tags'][0]
        for item in self.area_data:
            if siteName == item['sna']:
                selectd_data = item
                break
        
        # 顯示地圖window
        mapDisplay = MapDisplay(self,selectd_data)
        
    def search_site_Total(self):
        #建立KeyInWord的askstring
        KeyInWord = askstring("請輸入關鍵字", "ex:信義區")
        #刪除tree裡面的資料
        for item in self.tree.get_children():
            self.tree.delete(item)
        #增加關鍵字的資料到tree裡面
        for item in self.area_data:
            if KeyInWord in item['sna'] or KeyInWord in item['ar']:
                self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])
        #sbi_warnign_data
        for item in self.sbi_tree.get_children():
            self.sbi_tree.delete(item)
        sbi_sites_numbers = 0
        for item in self.sbi_warning_data:
            if KeyInWord in item['sna']:
                self.sbi_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']], tags=item['sna'])
                sbi_sites_numbers += 1
            self.sbi_warningFrame.configure(text=f"可借不足站點數:{sbi_sites_numbers}")
        
        for item in self.bemp_tree.get_children():
            self.bemp_tree.delete(item)
        bemp_site_number = 0
        for item in self.bemp_warning_data:
            if KeyInWord in item['sna']:
                self.bemp_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']], tags=item['sna'])
                bemp_site_number += 1
            self.bemp_warningFrame.configure(text=f"可還不足站點數:{bemp_site_number}")

    '''
    def search_site_sbi(self):
        #刪除sbi_tree裡面的資料
        for item in self.sbi_tree.get_children():
            self.sbi_tree.delete(item)
        #增加關鍵字的資料到sbi_tree裡面
        for item in self.sbi_warning_data :
            if KeyInWord in item['sna']:
                self.sbi_tree.insert('', tk.END, [item['sna'][11:], item['sbi'], item['bemp']])
    '''
    
    def menu_setting_click(self):
        global sbi_numbers,bemp_numbers
        retVal = askinteger("目前設定不足數量為","請輸入不足可借可還數量",minvalue=0,maxvalue=5)
        sbi_numbers =retVal
        bemp_numbers =retVal
    #
    def radio_Event(self):
        #抓按下去的時間
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        #刪除資料
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in self.sbi_tree.get_children():
            self.sbi_tree.delete(item)

        for item in self.bemp_tree.get_children():
            self.bemp_tree.delete(item)

        area_name = self.radioStringVar.get()
        #顯示名稱與時間
        self.bottomFrame.config(text=f"{area_name}-{nowString}")
        self.area_data = datasource.getInfoFromArea(area_name)
        #篩選可借站點數並顯示
        self.sbi_warning_data = datasource.filter_sbi_warning_data(self.area_data, sbi_numbers)
        sbi_site_numbers = len(self.sbi_warning_data)
        self.sbi_warningFrame.config(text=f"可借不足站點數:{sbi_site_numbers}")
        #篩選可還站點數並顯示
        self.bemp_warning_data = datasource.filter_bemp_warning_data(self.area_data, bemp_numbers)
        bemp_site_numbers = len(self.bemp_warning_data)
        self.bemp_warningFrame.configure(text=f"可還不足站點數:{bemp_site_numbers}")
        #建立資料顯示
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])

        for item in self.sbi_warning_data:
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])

        for item in self.bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])
        
# 主程式
def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()


if __name__ == "__main__":
    main()
