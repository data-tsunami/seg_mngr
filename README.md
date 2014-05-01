seg_mngr
========

Soporte de proceso de seguridad IT

Requerimientos
-------------

* Python 2.6
* virtualenv

Setup del ambiente de desarrollo
------------------------------

* Clonar repo `git clone git@github.com:data-tsunami/seg-mngr.git`
* Activar virtualenv `. virtualenv/bin/activate`
* Instalar dependencias `pip install -r requirements.txt`
* Setup BD `python manager syncdb` & `python manager migrate`

TODO
----

* `psycopg2`

