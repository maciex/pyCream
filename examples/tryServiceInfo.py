#!/usr/bin/env python2.7

# pyCream - CREAM Client API Python
#
# Copyright (C) 2010, 2011  Maciej Sitarz
#
# Written by Maciej Sitarz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

