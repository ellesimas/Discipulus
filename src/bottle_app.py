# -*- coding: utf-8 -*-
# SPDX License Indentifier : GPL 3.8-or-later
'''
* As rotas que direcionam para outras abas da web,
    através do gerenciador de de http.
* Framework Bottle utilizado. Documentação em <https://wiki.python.org/moin/Routing>
.. versionadded::      20.1.0


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
    '''Roteia a página principal.
    '''
    return 'Tutorial Discipulus: Introdução aplicativo web'

@route('/next')
def rota_dois():
    '''Exemplo da geração de uma segunda rota qualquer.
    '''
    return 'Bem-vindo à segunda rota'

@route('/versao')
def rota_credits():
    """Roteia o caminho para retornar a versão do sistema.
       O módulo chamado é o main com sua classe Main importado
       linhas acima.
    """
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
       static_file(filename, root='/home/ellesimas/dev/Discipulus/docs/build/html', mimetype='text/html')
       expressão que permitiu uma visualização primitiva da documentação. Esta vsualização simples tem
       justificativa na ausência do roteamento do css que se encontra no caminho
       ../docs/build/html/_static
    '''

@route('/doc/<filename:re:.*\.css>')
def rota_css_doc(filename):
    """Roteia o caminho /vs para a page html gerada pelo sphinx, chamando css
    """
    return static_file(filename, root='/home/ellesimas/dev/Discipulus/docs/build/html/', mimetype='text/css')

application = default_app()

