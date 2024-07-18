import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class P(Popup):
    pass

def show_popup():
    show = P()

    show.open()

class Calculator(GridLayout):
    
    btn_0 = ObjectProperty(None)
    btn_1 = ObjectProperty(None)
    btn_2 = ObjectProperty(None)
    btn_3 = ObjectProperty(None)
    btn_4 = ObjectProperty(None)
    btn_5 = ObjectProperty(None)
    btn_6 = ObjectProperty(None)
    btn_7 = ObjectProperty(None)
    btn_9 = ObjectProperty(None)
    btn_add = ObjectProperty(None)
    btn_subtract = ObjectProperty(None)
    btn_multiply = ObjectProperty(None)
    btn_divide = ObjectProperty(None)
    btn_equal = ObjectProperty(None)
    btn_decimal = ObjectProperty(None)
    btn_del = ObjectProperty(None)
    text_ = ObjectProperty(None)

    string = ""

    def clicked(self, btn):
        self.string += btn.text
        self.text_.text = self.string

    def delete(self):
        self.string = self.string[:len(self.string) - 1]
        self.text_.text = self.string

    def decimal(self):
        list = self.string.split()

        if len(list) == 1:
            if self.string.count(".") == 0:
                self.string += "."

                self.text_.text = self.string

        elif len(list) > 1:
            if (list[-1]) != "+" or (list[-1]) !=  "-" or (list[-1]) != "*" or (list[-1]) != "/":
                if (list[-1]).count(".") == 0:
                    self.string += "."

                    self.text_.text = self.string 

        print(list)

    def clicked_action_btn(self, btn):

        text_to_add =  " " + btn.text + " "

        if self.string.count("/") == 0 and self.string.count("*") == 0 and self.string.count("-") == 0 and self.string.count("+") == 0:
            self.string += text_to_add

            self.text_.text = self.string

    def equal_pressed(self):

        list = self.string.split()

        if len(list) == 1 or len(list) == 2:
            show_popup()

        else:
            
            num1 = float(list[0])
            num2 = float(list[2])

            operator = list[1]

            if operator == "+":
                answer = num1 + num2
                answer = str(answer)

                self.string = answer
                self.text_.text = self.string

            elif operator == "-":
                answer = num1 - num2
                answer = str(answer)

                self.string = answer
                self.text_.text = self.string

            elif operator == "*":
                answer = num1 * num2
                answer = str(answer)

                self.string = answer
                self.text_.text = self.string

            elif operator == "/":

                if(num2 == 0):
                    self.string = ""
                    show_popup()

                answer = num1 / num2
                answer = str(answer)

                self.string = answer
                self.text_.text = self.string
    
class MainApp(App):
    def build(self):
        return Calculator()
    
Calc = MainApp()
Calc.run()

# I think there maybe bugs related to the "-" sign in this app. I also think I've also done a great job after watching only one tutorial series. Granted I've generously used Google and GPT.
# The most important thing that I've realised while building this is that Calculators are basically String functions wrapped under a GUI.