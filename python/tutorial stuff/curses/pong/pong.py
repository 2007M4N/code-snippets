#!/usr/bin/env python
# coding: utf-8

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Copyright (C) 2013 Fabian Nedoluha <finga_license@onders.org>
"""

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

# scores
pl1_score = 0
pl2_score = 0

scores_begin_x = 0
scores_begin_y = int(size_y - 5)
scores_height = 5
scores_width = int(size_x)
scores_win = curses.newwin(scores_height, scores_width, scores_begin_y, scores_begin_x)

# make player1
pl1_begin_x = 2
pl1_begin_y = int(size_y / 2 - 5)
pl1_height = 6
pl1_width = 3
pl1_win = curses.newwin(pl1_height, pl1_width, pl1_begin_y, pl1_begin_x)

# make player2
pl2_begin_x = size_x - 5
pl2_begin_y = int(size_y / 2 - 5)
pl2_height = 6
pl2_width = 3
pl2_win = curses.newwin(pl2_height, pl2_width, pl2_begin_y, pl2_begin_x)

# bit/ball
bit_begin_x = int(size_x / 2 - 1)
bit_begin_y = int(size_y / 2 - 3)
bit_height = 1
bit_width = 2
bit_move_x = -1
bit_move_y = 0
bit_win = curses.newwin(bit_height, bit_width, bit_begin_y, bit_begin_x)

# help
hlp_begin_x = int(size_x / 2 - 28)
hlp_begin_y = int(size_y - 4)
hlp_height = 4
hlp_width = 56
hlp_win = curses.newwin(hlp_height, hlp_width, hlp_begin_y, hlp_begin_x)
hlp_win.addstr(0,0, 'A:\tPlayer 1 up')
hlp_win.addstr(1,0, 'Z:\tPlayer 1 down')
hlp_win.addstr(2,0, 'Q:\tQuit')
hlp_win.addstr(0,34, 'Up:\tPlayer 2 up')
hlp_win.addstr(1,34, 'Down:\tPlayer 2 down')
hlp_win.addstr(2,34, 'P:\tPause')

# game logic
while True:

    # update screen
    curses.doupdate()
    
    # game tick
    time.sleep(0.02)

    # bounce on top & bottom
    if (bit_begin_y + bit_move_y < 0) | (bit_begin_y + bit_move_y > size_y - 6):
        bit_move_y *= -1

    # collusion with pl1
    if (bit_begin_x + bit_move_x < 5):
        if (bit_begin_y + bit_move_y > pl1_begin_y - 1) & (bit_begin_y + bit_move_y < pl1_begin_y + pl1_height):
            # change direction
            bit_move_x *= - 1
            
            # angle
            bit_diff = bit_begin_y - pl1_begin_y
            if bit_diff == 0:
                bit_move_y -= 0.5
            elif bit_diff == 1:
                bit_move_y -= 0.3
            elif bit_diff == 2:
                bit_move_y -= 0.1
            elif bit_diff == 3:
                bit_move_y += 0.1
            elif bit_diff == 4:
                bit_move_y += 0.3
            elif bit_diff == 5:
                bit_move_y += 0.5
        # hit?
        elif (bit_begin_x + bit_move_x < 0):
            pl2_score += 1
            curses.beep()
            time.sleep(0.5)
            bit_begin_x = int(size_x / 2 - 1)
            bit_begin_y = int(size_y / 2 - 3)
            bit_move_x = -1
            bit_move_y = 0

    # collusion with pl2, comments == # collusion with pl1
    if (bit_begin_x + bit_move_x > size_x - 7):
        if (bit_begin_y + bit_move_y > pl2_begin_y - 1) & (bit_begin_y + bit_move_y < pl2_begin_y + pl2_height):
            bit_move_x *= - 1
            bit_diff = bit_begin_y - pl1_begin_y
            if bit_diff == 0:
                bit_move_y -= 0.5
            elif bit_diff == 1:
                bit_move_y -= 0.3
            elif bit_diff == 2:
                bit_move_y -= 0.1
            elif bit_diff == 3:
                bit_move_y += 0.1
            elif bit_diff == 4:
                bit_move_y += 0.3
            elif bit_diff == 5:
                bit_move_y += 0.5
        elif (bit_begin_x + bit_move_x > size_x - 2):
            pl1_score += 1
            curses.beep()
            time.sleep(0.5)
            bit_begin_x = int(size_x / 2 - 1)
            bit_begin_y = int(size_y / 2 - 3)
            bit_move_x = 1
            bit_move_y = 0

    # update ball
    bit_begin_x = bit_begin_x + bit_move_x
    bit_begin_y = bit_begin_y + bit_move_y
    bit_win.mvwin(int(bit_begin_y), int(bit_begin_x))
    
    # player input
    c = stdscr.getch()
    if c == ord('z'):
        # move pl1 down
        if pl1_begin_y < size_y - 11:
            pl1_begin_y = pl1_begin_y + 1
            pl1_win.mvwin(pl1_begin_y, pl1_begin_x)
    elif c == ord('a'):
        # move pl1 up
        if pl1_begin_y > 0:
            pl1_begin_y = pl1_begin_y - 1
            pl1_win.mvwin(pl1_begin_y, pl1_begin_x)
    elif c == curses.KEY_DOWN:
        # move pl2 down
        if pl2_begin_y < size_y -11:
            pl2_begin_y = pl2_begin_y + 1
            pl2_win.mvwin(pl2_begin_y, pl2_begin_x)
    elif c == curses.KEY_UP:
        # move pl2 up
        if pl2_begin_y > 0:
            pl2_begin_y = pl2_begin_y - 1
            pl2_win.mvwin(pl2_begin_y, pl2_begin_x)
    elif c == ord('p'):
        # pause
        stdscr.nodelay(0)
        while True:
            c = stdscr.getch()
            if c == ord('p'):
                stdscr.nodelay(1)
                break;
            elif c == ord('q'):
                # close application
                curses.nocbreak()
                stdscr.keypad(0)
                curses.echo()
        
                # end it
                curses.endwin()
                exit()
                if c == ord('p'):
                    stdscr.nodelay(1)
            
    elif c == ord('q'):
        # close application
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        
        # end it
        curses.endwin()
        exit()
    # update most & write score
    stdscr.bkgd(curses.color_pair(1))
    bit_win.bkgd(curses.color_pair(2))
    scores_win.bkgd(curses.color_pair(2))
    pl1_win.bkgd(curses.color_pair(2))
    pl2_win.bkgd(curses.color_pair(2))
    hlp_win.bkgd(curses.color_pair(2))
    stdscr.noutrefresh()
    bit_win.noutrefresh()
    pl1_win.noutrefresh()
    pl2_win.noutrefresh()
    scores_win.noutrefresh()
    hlp_win.noutrefresh()
    scores_win.addstr(1, 1, 'score: ' + str(pl1_score))
    scores_win.addstr(1, int(size_x - 10), 'score: ' + str(pl2_score))
