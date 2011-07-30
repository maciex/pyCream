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
import string
import time

from random import Random
from Cream import *

#
#    A delegated proxy must have a string identifier. Try to choose it as unique as possible
#
delegationID = "DelegationID_" + ''.join( Random().sample(string.letters+string.digits, 4) )

connection_timeout = 30

serviceHost = "https://cream-2-fzk.gridka.de:8443"

#
#  A simple JDL describing a fake job
#
JDL = "[ VirtualOrganisation=\"belle\"; BatchSystem=\"pbs\"; QueueName = \"short\"; executable=\"/bin/sleep\"; arguments=\"20\"; ]"
JDL2 = "[ VirtualOrganisation=\"belle\"; BatchSystem=\"pbs\"; QueueName = \"short\"; executable=\"/bin/sleep\"; arguments=\"10\"; ]"

leaseID         = "" # YOU'RE NOT INTERESTED TO IT NOW
delegationProxy = "" # YOU'RE NOT INTERESTED TO IT NOW

#
#  Do not start immediately the job. The job will stay in the CREAM CE as a "REGISTERED" job that
#  can be started later. This is needed if you have to send some input sand box before the job start; otherwise
#  set autostart to true.
#
autostart = False

CreamJID = ""
CreamURL = ""
CreamJID2 = ""
CreamURL2 = ""



# Proxy delegation
def delegate():

	global serviceHost

	print "==> Proxy delegation"

	creamClient = CreamProxyFactory.make_CreamProxyDelegate( delegationID, connection_timeout )

	#
	# [...]
	# Check the NULLNESS of creamClient and take the proper action if it is NULL
	# [...]
	#

	serviceAddress = serviceHost + "/ce-cream/services/gridsite-delegation"

	try:
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		raise Exception("Failed to delegate proxy")

	print "Proxy with delegation id [" + delegationID + "] succesfully delegated to endpoint [" + serviceAddress + "]"
	return 0


# Job registration
def register():

	global JDL
	global serviceHost
	global delegationID
	global delegationProxy
	global leaseID
	global autostart
	global CreamURL
	global CreamJID

	print "\n==> Job registration"

	#
	#  Create a JobDescription for the job. Note the "foo" string that identifies this job. When registering
	#  multiple jobs with a single JobRegister operation, the "foo" ID is needed to identify this
	#  particular job in the server's response that will contain information about registration of all jobs.
	#  See below...
	#
	jd = JobDescriptionWrapper(JDL, delegationID, delegationProxy, leaseID, autostart, "foo")

	properties = stdMapStringString()

	reqs = RegisterArrayRequest()
	reqs.append( jd )
	resp = RegisterArrayResult()

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

	serviceAddress = serviceHost + "/ce-cream/services/CREAM2"

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

	CreamURL  = registrationResponse[1].getCreamURL()
	CreamJID  = registrationResponse[1].getCreamJobID()
	#CreamJID  = creamURL + "/" + CreamJID

	registrationResponse[1].getProperties( properties )
	ISB_upload_url = properties["CREAMInputSandboxURI"]

	print "Cream Job ID=[" + CreamJID + "]"
	print "InputSandBox Upload URL=[" + ISB_upload_url + "]"

	return 0

# Many Jobs registration
def registerMany():

	global JDL
	global JDL2
	global serviceHost
	global delegationID
	global delegationProxy
	global leaseID
	global autostart
	global CreamURL
	global CreamJID
	global CreamURL2
	global CreamJID2

	print "\n==> Many jobs registration"

	#
	#  Create a JobDescription for the job. Note the "foo" string that identifies this job. When registering
	#  multiple jobs with a single JobRegister operation, the "foo" ID is needed to identify this
	#  particular job in the server's response that will contain information about registration of all jobs.
	#  See below...
	#
	jd = JobDescriptionWrapper(JDL, delegationID, delegationProxy, leaseID, autostart, "foo")
	jd2 = JobDescriptionWrapper(JDL2, delegationID, delegationProxy, leaseID, autostart, "foo2")

	properties = stdMapStringString()
	properties2 = stdMapStringString()

	reqs = RegisterArrayRequest()
	reqs.append( jd )
	reqs.append( jd2 )
	resp = RegisterArrayResult()

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

	serviceAddress = serviceHost + "/ce-cream/services/CREAM2"

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
	registrationResponse2 = resp["foo2"]

	#
	# Use the boost function to extract relevant information for registered job.
	#
	if JobIdWrapper.OK != registrationResponse[0]:
		print "FATAL: " + registrationResponse[2]
		return 1
	if JobIdWrapper.OK != registrationResponse2[0]:
		print "FATAL: " + registrationResponse2[2]
		return 1

	CreamURL  = registrationResponse[1].getCreamURL()
	CreamURL2  = registrationResponse2[1].getCreamURL()
	CreamJID  = registrationResponse[1].getCreamJobID()
	CreamJID2  = registrationResponse2[1].getCreamJobID()
	#CreamJID  = creamURL + "/" + CreamJID
	#CreamJID2  = creamURL2 + "/" + CreamJID2

	registrationResponse[1].getProperties( properties )
	registrationResponse2[1].getProperties( properties2 )
	ISB_upload_url = properties["CREAMInputSandboxURI"]
	ISB_upload_url2 = properties2["CREAMInputSandboxURI"]

	print "Cream Job ID=[" + CreamJID + "]"
	print "Cream Job2 ID=[" + CreamJID2 + "]"
	print "InputSandBox Upload URL=[" + ISB_upload_url + "]"
	print "InputSandBox2 Upload URL=[" + ISB_upload_url2 + "]"

	return 0


