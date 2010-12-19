
#BOOST_ROOT=
#BOOST_BUILD_PATH=
BUILD_TYPE=release

GEN_SCRIPT = generate_code.py

PYCPP_SCRIPTS = \
	environment.py \
	generate_code.py

HEADERS = \
	python_Cream.h \
	python_Cream_aliases.h \
	python_Cream_masterlist.h \
	python_Cream_precompiled.h \
	python_Cream_sizeof.h


GENERATED = \
	cache \
	indexing_suite \
	Cream.cpp \
	exposed_decl.pypp.txt \
	named_tuple.py \
	environment.pyc


./bin/gcc-4.1.2/$(BUILD_TYPE)/Cream.so: Jamroot boost-build.jam temp_fix
	BOOST_ROOT=$(BOOST_ROOT) BOOST_BUILD_PATH=$(BOOST_BUILD_PATH) bjam -d+2 $(BUILD_TYPE)

Cream.cpp: $(HEADERS) $(PYCPP_SCRIPTS) temporary_fix.sh
	python2.7 $(GEN_SCRIPT)

temp_fix: Cream.cpp temporary_fix.sh
	./temporary_fix.sh Cream.cpp

test: ./bin/gcc-4.1.2/$(BUILD_TYPE)/Cream.so
	PYTHONPATH="./bin/gcc-4.1.2/$(BUILD_TYPE)" python2.7 examples/test.py

clean:
	rm -fr $(GENERATED)

cleanall: clean
	rm -fr ./bin

