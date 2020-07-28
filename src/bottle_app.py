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
from main import Main

''' na linha 26 importei uma classe presente no caminho
    ellesimas/dev/Discipulus/src/main.py
'''

@route('/')
def rota_padrao():
    return 'Tutorial Discipulus: Introdução aplicativo web'

@route('/next')
def rota_dois():
    return 'Bem-vindo à segunda rota'

@route('/versao')
def rota_credits():
    """Roteia o caminho /vs para retornar a versão do sistema."""
    return 'Tutorial Discipulus - Versão do sistema: {}'.format(Main().pega_versao())

application = default_app()

