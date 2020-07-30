# -*- coding: utf-8 -*-
'''

..version::20.1.0


.. Note::
  Este é um pequeno documento em fase de construção que buscar ser um log para processos importantes que ocorreram
  durante a construção deste documento.


Comandos básicos no terminal linux
---------------------------------------

  * :cat {opção} |arquivo|: {>}criar, [cat _.extens]visualizar,[CTRL+D]sair_editor.
  * :cd: Alterna para diretório. {cd -]dir ant., [cd ca/mi/nho] último dir.
  * :cp ../caminho/vigente . : Copia arquivo para a pasta/diretório vigente
  * :-f: Força ação do console.
  * :ls: Mostra todos os arquivos visíveis e diretórios internos ao vigente.
  * :ls -a: Mostra, além dos arquivos visíveis, os ocultos.
  * :mkdir: Cria diretório.
  * :pip install <programa>: Instala o recurso.
  * :python |arquivo|: Roda o script no console.
  * :rm |arquivo|: Deleta arquivo.
  * :rmdir |diretório|: Deleta diretório vazio.
  * :-r: Ação recursiva. Ação de árvore toda
  * :sphinx-quickstart: Gera arquivos pertinentes à ação python.
  * :touch: Cria novo arquivo. Necessita extensão.
  * :vi |arquivo|: Mostra o que gerará a documentação. Para sair :wq:.
  * :mv <caminho/raiz> <des/ti/no>: move arquivo para outro diretório

Comando de articulação pythonanywhere e github
--------------------------------------------------

  * :git clone "url projeto": clona projeto do github.
  * :git status: informa situação do repositório vigente (se existente).
  * :git add <file>: Adiciona o documento no mester.
  * :git commit -am 'mensagem': Atualiza as informações no projeto github.
  * :git push: Envia conteúdo da IDE para o gestor.
  * :git pull: Upa conteúdo do gestor para a IDE.

Erros
----------------------
  * :Non-ASCII '\xc3': Parte do código em pt não reconhecido. #-*- coding: utf-8 -*-.
  * :No module named 'bottle': O readthedocs não encontrou o requerimento bottle. Crie um através de um .txt!.
  * :*** No rule to make target 'html'.  Stop.: Dirija-se ao diretório que apresente o 'makefile'.
  * :sphinx.errors.SphinxError: master file /home/../contents.rst not found: master_doc = 'index' no conf.py.
  * :brython.js:5218 Uncaught vitollino: Ao rodar o web page o vitollino não foi encontrado por ausênci do _init_. Gere um _init_ no src do seu repositório.
  * :uncaught delta error 5218: Com certeza é erro de sintaxe! vá consertar!

Importação de diretórios internos
----------------------------------
#. Arquivos importados para o diretório externo ao repositório vigente não aparece na documentação.
#. Faz-se necessário IMPORTAR as dependências!

Instalação E Uso Do Sphinx
------------------------------

 *  :Sphinx: É o gerenciador de documentação python. Ele media a transferência para o Read the docs.
 *  :sphinx-quickstart: É encontrado na documentação sphinx como o disparador do processo de documentação.
 *  :make html: The HTML pages are in build/html. USAR SEMPRE QUE ADICIONAR ALGO QUE TENHA DE SER LIDO EM HTML.
 *  :Diretivas:
 *  :toctree: Interno ao rst.py. O toctree é uma diretiva raiz da árvore de índice. É uma maneira de conectar vários arquivos numa única hierarquia.
 *  :automodule:
 *  :Extensions:


Operações Python
---------------------
  * :Format():

Organização Dos Diretórios 
------------------------------

  * :dev: Diretório principal de desenvolvimento;
  * :Source |src|: Diretório para acomodação de arquivos .py;
  * :docs: Diretório para acomodação dos arquivos de  documentação;
  * :docs/source/conf.py: É onde estarão as principais diretrizes de organização do documento;
  * :docs/source/index.rst: Contém a raiz da árvore de índice ou toctree;

Organização Dos Arquivos 
------------------------------
  * :index:Geralmente é uma página principal
  * :html: Serve as informações antes compostas de python
  * :index.html: 
  
WEB
-------
 *  :html| mimetype|: O MIME type é o mecanismo para dizer ao cliente a variedade de documentos transmitidos. Sintaxe - Tipo/subtipo
 
HTML 
------
* :index.html: Documento principal que servirá os documentos importados. Necessário fazer para cada nova sala?
* :head: Instruções preliminares para antes de implementar o html
* :body: 
* :<script type="text/python">: Diz que a partir desta linha o que está escrito é python
CSS
------
* :viewport: Auxilia css a redimensionar a tela quando janela for maximizada ou minimizada
  * :content="width=device-width, initial-scale=1": Repassa para o ccs a largura do dispositivo para poder ajustar o Layout 
  
BRYTHON
----------
* :Brython: É o interpretador python escrito em javascript. É um compilador que permite rodar o python dentro do browser.
* :cdn: É um endereço que permite pegar um objeto do servidor mais próximo à minha localização.
* <body onload="brython()">: Carregador visual

VITOLLINO
----------
* :<div id="pydiv"></div>: O vitollino procura no corpo de html cujo id seja pydiv, colocando todos os componentes do vitollino.
* :div: É um container do html. Uma caixinha.

'''
