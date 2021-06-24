from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QComboBox, QMessageBox


class Calculator():
	def count(self):
		info = self.textEdit.toPlainText()
		info2 = self.textEdit2.toPlainText()
		if ((info == '') or (info2 == '') or (not info.isdigit()) or (not info2.isdigit())):
			self.textEdit3.setPlainText('请输入数值')
		else:
			info = info.replace(' ','')
			info2 = info2.replace(' ','')
			cal = self.combox.currentText()
			if cal == '＋':
				newinfo = int(info) + int(info2)
			elif cal == '－':
				newinfo = int(info) - int(info2)
			elif cal == '×':
				newinfo = int(info) * int(info2)
			elif cal == '÷':
				newinfo = int(info) / int(info2)
			self.textEdit3.setPlainText(str(newinfo))

	def __init__(self):
		self.window = QMainWindow()
		self.window.resize(700,150)
		self.window.move(700,400)
		self.window.setWindowTitle('计算器 by wpsec')

		self.textEdit = QPlainTextEdit(self.window)
		self.textEdit.setPlaceholderText('输入数值')
		self.textEdit.move(10,25)
		self.textEdit.resize(100,30)

		self.textEdit2 = QPlainTextEdit(self.window)
		self.textEdit2.setPlaceholderText('输入数值')
		self.textEdit2.move(10,80)
		self.textEdit2.resize(100,30)

		self.combox = QComboBox(self.window)
		self.combox.addItem('＋')
		self.combox.addItem('－')
		self.combox.addItem('×')
		self.combox.addItem('÷')
		self.combox.move(150,50)

		self.button = QPushButton('计算',self.window)
		self.button.move(300,50)
		self.button.clicked.connect(self.count)

		self.textEdit3 = QPlainTextEdit(self.window)
		self.textEdit3.setPlaceholderText('答案')
		self.textEdit3.move(450,50)
		self.textEdit3.resize(100,30)

app = QApplication([])
start = Calculator()
start.window.show()
app.exec_()
