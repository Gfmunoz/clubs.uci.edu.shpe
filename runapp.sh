#!/bin/bash

if [[ "$VIRTUAL_ENV" != "" ]]
then
	echo "Running in $VIRTUAL_ENV"
	export FLASK_APP=app
	export FLASK_ENV=development
	flask create_tables
	flask run
else
	echo "Not running in (venv)"
	echo "Launching (venv)"
	. venv/bin/activate
	export FLASK_APP=app
	export FLASK_ENV=development
	flask create_tables
	flask run
fi

exit 0
