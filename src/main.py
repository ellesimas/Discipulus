# -*- coding: utf-8 -*-;
# Discipulus.main.py

'''
=============================
Tutorial Inicial Discipulu's
=============================

..codeauthor:: Emanuelle Simas

Me encontre em `ellesimas`_.

.. _ellesimas: https://github.com/ellesimas/


..version:: 1.0


Neste tutorial encontrá:
------------------------

#. Enconding utf 8
#. Comandos básicos no terminal linux
#. Comando de articulação pythonanywhere e github
  * :git clone "url projeto": clona projeto do github
  * :git status: informa situação do repositório vigente (se existente)
  * :git commit -am 'mensagem': Atualiza as informações no projeto github
  * :git push: Envia conteúdo da IDE para o gestor
  * :git pull: Upa conteúdo do gestor para a IDE


Classes neste módulo
---------------------


'''

class main():
    ''' Classe exemplo

       :param self: Chama ele mesmo
    '''

    j = 300

    def __init__(self):
        for i in range(10):
            print(i)

if __name__=="__main__":
    main()