#!/bin/bash

cd $(dirname $0)

for x in $(cd ../seg_mngr ; ls -1 *.py | cut -d . -f 1 | grep -v seg_mngr_settings_local | grep -v __init__ | sort) ; do
	F=seg_mngr_${x}.rst

cat > $F <<EOF

.. ARCHIVO AUTOGENERADO! Sera sobreescrito si se ejecuta ./gen.sh

seg_mngr.$x
====================================

.. automodule:: seg_mngr.$x
   :members:

EOF

done

