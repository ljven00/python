""" this program simulates two rolling dice"""

from random import randint
from time import sleep

class Dice:

    __MIN = 1
    __MAX = 6

    # text representation of a die
    __dice = ["\n  *\n",
        "*\n\n    *",
        "*\n  *\n    *",
        "*   *\n\n*   *",
        "*   *\n  *\n*   *",
        "*   *\n*   *\n*   *"
    ]

    def __init__(self, name = "User"):
        self.roll()
        self.__user_score = 0
        self.__roll_count = 0
        self.__username = name

    def __repr__(self):
        return f"A pair of dice\nFirst die:\n{self.__die1_graph}\
        \nSecond die:\n{self.__die2_graph}"

    def __str__(self):
        return f"A pair of dice\nFirst die: {self.__die1}\
        \nSecond die: {self.__die2}"

    # rolling the dice initiate the value of the instance variable
    def roll(self):
        self.__die1 = randint(Dice.__MIN, Dice.__MAX)
        self.__die2 = randint(Dice.__MIN, Dice.__MAX)
        self.__roll_sum = self.__die1 + self.__die2
        self.__die1_graph = Dice.__dice[self.__die1 - 1]
        self.__die2_graph = Dice.__dice[self.__die2 - 1]

    # priting on stdout the text image of the dice
    def show(self):
        print(f"Here comes a roll of {self.__roll_sum}")
        print(self.__die1_graph)
        print("-"*5)
        print(self.__die2_graph)

    def setUsername(self, name):
        self.__username = "Anonymous" if name == "" else name

    def __intro(self):
        print("Welcome to the rolling dice game!")
        self.setUsername(input("Please enter your name: "))
        print(f"Welcome {self.__username}\nLet the game begins...")

    def __goodbye(self):
        print(f"You are leaving so soon {self.__username}...")
        sleep(1)
        print("Thank you for playing...")
        sleep(1)
        print(f"Out of {self.__roll_count} rolls, you won {self.__user_score}.")
        print("See you soon!")

    def play(self):
        play_again = "y"
        self.__intro()
        sleep(2)
        while play_again == "y" or play_again == "Y":
            self.__roll_count += 1
            self.roll()
            if self.__roll_sum > 6:
                self.__user_score += 1
            self.show()
            play_again = input("Another round? (y for yes, any key for no): ")
        else:
            self.__goodbye()


    def getRollCount(self):
        return self.__roll_count

rolling_dice = Dice()
rolling_dice.play()
