#ifndef __CREAM_PYTHON_H___
#define __CREAM_PYTHON_H__

//See best practices section in Py++ documentation
#include <iostream>

#include <string>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <exception>


#include "python_Cream_masterlist.h"


// First we create a magic namespace to hold all our aliases
namespace pyplusplus {
	namespace aliases {
		using namespace glite::ce::cream_client_api::cream_exceptions;
		using namespace glite::ce::cream_client_api::job_statuses;
		using namespace glite::ce::cream_client_api::soap_proxy;
		using namespace glite::ce::cream_client_api::util;
		using namespace glite::ce::cream_client_api::util::CEUrl;
#include "python_Cream_aliases.h"
	}
}

// Expos everything needed (and more) to ensure GCCXML makes them visible to Py++
namespace python_Cream {
	namespace details {
		inline void instantiate() {
			using namespace glite::ce::cream_client_api::cream_exceptions;
			using namespace glite::ce::cream_client_api::job_statuses;
			using namespace glite::ce::cream_client_api::soap_proxy;
			using namespace glite::ce::cream_client_api::util;
			using namespace glite::ce::cream_client_api::util::CEUrl;

			using namespace pyplusplus::aliases;
#include "python_Cream_sizeof.h"
		}
	}
}

#endif // __CREAM_PYTHON_H__

