# -*- coding: utf-8 -*-
# Discipulus.main.py

'''
.. sectionauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. versionadded:: 20.1.0
   Versão inicial.

.. note::

    Este documento faz parte do método de Ensino da programação e desenvolvimento
    orientando pelo Doutor e Professor Carlo Emmanoel Tolla de Oliveira.
    Git Hub: `CarloTolla`_.

.. _CarloTolla: https://github.com/carlotolla

Neste tutorial encontrá:
------------------------

#. Uso Enconding utf 8
#. Comandos básicos no terminal linux
#. Comando de articulação pythonanywhere e github
#. Processo de criação de uma WebPage inicial
#. Instalação e uso do sphinx


Classes neste módulo:
---------------------
     :py:class: 'Main' Exemplo de classe qualquer

Changelog
---------

.. versionadded:: 20.1.0
        Documentação do tutorial

'''

class Main():
    """ Classe exemplo

       :param self: Chama ele mesmo.
       :param versao: Retorna a versão colocada.

    """

    def __init__(self, versao = "20.1.0"):
        """Printa a versão da classe dez vezes

           :param versao: Torna-se default, um atributo da classe Main.
        """
        self.versao = versao
        #for i in range(10):
            #print("Classe exemplo. Versão {}".format(versao))

    def pega_versao(self):
        '''
           :return: A versao do sistema
        '''
        return self.versao

if __name__=="__main__":
    print(Main().pega_versao())