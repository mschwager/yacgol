#!/usr/bin/env python3

import argparse
import tkinter

UNDER_POPULATION_COUNT = 2
OVER_POPULATION_COUNT = 3
REPRODUCTION_COUNT = 3


class CellButton(tkinter.Button):
    DEFAULT_COLOR = 'black'
    INVERTED_COLOR = 'white'

    def __init__(self, window, *args, **kwargs):
        super(CellButton, self).__init__(
            window,
            *args,
            command=self.flip,
            **kwargs
        )

        self.initialize()

    def initialize(self):
        self.configure(bg=self.DEFAULT_COLOR)
        self.alive = False

    def flip(self):
        if self.alive:
            self.configure(bg=self.DEFAULT_COLOR)
            self.alive = False
        else:
            self.configure(bg=self.INVERTED_COLOR)
            self.alive = True


class CellGrid:
    NEIGHBOR_COORDINATES = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
    ]
    SPEED_MIN = 1
    SPEED_MAX = 10

    def __init__(self, window, length, width):
        self.window = window
        self.length = length
        self.width = width
        self.continuing = False
        self.current_speed = 1
        self.after_id = None

        self.cell_buttons = [
            [
                CellButton(self.window)
                for _ in range(self.length)
            ]
            for _ in range(self.width)
        ]

        self._apply_cell_buttons(
            lambda cell_button, x, y: cell_button.grid(row=y, column=x)
        )

    def _apply_cell_buttons(self, func):
        for y, row in enumerate(self.cell_buttons):
            for x, cell_button in enumerate(row):
                func(cell_button, x, y)

    def reset(self):
        self.continuing = False

        if self.after_id:
            self.window.after_cancel(self.after_id)
            self.after_id = None

        self._apply_cell_buttons(
            lambda cell_button, x, y: cell_button.initialize()
        )

    def neighbor_count(self, x, y):
        return sum(
            int(self.cell_buttons[(y + j) % self.width][(x + i) % self.length].alive)
            for i, j in self.NEIGHBOR_COORDINATES
        )

    def step(self):
        def add_neighbor_count(cell_button, x, y):
            cell_button.neighbor_count = self.neighbor_count(x, y)

        self._apply_cell_buttons(add_neighbor_count)

        def apply_rules(cell_button, x, y):
            if cell_button.alive and cell_button.neighbor_count < UNDER_POPULATION_COUNT:
                cell_button.flip()
            elif cell_button.alive and cell_button.neighbor_count > OVER_POPULATION_COUNT:
                cell_button.flip()
            elif not cell_button.alive and cell_button.neighbor_count == REPRODUCTION_COUNT:
                cell_button.flip()

        self._apply_cell_buttons(apply_rules)

    def continue_(self, seconds=1, times=None):
        self.continuing = True

        milliseconds = int(1000 * seconds / self.current_speed)

        self.step()

        if times is None:
            self.after_id = self.window.after(
                milliseconds,
                self.continue_,
                seconds,
                None
            )
        elif times > 0:
            self.after_id = self.window.after(
                milliseconds,
                self.continue_,
                seconds,
                times - 1
            )

    def speed(self, current_speed):
        self.current_speed = int(current_speed)


def parse_args():
    p = argparse.ArgumentParser(description='''
        A pure Python implementation of Conway's Game of Life using Tkinter.
        ''', formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument(
        '-l',
        '--length',
        action='store',
        default=10,
        type=int,
        help='grid length'
    )

    p.add_argument(
        '-w',
        '--width',
        action='store',
        default=10,
        type=int,
        help='grid width'
    )

    args = p.parse_args()
    return args


def main():
    args = parse_args()

    root = tkinter.Tk()
    root.title("Conway's Game of Life")

    cell_frame = tkinter.Frame(root, borderwidth=50)
    cell_frame.pack()

    cell_grid = CellGrid(cell_frame, args.length, args.width)

    command_frame = tkinter.Frame(root, borderwidth=10)
    command_frame.pack(side=tkinter.TOP)

    step_button = tkinter.Button(
        command_frame,
        text='Step',
        command=cell_grid.step
    )
    step_button.grid(row=0, column=0)

    continue_button = tkinter.Button(
        command_frame,
        text='Continue',
        command=cell_grid.continue_
    )
    continue_button.grid(row=0, column=1)

    reset_button = tkinter.Button(
        command_frame,
        text='Reset',
        command=cell_grid.reset
    )
    reset_button.grid(row=0, column=2)

    exit_button = tkinter.Button(
        command_frame,
        text='Exit',
        command=root.destroy
    )
    exit_button.grid(row=0, column=3)

    speed_scale_frame = tkinter.Frame(root, borderwidth=10)
    speed_scale_frame.pack(side=tkinter.TOP)

    speed_scale = tkinter.Scale(
        speed_scale_frame,
        from_=CellGrid.SPEED_MIN,
        to=CellGrid.SPEED_MAX,
        orient=tkinter.HORIZONTAL,
        command=cell_grid.speed
    )
    speed_scale.grid(row=0, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
