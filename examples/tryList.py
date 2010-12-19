#!/usr/bin/env python2.7

import sys

from Cream import *

def main():

	#
	#  This vector will contain the list of jobs returned by the CREAM CE
	#
	jobIdWrapperVetor = stdVectorJobIdWrapper()
	connection_timeout = 30  # seconds

	creamClient = CreamProxyFactory.make_CreamProxyList( jobIdWrapperVetor, connection_timeout )

	#
	# [...]
	#
	# Check the NULLNESS of creamClient and take the proper action if it is NULL
	#
	# [...]
	#

	#
	#  Substitute with your hostname
	#
	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2"

	try:
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	for job in jobIdWrapperVetor:
		print job.getCreamJobID()

if __name__ == "__main__":
	sys.exit(main())

