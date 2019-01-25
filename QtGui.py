from PyQt5 import QtWidgets, uic

from blockchain import get_all_blocks, create_new_block, mine


class GUI:
    dlg = 1

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.dlg = uic.loadUi('ui.ui')

        self.dlg.ViewButton.clicked.connect(lambda: self.view_file())
        self.dlg.mainTab.currentChanged.connect(self.update_listbox)
        self.dlg.MineButton.clicked.connect(lambda: self.mine_pressed())
        self.dlg.AddButton.clicked.connect(self.add_block)
        # dlg.DecompressIt.clicked.connect(decomp)
        # dlg.browseToDesDirectory.clicked.connect(dir_to_save)
        self.dlg.show()
        self.update_listbox()
        app.exec()

    def view_file(self):
        self.dlg.BlockDetail.setStyleSheet('color: black')
        f = self.dlg.BlocksList.currentItem().text()
        file_name = "blocks/" + f + ".txt"
        file = open(file_name, "r")
        content = file.readlines()[1:]
        file.close()
        tex = ''
        for i in content:
            tex += i
        self.dlg.BlockDetail.setText(tex)

    def create_file(self, sender, receiver, mes):
        create_new_block(sender, receiver, mes)
        # messagebox.showinfo("success", "new block created!")

    def mine_pressed(self):
        res_list = mine()
        if res_list[0]:
            self.dlg.BlockDetail.setText(
                "Success\n" + "All documents are secure!\nYou mine " + str(res_list[1] // 5 + 1) + " coin(s)")
            self.dlg.BlockDetail.setStyleSheet('color: black')
        else:
            self.dlg.BlockDetail.setText(
                "Danger\n" + "Some documents are damaged!\nYou mine " + str(res_list[1] // 5 + 1) + " coin(s)")
            self.dlg.BlockDetail.setStyleSheet('color: red')

    def update_listbox(self):
        path = "blocks/"
        file_list = get_all_blocks(path)
        ls = []
        for i in file_list:
            ls.append(i.split('.')[0])
        self.dlg.BlocksList.clear()
        self.dlg.BlocksList.addItems(ls)

    def add_block(self):
        self.create_file(self.dlg.SenderEdit.text(),
                         self.dlg.RecieverEdit.text(),
                         self.dlg.MessageEdit.toPlainText())


g = GUI()
