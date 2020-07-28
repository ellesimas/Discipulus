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
from bottle import static_file
''' Static_file importado para 'chamar' a page html do sphinx em uma das rotas
'''
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


"""@route('/images/<filename:re:.*\.png>') expressão regular anterior.
   doc é o root
   .* diz para importar tudo que termine com html.
   leia roteie qualquer coisa que tenha doc na frente
"""
@route('/doc/<filename:re:.*\.html>')
def rota_doc(filename):
    """Roteia o caminho /vs para a page html gerada pelo sphinx.
       Na web <domínio.com/doc/filename/html>
       Atenção que o doc da chamada deve ser o root não a pasta.
    """
    return static_file(filename, root='/home/ellesimas/dev/Discipulus/docs/build/html', mimetype='text/html')
'''O bottle consegue servir arquivos estáticos.
   static_file(filename, root='/path/to/image/files', mimetype='image/png')
   expressão anterior

'''

application = default_app()

