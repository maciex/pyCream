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

import os

_DEBUG = True

#
# 
#
module_name = "Cream"
namespaces = [
        "glite::ce::cream_client_api::cream_exceptions"
        , "glite::ce::cream_client_api::job_statuses"
        , "glite::ce::cream_client_api::soap_proxy"
        , "glite::ce::cream_client_api::util"
        , "glite::ce::cream_client_api::util::CEUrl"
        ]

headers = [ "python_Cream.h" ] 

classes = [
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

# Cream enumerations
enumerations = [
        'job_status'
        ]

# Cream functions
functions = [
        'getStatusNum'
        , 'isFailed'
        , 'isFinished'
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

#
#
#
include_dirs = [ 
        os.getcwd()
        , "/usr/include"
        , "/opt/b2cgs/python2.7/include/python2.7"
        , "/opt/glite/include"
        , "/opt/glite/include/glite/ce/cream-client-api-c"
        ]

#
#
#
root_dir = "./"
cache_dir = os.path.join( root_dir, "cache", )
cache_file = os.path.join( cache_dir, "Cream_cache.xml" )

