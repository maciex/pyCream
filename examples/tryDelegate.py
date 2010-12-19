#!/usr/bin/env python2.7

import sys
import string

from random import Random
from Cream import *

def main():
	#
	#    A delegated proxy must have a string identifier. Try to choose it as unique as possible
	#
	delegationID    = "DelegationID"

	connection_timeout = 30 # seconds

	creamClient = CreamProxyFactory.make_CreamProxyDelegate( delegationID, connection_timeout );

	#
	# [...]
	#
	# Check the NULLNESS of creamClient and take the proper action if it is NULL
	#
	# [...]
	#

	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/gridsite-delegation";


	try:
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	print "Proxy with delegation id [" + delegationID + "] succesfully delegated to endpoint [" + serviceAddress + "]"
	return 0

if __name__ == "__main__":
	sys.exit(main())

