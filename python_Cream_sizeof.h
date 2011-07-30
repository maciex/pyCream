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


size_t size = 0;
size = sizeof( AbsCreamProxy );
size = sizeof( CreamProxyFactory );
size = sizeof( EventWrapper );
//size = sizeof( JobCommandWrapper );
size = sizeof( JobDescriptionWrapper );
size = sizeof( JobFilterWrapper );
size = sizeof( JobIdWrapper );
size = sizeof( JobInfoWrapper );
size = sizeof( JobPropertyWrapper );
size = sizeof( JobStatusWrapper );
size = sizeof( ResultWrapper );
size = sizeof( ServiceInfoWrapper );

AbsCreamProxy *absCreamProxy = CreamProxyFactory::make_CreamProxyDelegate( "a", 1 );
delete absCreamProxy;

CreamProxyFactory creamProxyFactory( );
EventWrapper eventWrapper( "a", "b", 1, std::vector<CREAMTYPES__Property*>() );
// Class constructor is protected, no idea how to create an object
//JobCommandWrapper jobCommandWrapper();
JobDescriptionWrapper jobDescriptionWrapper( "a", "b", "c", "d", false, "e" );
JobFilterWrapper jobFilterWrapperr( std::vector< JobIdWrapper >(), std::vector< std::string >(), 1, 2, "a", "b" );
JobIdWrapper jobIdWrapper( "a", "b", std::vector<JobPropertyWrapper>() );
JobInfoWrapper jobInfoWrapper( );
JobPropertyWrapper jobPropertyWrapper( "a", "b" );
JobStatusWrapper jobStatusWrapper( );
ResultWrapper resultWrapper( );
ServiceInfoWrapper serviceInfoWrapper( );


// Cream CE exceptions
size = sizeof( auth_ex );
size = sizeof( ceid_syntax_ex );
size = sizeof( classad_syntax_ex );
size = sizeof( file_ex );
size = sizeof( invalidTimestamp_ex );
size = sizeof( soap_ex );
size = sizeof( soap_runtime_ex );
size = sizeof( BaseException );
size = sizeof( AuthorizationException );
size = sizeof( ConnectionTimeoutException );
size = sizeof( DelegationException );
size = sizeof( GenericException );
size = sizeof( GridProxyDelegationException );
size = sizeof( InternalException );
size = sizeof( InvalidArgumentException );
size = sizeof( JobStatusInvalidException );
size = sizeof( JobSubmissionDisabledException );
size = sizeof( JobUnknownException );
size = sizeof( NoSuitableResourceException );
size = sizeof( OperationNotSupportedException );

auth_ex auth_ex( "a" );
ceid_syntax_ex ceid_syntax_ex( "a" );
classad_syntax_ex classad_syntax_ex( "a" );
file_ex file_ex( "a" );
invalidTimestamp_ex invalidTimestamp_ex( "a" );
soap_ex soap_ex( "a" );
soap_runtime_ex soap_runtime_ex( "a" );
BaseException baseException( "a", "b", "c", "d", 1 );
AuthorizationException authorizationException( "a", "b", "c", "d", 1 );
ConnectionTimeoutException connectionTimeoutException( "a" );
DelegationException delegationException( "a" );
GenericException genericException( "a", "b", "c", "d", 1 );
GridProxyDelegationException gridProxyDelegationException( "a", "b", "c", "d", 1 );
InternalException internalException( "a" );
InvalidArgumentException invalidArgumentException( "a", "b", "c", "d", 1 );
JobStatusInvalidException jobStatusInvalidException( "a", "b", "c", "d", 1 );
JobSubmissionDisabledException jobSubmissionDisabledException( "a", "b", "c", "d", 1 );
JobUnknownException jobUnknownException( "a", "b", "c", "d", 1 );
NoSuitableResourceException noSuitableResourceException( "a", "b", "c", "d", 1 );
OperationNotSupportedException operationNotSupportedException( "a", "b", "c", "d", 1 );

// STL
size = sizeof( stdPairLongLong );
size = sizeof( stdPairStringLong );
size = sizeof( stdPairStringString );
stdPairLongLong stdPairLongLong();
stdPairStringLong stdPairStringLong();
stdPairStringString stdPairStringString();

size = sizeof( stdMapStringString );
stdMapStringString stdMapStringString();

size = sizeof( stdVectorString );
stdVectorString stdVectorString();

size = sizeof( stdAllocatorChar );
stdAllocatorChar stdAllocatorChar();

// boost::tuple
size = sizeof( TupleJobIdWrapper );
size = sizeof( TupleJobStatusWrapper );
size = sizeof( TupleJobInfoWrapper );

TupleJobIdWrapper tupleJobIdWrapper();
TupleJobStatusWrapper tupleJobStatusWrapper();
TupleJobInfoWrapper tupleJobInfoWrapper();

size = sizeof( RegisterArrayResult );
size = sizeof( StatusArrayResult );
size = sizeof( InfoArrayResult );
size = sizeof( RegisterArrayRequest );

RegisterArrayResult registerArrayResult();
StatusArrayResult statusArrayResult();
InfoArrayResult infoArrayResult();
RegisterArrayRequest registerArrayRequest();

size = sizeof( stdVectorJobIdWrapper );
size = sizeof( stdVectorJobPropertyWrapper );
size = sizeof( stdVectorJobStatusWrapper );
stdVectorJobIdWrapper stdVectorJobIdWrapper();
stdVectorJobPropertyWrapper stdVectorJobPropertyWrapper();
stdVectorJobStatusWrapper stdVectorJobStatusWrapper();

