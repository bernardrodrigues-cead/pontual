# Makefile
#
# Frederico Sales
# <frederico.sales@uab.ufjf.br>
# 2022
#

#
## settings
#
.ONESHELL:
.PHONY: all help run clean migrate migrations superuser clear install update shell

#
## PATH's
#
SRC          := ./
VENV_BIN_DIR := ~/.venvs/cead-pontual/bin
ACTIVATE     := ${VENV_BIN_DIR}/activate
PYTHON_BIN   := ${VENV_BIN_DIR}/python
PIP_BIN      := ${VENV_BIN_DIR}/pip
MANAGE       := ${SRC}/manage.py
REQUIREMENTS := requirements/requirements.txt

#
## targets
#

#: Do nothing.
all:
	@clear
	@echo ""
	@echo "This target do nothing."
	@echo "Try make help"
	@echo ""


#: Display help and targets.
help:
	@clear
	@echo "Display this help, and targets."
	@echo ""
	@echo "--------------------------------------------------"
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
     | grep -v -- -- \
     | sed 'N;s/\n/###/' \
     | sed -n 's/^#: \(.*\)###\(.*\):.*/\2###\1/p' \
     | column -t  -s '###'
	 @echo "--------------------------------------------------"
	@echo ""


#: Run django application on default port: 8000
run:
	${PYTHON_BIN} ${MANAGE} runserver 0.0.0.0:8000


#: Light cleaning.
clean:
	@clear
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".DS_Store" -exec rm -rf {} +


#: Heavy cleaning.
clear:
	@clear
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".DS_Store" -exec rm -rf {} +
	@find . -name "[0][0]*.py" -exec rm -f {} +


#: Migration
migrations:
	${PYTHON_BIN} ${MANAGE} makemigrations


#: Migrate
migrate:
	${PYTHON_BIN} ${MANAGE} migrate


#: Update the project requirements.
update:
	${PIP_BIN} install -U -r ${UPDATE}


#: Create the superuser.
superuser:
	$(PYTHON_BIN) ${MANAGE} createsuperuser


#: Duh self explanatory...
install:
	${PIP_BIN} install -r ${REQUIREMENTS}


#: Run the freaking shell.
shell:
 #   ${PYTHON_BIN} ${MANAGE} shell

 