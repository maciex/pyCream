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

