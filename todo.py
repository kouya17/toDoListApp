import tkinter as Tk

ToDo = []
txt = []
spent = []
spentNumber = []
spentButton = []
estimate = []
estimateNumber = []
deleteButton = []


class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Todo List')
        self.master.geometry('500x300')

        # 変数初期化
        self.ToDoNumber = 0
        # self.ToDo = []
        # self.txt = []
        # self.spent = []
        # self.spentNumber = []
        # self.spentButton = []
        # self.estimate = []
        # self.estimateNumber = []
        # self.deleteButton = []

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
        txt.append(txtNew)
        ToDo.append(ToDoNew)

        # 新しいラベルをToDoリストの末尾に追加
        self.ToDoNumber += 1
        ToDoNew.grid(row=self.ToDoNumber, column=0)

        # 経過時間を表すラベルを配置
        spentNumberNew = Tk.StringVar()
        spentNumberNew.set('0')
        spentNew = Tk.Label(self, width=2, textvariable=spentNumberNew)
        spent.append(spentNew)
        spentNumber.append(spentNumberNew)
        spentNew.grid(row=self.ToDoNumber, column=1)

        # 押すと経過時間を+1させるボタンを配置
        spentButtonNew = Tk.Button(self, text='+1',
                                   command=spentPlusOne(spentNumberNew))
        spentButton.append(spentButtonNew)
        spentButtonNew.grid(row=self.ToDoNumber, column=2)

        # 目標時間を表すラベルを配置
        estimateNumberNew = Tk.StringVar()
        estimateNumberNew.set(self.TimeBox.get())
        estimateNew = Tk.Label(self, width=2, textvariable=estimateNumberNew)
        # self.estimate.append(estimateNew)
        estimate.append(estimateNew)
        estimateNumber.append(estimateNumberNew)
        estimateNew.grid(row=self.ToDoNumber, column=3)

        # 削除ボタンを配置
        deleteButtonNew = Tk.Button(self, text='×',
                                    command=deleteToDoList(self.ToDoNumber))
        deleteButton.append(deleteButtonNew)
        deleteButtonNew.grid(row=self.ToDoNumber, column=4)

        # EditBoxに書かれている文字列を消去
        self.EditBox.delete(0, Tk.END)

        # TimeBoxに書かれている文字列を消去
        self.TimeBox.delete(0, Tk.END)


class spentPlusOne:  # 参考(http://www.shido.info/py/tkinter5.html)
    def __init__(self, spentNumber):
        self.spentNumber = spentNumber

    def __call__(self, event=None):
        self.spentNumber.set(str(int(self.spentNumber.get())+1))


class deleteToDoList:
    def __init__(self, toDoNumber):
        # self.estimate = estimate
        self.toDoNumber = toDoNumber

    def __call__(self, event=None):
        estimate[self.toDoNumber-1].destroy()
        # estimate.pop(self.toDoNumber-1)
        ToDo[self.toDoNumber-1].destroy()
        spent[self.toDoNumber-1].destroy()
        spentButton[self.toDoNumber-1].destroy()
        deleteButton[self.toDoNumber-1].destroy()


root = Tk.Tk()
app = Application(master=root)
app.mainloop()
