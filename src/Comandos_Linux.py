'''
:~___/__/__$: Intrui sobre onde você está no bash.
:pwd: Indica em qual repositório o usuário está. 
:hostname: apresenta o nome do host local.
:Shel: Interpreta os comando do terminal.
:man <comando>: é o manual de comandos. 'q' exita.


COMANDO MUDANÇA DE DIRETÓRIO
-----------------------------
:cd /nome_do_diretório: direciona para o diretório requerido;
:cd ~: volta para o diretório raiz;
:cd -: volta para o diretório inicial, home; 

Mostrador
-----------
#. :ls: Diz os arquivos dentro do diretório;
#. :ls -a: Mostra os ocultos;
#. :ls <nome do diretório>: Mostra os arquivos da pasta pedida;
#. :ls -F: Os diretórios são apresentados como 'dir/';
#. :ls -F /etc: Informa os diretórios do destino 'int_etc/';
#. :ls -l <caminho> : Mostra em lista longa o Tipo de arquivo <d> <->, usuário dono, grupo associado ao recurso, 
                      Permissões, data de modificação e criação internos ao caminho;
#. :file <arquivo>: Diz o tipo de arquivo text, executável, etc.; 
  * :-: Arquivo comum;
  * :d: Diretório;
  * :b: Arquivo de bloco. Referente a gerenciadores de bloco;
#. :cat <nome_do_arquivo>: Mostra o conteúdo do arquivo;
#  :cat > <nome_do_arquivo>: Permite a escrita no editor do SHELL.CTRL+C exita;

Criação e destruição
---------------------
#. :mkdir <nome_desejado_>: Criação de diretório;
#. :rmdir <nome_diretorio>: Apaga diretórios VAZIOS;
#  :rm -r <nome_diretorios>: Apaga diretorios com elementos em recursão;
#. :rm -fr <nome_diretorio>: Força o apagamento do diretório;
#. :rm -i <nome_do_arquivo.ext>: Apaga arquivo solcitando confirmação;
#. :echo "Texto 1" > <nome_e_extensão_a_ser_criado>: criar um arquivo com a extensão e conteúdo colocados;
#. :echo "Texto 2" >> <nome_e_extensão_a_ser_criado>: Adiciona o novo conteúdo abaixo do conteúdo anterior;
#. :cp <nome_arquivo.ext>: Cria uma cópia do arquivo e diretórios ao qual é gerado no mesmo lugar da origem;
#. :cd -avr <nome_do_arquivo_de_transferencia>: Copia mantendo os atrivbutos <-a>, permite visualização dos processos
                                                <-v> e pratica em recursão <r> no arquivo de destino;
#  :cat > <nome_do_arquivo>: Permite criação e escrita no editor do SHELL. CTRL+C exita;
#  :touch <caminho/nome_do_arquivo.txt>: Cria arquivo;
#. :touch <caminh/nome_do_arquivo{1..2}.txt>: Cria duas versões do arquivo;


Alterar
-------
#. :mv <nome_atual.ext> <nome_requerido.ext>: Altera nome do arquivo;
#  :cat > <nome_do_arquivo>: Permite a escrita no editor do SHELL. para sair, CTRL+C;

Movientação
-----------
#. :mv <arquivo.ext> <caminho/de/destino>: move o arquivo para o caminho especificado;
#. :mv Caminho/requerido/ <nome_original> <nome_requerido>: Altera a localização do arquivo e muda nome; 


Especificações
--------------_
#. :inicio_requerido + *: "*" é completado por qualquer informação que COMECE por nome_requerido;

'''
