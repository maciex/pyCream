#!/usr/bin/env python

import sys

#
#  CREAM CLIENT API module import
#
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
	#  If you have to start another job put its Cream Job ID into another string variable. Uncomment the following line:
	#
	# localCreamJID2 = "THE ID YOU RECEIVED FROM CREAM WITH THE REGISTRATION OPERATION"


	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(localCreamJID1, creamURL, stdVectorJobPropertyWrapper() )

	#
	#  need to start another job ? then create another JobIdWrapper object; uncomment the following line:
	#
	# job2 = JobIdWrapper(localCreamJID2, creamURL, stdVectorJobPropertyWrapper() )


	JobVector = stdVectorJobIdWrapper()
	JobVector.append( job1 )

	#
	#  need to start another job ? insert job2 in the JobVector. Uncomment the following line:
	#
	# JobVector.append( job2 )

	leaseID = "" #YOU'RE NOT INTERESTED TO IT NOW; just leave it empty

	#
	#  Al the job we've to start must have been registered with the same delegation identifier. 
	#  Let's Put it in this string variable...
	#
	delegationID = "DelegationID"

	#
	#  Build a JobFilterWrapper object that is the main piece of the JobStart request
	#  fromDate and to Date specify the time range in which the job have been submitted.
	#  By specifying the fromDate/toDate time range we select which jobs to start.
	#  "-1" means "no limit". Then fromData = toDate = -1 means "all jobs".
	#
	#  statusVec specify a list of job states. A job will be started if it is in one of the states
	#  specified in the statusVec. An empty statusVec means "the job in any status", but of course all the 
	#  jobs that need to be started are all in the same "REGISTERED" status; this explain why this vector
	#  must be empty.
	#
	#  statusVec is useful in other scenarios (cancelling/suspending jobs etc.) that need a 
	#  JobFilterWrapper as filter of jobs to process (for example 
													  #  one could want to cancel RUNNING OR IDLE jobs).

	fromDate = -1
	toDate   = -1
	statusVec = stdVectorString()

	jfw = JobFilterWrapper( JobVector, statusVec, fromDate, toDate, delegationID, leaseID )

	connection_timeout = 30 # seconds

	#
	#  This class will contain the result (as sent back from the CREAM CE) of the start of the jobs
	#
	result = ResultWrapper()

	#
	#  Build the client pointer
	creamClient = CreamProxyFactory.make_CreamProxyStart( jfw, result, connection_timeout )

	#
	#   [...]
	#
	#  BE CAREFUL !!!
	#
	#  Please Check the 'NULLNESS' of the creamClient variable and take the proper action if it is NULL
	#
	#  [...]
	#

	#
	#  An example of a valid CREAM CE URI. Of course you'll have to replace cream-12.pd.infn.it with your
	#  machine name.
	#
	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2"

	try:
		#
		# /tmp/x509up_u501 is a proxy file generated with voms-proxy-init
		#
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except (BaseException,  InvalidArgumentException, GridProxyDelegationException, JobSubmissionDisabledException,
			JobStatusInvalidException, JobUnknownException, GenericException, AuthorizationException, DelegationException,
			InternalException, ConnectionTimeoutException, auth_ex, soap_ex, soap_runtime_ex), ex:
		print "FATAL: " + ex.what()
		return 1

	#
	#  After JobStart invocation we want to know which jobs have been started, which one have not for several reasons:
	#
	#  result.getNotExistingJobs() - returns a list of job we tried to start but they where not present in the CE CREAM
	#  result.getNotMatchingStatusJobs() - returns the list of job that are not in no one of the states specified in the statusVec
	#  result.getNotMatchingDateJobs() - returns the list of job that are not in the timerange fromDate--toDate
	#  result.getNotMatchingProxyDelegationIdJobs() - returns the list of job that have not registered with the delegation identifier specified in the delegationID variable
	#  result.getNotMatchingLeaseIdJobs() - returns the list of job that have not registered with the lease identifier specified in the leaseID variable (but the case it is empty)
	#

	return 0

if __name__ == "__main__":
	sys.exit(main());

