from calculator_ui import UiCalculator


class Calculator(UiCalculator):
    def setupUi(self, UI_Calculator):
        super().setupUi(UI_Calculator)
        self.pushButton_0.clicked.connect(lambda: self.action_number("0"))
        self.pushButton_1.clicked.connect(lambda: self.action_number("1"))
        self.pushButton_2.clicked.connect(lambda: self.action_number("2"))
        self.pushButton_3.clicked.connect(lambda: self.action_number("3"))
        self.pushButton_4.clicked.connect(lambda: self.action_number("4"))
        self.pushButton_5.clicked.connect(lambda: self.action_number("5"))
        self.pushButton_6.clicked.connect(lambda: self.action_number("6"))
        self.pushButton_7.clicked.connect(lambda: self.action_number("7"))
        self.pushButton_8.clicked.connect(lambda: self.action_number("8"))
        self.pushButton_9.clicked.connect(lambda: self.action_number("9"))
        self.pushButton_add.clicked.connect(lambda: self.action_operator("+"))
        self.pushButton_substract.clicked.connect(lambda: self.action_operator("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.action_operator("*"))
        self.pushButton_divide.clicked.connect(lambda: self.action_operator("/"))
        self.pushButton_clear.clicked.connect(self.action_clear)
        self.pushButton_delete.clicked.connect(self.action_del)
        self.pushButton_percent.clicked.connect(self.action_percent)
        self.pushButton_negetive.clicked.connect(self.action_negetive)
        self.pushButton_decimal.clicked.connect(self.action_decimal)
        self.pushButton_equal.clicked.connect(self.action_equal)

    def action_number(self, n):
        text = self.label.text()
        if text == "INVALID":
            text = ""
        self.label.setText(text + n)

    def action_negetive(self):
        text = self.label.text()
        if text.find(".") == -1:
            n = int(text)
            n = n * (-1)
            self.label.setText(str(n))
        else:
            n = float(text)
            n = n * (-1)
            self.label.setText(str(n))

    def action_operator(self, operator):
        text = self.label.text()
        self.label.setText(text + operator)

    def action_decimal(self):
        text = self.label.text()
        if text.find(".") == -1:
            self.label.setText(text + ".")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        # print(text[:len(text))
        self.label.setText(text[:len(text)-1])

    def action_percent(self):
        text = self.label.text()
        if text.find(".") == -1:
            n = int(text)
            n = n / 100
            self.label.setText(str(n))
        else:
            n = float(text)
            n = n / 100
            self.label.setText(str(n))

    def action_equal(self):
        eqn = self.label.text()
        try:
            ans = eval(eqn)
            self.label.setText(str(ans))
        except:
            self.label.setText("INVALID")
