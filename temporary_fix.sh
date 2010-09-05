
CREAM_CPP=$1

sed -i '/stdVectorJobPropertyWrapper_exposer.def( bp::indexing::vector_suite< std::vector< glite::ce::cream_client_api::soap_proxy::JobPropertyWrapper > >() );/d' ${CREAM_CPP} || exit 1
sed -i '/list_less__std_scope_pair_less_glite_scope_ce_scope_cream_client_api_scope_soap_proxy_scope_JobIdWrapper_comma__std_scope_string_greater___greater__exposer.def( bp::indexing::list_suite< std::list< std::pair<glite::ce::cream_client_api::soap_proxy::JobIdWrapper, std::string> > >() );/d' ${CREAM_CPP} || exit 1

