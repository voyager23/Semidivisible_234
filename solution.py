#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  solution.py
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


from sympy import sieve, primefactors, primerange,\
	prevprime, nextprime
from math import floor, factorial, sqrt

def seq_primes(lo,hi):
	# lo,hi sequential primes
	losqr = lo*lo
	hisqr = hi*hi
	# list some multiples of lo prime
	a = [(lo * x) for x in range(lo, (hisqr//lo + 1), +1 )]
	# list some multiples of hi prime	
	b = [(hi * x) for x in range(hi, (losqr//hi), -1 )]	
	b.reverse()	
	#consolidate two lists
	unique = []
	while True:
		if len(a)==0:
			unique += b
			break
		elif len(b)==0:
			unique += a
			break
		else:
			if a[0] < b[0]:
				unique.append(a.pop(0))
			elif b[0] < a[0]:
				unique.append(b.pop(0))
			else:
				#print(f"Dropping {a[0]}")
				a.pop(0)
				b.pop(0)
	#print(unique)
	unique = unique[1:-1]
	#print(unique)	#[10, 12, 18, 20, 21, 24]
	# now determine if any terms are SemiDivNum
	u = []
	for n in unique:
		x = n%lo
		y = n%hi
		if (x != y) and ((x == 0) or (y == 0)):
			#print(f"{n} is SDN")
			u.append(n)
	return u

#-----------------------------------------------------------------------
def main(args):
	limit =  100000000000
	limit =  999966663333
	print(limit)
	lps = 3
	hps = 5
	terms = 1	# 8
	Sum = 8
	while True:
		u = seq_primes(lps,hps)
		lps = hps
		hps = nextprime(lps)		
		if u[-1] > limit:
			# prune terms from u
			while len(u)>0 and u[-1]>=limit:
				u.pop()
			# update terms variable
			terms += len(u)
			Sum += sum(u)
			break
		else:
			terms += len(u)
			Sum += sum(u)
		
	print(f"Terms: {terms} Sum: {Sum}")
	print(" Solution: 1259187438574927161 ")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
