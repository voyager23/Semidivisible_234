#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  interval.py
#  
#  Copyright 2022 mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from math import sqrt

def main(args):
	for n in range(9,26):
		lps = 3
		hps = 5
		a = n%lps
		b = n%hps
		print(f"n:{n}, sqrt:{sqrt(n)} a:{n%lps} b:{n%hps}")
		if (a != b) and (a == 0 or b == 0):
			print("@")
			
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
