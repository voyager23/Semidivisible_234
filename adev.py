#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  adev.py
#  
# Initial thoughts on semidivisible numbers


from sympy import sieve, primefactors, primerange,\
	prevprime, nextprime
from math import floor, factorial, sqrt

def seq_primes(lo,hi):
	# lo,hi sequential primes
	losqr = lo*lo
	hisqr = hi*hi
	# list some multiples of lo prime
	a = [(lo * x) for x in range(lo, (hisqr//lo + 1), +1 )]
	
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
				print(f"Dropping {a[0]}")
				a.pop(0)
				b.pop(0)
	#
	return unique

#-----------------------------------------------------------------------

def main(args):
	Limit = 999966663333
	hiprime = nextprime(sqrt(Limit))
	print(hiprime)
	
	lp = 2
	hp = nextprime(lp)
	while True:
		u = seq_primes(lp,hp)
		print(u)
		
		# process returned list, drop duplicates and numbers exceeding Limit
		
		lp = hp
		hp = nextprime(lp)
		if hp > hiprime:
			break

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
