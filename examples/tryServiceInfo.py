#!/usr/bin/env python2.7

import sys
import time

#
#  CREAM CLIENT API module import
#
from Cream import *

def main():

	connection_timeout = 30 # seconds

	#
	#  This structure will contain the information of the running CREAM CE
	#
	serviceInfoWrapper = ServiceInfoWrapper()
	verbosity = 3 # verbosity level

	creamClient = CreamProxyFactory.make_CreamProxyServiceInfo(serviceInfoWrapper, verbosity, connection_timeout )

	#
	# [...]
	#
	# Check the NULLNESS of creamClient and take the proper action if it is NULL
	#
	# [...]
	#

	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2"


	try:
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	startTime = serviceInfoWrapper.getStartupTime()

	print ""
	print "Cream Version      : " + serviceInfoWrapper.getInterfaceVersion()
	print "Started at         : " + time.asctime( time.localtime( startTime ) )
	print "Submission enabled : " + ( serviceInfoWrapper.getAcceptJobSubmission() ? "yes" : "no" )
	print "CEMon address      : " + serviceInfoWrapper.getCEMonURL()

	return 0

if __name__ == "__main__":
	sys.exit(main())

