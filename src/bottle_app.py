
'''
==============================
Tutorial Inicial Discipulu's
==============================

..codeauthor:: Emanuelle Simas

Me encontre em `ellesimas`_.

.. _ellesimas: https://github.com/ellesimas/


..version:: 1.0


Neste modulo encontrará:
------------------------
   As rotas que direcionam para outras abas da web.
   Utilizei o Framework Bottle que tem sua documentação
   wncontrável em <https://wiki.python.org/moin/Routing>
    
'''
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/versao')
def hello_world():
    return main.py


application = default_app()

