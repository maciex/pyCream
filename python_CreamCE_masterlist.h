
//#include <glite/ce/cream-client-api-c/cream_client_soapStub.h>

// Cream CE classes
#include <glite/ce/cream-client-api-c/AbsCreamProxy.h>
#include <glite/ce/cream-client-api-c/CEUrl.h>
#include <glite/ce/cream-client-api-c/ConfigurationManager.h>
#include <glite/ce/cream-client-api-c/CreamProxyFactory.h>
#include <glite/ce/cream-client-api-c/CreamProxy_Impl.h>
#include <glite/ce/cream-client-api-c/EventWrapper.h>
#include <glite/ce/cream-client-api-c/ExceptionFactory.h>
// Class constructor is protected, no idea how to create an object
//#include <glite/ce/cream-client-api-c/JobCommandWrapper.h>
#include <glite/ce/cream-client-api-c/JobDescriptionWrapper.h>
#include <glite/ce/cream-client-api-c/JobFilterWrapper.h>
#include <glite/ce/cream-client-api-c/JobIdWrapper.h>
#include <glite/ce/cream-client-api-c/JobInfoWrapper.h>
#include <glite/ce/cream-client-api-c/JobPropertyWrapper.h>
#include <glite/ce/cream-client-api-c/JobStatusWrapper.h>
#include <glite/ce/cream-client-api-c/ResultWrapper.h>
#include <glite/ce/cream-client-api-c/ServiceInfoWrapper.h>
#include <glite/ce/cream-client-api-c/VOMSWrapper.h>
#include <glite/ce/cream-client-api-c/certUtil.h>

//#include <glite/ce/cream-client-api-c/creamApiLogger.h>
//#include <glite/ce/cream-client-api-c/cream_client_soapH.h>

// Cream CE exceptions
#include <glite/ce/cream-client-api-c/auth_ex.h>
#include <glite/ce/cream-client-api-c/ceid_syntax_ex.h>
#include <glite/ce/cream-client-api-c/classad_syntax_ex.h>
#include <glite/ce/cream-client-api-c/file_ex.h>
#include <glite/ce/cream-client-api-c/invalidTimestamp_ex.h>
#include <glite/ce/cream-client-api-c/soap_ex.h>
#include <glite/ce/cream-client-api-c/soap_runtime_ex.h>
#include <glite/ce/cream-client-api-c/AuthorizationException.h>
#include <glite/ce/cream-client-api-c/BaseException.h>
#include <glite/ce/cream-client-api-c/ConnectionTimeoutException.h>
#include <glite/ce/cream-client-api-c/DelegationException.h>
#include <glite/ce/cream-client-api-c/GenericException.h>
#include <glite/ce/cream-client-api-c/GridProxyDelegationException.h>
#include <glite/ce/cream-client-api-c/InternalException.h>
#include <glite/ce/cream-client-api-c/InvalidArgumentException.h>
#include <glite/ce/cream-client-api-c/JobStatusInvalidException.h>
#include <glite/ce/cream-client-api-c/JobSubmissionDisabledException.h>
#include <glite/ce/cream-client-api-c/JobUnknownException.h>
#include <glite/ce/cream-client-api-c/NoSuitableResourceException.h>
#include <glite/ce/cream-client-api-c/OperationNotSupportedException.h>

