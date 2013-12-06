#!/usr/bin/python2.7 

import argparse
import socket


def action(domain):
	#add possible sub domains here

	possible_domains = ['direct.','ftp.']

	for x in range(0,len(possible_domains)):
		possible_domains[x] = possible_domains[x] + str(domain)
	for d in possible_domains:
		try:
			print "Possible On "+ str(d) + " / " + socket.gethostbyname(d)
		except:
			print "Error On " + str(d)
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--domain',help='the domain name that you want to resolve from cloudflare')
	args = parser.parse_args()
	action(args.domain)

if __name__ == "__main__":
   parse()
