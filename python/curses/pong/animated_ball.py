#!/usr/bin/env python
# coding: utf-8

# import classes
import curses
import time

# initialize
stdscr = curses.initscr()

# getch non-blocking
stdscr.nodelay(1)

# disable echoing
curses.noecho()

# react to keys instantly
curses.cbreak()

# also to special keys
stdscr.keypad(1)

# color
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

# get terminal size
size = stdscr.getmaxyx()
size_x = size[1]
size_y = size[0]

# bit/ball
bit_begin_x = int(size_x / 2 - 1)
bit_begin_y = int(size_y / 2 - 3)
bit_height = 1
bit_width = 2
bit_move_x = -1
bit_move_y = 2
bit_win = curses.newwin(bit_height, bit_width, bit_begin_y, bit_begin_x)

speed = 0.1

while True:
    curses.doupdate()
    time.sleep(speed)
    if (bit_begin_x + bit_move_x < 0) | (bit_begin_x + bit_move_x > size_x - 2):
        bit_move_x = bit_move_x * -1
        curses.beep()
    if (bit_begin_y + bit_move_y < 0) | (bit_begin_y + bit_move_y > size_y - 1):
        bit_move_y = bit_move_y * -1
        curses.beep()
    bit_begin_x = bit_begin_x + bit_move_x
    bit_begin_y = bit_begin_y + bit_move_y
    bit_win.mvwin(int(bit_begin_y), int(bit_begin_x))
    c = stdscr.getch()
    if c == ord('q'):
        # close application
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        
        # end it
        curses.endwin()
        exit()
    stdscr.bkgd(curses.color_pair(1))
    bit_win.bkgd(curses.color_pair(2))
    stdscr.noutrefresh()
    bit_win.noutrefresh()
