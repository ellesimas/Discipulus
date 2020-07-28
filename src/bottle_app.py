# -*- coding: utf-8 -*-
# SPDX License Indentifier : GPL 3.8-or-later

'''
==============================
Tutorial Inicial Discipulu's
==============================

..codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

..version:: 1.0


Neste modulo encontrará:
------------------------

.. versionadded::      20.1.0
   As rotas que direcionam para outras abas da web.
   Responsabilidade do gerenciador de chamadas http.
   Utilizei o Framework Bottle que tem sua documentação
   encontrável em <https://wiki.python.org/moin/Routing>

'''

from bottle import default_app, route

@route('/')
def hello_world():
    return 'Tutorial Discipulus: Introdução aplicativo web'



application = default_app()