def start():

	global CreamJID
	global CreamURL
	global delegationID
	global leaseID
	global connection_timeout
	global serviceHost

	print "\n==> Job starting"

	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(CreamJID, CreamURL, stdVectorJobPropertyWrapper() )

	JobVector = stdVectorJobIdWrapper()
	JobVector.append( job1 )

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

	serviceAddress = serviceHost + "/ce-cream/services/CREAM2"

	try:
		#
		# /tmp/x509up_u501 is a proxy file generated with voms-proxy-init
		#
		creamClient.setCredential( "/tmp/x509up_u1000" )
		creamClient.execute( serviceAddress )
	except Exception, ex:
		print "FATAL: ", ex
		return 1

	print "Job started"
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


def status():

	global delegationID
	global connection_timeout
	global serviceHost
	global JDL
	global leaseID
	global delegationProxy
	global autostart
	global CreamJID
	global CreamURL

	print "\n==> Job status"

	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(CreamJID, CreamURL, stdVectorJobPropertyWrapper() )

	JobVector = stdVectorJobIdWrapper()

	#
	#  Let's put all jobs to query in the JobVector array. An empty array means we're
	#  asking CREAM for status of ALL jobs present in the CE.
	#
	JobVector.append( job1 )

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

	serviceAddress = serviceHost + "/ce-cream/services/CREAM2"


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
			print "For Job [%s] CREAM returned a fault: [%s]" % ( jobId, job[1] )
			return 0

def info():

	global delegationID
	global connection_timeout
	global serviceHost
	global JDL
	global leaseID
	global delegationProxy
	global autostart
	global CreamJID
	global CreamURL

	print "\n==> Job info"

	#
	#  Build a JobIdWrapper object basing on the Cream Job ID. Let's ignore for now the property array...
	#
	job1 = JobIdWrapper(CreamJID, CreamURL, stdVectorJobPropertyWrapper() )

	JobVector = stdVectorJobIdWrapper()

	#
	#  Let's put all jobs to query in the JobVector array. An empty array means we're
	#  asking CREAM for status of ALL jobs present in the CE.
	#
	JobVector.append( job1 )

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

	#
	#  This class will contain the result (as sent back from the CREAM CE) of the start of the jobs
	#
	result = ResultWrapper()

	#
	#  Build the client pointer
	#

	Iresult = InfoArrayResult()

	creamClient = CreamProxyFactory.make_CreamProxyInfo( jfw, Iresult, connection_timeout )

	#
	# [...]
	#
	# BE CAREFUL !!!
	#
	# Please Check the 'NULLNESS' of the creamClient variable and take the proper action if it is NULL
	#
	# [...]
	#

	serviceAddress = serviceHost + "/ce-cream/services/CREAM2"

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
	#  See the JobInfoWrapper documentation
	#

	for jobId in Iresult.keys():
		job = Iresult[jobId]

		if job[0] == JobInfoWrapper.OK: # Information current job has been returned
			theJob = job[1]

			#
			# See the JobInfoWrapper documentation for the long list of the 'getter' methods and what they return...
			# Invoke them on the object "theJob" here to print the relevant information.
			# ...
			# ...
			# for example:
			#
			status = stdVectorJobStatusWrapper()
			theJob.getStatus(status)
			print status[0].getStatusName()

		else:
			print "For Job [%s] CREAM returned a fault: [%s]" % ( jobId, job[2] )
			return 0


def stop():

	print "\n==> Job stopping"



if __name__ == "__main__":
    try:
        delegate()
        register()
#        registerMany()
        start()
        status()
        info()
        stop()
        status()
        print "Test successfull!"
    except Exception, ex:
        print "Test failed!"
        print ex

