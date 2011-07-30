/*  pyCream - CREAM Client API Python
 
   Copyright (C) 2010, 2011  Maciej Sitarz
 
   Written by Maciej Sitarz
 
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
 
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
 
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>. */

// STL
typedef std::pair< long, long > stdPairLongLong;
typedef std::pair< std::string, long > stdPairStringLong;
typedef std::pair< std::string, std::string > stdPairStringString;

typedef std::map< std::string, std::string > stdMapStringString;

typedef std::vector< std::string > stdVectorString;
typedef std::allocator< char > stdAllocatorChar;


// Cream typedef classes
typedef boost::tuple< JobIdWrapper::RESULT, JobIdWrapper, std::string > TupleJobIdWrapper;
typedef boost::tuple< JobStatusWrapper::RESULT, JobStatusWrapper, std::string > TupleJobStatusWrapper;
typedef boost::tuple< JobInfoWrapper::RESULT, JobInfoWrapper, std::string > TupleJobInfoWrapper;

typedef std::map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string > > RegisterArrayResult;
typedef std::map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string > > StatusArrayResult;
typedef std::map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string > > InfoArrayResult;

typedef std::vector< JobIdWrapper > stdVectorJobIdWrapper;
typedef std::vector< JobPropertyWrapper > stdVectorJobPropertyWrapper;
typedef std::vector< JobStatusWrapper > stdVectorJobStatusWrapper;

typedef std::list< JobDescriptionWrapper* > RegisterArrayRequest;

