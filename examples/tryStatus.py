#!/usr/bin/env python

import sys

#
#  CREAM CLIENT API module import
#
from Cream import *

def main():

	#
	#  Substitute with your hostname
	#
	creamURL = "https://cream-12.pd.infn.it:8443/ce-cream/services/CREAM2"

	#
	#  Substitute with your real CREAM Job ID returned by the JobRegister operation
	#
	localCreamJID1 = ""

	#
	#  If you have to query another job put its Cream Job ID into another string variable. Uncomment the following line:
	#
	#  string localCreamJID2 = "THE ID YOU RECEIVED FROM CREAM WITH THE REGISTRATION OPERATION";


	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(localCreamJID1, creamURL, stdVectorJobPropertyWrapper() )

	#
	#  need to query another job ? then create another JobIdWrapper object; uncomment the following line:
	#
	# job2 = JobIdWrapper(localCreamJID1, creamURL, stdVectorJobPropertyWrapper> )


	JobVector = stdVectorJobIdWrapper()

	#
	#  Let's put all jobs to query in the JobVector array. An empty array means we're
	#  asking CREAM for status of ALL jobs present in the CE.
	#
	JobVector.append( job1 )

	#
	#  need to query another job ? insert job2 in the JobVector. Uncomment the following line:
	#
	#  JobVector.push_back( job2 );

	leaseID = ""  # YOU'RE NOT INTERESTED TO IT NOW; just leave it empty

	#
	#  For JobStatus operation just leave this empty
	#
	delegationID = ""

	#
	#  Build a JobFilterWrapper object that is the main argument of the JobStart request.
	#  fromDate and to Date specify the time range in which the jobs have been submitted.
	#  By specifying the fromDate/toDate time range we select which jobs we want to query.
	#  "-1" means "no limit". Then fromData = toDate = -1 means "all jobs".
	#
	#  statusVec specify a list of job states. A job will be queried if it is in one of the states
	#  specified in the statusVec. An empty statusVec means "the job in any status".
	#
	fromDate = -1
	toDate   = -1
	statusVec = stdVectorString()

	jfw = JobFilterWrapper( JobVector, statusVec, fromDate, toDate, delegationID, leaseID )

	connection_timeout = 30  # seconds

	#
	#  This class will contain the result (as sent back from the CREAM CE) of the start of the jobs
	#
	result = ResultWrapper()

	#
	#  Build the client pointer
	#

	Sresult = StatusArrayResult()

	creamClient = CreamProxyFactory.make_CreamProxyStatus( jfw, Sresult, connection_timeout )

	#
	#  [...]
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
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	#
	#  See the JobStatusWrapper documentation
	#
	for jobId in Sresult.keys():
		job = Sresult[jobId]
		if job[0] == JobIdWrapper.RESULT.OK:
			statusTime = time.asctime( time.localtime( job[1].getTimestamp() ) ) 
			print "Job [%s] is in status [%s] occurred at [%s]" % ( jobId, job[1].getStatusName(), statusTime )
		else:
			print "For Job [%s] CREAM returned a fault: [%s]" % ( jobId, job[2] )
			return 0

if __name__ == "__main__":
	sys.exit(main())

