#!/usr/bin/env python

import sys

from Cream import *

def main():

	connection_timeout = 30  # seconds

	#
	#  Set the enable or disable submission by choosing the boolean value...
	#

	enable = True # or False

	creamClient = CreamProxyFactory.make_CreamProxyAcceptNewJobSubmissions(enable, connection_timeout)

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
	except (BaseException,  InvalidArgumentException, GridProxyDelegationException, JobSubmissionDisabledException,
			JobStatusInvalidException, JobUnknownException, GenericException, AuthorizationException, DelegationException,
			InternalException, ConnectionTimeoutException, auth_ex, soap_ex, soap_runtime_ex), ex:
		print "FATAL: " + ex.what()
		return 1

	return 0

if __name__ == "__main__":
	sys.exit(main())

