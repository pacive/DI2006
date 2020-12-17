import tkinter as tk
from tkinter import messagebox, ttk, N, W, S, E
import random
import uielements

class MasterMind:
    BOARD_WIDTH = 360
    BOARD_HEIGHT = 600
    COLORS = ('RED', 'GREEN', 'BLUE', 'YELLOW', 'BLACK', 'WHITE', 'CYAN', 'MAGENTA')

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind")
        self.root.option_add('*tearOff', 0)
        self.menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu)
        self.window = ttk.Frame(self.root)
        self.window.grid(column = 0, row = 0, sticky=(N, W, E, S))
        self.canvas = tk.Canvas(self.window, width=self.BOARD_WIDTH, height=self.BOARD_HEIGHT)
        self.peg_grid = uielements.Grid(self.canvas, \
            self.BOARD_WIDTH - 250, self.BOARD_HEIGHT - 520, 10, 4, 50, 50)
        self.score_grid = uielements.Grid(self.canvas, 30, self.BOARD_HEIGHT - 520, 10, 1, 50, 50)
        self.check_button = ttk.Button(self.canvas, text="Check!", command=self.validate_line, state='disabled')

        self.base_pegs = {}
        self.code_pegs = []
        self.hint_pegs = []
        self.placed_pegs = [[None, None, None, None] for _ in range(10)]
        self.round = 0
        self.code = None
        self.start()
        self.root.mainloop()

    def start(self):
        self.root['menu'] = self.menu
        self.menu.add_cascade(menu=self.file_menu, label='File')
        self.file_menu.add_command(label='New game', command=self.reset)
        self.file_menu.add_command(label='Exit', command=exit)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.create_window(55, 40, window=self.check_button)
        self.peg_grid.draw()
        self.score_grid.draw()
        self.create_pegs()
        self.code = self.generate_code()

    def reset(self):
        for row in self.placed_pegs:
            for i, peg in enumerate(row):
                if isinstance(peg, uielements.Peg):
                    peg.remove()
                row[i] = None

        for peg in self.code_pegs:
            peg.remove()

        for peg in self.hint_pegs:
            self.canvas.delete(peg)

        self.code_pegs.clear()
        self.hint_pegs.clear()
        self.code = self.generate_code()
        self.round = 0

    def create_pegs(self):
        for color in self.COLORS:
            self.reset_peg(color)
        self.canvas.tag_raise('peg', 'all')

    def reset_peg(self, color):
        self.base_pegs[color] = uielements.Peg(self.canvas, color, \
            self.BOARD_WIDTH - 20, (self.BOARD_HEIGHT - 50) - self.COLORS.index(color) * 30, self)

    def place_peg(self, x, y, peg):
        field = self.peg_grid.get_field(x, y)
        self.reset_peg(peg.color)
        for i in range(len(self.placed_pegs[self.round])):
            if self.placed_pegs[self.round][i] is peg:
                self.placed_pegs[self.round][i] = None

        if field is None or field['row'] != self.round:
            peg.remove()
        else:
            self.placed_pegs[field['row']][field['col']] = peg
            peg.move_to(*self.peg_grid.get_field_center(field['row'], field['col']))

        if not None in self.placed_pegs[self.round]:
            self.check_button.state(['!disabled'])
        else:
            self.check_button.state(['disabled'])

    def validate_line(self):
        score = []
        code = list(self.code)
        for i, peg in enumerate(self.placed_pegs[self.round]):
            if peg.color == self.code[i]:
                score.append(2)
                code[i] = None

        for peg in self.placed_pegs[self.round]:
            if peg.color in code:
                score.append(1)
                code.remove(peg.color)

        self.show_score(score)

        if score == [2, 2, 2, 2]:
            self.victory()
        elif self.round == 9:
            self.loss()

        self.next_round()

    def show_score(self, score):
        center_x, center_y = self.score_grid.get_field_center(self.round, 0)
        for i, s in enumerate(score):
            x = center_x - (-1)**i * 10
            y = center_y - (-1)**(i//2) * 10
            color = uielements.COLORS['WHITE']
            if s == 2:
                color = uielements.COLORS['BLACK']
            self.hint_pegs.append(uielements.draw_circle(self.canvas, x, y, 5, fill=color))

    def next_round(self):
        for peg in self.placed_pegs[self.round]:
            peg.freeze()
        self.check_button.state(['disabled'])
        self.round += 1

    def generate_code(self):
        code = []
        for _ in range(4):
            code.append(random.choice(self.COLORS))
        return tuple(code)

    def victory(self):
        self.show_code()
        messagebox.showinfo(message='You won!')

    def loss(self):
        self.show_code()
        messagebox.showinfo(message='Sorry, you lost!')

    def show_code(self):
        for i, color in enumerate(self.code):
            x = self.peg_grid.get_field_center(0, i)[0]
            peg = uielements.Peg(self.canvas, color, x, 40, self)
            peg.freeze()
            self.code_pegs.append(peg)


MasterMind()
