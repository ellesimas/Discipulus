# -*- coding: utf-8 -*-
# Discipulus.main.py

'''

..codeauthor:: Emanuelle Simas

Git Hub: `ellesimas`_.

.. _ellesimas: https://github.com/ellesimas/


..version:: 20.1.0

Este documento faz parte do método de Ensino da programação e desenvolvimento
orientando pelo Doutor e Professor Carlo Emmanoel Tolla de Oliveira.
Git Hub: `CarloTolla`_.

.. _CarloTolla: https://github.com/carlotolla

Neste tutorial encontrá:
------------------------

#. Uso Enconding utf 8
#. Comandos básicos no terminal linux
#. Comando de articulação pythonanywhere e github
  * :git clone "url projeto": clona projeto do github;
  * :git status: informa situação do repositório vigente (se existente);
  * :git commit -am "mensagem": Atualiza as informações no projeto github;
  * :git push: Envia conteúdo da IDE para o gestor;
  * :git pull: Upa conteúdo do gestor para a IDE;
#. Processo de criação de uma WebPage inicial
  * :Frameworks:
  * :Framework Bottle:
#. Instalação e uso do sphinx
  * :pip install sphinx: instala o sphinx;
  * :sphinx-quickstart: Starta a construção da documentação;

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