import tkinter as tk

class Tk_GUI:
    def __init__(self,title):
        win = tk.Tk()
        self.win = win
        win.protocol("WM_DELETE_WINDOW",self.on_closeing)
        win.title(title)
        #win.minsize(width=400,height=400)
        label=tk.Label(win, text="為提供更優的操作體驗本軟體採用網頁呈現介面！\n如果您忘記連結可以直接複製底下的連結打開介面")   #建立標籤物件
        label.config(font=(None,10))
        label.pack()

        url_input = tk.Text(win,height=2,width=100)
        # url_input.
        url_input.pack()
        self.url_input = url_input

        label=tk.Label(win, text="關閉本視窗將會關閉所有程序")   #建立標籤物件
        label.pack()
        label.config(font=(None,10))


    def Start_Tk(self):
        self.win.mainloop()

    def on_closeing(self):
        print("EXIT GUI")
        self.win.destroy()


obj = Tk_GUI("Title")
obj.url_input.insert(tk.INSERT,"URL")
obj.Start_Tk()