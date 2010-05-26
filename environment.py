#!/usr/bin/python

import os

_DEBUG = True

#
# 
#
module_name = "Cream"
namespaces = [
        "glite::ce::cream_client_api::util"
        , "glite::ce::cream_client_api::util::CEUrl"
        , "glite::ce::cream_client_api::soap_proxy"
        , "glite::ce::cream_client_api::cream_exceptions"
        ]

headers = [ "python_Cream.h" ] 

include_classes = [
        # Include some STL templates
        'pair<long, long>'
        , 'pair<std::string, long>'
        , 'pair<std::string, std::string>'

        , 'map<std::string, std::string>'

        , 'vector<std::string>'
        , 'allocator<char>'

        , 'map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> >'
        , 'map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string> >'
        , 'map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string> >'

        , 'list<JobDescriptionWrapper*>'

        , 'vector<JobIdWrapper>'
        , 'vector<JobPropertyWrapper>'
        , 'vector<JobStatusWrapper>'


        , 'AbsCreamProxy'
        , 'CreamProxyFactory'
        , 'EventWrapper'
        # Class constructor is protected, no idea how to create an object
        #		, 'JobCommandWrapper'
        , 'JobDescriptionWrapper'
        , 'JobFilterWrapper'
        , 'JobIdWrapper'
        , 'JobInfoWrapper'
        , 'JobPropertyWrapper'
        , 'JobStatusWrapper'
        , 'ResultWrapper'
        , 'ServiceInfoWrapper'
        ]

# Cream exceptions
exception_classes = [
        'auth_ex'
        , 'ceid_syntax_ex'
        , 'classad_syntax_ex'
        , 'file_ex'
        , 'invalidTimestamp_ex'
        , 'soap_ex'
        , 'soap_runtime_ex'
        , 'BaseException'
        , 'AuthorizationException'
        , 'ConnectionTimeoutException'
        , 'DelegationException'
        , 'GenericException'
        , 'GridProxyDelegationException'
        , 'InternalException'
        , 'InvalidArgumentException'
        , 'JobStatusInvalidException'
        , 'JobSubmissionDisabledException'
        , 'JobUnknownException'
        , 'NoSuitableResourceException'
        , 'OperationNotSupportedException'

        #		, 'RegisterArrayResult'
        #		, 'StatusArrayResult'
        #		, 'InfoArrayResult'
        #		, 'RegisterArrayRequest'
        ]

exclude_classes = [ ]

#
#
#
include_dirs = [ 
        os.getcwd()
        , "/usr/include"
        , "/usr/include/python2.4"
        , "/opt/glite/include"
        , "/opt/glite/include/glite/ce/cream-client-api-c"
        ]

#
#
#
root_dir = "./"
cache_dir = os.path.join( root_dir, "cache", )
cache_file = os.path.join( cache_dir, "Cream_cache.xml" )

