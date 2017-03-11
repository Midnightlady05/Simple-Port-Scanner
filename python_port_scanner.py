#!/usr/bin/python

import sys, getopt
from socket import *
import subprocess
import requests
import struct


#print urllib2.__file__  prints to screen where the urllib2 is located

def main(argv):
   hostname = ''
   ip_address = ''
   min_port=0
   max_port=5000
   udt_opt= False
   try:
      opts, args = getopt.getopt(argv,"h:n:i:r:u:",["help","hostname","ip","range"])
   except getopt.GetoptError:
      print 'Getopt error:portscnner.py -i <ip address> -n <hostname> -r<range example: 1-1000> -h help'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ('-h', "--help"):
         print 'portscnner.py -i <ip address> -n <hostname> -r<range example: 1-1000> -h help'
         sys.exit()
      elif opt in ("-n", "--hostname"):
         hostname = arg
	 ip_address=gethostbyname(hostname)
      elif opt in ("-i", "--ip"):
	 #print (arg)
	 ip_address =(arg)
	 #print "ip address is: %s" %(ip_address)
      elif opt in ("-r", "--range"):
	 iprange = arg.split('-')
	 min_port = int (iprange[0])
	 max_port = int (iprange[1])
      elif opt in ("-u"):
	 udt_opt=True
   if(len(argv)==0):
       print 'portscnner.py -i <ip address> -n <hostname> -r<range example: 1-1000> -h help'
       sys.exit(2)

   #print argv
   #print 'number of threads is ', num_thread
   #print 'Url is ', inputhtml

   try:
	print "Start Scan"	
	for port in range(min_port, max_port):
	   s = socket(AF_INET, SOCK_STREAM)
	   r = s.connect_ex((ip_address,port))
	   if r==0:
	      print "Port %d: Open" %(port)
	   s.close()
	   if(udt_opt):
	      for port in range(min_port, max_port):
	         try: 
		   t=socket(AF_INET, SOCK_DGRAM)
		   t.settimeout(0.1)
	      	   t.sendto("--Test--",(ip_address, port))
	      	   data,address = t.recvfrom(255)
	         except Exception, e:
			try: errno, errtxt = e
			except ValueError:
			      print "UDP Port %d: Open" %(port)
			else:				
			      print "UDP Port %d: Closed" %(port)
		 t.close()
   except KeyboardInterrupt:
	sys.exit(1)
   except error:
	print "connection error"
	sys.exit(1)
   except gaierror:
	print "hostname error"
	sys.exit(1)
   print "Scanning Complete thank you"

if __name__ == "__main__":
   main(sys.argv[1:])