#!/usr/bin/env python

import sys

from Cream import *

def main():
	#
	#  A simple JDL describing a fake job
	#
	JDL = "[ VirtualOrganisation=\"belle\"; BatchSystem=\"pbs\"; QueueName = \"short\"; executable=\"/bin/sleep\"; arguments=\"120\"; ]";

	#
	#  The delegationID string variable must contain a string that you 
	#  previously choose as identifier of a delegated proxy.
	#
	delegationID    = "DelegationID"
	leaseID         = "" # YOU'RE NOT INTERESTED TO IT NOW
	delegationProxy = "" # YOU'RE NOT INTERESTED TO IT NOW

	#
	#  Do not start immediately the job. The job will stay in the CREAM CE as a "REGISTERED" job that
	#  can be started later. This is needed if you have to send some input sand box before the job start; otherwise
	#  set autostart to true.
	#
	autostart       = False

	#
	#  Create a JobDescription for the job. Note the "foo" string that identifies this job. When registering
	#  multiple jobs with a single JobRegister operation, the "foo" ID is needed to identify this
	#  particular job in the server's response that will contain information about registration of all jobs.
	#  See below...
	#
	jd = JobDescriptionWrapper(JDL, delegationID, delegationProxy, leaseID, autostart, "foo")

	properties = stdMapStringString()
	localCreamJID = ""

	reqs = RegisterArrayRequest()
	reqs.append( jd )
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
	# An example of a valid CREAM CE URI. Of course you'll have to replace cream-12.pd.infn.it with your
	# machine name.
	#
	serviceAddress = "https://cream-2-fzk.gridka.de:8443/ce-cream/services/CREAM2";

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
	# Identify our job using the "foo" ID extracting the value corresponding to the 
	# key "foo" of the resp std::map.
	#
	registrationResponse = resp["foo"]

	#
	# Use the boost function to extract relevant information for registered job.
	#
	if JobIdWrapper.OK != registrationResponse[0]:
		print "FATAL: " + registrationResponse[2]
		return 1

	creamURL  = registrationResponse[1].getCreamURL()
	CreamJID  = registrationResponse[1].getCreamJobID()
	CreamJID  = creamURL + "/" + CreamJID

	registrationResponse[1].getProperties( properties )
	ISB_upload_url = properties["CREAMInputSandboxURI"]

	print "Cream Job ID=[" + CreamJID + "]"
	print "InputSandBox Upload URL=[" + ISB_upload_url + "]"

	return 0

if __name__ == "__main__":
	sys.exit(main())

