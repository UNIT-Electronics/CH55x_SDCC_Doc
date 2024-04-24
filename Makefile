# File Names
NAME = ROUST
file = src
# Symbolic Targets
help:
	@echo "Use the following commands:"
	@echo "make all     create files and build the project"
	@echo "make env     create the project environment"
	@echo "make clean   remove all  files"


all: build

build:
	@cd src && ./make.bat clean && ./make.bat html
	@cp -R src/build/html/* docs
	@echo "Documentation built and copied to docs"
