|1|Fundamentos da Lógica|5|
|---|---|---|
|1.1|Introdução|5|
|1.2|Proposições Simples e Compostas|5|
|1.3|Operadores ou Conectivos|6|
|2|Expressões lógicas e Tabela-verdade:|13|
|2.1|Tautologia|14|
|2.2|Contradição|14|
|2.3|Contingência|14|
|2.4|Para pensar|15|
|2.5|Exercícios|15|
|2.6|Equivalência de proposições|15|
|2.7|Circuitos digitais e portas lógicas|19|
|2.8|Consequência Lógica|20|
|2.9|Lógica de Predicados|24|
|3|Teoria dos Conjuntos|32|
|3.1|Introdução|32|
|3.2|Relações Básicas|33|
|3.3|Cardinalidade|34|
|3.4|Operações entre conjuntos|35|
|3.5|Diagramas de Venn|39|
|3.6|Exercícios:|39|
|4|Relações e Funções|43|
|4.1|Relações|43|
|4.2|Representando relações:|43|
|4.3|Relações dentro de um conjunto|43|

|4.4||Propriedades das relações|44|
|---|---|---|---|
|4.5||Combinando relações|46|
|4.6||Funções|47|
|4.7||Relações vs. Funções|47|
|4.8||Soma e produto entre funções|47|
|4.9||Composição|48|
|4.10||Propriedade das funções|48|
|5|Relações de Recorrência||50|
|5.1||Sequências|50|
|5.2||Sucessão recursiva|50|
|5.3||Progressão Aritmética|51|
|5.4||Progressão geométrica|52|
|5.5||Progressão Harmônica|53|
|5.6||Somatório|53|
|5.7||Produtório|54|
|5.8||Definição Recursiva|54|
|5.9||Recursividade de funções|55|
|5.10||Indução e recursão|55|
|5.11||Conjuntos recursivos|56|
|5.12||Definir a Relação de Recorrência|56|
|5.13||Grau da relação de recorrência:|58|
|5.14||Equação de uma relação de recorrência:|58|
|6|Métodos de Prova||60|
|6.1||Introdução|60|
|6.2||Teorema|60|
|6.3||Lemas e Corolários|60|
|6.4||Conjecturas|61|
|6.5||O que não é preciso provar|61|
||||3|

Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a conjunção “p e q” corresponderá à interseção do conjunto p com o conjunto q:

Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a disjunção “p ou q” corresponderá à união do conjunto p com o conjunto q:

Representando em conjuntos, a disjunção exclusiva corresponde a união de p e q menos a intersecção de p e q.

Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a proposição condicional “Se p então q” corresponderá à inclusão do conjunto p no conjunto q (p está contido em q):

Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a proposição bicondicional “p se e somente se q” corresponderá à igualdade dos conjuntos p e q.

## **3 Teoria dos Conjuntos**

Um conjunto é uma estrutura que representa uma coleção não ordenada de zero ou mais objetos distintos, podendo ser infinitos. A teoria dos conjuntos trata das operações entre conjuntos e as afirmações acerca de conjuntos. Esta teoria é muito usada em Computação.

Praticamente tudo que podemos fazer com objetos individuais podemos fazer com conjuntos, por exemplo, comparar, combinar, se referir a ele, diferenciar um de outro,... E podemos ainda fazer coisas que não podemos fazer com objetos individuais:

A base da teoria dos conjuntos é a relação binária entre um elemento e um conjunto, por exemplo, se o elemento ‘a’ pertence ao conjunto S, ou não. Se pertence dizemos que ‘a’  S, caso ∈ contrário ‘a’ ∉ S.

Dois conjuntos só serão iguais se e somente se todos os seus elementos forem os mesmos, não importando como os conjuntos foram definidos:

