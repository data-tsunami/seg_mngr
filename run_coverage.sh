#!/bin/bash

if [ "$VIRTUAL_ENV" = "" ] ; then
	echo "ERROR: virtualenv (o alguno de la flia.) no encontrado"
	exit 1
fi

cd $(dirname $0)

coverage run --omit='seg_mngr/migrations/*,seg_mngr_settings_local.py,seg_mngr/settings.py' --source='seg_mngr' manage.py test seg_mngr
coverage html -d /tmp/seg-mngr-coverity
which gnome-open > /dev/null 2> /dev/null && gnome-open /tmp/seg-mngr-coverity/index.html

