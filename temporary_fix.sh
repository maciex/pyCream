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

CREAM_CPP=$1

sed -i '/stdVectorJobPropertyWrapper_exposer.def( bp::indexing::vector_suite< std::vector< glite::ce::cream_client_api::soap_proxy::JobPropertyWrapper > >() );/d' ${CREAM_CPP} || exit 1
sed -i '/list_less__std_scope_pair_less_glite_scope_ce_scope_cream_client_api_scope_soap_proxy_scope_JobIdWrapper_comma__std_scope_string_greater___greater__exposer.def( bp::indexing::list_suite< std::list< std::pair<glite::ce::cream_client_api::soap_proxy::JobIdWrapper, std::string> > >() );/d' ${CREAM_CPP} || exit 1