**3.1.2 Conjuntos Padrões** Números Naturais N = {0, 1, 2, 3, ...} : Números Inteiros Z = {..., -3, -2, -1, 0, 1, 2, 3,...} Números Racionais Q = {1.1, 2.5, 14, -2, ...} Números Irracionais I = {π, e, 2, ...} Números Reais R = {4.3, -1.1, 0, 2, ...} Números Complexos C = {z | z = x + iy ∧ i² = -1 ∧ x∈ R ∧ y  R} ∈ Números Quatérnios H = {q | q = u + xi + yj + zk ∧ i² = j² = k² = -1 ∧ ((u ∧ x ∧ y ∧ z)  ∈

## **3.2 Relações Básicas**

Podemos definir igualdade entre conjuntos em termos da relação ∈:

- “Dois conjuntos são iguais, se e somente se, possuem os mesmos elementos.”

## **3.3 Cardinalidade**

|S| (lemos “a cardinalidade de S”) é  a medida que indica o número de elementos diferentes que S possui. Exemplo, |∅|=0, |{1,2,3}| = 3, |{a,b}| = 2, |{{1,2,3},{4,5}}| = 2.

Alguns conjuntos infinitos: N, Z, R, …

O conjunto das partes P(S) de um conjunto S é o conjunto que cujos elementos são todos os subconjuntos de S.

Existem conjuntos infinitos com tamanhos diferentes!

## **3.4 Operações entre conjuntos**

O Produto Cartesiano de 2 conjuntos :

Para conjuntos não vazios A e B:

O Produto Cartesiano de 2 ou + conjuntos é:

Para conjuntos A, B, a união A∪B é o conjunto que contém todos os elementos que estão em A, ou (“∨”) em B (ou, em ambos).

Sejam os conjuntos _A_ , _B. Sua interseção A_ ∩ _B_ é o conjunto que contém todos os elementos

Dois conjuntos A e B são ditos disjuntos sss sua interseção é vazia ( _A_ ∩ _B_ =∅)

Este príncipio pode ser expandido para 3 conjuntos:

## **3.4.6 Diferença entre conjuntos**

A lógica proposicional e a teoria dos conjuntos são isomorfas:

conjuntos, podemos:

Criamos colunas para diferentes expressões de conjuntos.

Como a união e a intersecção são comutativas e associativas podemos generalizar para n conjuntos:

(A1,…,An) ou até para conjuntos não ordenados X={A | P(A)}.

A∪A2∪…∪An = ((…((A1∪ A2) ∪…)∪ An) Notação “Big U” : Infinitos conjuntos:

Infinitos conjuntos:

## **3.5 Diagramas de Venn**

2. Dados os conjuntos A = {0, 1}, B = {0, 1, 2} e C = {2, 3}, determine (A U B) ∩ (B U C).

3. Considerando os conjuntos U = {0, 1, 2, 3, 4, 5, 6}, A = {1, 2}, B = {2, 3, 4}, C = {4, 5}

5. Encontre dois conjuntos A e B de forma que A ∈ B e A C B.

7. Sejam os conjuntos numéricos A = {2, 4, 8, 12, 14}; B = {5, 10, 15, 20, 25} e C = {1, 2,

5) A = {1, 2, 3} e B = {1, 2, 3}, *quaisquer dois conjuntos iguais.

A união de quaisquer dois conjuntos pode resultar no máximo em 100% dos elementos presentes nestes dois conjuntos, assim:

Uma relação é uma correspondência existente entre conjuntos não vazios. Por exemplo, dois conjuntos A e B. O conjunto A é denominado conjunto de partida, ou domínio, e o conjunto B é denominado conjunto de chegada, ou contradomínio.

A correspondência entre os dois conjuntos é dada em termos de pares ordenados, onde o primeiro elemento do par ordenado procede do conjunto de partida A e o segundo elemento do par ordenado procede do conjunto de chegada B. Quando temos uma relação entre dois conjuntos, chamamos de relação binária. O conjunto de elementos de B presentes nos pares ordenados são chamados de imagem.

Em outras palavras: sejam os conjuntos A e B, uma relação binária entre estes conjuntos é um subproduto de AxB. Para uma relação binária R temos que R AxB. A notação aRb denota

Relações são conjuntos, podemos aplicar operadores de conjuntos a elas. Dadas duas relações R1 e R2, ambas do conjunto A no conjunto B, então podemos combiná-las em R1 ∪ R2, R1 ∩ R2, ou R1 – R2. Em cada caso o resultado será uma nova relação de A em B.

_f_ (x), onde y ∈ R. Sejam A e B dois conjuntos, então dizemos que uma função _f_ de A em B ( _f_ :A→B) é uma associação de um único elemento _f_ (x) ∈ B a cada elemento x ∈ A.

Logo: se _f_ é bijetora e A e B são conjuntos finitos, então n|A| = n|B|.

## **5.11 Conjuntos recursivos**

Definições recursivas de conjuntos também têm duas partes:

É possível determinar subconjuntos que também são infinitos, basta mostrar como construir um conjunto infinito de triplas em que x²+y²=z², mesmo que esse conjunto não inclua algumas triplas com essa propriedade.

## **7.2.3 Estendendo os princípios aditivo e multiplicativo para conjuntos finitos**

**Regra da Soma:** Seja A1, A2, …, Am conjuntos disjuntos. Então o número de maneiras de escolher um elemento de um desses conjuntos é |A1 ∪ A2 ∪ … ∪ Am | =

**Regra do Produto:** Sejam A1, A2, …, Am conjuntos finitos. Então o número de maneiras de escolher um elemento de cada conjunto na ordem A1, A2, …, Am é

R.: Considere os subconjuntos de A:

𝑝 Calcular 𝐶 é equivalente a responder: Quantos subconjuntos de _T_ existem contendo p 𝑛+1

Em teoria de conjuntos isso corresponde a conjuntos A1 e A2 que não são disjuntos (possuem

elementos repetidos entre eles). Então, para sabermos a cardinalidade da união entre A1 e A2, temos:

Somando a cardinalidade das duas séries temos 151+150 = 301 números. Como estavam à venda 300 números (de 1 a 300), temos 301 números para serem alocados em 300 posições, então pelo princípio da casa dos pombos, pelo menos dois números são iguais.