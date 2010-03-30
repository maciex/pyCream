#!/usr/bin/python

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
from pyplusplus.decl_wrappers import doxygen

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
				, environment.cache_file )
	mb = module_builder.module_builder_t(
				  [ xml_cached_fc ]
				, working_directory=environment.root_dir
				, include_paths=environment.include_dirs
				, define_symbols=defined_symbols
				, undefine_symbols=undefine_symbols
				, indexing_suite_version=2
				)
# TODO Problably not needed
#	mb = module_builder.module_builder_t(
#				files=environment.headers
#				, working_directory=environment.root_dir
#				, include_paths=environment.include_dirs
#				, define_symbols=defined_symbols
#				, undefine_symbols=undefine_symbols
#				, cache=directory_cache_t( environment.cache_dir )
#				, indexing_suite_version=2 )

	#1/0
	# Include Cream classes
	mb.classes( lambda cls: cls.name in environment.include_classes ).include()

	# Include Cream typedef classes
	#mb.class_( 'map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> >' ).include()
	#mb.class_( 'map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string> >' ).include()
	#mb.class_( 'map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string> >' ).include()
	#mb.class_( 'list<JobDescriptionWrapper*>' ).include()

	#for class_name in environment.include_classes:
	#	print "Including class '%s'" % class_name
	#	mb.class_( name=class_name ).include()

	# Exclude Cream CE classes
	#mb.classes( lambda cls: cls.name in environment.exclude_classes ).exclude()
#	for class_name in environment.exclude_classes:
#		print "Excluding class '%s'" % class_name
#		mb.class_( name=class_name ).exclude()

	# Exclude all protected functions
	mb.calldefs( access_type_matcher_t( 'protected' ) ).exclude()

	# Exclude some functions
	# I think it's a quite new function (even not yet documented, so no idea which params are in/out)
	mb.class_( 'CreamProxyFactory' ).mem_fun( 'make_CreamProxy_QueryEvent' ).exclude()

	# Take care of call policies for some functions

	# CreamProxyFactory
	for fun in mb.class_( name='CreamProxyFactory' ).member_functions( lambda decl: decl.name.startswith( 'make_CreamProxy' ) ):
		print "Setting call policy 'return_value_policy( manage_new_object )' for function: '%(parent)s::%(name)s'" % { 'parent' : fun.parent.name, 'name' : fun.name }
		fun.call_policies = call_policies.return_value_policy( call_policies.manage_new_object )

	# Function transformations

	# JobPropertyWrapper has protected operator=
	#mb.class_( 'JobPropertyWrapper' ).noncopyable = True

# Temporarily disable some warnings (messages showed by py++ below)

# TODO If needed write those functions
#messages.disable( messages.W1023 )
#> warning W1023: Py++ will generate class wrapper - there are few functions that
#> should be redefined in class wrapper. The functions are: getDescription,
#> getErrorCode, getFaultCause, getMethodName, getTimeStamp, what.

# TODO No idea what to do :|
#messages.disable( messages.W1031 )
#> warning W1031: Py++ will generate class wrapper - user asked to expose non -
#> public member function "AbsCreamProxy"

# TODO No idea what to do :|
#messages.disable( messages.W1046 )
#> warning W1046: The virtual function was declared with empty throw. Adding the
#> ability to override the function from Python breaks the exception
#> specification. The function wrapper can throw any exception. In case of
#> exception in run-time, the behaviour of the program is undefined!

# TODO Simple fix XXX http://www.language-binding.net/pyplusplus/documentation/functions/transformation/transformation.html?highlight=function%20transformation
#messages.disable( messages.W1009 )
#> execution error W1009: The function takes as argument (name=execTime, pos=6) non-const reference to Python immutable type - function could not be called from Python. Take a look on "Function Transformation" functionality and define the transformation.


	# Well, don't you want to see what is going on?
	mb.print_declarations()

	#def my_doc_extractor( decl ):
	#	print decl.location.file_name + str( decl.location.line )
	#	return decl.location.file_name + str( decl.location.line )

	# Creating code creator. After this step you should not modify/customize declarations.
	# Additionaly extract Doxygen like documentation
	#mb.build_code_creator( module_name='Cream', doc_extractor=doxygen.doxygen_doc_extractor() )
	mb.build_code_creator( module_name='Cream' )
	#mb.build_code_creator( module_name='Cream', doc_extractor=my_doc_extractor )


	mb.code_creator.precompiled_header = 'boost/python.hpp'

	# It is common requirement in software world - each file should have license
	mb.code_creator.license = '// GPLv3 License'

	# I don't want absolute includes within code
	mb.code_creator.user_defined_directories.append( os.path.abspath('.') )


	# Writing code to file.
	mb.write_module( "Cream.cpp" )
	#mb.split_module(
	#		  "src"
	#		, on_unused_file_found=os.remove
	#		, use_files_sum_repository=True
	#		)


if __name__ == '__main__':
	start_time = time.time()
	cpu_start_time = time.clock()
	#common_utils.setup_logging ("log.out")
	if _DEBUG:
		pdb.run('generate_code()')
	else:
		generate_code()
		print 'PyCream source code was created ( %f min, %f minof CPU time ).' % (  ( time.time() - start_time )/60, ( time.clock() - cpu_start_time )/60 )

