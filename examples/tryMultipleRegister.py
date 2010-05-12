#!/usr/bin/env python

import sys

from Cream import *

def main():
	#
	# Two simple JDLs describing two fake jobs
	JDL1 = "[ ce_id=\"cream-12.pd.infn.it:8443/cream-pbs-cream_1\"; X509UserProxy=\"/tmp/x509up_u501\"; edg_jobid=\"https://grid005.pd.infn.it:9000/0000000000000000000002\"; VirtualOrganisation=\"infngrid\"; executable=\"/bin/sleep\"; arguments=\"120\"; LB_sequence_code = \"UI=000003:NS=0000000003:WM=000000:BH=0000000000:JSS=000000:LM=000000:LRMS=000000:APP=000000\"; BatchSystem=\"pbs\"; QueueName = \"short\"; ]"

	JDL2 = "[ ce_id=\"cream-12.pd.infn.it:8443/cream-pbs-cream_1\"; X509UserProxy=\"/tmp/x509up_u501\"; edg_jobid=\"https://grid005.pd.infn.it:9000/0000000000000000000003\"; VirtualOrganisation=\"infngrid\"; executable=\"/bin/sleep\"; arguments=\"240\"; LB_sequence_code = \"UI=000003:NS=0000000003:WM=000000:BH=0000000000:JSS=000000:LM=000000:LRMS=000000:APP=000000\"; BatchSystem=\"pbs\"; QueueName = \"short\"; ]"

	#
	#  The delegationID string variable must contain a string that you previously choose as identifier of a delegated proxy.
	#
	delegationID1    = "DelegationID1"
	delegationID2    = "DelegationID2"
	leaseID          = "" #YOU'RE NOT INTERESTED TO IT NOW
	delegationProxy  = "" #YOU'RE NOT INTERESTED TO IT NOW

	#
	#  Do not start immediately the jobs. The jobs will stay in the CREAM CE as a "REGISTERED" jobs that
	#  can be started later. This is needed if you have to send some input sand box before the job start; otherwise
	#  set autostart to true.
	#
	autostart       = False

	#
	#  Create a JobDescription for the job. Note the "foo1" and "foo2" strings that identify the jobs. When registering
	#  multiple jobs with a single JobRegister operation (as in this example), the "fooX" ID is needed to identify 
	#  one particular job in the server's response that will contain information about registration of all jobs.
	#  See below...
	#
	jd1 = JobDescriptionWrapper(JDL1, delegationID1, delegationProxy, leaseID, autostart, "foo1")
	jd2 = JobDescriptionWrapper(JDL2, delegationID2, delegationProxy, leaseID, autostart, "foo2")

	properties1 = stdMapStringString()
	properties2 = stdMapStringString()

	localCreamJID1 = ""
	localCreamJID2 = ""

	reqs = RegisterArrayRequest()
	reqs.append( jd1 )
	reqs.append( jd2 )
	resp = RegisterArrayResult()

	connection_timeout = 30 # seconds

	creamClient = CreamProxyFactory.make_CreamProxyRegister( reqs, resp, connection_timeout )

	#
	# [...]
	#
	# BE CAREFUL !!!
	#
	# Please Check the 'NULLNESS' of the creamClient variable and take the proper action if it is NULL
	#
	# [...]
	#

	#
	#  An example of a valid CREAM CE URI. Of course you'll have to replace cream-12.pd.infn.it with your
	#  machine name.
	#
	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2";

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
	#  Identify our job using the "foo" ID as key of the resp std::map.
	#
	registrationResponse_forJob1 = resp["foo1"];
	registrationResponse_forJob2 = resp["foo2"];

	#
	#  PROCESS RESULT
	#  Use the boost function to extract relevant information for registered job.
	#
	if JobIdWrapper.OK != registrationResponse_forJob1[0]:
		print "FATAL: " + registrationResponse_forJob1[2]
		return 1

	creamURL1  = registrationResponse_forJob1[1].getCreamURL()
	CreamJID1  = registrationResponse_forJob1[1].getCreamJobID()
	CreamJID1  = creamURL1 + "/" + CreamJID1

	registrationResponse_forJob1[1].getProperties( properties1 )
	ISB_upload_url1 = properties1["CREAMInputSandboxURI"]

	print "Cream Job ID=[" + CreamJID1 + "]"
	print "InputSandBox Upload URL=[" + ISB_upload_url1 + "]"

	#
	#  Repeat the code from "PROCESS RESULT" for the variable registrationResponse_forJob2
	#  ...
	#  ...
	#

	return 0

if __name__ == "__main__":
	sys.exit(main())
