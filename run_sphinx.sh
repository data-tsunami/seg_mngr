#!/bin/bash

if [ "$VIRTUAL_ENV" = "" ] ; then
	echo "ERROR: virtualenv (o alguno de la flia.) no encontrado"
	exit 1
fi

cd $(dirname $0)

export PYTHONPATH=$(pwd)
export DJANGO_SETTINGS_MODULE="seg_mngr.settings"

cd docs
make html

which gnome-open > /dev/null 2> /dev/null && gnome-open _build/html/index.html

