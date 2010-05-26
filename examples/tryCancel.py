#!/usr/bin/env python

import sys
import string

from random import Random
from Cream import *

def main():

	#
	#  Substitute with a your hostname
	#
	creamURL = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2"

	#
	#  Substitute with a real CREAM Job ID, as returned by the JobRegister operation
	#
	localCreamJID1 = "THE ID YOU RECEIVED FROM CREAM WITH THE REGISTRATION OPERATION"

	#
	#  If you have to cancel another job put its Cream Job ID into another string variable. Uncomment the following line:
	#
	#  localCreamJID2 = "THE ID YOU RECEIVED FROM CREAM WITH THE REGISTRATION OPERATION"


	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(localCreamJID1, creamURL, stdVectorJobPropertyWrapper() )

	#
	#  need to cancel another job ? then create another JobIdWrapper object; uncomment the following line:
	#
	# job2 = JobIdWrapper(localCreamJID2, creamURL, stdVectorJobPropertyWrapper() )


	JobVector = stdVectorJobIdWrapper()

	#
	#  An empty JobVector means "Cancel all jobs". To "all jobs" the user can also
	#  apply a filter; see below.
	#
	JobVector.append( job1 )

	#
	#  need to cancel another job ? insert job2 in the JobVector. Uncomment the following line:
	#
	#  JobVector.push_back( job2 )

	leaseID = "" # YOU'RE NOT INTERESTED TO IT NOW; just leave it empty

	#
	#  Just leave this delegation argument empty
	#
	delegationID = "DelegationID"

	#
	#  Build a JobFilterWrapper object that is the main piece of the JobCancel request
	#  fromDate and to Date specify the time range in which the job have been submitted.
	#  By specifying the fromDate/toDate time range we select which jobs to cancel.
	#  "-1" means "no limit". Then fromData = toDate = -1 means "all jobs".
	#
	#  statusVec specify a list of job states. A job will be cancelled if it is in one of the states
	#  specified in the statusVec. An empty statusVec means "the job in any status".
	#
	#
	fromDate = -1
	toDate   = -1
	statusVec = stdVectorString()

	jfw = JobFilterWrapper( JobVector, statusVec, fromDate, toDate, delegationID, leaseID )

	connection_timeout = 30 # seconds

	#
	#  This class will contain the result (as sent back from the CREAM CE) of the cancelation of the jobs
	#
	result = ResultWrapper()

	#
	#  Build the client pointer
	#
	creamClient = CreamProxyFactory.make_CreamProxyCancel( jfw, result, connection_timeout )

	#
	# [...]
	#
	# BE CAREFUL !!!
	#
	# Check the NULLNESS of creamClient and take the proper action if it is NULL
	#
	# [...]
	#

	#
	#  An example of a valid CREAM CE URI. Of course you'll have to replace cream-12.pd.infn.it with your
	#  machine name.
	#
	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2"

	try:
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	#
	#   After JobCancel invocation we want to know which jobs have been cancelled, which one have not for several reasons:
	#
	#  result.getNotExistingJobs() - returns a list of job we tried to cancel but they where not present in the CE CREAM
	#  result.getNotMatchingStatusJobs() - returns the list of job that are not in no one of the states specified in the statusVec
	#  result.getNotMatchingDateJobs() - returns the list of job that are not in the timerange fromDate--toDate
	#  result.getNotMatchingProxyDelegationIdJobs() - returns the list of job that have not registered with the delegation identifier specified in the delegationID variable
	#  result.getNotMatchingLeaseIdJobs() - returns the list of job that have not registered with the lease identifier specified in the leaseID variable (but the case it is empty)
	#
	#

if __name__ == "__main__":
	sys.exit(main())

