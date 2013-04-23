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
import os
import time
import httplib2

def opener(path, flags):
    return os.open(path, flags)

try: input = raw_input
except NameError: pass

url = input('URL: http://')
itime = input('Interval Time [sec]: ')
count = input('Loop Count: ')
filename = input('Save to[' + str(url) + '.txt]: ')

if filename == '':
    filename = url + '.txt'

file = open(str(filename), 'w')

for i in range(int(count)):

    print('Round: ' + str(i + 1))
    resp, content = httplib2.Http().request('http://' + str(url))
    with open(str(filename), 'a', opener=opener) as f:
        print(resp, file=f)
        print(content, file=f)
    os.close
    if i != (int(count) - 1):
        time.sleep(float(itime))

print('done...')
exit()
