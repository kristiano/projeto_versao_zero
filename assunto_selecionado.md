|1|Características básicas da linguagem|2|
|---|---|---|
|2|Obtenção e instalação|2|
|3|Variáveis|3|
|4|Strings|3|
||4.1<br>Manipulando Strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|4|
|5|Operações matemáticas|5|
|6|Entrada de Dados|6|
|7|Estruturas de controle|7|
||7.1<br>While<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
||7.2<br>If . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
||7.3<br>For . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
|8|Funções|9|
||8.1<br>Variáveis em funções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||8.2<br>Recursividade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||8.3<br>Módulos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|9|Listas|13|
||9.1<br>Inserindo um novo dado a uma lista . . . . . . . . . . . . . . . . . . . . . .|15|
||9.2<br>Impressão dos conteúdos da lista<br>. . . . . . . . . . . . . . . . . . . . . . .|15|
||9.3<br>Determinar em que ordem um elemento aparece na lista<br>. . . . . . . . . .|16|
||9.4<br>Remover um elemeto de uma lista . . . . . . . . . . . . . . . . . . . . . . .|16|
||9.5<br>Descobrir o tamanho de uma lista . . . . . . . . . . . . . . . . . . . . . . .|16|
||9.6<br>Range<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
|10|Expressões booleanas|17|

Isso nos mostra que uma string segue uma determinada indexação onde cada caractere assume um endereço que, pode ser acessado colocando o nome da variável, que contém a string, e após, entre os colchetes, o endereço da célula que contém o caractere desejado.

>>> for contador in range(1, 11):

A estrutura acima utiliza uma variável criada, no caso contador, para percorrer cada elemento da lista criada com o comando range(1,11), com isso, cada repetição feita pelo loop for fará com que a variável contador aponte para um diferente valor dentro da lista formada pela função range e logo em seguida imprima esse valor.

## 9 Listas

Listas são sequências de variáveis. Após denidas, podem ser modicadas de várias maneiras, pois são mutáveis.

Alguns comandos referentes a listas:

Nós já vimos anteriormente que variáveis comuns armazenam um único valor. Entretanto, existem outros tipos de variáveis capazes de armazenar mais de um valor. Em Python, chamamos essas variáveis com capacidade de armazenamento de listas ou vetores. Vamos explicar a sintaxe de uma lista através das linhas de código exibidas abaixo:

Depois inserimos o comando while 1: que faz com que o nosso programa entre em loop. O programa vai rodar indenidamente até ser dado o comando Ctrl+D, ou até que o programa seja fechado. Uma vez nesse loop, é denida pelo usuário a variável qual_mes", e depois de um tratamento de erros, feito com a utilização de um comando if, é nos devolvido o nome do mês selecionado, Na última linha do código utilizamos uma propriedade da lista, que é buscar um dado da lista, que se dá escrevendo o nome da lista e entre colchetes o número referente ao local da lista onde está o dado requerido (lista[número]). Observe que na nossa linha de código print é dado pelo mês escolhido menos um, ou seja: o Python indexa suas listas partindo do zero.

Infelizmente o comando .append só consegue adicionar um dado na lista por vez, mas se quisermos adicionar mais dados podemos simplesmente somar listas, multiplicá-las, ou utilizar o comando .extend :

Para remover um elemento de uma lista utilizamos o comando del , referenciando o index, ou posição da lista, onde haverá a remoção.

## 9.6 Range

A função range gera um vetor contendo números (inteiros) sequênciais, obedecendo a regra de escrita:

range(inicio,m)

>>>vetor = range(1,11) >>>print vetor

A função range aceitará quaisquer números inteiros desde que o número inicial seja maior que o número nal, bem como quando apenas o número nal é passado para a função, portanto são válidas as contruções:

>>> range(1, 10) [1, 2, 3, 4, 5, 6, 7, 8, 9] >>> range(-32, -20) [-32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21] >>> range(5,21) [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] >>> range(5) [0, 1, 2, 3, 4] >>> range(21, 5) [ ]

Outra característica importante desse comando é a de adicionar uma terceira variável no range, indicando o incremento entre os números delimitados.

>>>range(0,24,4) [0, 4, 8, 12, 16, 20, 24]