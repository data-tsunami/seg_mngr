SegManager
==========

Soporte de procesos de seguridad IT


* Jira: [https://data-tsunami.atlassian.net/secure/RapidBoard.jspa?rapidView=4](https://data-tsunami.atlassian.net/secure/RapidBoard.jspa?rapidView=4 "Repositorio Jira")


Requerimientos
--------------

* Python 2.6 (para deployar en CentOS!)
* virtualenv (o similar)

Setup del ambiente de desarrollo
------------------------------

* Clonar repo `git clone git@github.com:data-tsunami/seg_mngr.git`
* Activar virtualenv `. virtualenv/bin/activate`
* Instalar dependencias `pip install -r requirements.txt`
* Crear settings local `touch seg_mngr_settings_local.py`
* Setup BD `python manager syncdb` & `python manager migrate`

Otras configuraciones:

* encoding de archivos: `UTF-8`
* New lin: `Unix`

TODO
----

* `psycopg2`

