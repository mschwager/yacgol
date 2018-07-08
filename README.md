# Yet Another Conway's Game of Life

[![Build Status](https://travis-ci.org/mschwager/yacgol.svg?branch=master)](https://travis-ci.org/mschwager/yacgol)
[![Coverage Status](https://coveralls.io/repos/github/mschwager/yacgol/badge.svg?branch=master)](https://coveralls.io/github/mschwager/yacgol?branch=master)

`yacgol` is a pure Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) using [Tkinter](https://docs.python.org/3/library/tkinter.html).

> The game is a zero-player game, meaning that its evolution is determined
> by its initial state, requiring no further input. One interacts with the
> Game of Life by creating an initial configuration and observing how it
> evolves, or, for advanced players, by creating patterns with particular
> properties.
>
> At each step in time, the following transitions occur:
>
> 1. Any live cell with fewer than two live neighbors dies, as if by under population.
> 2. Any live cell with two or three live neighbors lives on to the next generation.
> 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
> 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
>
> - Conway's Game of Life Wikipedia page


# Installing

```
$ pip install yacgol
$ yacgol -h
```

# Using

Most interactions with `yacgol` will take place within the Tkinter UI. So
fire up `yacgol` and check it out!

# Developing

First, install development packages:

```
$ pip install -r requirements-dev.txt
```

## Testing

```
$ nose2
```

## Linting

```
$ flake8
```

## Coverage

```
$ nose2 --with-coverage
```
