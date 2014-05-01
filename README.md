seg_mngr
========

Soporte de proceso de seguridad IT

Requerimientos
-------------

* Python 2.6
* virtualenv

Setup del ambiente de desarrollo
------------------------------

* Clonar repo `git clone git@github.com:data-tsunami/seg_mngr.git`
* Activar virtualenv `. virtualenv/bin/activate`
* Instalar dependencias `pip install -r requirements.txt`
* Crear settings local `touch seg_mngr_settings_local.py`
* Setup BD `python manager syncdb` & `python manager migrate`

Otras configuraciones:

* encoding de archivos: UTF-8
* New lin: Unix

TODO
----

* `psycopg2`

