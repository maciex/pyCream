
/*sizeof( CREAMTYPES__Command );
sizeof( CREAMTYPES__Event );
sizeof( CREAMTYPES__JobDescription );
sizeof( CREAMTYPES__JobFilter );
sizeof( CREAMTYPES__JobId );
sizeof( CREAMTYPES__JobInfo );
sizeof( CREAMTYPES__Property );
sizeof( CREAMTYPES__Lease );
sizeof( CREAMTYPES__ServiceInfo );
sizeof( CREAMTYPES__Status );

CREAMTYPES__Command creamtypes__Command();
CREAMTYPES__Event creamtypes__Event();
CREAMTYPES__JobDescription creamtypes__JobDescription();
CREAMTYPES__JobFilter creamtypes__JobFilter();
CREAMTYPES__JobId creamtypes__JobId();
CREAMTYPES__JobInfo creamtypes__JobInfo();
CREAMTYPES__Lease creamtypes__Lease();
CREAMTYPES__Property creamtypes__Property();
CREAMTYPES__ServiceInfo creamtypes__ServiceInfo();
CREAMTYPES__Status creamtypes__Status();
*/
sizeof( AbsCreamProxy );
sizeof( CreamProxyFactory );
sizeof( EventWrapper );
//sizeof( JobCommandWrapper );
sizeof( JobDescriptionWrapper );
sizeof( JobFilterWrapper );
sizeof( JobIdWrapper );
sizeof( JobInfoWrapper );
sizeof( JobPropertyWrapper );
sizeof( JobStatusWrapper );
sizeof( ResultWrapper );
sizeof( ServiceInfoWrapper );

AbsCreamProxy *absCreamProxy = CreamProxyFactory::make_CreamProxyDelegate( "a", 1 );
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
sizeof( auth_ex );
sizeof( ceid_syntax_ex );
sizeof( classad_syntax_ex );
sizeof( file_ex );
sizeof( invalidTimestamp_ex );
sizeof( soap_ex );
sizeof( soap_runtime_ex );
sizeof( BaseException );
sizeof( AuthorizationException );
sizeof( ConnectionTimeoutException );
sizeof( DelegationException );
sizeof( GenericException );
sizeof( GridProxyDelegationException );
sizeof( InternalException );
sizeof( InvalidArgumentException );
sizeof( JobStatusInvalidException );
sizeof( JobSubmissionDisabledException );
sizeof( JobUnknownException );
sizeof( NoSuitableResourceException );
sizeof( OperationNotSupportedException );

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
sizeof( std::pair<long, long> );
sizeof( std::pair<std::string, std::string> );
sizeof( std::pair<std::string, long> );
sizeof( std::allocator<char> );

sizeof( std::list<JobDescriptionWrapper*> );

sizeof( boost::tuple<std::string, std::string, std::string> );
sizeof( boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> );
sizeof( std::map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> > );

sizeof( std::map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string> > );
sizeof( std::map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string> > );

