import tkinter as Tk


class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Todo List')
        self.master.geometry('400x300')

        # 変数初期化
        self.ToDoNumber = 0
        self.ToDo = []
        self.txt = []
        self.spent = []
        self.spentNumber = []
        self.estimate = []
        self.estimateNumber = []

        # ウィジェットの生成・配置
        self.create_widgets()

        self.pack()

    def create_widgets(self):
        # ToDOタイトル入力ボックス
        self.EditBox = Tk.Entry(self, width=30)
        # self.EditBox.pack(side='left')
        self.EditBox.grid(row=0, column=0)

        # 目標時間入力ボックス
        self.TimeBox = Tk.Entry(self, width=2)
        self.TimeBox.grid(row=0, column=1)

        # 追加ボタン
        Button = Tk.Button(self, text='追加')
        Button.bind('<Button-1>', self.DeleteEntryValue)
        # Button.pack(side='left')
        Button.grid(row=0, column=2)

        # MessageBox.pack(side='top')
        # Todo1.grid(row=1, column=0)

    def DeleteEntryValue(self, event):
        # EditBoxに書かれている文字列をtxtNewに代入
        txtNew = Tk.StringVar()
        txtNew.set(self.EditBox.get())

        # 新たにラベル(ToDoリスト)を作成
        ToDoNew = Tk.Label(self, width=30, textvariable=txtNew)

        # 新たに作成したラベル,txtをリストに追加
        self.txt.append(txtNew)
        self.ToDo.append(ToDoNew)

        # 新しいラベルをToDoリストの末尾に追加
        self.ToDoNumber += 1
        ToDoNew.grid(row=self.ToDoNumber, column=0)

        spentNumberNew = Tk.StringVar()
        spentNumberNew.set('0')
        spentNew = Tk.Label(self, width=2, textvariable=spentNumberNew)
        self.spent.append(spentNew)
        self.spentNumber.append(spentNumberNew)
        spentNew.grid(row=self.ToDoNumber, column=1)

        estimateNumberNew = Tk.StringVar()
        estimateNumberNew.set(self.TimeBox.get())
        estimateNew = Tk.Label(self, width=2, textvariable=estimateNumberNew)
        self.estimate.append(estimateNew)
        self.estimateNumber.append(estimateNumberNew)
        estimateNew.grid(row=self.ToDoNumber, column=2)

        # EditBoxに書かれている文字列を消去
        self.EditBox.delete(0, Tk.END)

        # TimeBoxに書かれている文字列を消去
        self.TimeBox.delete(0, Tk.END)


root = Tk.Tk()
app = Application(master=root)
app.mainloop()
