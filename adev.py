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
				print(f"Dropping {a[0]}")
				a.pop(0)
				b.pop(0)
	print(unique)
	# determine if list entry is semidivisible
	
	return unique

#-----------------------------------------------------------------------

def main(args):
	#Limit = 999966663333
	Limit = 25
	hiprime = nextprime(sqrt(Limit))
	print(hiprime)
	
	lp = 3
	hp = nextprime(lp)
	terms = 0
	intervals = 0
	while True:
		u = seq_primes(lp,hp)
		while u[-1] > Limit:
			u.pop()
		print(u)
		terms += len(u)
		intervals += 1
		
		# process returned list, drop duplicates and numbers exceeding Limit
		
		lp = hp
		hp = nextprime(lp)
		if hp > hiprime:
			break
	print(f"{terms} terms found.")
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
