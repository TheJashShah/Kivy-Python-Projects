import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random

class MainWindow(Screen):
    pass

class Rock_Paper_Scissors(Screen):
    player_text = ObjectProperty(None)
    comp_text = ObjectProperty(None)
    result_text = ObjectProperty(None)

    rock_btn = ObjectProperty(None)
    player_btn = ObjectProperty(None)
    scissors_btn = ObjectProperty(None)

    player_played = None

    def click_rock(self):
        self.player_text.text = ("You Played: Rock")
        self.player_played = "Rock"
        self.main_func() 

    def click_paper(self):
        self.player_text.text = ("You Played: Paper")
        self.player_played = "Paper"
        self.main_func() 

    def click_scissors(self):
        self.player_text.text = ("You Played: Scissors")
        self.player_played = "Scissors"
        self.main_func()

    def main_func(self):
        comp_played = random.choice(["Rock", "Paper", "Scissors"])
        self.comp_text.text = ("Comp Played: " + comp_played)

        dict = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

        for element in dict:
            if element == self.player_played:

                if dict[element] == comp_played:
                    self.result_text.text = "Result: Comp Wins!"
                
                elif (self.player_played == comp_played):
                    self.result_text.text = "Result: Its a Tie!"
                
                else:
                    self.result_text.text = "Result: Player Wins!"

class Guess_the_number(Screen):
    
    input_ = ObjectProperty(None)
    guess = ObjectProperty(None)
    new = ObjectProperty(None)
    res_text = ObjectProperty(None)

    target_num = 0

    def generate_new(self):
        self.target_num = random.randint(1, 100)
        self.res_text.text = "Press Guess to guess!"

    def guess_btn(self):

        if self.input_.text.isnumeric():
            guessed = int(self.input_.text)
        
        else:
            guessed = -1

        if guessed == -1:
            self.res_text.text = "Enter only Integers."

        elif guessed < self.target_num:
            self.res_text.text = "Your guess is Lower!"

        elif guessed > self.target_num:
            self.res_text.text = "Your Guess is Higher!"

        elif guessed == self.target_num:
            self.res_text.text = "You have correctly guessed the number!"

class Tic_Tac_Toe(Screen):
    btn_1 = ObjectProperty(None)
    btn_2 = ObjectProperty(None)
    btn_3 = ObjectProperty(None)
    btn_4 = ObjectProperty(None)
    btn_5 = ObjectProperty(None)
    btn_6 = ObjectProperty(None)
    btn_7 = ObjectProperty(None)
    btn_8 = ObjectProperty(None)
    btn_9 = ObjectProperty(None)

    txt = ObjectProperty(None)

    count = 0

    def on_kv_post(self, base_widget):
        self.list_ = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]

    def update_board(self):
        self.Board = ["", self.btn_1.text, self.btn_2.text, self.btn_3.text, self.btn_4.text, self.btn_5.text, self.btn_6.text, self.btn_7.text, self.btn_8.text, self.btn_9.text]

    def check_for_win(self, char):
        self.update_board()

        if(self.Board[1] == char and self.Board[2] == char and self.Board[3] == char) or (self.Board[4] == char and self.Board[5] == char and self.Board[6] == char) or (self.Board[7] == char and self.Board[8] == char and self.Board[9] == char) or (self.Board[1] == char and self.Board[4] == char and self.Board[7] == char) or (self.Board[2] == char and self.Board[5] == char and self.Board[8] == char) or (self.Board[3] == char and self.Board[6] == char and self.Board[9] == char) or (self.Board[1] == char and self.Board[5] == char and self.Board[9] == char) or (self.Board[3] == char and self.Board[5] == char and self.Board[7] == char):

            return True
        
    def disable_all(self):
        for btn in self.list_:
            btn.disabled = True

    def check_for_draw(self):
        self.update_board()

        if (not self.check_for_win("X")) and (not self.check_for_win("O")) and self.Board.count("") <= 2:
            return True

    def clicked(self, btn):
        if btn.text == "":
            
            if (self.count % 2 == 0):
                btn.text = "X"
                
            elif (self.count % 2 != 0):
                btn.text = "O"
                
            self.count += 1
            btn.disabled = True

        if (self.count % 2 == 0):
            self.txt.text = "Player one's turn..."
        elif (self.count %2 != 0):
            self.txt.text = "Player two's turn..."

        if self.check_for_win("X"):
            self.disable_all()
            self.txt.text = "Player one wins!"

        if self.check_for_win("O"):
            self.disable_all()
            self.txt.text = "Player two wins!"

        if self.check_for_draw():
            self.disable_all()
            self.txt.text = "Its a draw!"

    def reset(self):
        for btn in self.list_:
            btn.text = ""
            self.count = 0
            btn.disabled = False
            self.txt.text = "Player one's turn..."

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return kv
    
a = MainApp()
a.run()