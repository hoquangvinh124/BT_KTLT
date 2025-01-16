import random
from lucky_game import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.random.clicked.connect(self.main)
        self.newgame.clicked.connect(self.new_game)

    def reward(self, p, m):
        p -= 30
        m += 30
        first_box = int(self.label_1.text())
        second_box = int(self.label_2.text())
        third_box = int(self.label_3.text())

        if first_box == 7 and second_box == 7 and third_box == 7:
            total_reward = (100 + 0.5 * m) + (30 + 0.5 * m) + 10
            p += total_reward
            m -= 0.5 * m
        else:
            if first_box == 7:
                p += 100 + 0.5 * m
            if second_box == 7:
                p += 30 + 0.5 * m
            if third_box == 7:
                p += 10

        p = int(p)
        m = int(m)
        return p, m

    def random_label(self):
        random_number_1 = random.randint(0, 8)
        random_number_2 = random.randint(0, 9)
        random_number_3 = random.randint(0, 9)
        self.label_1.setText(f"{random_number_1}")
        self.label_2.setText(f"{random_number_2}")
        self.label_3.setText(f"{random_number_3}")

    def main(self):
        player = int(self.label_7.text())
        machine = int(self.label_8.text())
        if player < 30:
            pass
        else:
            self.random_label()
            player_after_random, machine_after_random = self.reward(player, machine)
            self.label_7.setText(f"{player_after_random}")
            self.label_8.setText(f"{machine_after_random}")

    def new_game(self):
        self.label_7.setText("100")
        self.label_8.setText("100")

    def show(self):
        self.MainWindow.show()
