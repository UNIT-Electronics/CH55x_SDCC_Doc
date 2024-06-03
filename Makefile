# File Names
NAME = ROUST
file = src
# Symbolic Targets
help:
	@echo "Use the following commands:"
	@echo "make all     create files and build the project"
	@echo "make pdfr     create the project environment"
	@echo "make clean   remove all  files"


all: build

build:
	@rm -rf docs && mkdir docs
	@cd src && ./make.bat clean && ./make.bat html
	@cp -R src/build/html/* docs && touch docs/.nojekyll
	@echo "Documentation built and copied to docs"

pdfr:
	@rm -rf pdf && mkdir pdf
	@cd src && ./make.bat clean && sphinx-build -M latexpdf source ../pdf	
	@echo "PDF built and copied to docs"
	@make build

clean:
	@rm -rf docs
	@rm -rf pdf
	# @rm -rf src
	@echo "All files removed"



	