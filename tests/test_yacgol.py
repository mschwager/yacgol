#!/usr/bin/env python

import tkinter
import unittest

import yacgol


class TestCellGrid(unittest.TestCase):

    def test_reset(self):
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 2, 2)

        cell_grid.cell_buttons[0][0].flip()
        cell_grid.cell_buttons[1][0].flip()
        cell_grid.cell_buttons[0][1].flip()
        cell_grid.cell_buttons[1][1].flip()
        cell_grid.reset()

        result = (
            int(cell_grid.cell_buttons[0][0].alive) +
            int(cell_grid.cell_buttons[1][0].alive) +
            int(cell_grid.cell_buttons[0][1].alive) +
            int(cell_grid.cell_buttons[1][1].alive)
        )
        expected = 0

        self.assertEqual(expected, result)

    def test_neighbor_count(self):
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 3, 3)

        flip_cell_coordinates = [
            (0, 2),
            (2, 2),
            (2, 0),
            (0, 0),
        ]

        for x, y in flip_cell_coordinates:
            cell_grid.cell_buttons[y][x].flip()

        result = cell_grid.neighbor_count(1, 1)
        expected = len(flip_cell_coordinates)

        self.assertEqual(expected, result)

    def test_neighbor_count_not_current(self):
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 3, 3)

        cell_grid.cell_buttons[1][1].flip()

        result = cell_grid.neighbor_count(1, 1)
        expected = 0

        self.assertEqual(expected, result)

    def test_blinker_step(self):
        """
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

        XOX    XXX
        XOX -> OOO
        XOX    XXX
        """
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 3, 3)

        cell_grid.cell_buttons[0][1].flip()
        cell_grid.cell_buttons[1][1].flip()
        cell_grid.cell_buttons[2][1].flip()

        cell_grid.step()

        self.assertTrue(cell_grid.cell_buttons[1][0].alive)
        self.assertTrue(cell_grid.cell_buttons[1][1].alive)
        self.assertTrue(cell_grid.cell_buttons[1][2].alive)

    def test_block_step(self):
        """
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

        XXXX    XXXX
        XOOX -> XOOX
        XOOX    XOOX
        XXXX    XXXX
        """
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 4, 4)

        cell_grid.cell_buttons[1][1].flip()
        cell_grid.cell_buttons[2][1].flip()
        cell_grid.cell_buttons[1][2].flip()
        cell_grid.cell_buttons[2][2].flip()

        cell_grid.step()

        self.assertTrue(cell_grid.cell_buttons[1][1].alive)
        self.assertTrue(cell_grid.cell_buttons[2][1].alive)
        self.assertTrue(cell_grid.cell_buttons[1][2].alive)
        self.assertTrue(cell_grid.cell_buttons[2][2].alive)

    def test_beacon_continue_(self):
        """
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

        OOXX    OOXX
        OXXX -> OOXX
        XXXO    XXOO
        XXOO    XXOO
        """
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 4, 4)

        cell_grid.cell_buttons[0][0].flip()
        cell_grid.cell_buttons[0][1].flip()
        cell_grid.cell_buttons[1][0].flip()
        cell_grid.cell_buttons[3][3].flip()
        cell_grid.cell_buttons[2][3].flip()
        cell_grid.cell_buttons[3][2].flip()

        cell_grid.continue_(seconds=0, times=2)

        # This oscillator has period 2 so it should be the same
        self.assertTrue(cell_grid.cell_buttons[0][0].alive)
        self.assertTrue(cell_grid.cell_buttons[0][1].alive)
        self.assertTrue(cell_grid.cell_buttons[1][0].alive)
        self.assertTrue(cell_grid.cell_buttons[3][3].alive)
        self.assertTrue(cell_grid.cell_buttons[2][3].alive)
        self.assertTrue(cell_grid.cell_buttons[3][2].alive)

    def test_speed(self):
        speed = 10
        root = tkinter.Tk()

        cell_grid = yacgol.CellGrid(root, 1, 1)

        cell_grid.speed(speed)

        result = cell_grid.current_speed
        expected = speed

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
