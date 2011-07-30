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

