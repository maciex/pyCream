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

