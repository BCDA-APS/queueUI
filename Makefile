################################################################################
# QSUI Makefile
################################################################################

checks: # Runs all the pre-commit checks
	@pre-commit install
	@pre-commit run --all-files || { echo "Checking fixes\n" ; pre-commit run --all-files; }

build: build-python # Builds the project

################
# Python Rules #
################

# (Make sure you've installed PDM)

init-python: pdm.lock deps # Installs the python environment (requires PDM)

build-python: init-python # Builds the pypi package for APP_NAME
	pdm build

###############################
# Python Dependency Managment #
###############################

pdm.lock: pyproject.toml # Generates the pdm.lock file
	pdm install --group :all

requirements/*.txt: pdm.lock
	pdm export --without-hashes --group :all -o requirements/requirements.txt

.PHONY += deps
deps: requirements/*.txt # Generates the requirements files for APP_NAME
	pdm install --group :all
