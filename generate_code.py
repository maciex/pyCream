#!/usr/bin/python2.6

import os, time

import pdb

from pygccxml import parser
from pygccxml.parser import config
from pygccxml.declarations.matchers import access_type_matcher_t

from pyplusplus import messages 
from pyplusplus import module_builder
from pyplusplus import function_transformers as FT
from pyplusplus.module_builder import directory_cache_t
from pyplusplus.module_builder import call_policies
#from pyplusplus.decl_wrappers import doxygen

import environment

_DEBUG = False

#
# the 'main'function
#
def generate_code():

	#
	# Use GCCXML to create the controlling XML file.
	# If the cache file (../cache/*.xml) doesn't exist it gets created, otherwise it just gets loaded
	# NOTE: If you update the source library code you need to manually delete the cache .XML file
	#
	#parser_conf = parser.project_reader.file_configuration_t( start_with_declarations=environment.namespaces )
	defined_symbols = []  
	undefine_symbols = []

	xml_cached_fc = parser.create_cached_source_fc(
			os.path.join( environment.root_dir, "python_Cream.h" )
			, environment.cache_file
			)
	mb = module_builder.module_builder_t(
			[ xml_cached_fc ]
			, working_directory=environment.root_dir
			, include_paths=environment.include_dirs
			, define_symbols=defined_symbols
			, undefine_symbols=undefine_symbols
			, indexing_suite_version=2
			)

	# Register boost::tuples
	mb.add_registration_code( 'boost::python::register_tuple< boost::tuple<glite::ce::cream_client_api::soap_proxy::JobIdWrapper::RESULT, glite::ce::cream_client_api::soap_proxy::JobIdWrapper, std::string>  >();' );
	mb.add_registration_code( 'boost::python::register_tuple< boost::tuple<glite::ce::cream_client_api::soap_proxy::JobStatusWrapper::RESULT, glite::ce::cream_client_api::soap_proxy::JobStatusWrapper, std::string> >();' );
	mb.add_registration_code( 'boost::python::register_tuple< boost::tuple<glite::ce::cream_client_api::soap_proxy::JobInfoWrapper::RESULT, glite::ce::cream_client_api::soap_proxy::JobInfoWrapper, std::string> >();' );

	# Expose classes
	mb.classes( lambda cls: cls.name in environment.classes ).include()
        # Expose enumerations
	mb.enumerations( lambda cls: cls.name in environment.enumerations ).include()
        # Expose functions
        mb.free_funs( lambda fun: fun.name in environment.functions ).include()

	# Exclude all protected functions
	mb.calldefs( access_type_matcher_t( 'protected' ) ).exclude()

	# Exclude some functions
	# I think it's a quite new function (even not yet documented, so no idea which params are in/out)
	mb.class_( 'CreamProxyFactory' ).mem_fun( 'make_CreamProxy_QueryEvent' ).exclude()

	# Take care of call policies for some functions
	# CreamProxyFactory
	mb.class_( name='CreamProxyFactory' ).member_functions( lambda decl: decl.name.startswith( 'make_CreamProxy' ) ).call_policies = call_policies.return_value_policy( call_policies.manage_new_object )

	# Translate exceptions
	for ex in environment.exception_classes:
		exception = mb.class_( ex )
		exception.translate_exception_to_string( ex, 'exc.what()')

	# Function transformations

	# JobPropertyWrapper has protected operator=
	mb.class_( 'JobPropertyWrapper' ).noncopyable = True

	# Temporarily disable some warnings (messages showed by py++ below)

	# Well, don't you want to see what is going on?
	#	mb.print_declarations()

	#def my_doc_extractor( decl ):
		#	print decl.location.file_name + str( decl.location.line )
		#	return decl.location.file_name + str( decl.location.line )

	# Creating code creator. After this step you should not modify/customize declarations.
	# Additionaly extract Doxygen like documentation
	#mb.build_code_creator( module_name='Cream', doc_extractor=doxygen.doxygen_doc_extractor() )
	mb.build_code_creator( module_name='Cream' )
	#mb.build_code_creator( module_name='Cream', doc_extractor=my_doc_extractor )


	mb.code_creator.add_include( 'pyplusplus_converters/tuples.hpp' )
	mb.code_creator.precompiled_header = 'boost/python.hpp'

	# It is common requirement in software world - each file should have license
	mb.code_creator.license = '// GPLv3 License'

	# I don't want absolute includes within code
	mb.code_creator.user_defined_directories.append( os.path.abspath('.') )


	# Writing code to file.
	mb.write_module( "Cream.cpp" )


if __name__ == '__main__':
	start_time = time.time()
	cpu_start_time = time.clock()
	#common_utils.setup_logging ("log.out")
	if _DEBUG:
		pdb.run('generate_code()')
	else:
		generate_code()
		print 'PyCream source code was created ( %f min, %f min of CPU time ).' % (  ( time.time() - start_time )/60, ( time.clock() - cpu_start_time )/60 )

