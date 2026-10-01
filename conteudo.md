## **1 Fundamentos da Lógica** 

## **1.1 Introdução** 

Geralmente nos expressamos, em português, através de interrogações, exclamações, ordens e afirmações, todas representadas através de sentenças. Tecnicamente, uma sentença pode ser: 

- Sentença declarativa (afirmativa): “A terra é maior que a lua.” 

- Sentença exclamativa: “Caramba!” 

- Sentença interrogativa: “Como é o seu nome?” 

- Sentença imperativa: “Estude mais.” 

O conceito mais elementar no estudo da lógica é o de **Proposição** . Proposição vem de “propor” que significa submeter à apreciação; requerer um juízo. Proposições são sentenças declarativas cujo conteúdo pode ser considerado **falso** ou **verdadeiro** . 

Então, se afirmarmos “a Terra é maior que a Lua”, estaremos diante de uma proposição cujo valor lógico é verdadeiro. Fica claro que quando falarmos em valor lógico estaremos nos referindo a um dos dois possíveis juízos que atribuímos a uma proposição: **verdadeiro (V)** ou **falso (F)** . 

Assim, uma proposição é simplesmente uma afirmativa, com algum significado definido, não ambíguo ou invalido, e que possuí um valor lógico (ou valor verdade), que pode ser **verdadeiro (V)** ou **falso (F)** . Uma proposição nunca pode assumir ambos os valores lógicos ou estar entre os dois. Mas podemos a priori não saber qual é o seu valor lógico. No raciocínio lógico as proposições devem obedecer sempre a três princípios fundamentais: 

- **Princípio da identidade:** Uma proposição verdadeira é verdadeira; uma proposição falsa é falsa. 

- **Princípio da Não-Contradição:** Nenhuma proposição poderá ser verdadeira e falsa ao mesmo tempo. 

- **Princípio do Terceiro Excluído:** Uma proposição ou será verdadeira, ou será falsa, não há outra possibilidade. 

## **1.2 Proposições Simples e Compostas** 

As proposições podem ser escritas em linguagem natural e/ou representadas por letras minúsculas (p, q, r, ...). 

- p: Tiago é professor. 

- q: 5 > 8. 

- r: Estudar lógica é muito divertido. 

5 

Proposições podem ser ditas _simples_ ou _compostas_ . Serão proposições simples (atômicas) aquelas que vêm sozinhas, desacompanhadas de outras proposições: “O professor é o Tiago”. E quando duas ou mais proposições vêm conectadas entre si, formando uma sentença maior, dizemos que é composta: “O professor é o Tiago e a disciplina é Matemática Discreta e Lógica”. 

## **Jogo das proposições:** 

|**Jogo das proposições:**|||||
|---|---|---|---|---|
|**Sentença**|**Afirmativa?**|**Proposição?**|**Simples ou**<br>**Composta**|**Valor lógico**|
|Elefantes são maioresque ratos.|V|V|<br>S|V|
|520 > 110|V|V|S|V|
|y> 5|F|-|-|-|
|Tchu biru biru bah.|F|-|-|-|
|Quem esta aí?|F|-|-|-|
|x = x + 1|F|-|-|-|
|Está chovendo.|V|V|S|F|
|Hoje é 1º dejaneiro e 10 > 11.|V|V|C|F|
|Por favor,não durmam.|F|-|-|-|
|Se elefantes fossem vermelhos, eles<br>poderiam tomar sorvete.|V|V|C|F|
|<br>x <yse e somente sey> x|V|V|C|V|
|Hoje équinta ou ontem foiquarta.|V|V|C|V|
|Ou hoje équinta ou ontem foiquarta.|V|V|C|F|
|Hoje équinta e ontem não foiquarta.|V|V|C|V|
|Hoje é quinta se e somente se ontem<br>foi quarta.|V|V|C|V|
|Comprarei uma mansão se e somente<br>se eu ganhar na loteria.|V|V|C|V|
|<br>Não comprei uma caneta.|V|V|S|V|



## **1.3 Operadores ou Conectivos** 

Operadores ou conectivos são utilizados para conectar duas ou mais proposições, formando assim uma proposição composta. Os operadores na lógica se assemelham aos operadores matemáticos, onde temos: 

● Operadores unários: operam sobre um operando, ex.: -3, 9; 

- Operadores binários: operam sobre dois operandos, ex.: 3 + 4, 2 x 5. 

Na lógica utilizamos operadores booleanos, que ao invés de operar sobre números, operam sobre proposições, a seguir os principais operadores: 

|**Operação**|**Nomenclatura**|**Termos**|**Símbolo**|
|---|---|---|---|
|Negação|NOT|Unário|**¬**|
|<br>Conjunção|AND|Binário|∧|



6 

|Disjunção|OR|Binário|∨|
|---|---|---|---|
|Disjunção Exclusiva|XOR|Binário|⊕|
|Disjunção Exclusiva<br>Implicação|IMPLIES|Binário|**→**|
|Bicondicional|IFF|Binário|**↔**|



## **1.3.1 Conjunção (e, and,** ∧ **):** 

Proposições compostas em que está presente o conectivo “e” são ditas CONJUNÇÕES. Simbolicamente, esse conectivo pode ser representado por “∧”. Então, se temos a sentença: 

“João é professor e Maria é estudante” 

poderemos representá-la apenas por: p ∧ q. onde: p = João é professor e q = Maria é estudante. 

## **Uma conjunção só será verdadeira, se ambas as proposições componentes forem também verdadeiras.** 

Diante disso, só podemos concluir que p ∧ q será verdadeira se p e q são verdades ao mesmo tempo. Assim, podemos construir uma tabela-verdade onde serão testadas todas as possibilidades de combinações de valores lógicos para p e para q: 

|João é professor|Maria é estudante|João é professor e Maria é estudante.|
|---|---|---|
|p|q|p ∧q|
|V|V|V|
|V|F|F|
|F|V|F|
|F|F|F|



Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a 

conjunção “p e q” corresponderá à interseção do conjunto p com o conjunto q: 

## **1.3.2 Disjunção (ou, or,** ∨ **):** 

Recebe o nome de DISJUNÇÃO toda proposição composta em que as partes estejam unidas pelo conectivo ou. Simbolicamente, representaremos esse conectivo por “∨”. Se temos a sentença: 

“João é professor ou Maria é estudante” 

poderemos representá-la apenas por: p ∨ q. onde: p = João é professor e q = Maria é estudante. 

## **Uma disjunção será falsa quando as duas partes que a compõem forem ambas falsas! E nos demais casos, a disjunção será verdadeira.** 

7 

|João é professor|Maria é estudante|João é professor ou Maria é estudante.|
|---|---|---|
|p|q|p ∨ q|
|V|V|V|
|V|F|V|
|F|V|V|
|F|F|F|



Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a disjunção “p ou q” corresponderá à união do conjunto p com o conjunto q: 

## **1.3.3 Disjunção exclusiva (ou... ou..., xor,** ⊕ **):** 

Observe as seguintes frases: 

“Vou comprar uma bola ou vou comprar um skate.” 

“Ou vou comprar uma bola ou vou comprar um skate.” 

A diferença é sutil, mas é importante. Como vimos na disjunção, na primeira frase o fato de a primeira proposição ser verdadeira não impede que a segunda também seja verdadeira e assim a disjunção entre elas seja verdadeira. Já na segunda frase, se for verdade que “vou comprar uma bola”, então teremos que não comprarei um skate. E vice-versa, ou seja, se for verdade que “vou comprar um skate”, então teremos que não comprarei a bola. 

Em outras palavras, a segunda frase apresenta duas situações mutuamente excludentes, sendo que apenas uma delas pode ser verdadeira, a outra será necessariamente falsa. Ambas nunca poderão ser, ao mesmo tempo, verdadeiras; e ambas nunca poderão ser, ao mesmo tempo, falsas. 

**A disjunção exclusiva só será verdadeira se houver uma das sentenças verdadeira e a outra falsa. Nos demais casos, a disjunção exclusiva será falsa.** 

|**outra falsa. Nos demais casos, a disjunção exclusiva será falsa.**|**outra falsa. Nos demais casos, a disjunção exclusiva será falsa.**|**outra falsa. Nos demais casos, a disjunção exclusiva será falsa.**|
|---|---|---|
|Vou comprar uma bola|Vou comprar um skate|Ou vou comprar uma bola ou<br>vou comprar um skate.|
|p|q|vou comprar um skate.<br>p⊕ q|
|V|V|pq<br>F|
|V|F|V|
|F|V|V|
|F|F|F|



Representando em conjuntos, a disjunção exclusiva corresponde a união de p e q menos a intersecção de p e q. 

8 

1.3.4 **Condicional ou Implicação (Se ... então ..., implies,** →): 

Sentenças condicionais seguem a seguinte estrutura: 

“Se amanhecer chovendo, então não irei à praia.” 

“Se João é professor, então Maria é estudante.” 

Para facilitar o entendimento vamos analisar a seguinte frase: 

“Se nasci em São Luís, então sou maranhense.” 

Qual a única maneira desta frase estar incorreta? Logicamente se a primeira parte for verdadeira e a segunda parte for falsa. Se alguém nasceu em São Luís, necessariamente esta pessoa é maranhense. Se alguém falar que é verdade que nasceu em São Luís e falar que não é verdade que é maranhense, então o conjunto todo será falso. 

No dia-a-dia sempre que temos uma situação do tipo “se a então b”, esperamos que exista uma relação de sentido entre a e b. Mas, na realidade, não é preciso que exista qualquer conexão de sentido entre o conteúdo das proposições componentes da condicional. Por exemplo, poderíamos ter a seguinte sentença: 

“Se a baleia é um mamífero então o papa é argentino.” 

O que interessa é apenas uma coisa: a primeira parte da condicional é uma condição suficiente para obtenção de um resultado necessário, que é a segunda parte. 

**Uma condicional só será falsa quando houver a condição suficiente, mas o resultado necessário não se confirmar. Ou seja, quando a primeira parte for verdadeira, e a segunda for falsa. Nos demais casos, a condicional será verdadeira.** 

|Nasci em São Luís|Sou maranhense|Se nasci em São Luís, então<br>sou maranhense.|
|---|---|---|
|p|q|p**→** q|
|V|V|V|
|V|F|F|
|F|V|V|
|F|F|V|



Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a proposição condicional “Se p então q” corresponderá à inclusão do conjunto p no conjunto q (p está contido em q): 

9 

**1.3.5 Bicondicional (... se e somente se ..., Iff,** ↔) **:** 

A estrutura bicondicional apresenta o conectivo “se e somente se”, separando as duas sentenças simples. 

“João fica feliz se e somente se Maria sorri.” 

“O Sampaio Corrêa vence se e somente se o Moto Club perder.” 

A bicondicional é equivalente a conjunção entre as duas condicionais: 

“Se o Sampaio Corrêa vence, então o Moto Club perde e se o Moto Club perde, então o Sampaio Corrêa vence.” 

**Haverá duas situações em que a bicondicional será verdadeira: quando antecedente e consequente forem ambos verdadeiros, ou quando forem ambos falsos. Nos demais casos, a bicondicional será falsa.** 

|Sampaio Corrêa vence|Moto Club perde|O Sampaio Corrêa vence se e somente se o<br>Moto Club perde.|
|---|---|---|
|p|q|p **↔** q|
|V|V|V|
|V|F|F|
|F|V|F|
|F|F|V|



Se as proposições p e q forem representadas como conjuntos, por meio de um diagrama, a proposição bicondicional “p se e somente se q” corresponderá à igualdade dos conjuntos p e q. 

## **1.3.6 Negação (não, not,** ¬, ~) **:** 

Para negar uma proposição simples basta colocar a partícula **não** na sentença, e seu valor verdade será o contrário. 

“Tiago é professor” => “Tiago não é professor.” 

Temos outras formas equivalentes de negar: 

“Não é verdade que Tiago é professor.” 

“É falso que Tiago é professor.” 

Também podemos negar a negação: 

10 

“Tiago não é professor” => “Não é verdade que Tiago não é professor” => “Tiago é professor” 

**Se uma proposição é verdadeira, quando negada torna-se falsa e vice-versa.** 

|Tiago é inteligente.|Tiago não é inteligente.|
|---|---|
|p|**¬**p|
|V|F|
|F|V|



## **1.3.7 Exercícios** 

- 1) Quais das frases abaixo são proposições: 

- a) A lua é feita de queijo. 

- b) Dois é um número primo. 

- c) O jogo terminará logo? 

- d) As taxas do ano que vem serão maiores. 

- e) x² - 4 = 0 

- 2) Formalize as seguintes frases interpretando os predicados s, m, c e n como sendo respectivamente “Sampaio Corrêa vence”, “Moto Club vence”, “está chovendo” e “está nevando”. 

   - a. Se está chovendo então o Sampaio Corrêa vence. 

   - b. Ou o Sampaio Corrêa vence ou o Moto Club vence e ou o Sampaio Corrêa vence ou o Moto Club perde. 

   - c. O Moto Club vence se, e somente se, o Sampaio Corrêa perder. 

   - d. Se o Moto Club vence, então está nevando ou chovendo, e o Sampaio Corrêa perde. 

   - e. Se está nevando, então nem o Moto Club e nem o Sampaio Corrêa vencem. 

- 3) Faça as tabelas-verdade do exercício anterior. 

## **1.3.8 Negação de proposições compostas:** 

Vimos que é fácil negar uma proposição simples, se o valor lógico é verdadeiro, passa a ser 

falso e vice-versa. Para negar uma proposição composta devemos primeiro observar qual o conectivo que esta sendo utilizado: 

## **Negação de uma conjunção ¬(p** ∧ q **):** 

Para negar uma proposição no formato de conjunção (p e q), faremos o seguinte: 

- **¬** 

- 1. Negaremos a primeira parte ( p); 

- **¬** 

- 2. Negaremos a segunda parte ( q); 

3. Trocaremos e por ou. 

11 

Logo, dizer que _“Não é verdade que João é médico e Pedro é dentista”_ é logicamente equivalente a dizer que _“João não é médico ou Pedro não é dentista”_ . 

Assim, podemos dizer que: 

## **¬(p** ∧ q **)** ⬄ **¬p** ∨ **¬** q 

Podemos comprovar pela tabela-verdade: 

|p|q|p∧q|**¬(p**∧ q**)**|**¬p **|**¬**q|**¬p **∨ **¬**q|
|---|---|---|---|---|---|---|
|V|V|V|F|F|F|F|
|V|F|F|V|F|V|V|
|F|V|F|V|V|F|V|
|F|F|F|V|V|V|V|



## **Negação de uma disjunção ¬(p** ∨ q **):** 

Para negar uma proposição no formato de disjunção (p ou q), faremos o seguinte: 

- **¬** 

- 1. Negaremos a primeira parte ( p); 

- **¬** 

- 2. Negaremos a segunda parte ( q); 

3. Trocaremos ou por e. 

Logo, dizer que _“Não é verdade que João é médico ou Pedro é dentista”_ é logicamente equivalente a dizer que _“João não é médico e Pedro não é dentista”_ . 

Assim, podemos dizer que: 

**¬(p** ∨ q **)** ⬄ **¬p** ∧ **¬** q 

Podemos comprovar pela tabela-verdade: 

|p|q|p∨ q|¬(p∨q)|**¬p **|**¬**q|**¬p **∧**¬**q|
|---|---|---|---|---|---|---|
|V|V|V|F|F|F|F|
|V|F|V|F|F|V|F|
|F|V|V|F|V|F|F|
|F|F|F|V|V|V|V|



## **Negação de uma implicação ¬(p → ):** 

Para negar uma implicação: 

1. Mantemos a primeira parte; 

2. Trocamos a implicação por e; 

3. Negamos a segunda parte. 

Logo, dizer que _“Se chover então levarei o guarda-chuva”_ é logicamente equivalente a 

dizer que _“Chove e eu não levo o guarda-chuva”_ . 

12 

## Assim: 

**¬(p →** q **)** ⬄ **p** ∧ **¬** q 

||||**¬(p →**q**)**⬄|**p**∧**¬**q||
|---|---|---|---|---|---|
|p|q|p**→** q|**¬(p→**q**)**|**¬**q|**p**∧**¬**q|
|V|V|V|F|F|F|
|V|F|F|V|V|V|
|F|V|V|F|F|F|
|F|F|V|F|V|F|



## **2 Expressões lógicas e Tabela-verdade:** 

Já vimos que uma _Tabela-Verdade_ que contém **duas** proposições apresentará exatamente um número de **quatro** linhas. Mas e se estivermos analisando uma proposição composta com três ou mais proposições? 

## **O número de linhas na tabela-verdade é igual a 2[n] , onde n é o número de proposições.** 

Ou seja, se estivermos trabalhando com duas proposições **p** e **q** , então a tabela-verdade terá 4 linhas. Se estivermos trabalhando com uma proposição composta que tenha **três** componentes **p, q e r,** a tabela-verdade terá **2[3] = 8** . E assim, por diante. 

Uma coisa muito importante que deve ser dita neste momento é que, na hora de construirmos a tabela-verdade de uma proposição composta qualquer, teremos que seguir uma certa ordem de precedência dos conectivos. Ou seja, os nossos passos terão que obedecer a uma sequência. Começaremos sempre trabalhando com o que houver dentro dos parênteses. Só depois, passaremos ao que houver fora deles. Em ambos os casos, sempre obedecendo à seguinte ordem: 

## **1. Faremos as negações** 

## **2. Faremos as conjunções ou disjunções, na ordem em que aparecerem;** 

## **3. Faremos a condicional;** 

## **4. Faremos a bicondicional.** 

Sempre que temos mais de uma proposição envolvida em uma sentença, temos uma expressão. Os parênteses são utilizados para agrupar sub-expressões. Por exemplo: 

“Conheci seu amigo e ele é muito inteligente ou muito doido.” 

Esta sentença deve ser traduzida para **p** ∨ **r)** , se ela for traduzida para  ( **p** ∨ **r** provavelmente terá um sentido diferente, e se ela fosse traduzida para **p** ∨ **r** , poderia ser ambígua. 

13 

## **2.1 Tautologia** 

Uma proposição composta formada por duas ou mais proposições p, q, r, ... será dita uma Tautologia se ela for **sempre verdadeira** , independentemente dos valores lógicos das proposições p, q, r, ... que a compõem. 

Em palavras mais simples: para saber se uma proposição composta é uma Tautologia, construiremos a sua tabela-verdade. Se a última coluna da tabela-verdade só apresentar verdadeiro (e nenhum falso), então estaremos diante de uma Tautologia. 

**¬** Exemplo: p ∨ p 

|emplo: p∨**¬**p|||
|---|---|---|
|p|**¬**p|p∨**¬**p|
|V|F|<br>V|
|F|V|V|



## **2.2 Contradição** 

Uma proposição composta formada por duas ou mais proposições p, q, r, ... será dita uma contradição se ela for sempre falsa, independentemente dos valores lógicos das proposições p, q, r ... que a compõem. Ou seja, construindo a tabela-verdade de uma proposição composta, se todos os resultados da última coluna forem FALSOS, então estaremos diante de uma contradição. 

Exemplo: p **¬** p 

|p|**¬**p|p<br>**¬**p|
|---|---|---|
|V|F|F|
|F|V|F|



## **2.3 Contingência** 

Uma proposição composta será dita uma contingência sempre que não for uma tautologia ou uma contradição. Isto é, o resultado de sua tabela-verdade não será nem somente valores verdadeiros e nem somente valores falsos, mas apresentará ambos. 

## **2.4 Para pensar** 

Quantos conectivos binários distintos vimos até agora? 

Conjunção, disjunção, disjunção exclusiva, condicional e bicondicional. Estes são os principais conectivos da lógica proposicional. 

Existem outros? Quantos podem existir? 

**==> picture [108 x 47] intentionally omitted <==**

14 

|F|V|V ou F|
|---|---|---|
|F|F|V ou F|



Um sexto conectivo bastante utilizado na lógica de circuitos eletrônicos é o NAND, que resulta na negação da conjunção. 

|p|q|p**NAND** q|
|---|---|---|
|V|V|<br>F|
|V|F|V|
|F|V|V|
|F|F|V|



Os outros dez conectivos são pouco utilizados, principalmente por que podem ser expressados pela combinação dos conectivos básicos. Os conectivos negação, conjunção e disjunção, são ditos universais, pois qualquer outro conectivo e qualquer expressão pode ser representada utilizando unicamente estes três conectivos. 

## **2.5 Exercícios** 

- 1 Verifique se as seguintes expressões abaixo são tautologias, contradições ou contingências, prove a sua afirmativa usando tabelas verdade. 

- a) (A→B)→[(A∨C)→(B∨C)] 

- b) (A∨B) ∧ (A∧B) 

- c) (A∧B) ∨ (C→A) ∧ (B∨C) 

## **2.6 Equivalência de proposições** 

Vimos nos tópicos anteriores alguns casos de equivalência de proposições. Dizemos que temos uma equivalência quando duas proposições são sintaticamente diferentes (i.e. textualmente), mas são semanticamente idênticas (i.e. possuem o mesmo significado). A notação de equivalência é dada pelo símbolo ⬄. 

Exemplo: 

**==> picture [109 x 13] intentionally omitted <==**

Como vimos, podemos comprovar pela tabela-verdade, onde encontramos que a 4[a] coluna **¬(p** ∨ q **)** é idêntica a 7[a] coluna **¬p** ∧ **¬** q: 

|a a 7a|colun|a**¬p**∧**¬**|q:||||
|---|---|---|---|---|---|---|
|p|q|p ∨ q|¬(p ∨ q)|**¬p **|**¬**q|**¬p **∧**¬**q|
|V|V|V|**F**|F|F|**F**|
|V|F|V|**F**|F|V|**F**|
|F|V|V|**F**|V|F|**F**|
|F|F|F|**V**|V|V|**V**|



Dentro das equivalências lógicas, existem algumas bastante populares e indiscutíveis, chamadas de Leis de Equivalência. As Leis de Equivalência são similares as identidades matemáticas, porém são aplicadas sobre proposições. Estas leis fornecem padrões que podem ser 

15 

utilizados para simplificar uma expressão complicada ou encontrar semelhança entre duas proposições distintas. 

A seguir estão listas as principais Leis de Equivalência, onde V representa uma tautologia e F representa uma contradição: 

|F representa uma contradição:|||
|---|---|---|
|**Lei **|**Aplicação**||
|Identidade|p∧V⬄p|p∨F⬄p|
|Dominação|p∨V⬄V|p∧F⬄F|
|Idempotência|p∨p⬄p|p∧p⬄p|
|Dupla Negação|¬¬p⬄p||
|Comutatividade|p∨q⬄q∨p|p∧q⬄q∧p|
|Associatividade|<br>(p∨q)∨r⬄p∨(q∨r)|<br>(p∧q)∧r⬄p∧(q∧r)|
|Distributiva|p∨(q∧r)⬄(p∨q)∧(p<br>∨r)|p∧(q∨r)⬄(p∧q)∨(p∧<br>r)|
|De Morgan|¬(p ∨ q) ⬄¬p ∧¬q|¬(p ∧q) ⬄¬p ∨ ¬q|
|Tautologia/Contradição Trivial|p∨ ¬p⬄V|p∧ ¬p⬄F|



Utilizando equivalências lógicas também podemos reescrever alguns operadores baseados em outros: 

|em outros:|||
|---|---|---|
|**Operador**|**Equivalência**||
|Ou exclusivo|p ⊕ q ⬄ (p ∨ q) ∧¬(p ∧q)|p ⊕ q ⬄ (p ∧¬q) ∨ (¬p ∧q)|
|Implicação/condicional|p →q⬄ ¬p∨q|p →q⬄ ¬q → ¬p|
|Bicondicional|p↔ q⬄(p→q) ∧ (q→ p)|p**↔** q⬄ ¬(p⊕ q)|



## **2.6.1 Sobre a condicional:** 

Uma proposição composta condicional p → q, aceita três proposições associadas a ela: 

- a recíproca da condicional: p → q : q → p 

- a contrária da condicional: p → q : ← p → ← q 

- a contrapositiva da condicional: p → q : ← q → ← p 

É importante perceber que apenas a contrapositiva é equivalente a condicional: 

|||||Condicional|Recíproca|Contrária|Contrapositiva|
|---|---|---|---|---|---|---|---|
|p|q|¬p|¬q|p→q|<br>q→p|¬p→ ¬q|<br>¬q→ ¬p|
|V|V|F|F|<br>V|<br>V|<br>V|<br>V|
|V|F|F|V|F|V|V|F|
|F|V|V|F|V|F|F|V|
|F|F|V|V|V|V|V|V|



16 

## **2.6.2 Provando a equivalência através da simplificação:** 

Até agora vimos que para provar a equivalência podíamos utilizar a tabela-verdade. Entretanto, quando temos expressões muito extensas, desenhar a tabela-verdade pode ser bastante trabalhoso. A alternativa para provar uma equivalência é a simplificação ou derivação simbólica através das Leis de Equivalência: 

Exemplo: 

Verifique utilizando a derivação simbólica a seguinte equivalência: 

(p ∧ ¬q) → (p ⊕ r) ⬄ ¬p ∨ q ∨¬r 

|(p∧¬q) → (p⊕ r)⬄¬p∨q∨¬r||
|---|---|
|(p∧¬q) → (p⊕ r)|Expandimos a condicional|
|¬(p∧¬q)∨(p⊕ r)|Expandimos a disjunção exclusiva|
|¬(p∧¬q) ∨((p∨r)∧¬(p∧ r))|De Morgan|
|(¬p∨q)∨((p∨r)∧¬(p∧ r))|Comutatividade do∨|
|(q∨¬p)∨((p∨r)∧¬(p∧ r))|Associatividade do∨|
|q∨(¬p∨((p∨r)∧¬(p∧ r)))|Distributiva do∨sobre o∧|
|q∨((¬p∨(p∨r)) ∧ (¬p∨¬(p∧ r)))|Associatividade do∨|
|q∨((¬p∨p) ∨r)∧ (¬p∨¬(p∧ r)))|Tautologia trivial|
|q∨((V∨r) ∧ (¬p∨¬(p∧ r)))|Dominação|
|q∨(V∧ (¬p∨¬(p∧ r)))|Identidade|
|q∨ (¬p∨¬(p∧ r))|De Morgan|
|q∨ (¬p∨(¬p∨ ¬r))|Associatividade do∨|
|q∨ ((¬p∨ ¬p)∨ ¬r)|Idempotência|
|q∨ (¬p∨ ¬r)|Associatividade do∨|
|(q∨ ¬p) ∨ ¬r|Comutatividade do∨|
|¬p∨q∨¬r|Q.E.D. (_Quod erat demonstrandum_)|
||Como queria demonstrar (C.Q.D.)|



## **2.6.3 Exercícios:** 

1. Simplificando a expressão: (p ∧ ( ¬ ( ¬ p ∨ q ))) ∨ (p ∧ q), utilizando as leis de equivalência, obtemos (coloque os passos utilizados para chegar a resposta): 

   - a) p 

   - b) q 

   - c) p ∧ q 

   - d) Tautologia 

   - e) Contradição 

17 

2. Um economista deu a seguinte declaração em uma entrevista: "Se os juros bancários são altos, 

então a inflação é baixa". Uma proposição logicamente equivalente à do economista é: 

a) Se a inflação não é baixa, então os juros bancários não são altos. 

b) Se a inflação é alta, então os juros bancários são altos. 

c) Se os juros bancários não são altos, então a inflação não é baixa. 

d) Os juros bancários são baixos e a inflação é baixa. 

e) Ou os juros bancários, ou a inflação é baixa. 

3. O rei ir à caça é condição necessária para o duque sair do castelo, e é condição suficiente para a 

duquesa ir ao jardim. Por outro lado, o conde encontrar a princesa é condição necessária e suficiente para o barão sorrir e é condição necessária para a duquesa ir ao jardim. O barão não 

sorriu. Logo: 

a) A duquesa foi ao jardim ou o conde encontrou a princesa. 

b) Se o duque não saiu do castelo, então o conde encontrou a princesa. 

c) O rei não foi à caça e o conde não encontrou a princesa. 

d) O rei foi à caça e a duquesa não foi ao jardim. 

e) O duque saiu do castelo e o rei não foi à caça. 

4. Dizer que “André é artista ou Bernardo não é engenheiro” é logicamente equivalente a dizer 

que: 

a) André é artista se e somente se Bernardo não é engenheiro. b) Se André é artista, então Bernardo não é engenheiro. 

c) Se André não é artista, então Bernardo é engenheiro. 

d) Se Bernardo é engenheiro, então André é artista. 

e) André não é artista e Bernardo é engenheiro. 

18 

## **2.7 Circuitos digitais e portas lógicas** 

Os conectivos lógicos podem ser representados por portas lógicas para representar circuitos lógicos. Circuitos lógicos são dispositivos que operam um ou mais sinais lógicos de entrada para produzir uma e somente uma saída, dependente da função implementada no circuito. São geralmente usadas em circuitos eletrônicos, por causa das situações que os sinais deste tipo de circuito podem apresentar: presença de sinal, ou "1"; e ausência de sinal, ou "0". 

A importância dessas portas lógicas está no fato de representarem os elementos básicos de construção da maioria dos circuitos digitais práticos. Quando se deseja construir um circuito lógico (ou digital) relativamente simples, usa-se uma placa de circuito impresso com soquetes sobre os quais insere-se um circuito integrado (CI) digital. A maioria dos CI's já são padronizados, e os mais comuns pertencem à série denominada 7400. Os mais simples utilizam a tecnologia de Integração em Pequena Escala (SSI - Small Scale Integration). 

Exemplo: 

1. Qual expressão representa o seguinte circuito? P ∧ ((P ∧ Q) ∨ ((P ∧ Q) ∨ Q)) 

2. Se a entrada P estiver ligada e a entrada Q desligada, qual o valor na saída? FALSO 

3. É possível reduzir o circuito acima e continuar obtendo as mesmas saídas de acordo com as entradas P e Q? (P ∧ Q) 

19 

## **2.8 Consequência Lógica** 

Trata-se de uma relação entre um conjunto de proposições e uma proposição final, na qual o primeiro acarreta o segundo. Por exemplo, diz-se que _"Caco é verde"_ é uma consequência lógica de _"todos os sapos são verdes"_ e _"Caco é um sapo"_ , porque seria auto-contraditório afirmar estas últimas sentenças e negar a primeira. A consequência lógica é a relação entre as premissas e a conclusão de um argumento válido. 

Um argumento é uma série de proposições P1, P2, P3, ..., Pn, Q. Um argumento é dito válido se sempre que as premissas (ou hipóteses) P1, P2, P3, ..., Pn forem verdadeiras e a conclusão Q também for. A validade depende somente da relação existente entre as premissas e a conclusão. Não é possível ter a conclusão falsa se as premissas forem verdadeiras. 

Veja o conjunto de proposições abaixo: 

“Na corrida, o carro do Massa bateu ou deu defeito. O carro do Massa não bateu, Logo, o carro do Massa deu defeito.” 

Na forma proposicional, temos as seguintes proposições: 

P: O carro do Massa bateu; 

Q: O carro do Massa deu defeito. 

Assim, podemos definir o argumento: (P ∨ Q), ¬ P, Q. 

Se um argumento P1, P2, ..., Pn, Q é válido. Dizemos que Q é logicamente consequente de P1, P2, ..., Pn. Ainda, P1, P2, ..., Pn implicam tautologicamente Q: 

**==> picture [198 x 12] intentionally omitted <==**

## **2.8.1 Verificando a validade de um argumento** 

A tabela-verdade é suficiente para verificar a validade de qualquer argumento na lógica proposicional. Na tabela, sempre que tivermos todas as premissas verdadeiras, a conclusão deve ser verdadeira para que o argumento seja válido. Caso contrário o argumento é inválido. 

Exemplo 1: 

Se o estudante come no bandejão então o estudante está bem alimentado. (P → Q) O estudante come no bandejão. ( P ) 

Logo: O estudante está bem alimentado. ( Q ) 

**==> picture [188 x 90] intentionally omitted <==**

20 

## Exemplo 2: 

Se ganho na loteria então sou sortudo. (P → Q) ¬ Não ganhei na loteria. ( P ) ¬ Logo: Não sou sortudo. ( Q ) 

|P|Q|P|→ Q|¬P|¬Q|
|---|---|---|---|---|---|
|V|V||V|F|**F**|
|V|F||F|F|**V**|
|F|V||V|V|**F**|
|F|F||V|V|**V**|
||||~~P → Q,¬P ∴ ¬Q ~~|||



Outra forma de verificar a validade é aplicar uma conjunção entre as premissas e implicar sobre a conclusão, se e somente se o resultado for uma tautologia então o argumento é válido. Exemplo: 

P → Q, P ∴ Q   =>  ((P → Q) ∧ P) → Q 

|||P → Q,|P∴Q   =>  ((|P → Q)∧P) → Q|
|---|---|---|---|---|
|P|Q|P→ Q|(P→ Q)∧P|((P→ Q)∧P)→Q|
|V|V|V|V|**V**|
|V|F|F|F|**V**|
|F|V|V|F|**V**|
|F|F|V|F|**V**|



P → Q, ¬ P ∴ ¬ Q  =>  (P → Q) ∧ ¬ P → ¬ Q 

||||P → Q|,¬P∴ ¬Q  =>  (|P → Q|)∧¬P →¬Q|
|---|---|---|---|---|---|---|
|P|Q|P→ Q|¬P|(P→ Q)∧ ¬P|¬Q|((P→ Q)∧ ¬P)→ ¬Q|
|V|V|V|F|F|F|**V**|
|V|F|F|F|F|V|**V**|
|F|V|V|V|V|F|**F**|
|F|F|V|V|V|V|**V**|



Existe ainda um terceiro método para verificar a validade de um argumento. Este método é baseado no uso de **regras de inferência** . 

## **2.8.2 Regras de inferência** 

Para verificar se Q é derivada de P1, P2, ..., Pn, aplica-se as regras de inferência a P1, P2 , ..., Pn e nas fórmulas derivadas delas, até que Q seja encontrado. Este método é considerado puramente sintático. 

As derivações partem de um conjunto de fórmulas admitidas como verdadeiras _a priori_ , denominadas de **axiomas** . As derivações levam a prova da validade do argumento. Uma **prova** é uma sequência de fórmulas proposicionais tal que cada fórmula é uma instância dos axiomas do sistema, derivada das anteriores pela aplicação das regras de inferência. O método de prova utilizado para verificar a validade de um argumento é a **dedução** . 

21 

Regras de Inferência: 

|Regras de|Inferência:|||||||||
|---|---|---|---|---|---|---|---|---|---|
|1) Conjunção|𝑃, 𝑄<br>𝑃∧𝑄|2) Simplificação<br>𝑃∧𝑄<br>𝑄||||3) Adição||𝑃<br>𝑃∨𝑄||
|4) Silogismo Disjuntivo<br>𝑃∨𝑄,¬𝑃<br>𝑄||5) Silogismo Hipotético<br>𝑃→𝑄<br>(<br>),(𝑄→𝑅)<br>(𝑃→𝑅)||||6) Modus Ponens<br>𝑃→𝑄<br>(<br>),𝑃<br>𝑄||||
||||||||𝑄|||
|7) Modus Tollens<br>𝑃→𝑄<br>(<br>),¬𝑄<br>¬𝑃||8) Contradição||𝑃,¬𝑃<br>𝑄||9) Dupla Negação<br>¬¬𝑃<br>𝑃<br>𝑜𝑢|||𝑃<br>¬¬𝑃|
|||||𝑄||||||
|10) Transitividade da<br>↔<br>𝑃↔𝑄<br>(<br>),(𝑄↔𝑅)<br>(𝑃↔𝑅)||11) Eliminação da<br>↔<br>𝑃↔𝑄<br>(<br>)<br>(𝑃→𝑄)<br>𝑜𝑢|||𝑃↔𝑄<br>(<br>)<br>(𝑄→𝑃)|12) Introdução da<br>↔<br>𝑃→𝑄<br>(<br>),(𝑄→𝑃)<br>(𝑃↔𝑄)||||



Exemplo: 

_Se João namora Maria então João é fiel a Maria._ 

_Se João namora Ana então João é fiel a Ana._ 

_Se João é fiel a Maria ou a Ana então João é fiel. João não é fiel._ 

_Logo, João não namora Maria e não namora Ana._ 

Analisando as proposições acima, podemos traduzi-las simbolicamente para: 

1. P → 

2. R → S 3. Q ∨ S → T 

4. ¬ T 

5. ∴ ¬ P ∧ ¬ R 

As proposições de 1 a 4 são as nossas premissas, o número 5 é a conclusão. Para provar a validade deste argumento devemos derivar as premissas através das regras de inferência até chegarmos na conclusão: 

6. ¬ (Q ∨ S) Modus Tollens de 3 e 4. 7. ¬ Q ∧ ¬ S De Morgan de 6. 8. ¬ Q Simplificação de 7. 9. ¬ P Modus Tollens de 8 e 1. 10. ¬ S Simplificação de 7. 11. ¬ R Modus Tollens de 10 e 2. 12. ¬ P ∧ ¬ R Conjunção de 11 e 9. 

Assim, provou-se por dedução a validade do argumento. 

22 

## **2.8.3 Exercícios:** 

- 1) Prove a validade do seguinte argumento: 

_Não está com sol, está frio._ 

_Vamos nadar somente se estiver com sol._ 

_Se não nadarmos vamos andar de barco._ 

_Se andarmos de barco chegaremos cedo em casa. Logo, vamos chegar cedo em casa._ 

- 2) Prove a validade dos seguintes argumento: 

a) P, ¬¬ (Q ∧ R) ∴ ¬¬ P ∧ R 

b) P ∧ Q, R ∴ Q ∧ R 

23 

## **2.9 Lógica de Predicados** 

Podemos usar a lógica proposicional para provar a validade de um grande números de inferências. Por exemplo: 

_Se está frio então vai nevar._ 

Vimos que esta proposição é equivalente a: 

_Se não nevar então não está frio._ 

Na lógica proposicional provamos esta equivalência facilmente pela tabela-verdade, onde 

iremos obter: p → q ⬄ ¬q → ¬p. 

Mas algumas inferências não podem ser provadas pela lógica proposicional, por exemplo: 

_Algumas pessoas são adoradas por todo mundo._ 

Podemos concluir então, que: 

_Todo mundo adora alguém._ 

Como ficariam as proposições destas duas sentenças? Dificilmente conseguiremos expressá-las com a lógica proposicional que vimos até agora. Para casos como este precisamos de regras mais expressivas, que contemplem o uso de palavras como _alguém_ , _todo mundo_ , _ninguém_ , entre outros. 

A lógica de predicados é uma extensão da lógica proposicional que permite a quantificação em classes de entidades. A lógica proposicional trata as sentenças como proposições simples e entidades atômicas. Por outro lado, a lógica de predicados distingue o sujeito de uma sentença do seu predicado. 

Na gramatica, se temos a sentença: 

_O cão está dormindo._ 

O sujeito é “ _O cão_ ” e o predicado é “está dormindo.”, na lógica de predicados seguiremos o mesmo padrão. 

## **2.9.1 Fórmulas da lógica de predicados** 

As constantes que identificam indivíduos ou objetos serão: a, b, c, ... 

As variáveis individuais sobre estas constantes serão: x, y, z, ... 

O resultado da aplicação de um predicado **P** sobre uma constante **a** é a proposição **P(a)** , que 

significa que: o objeto denotado por **a** possui a propriedade denotada por **P** . 

O resultado da aplicação de um predicado **P** sobre uma variável **x** é a proposição **P(x)** , que 

significa que: todos os objetos do tipo **x** possuem a propriedade denotada por **P** . 

Por exemplo: 

Digamos que **a = 2** , **P =** _“é um número primo.”_ e **x** = conjunto de números primos, então: 

24 

P(a) é a forma proposicional de: _“2 é um número primo.”_ e 

P(x) é a forma proposicional de: _“x é um número primo.”_ 

A lógica de predicados generaliza a noção de predicado para permitir a inclusão de funções 

de qualquer número de argumentos. Exemplo: 

Seja R(x, y) = _“x ama y”_ , então se x = “Mário” e y = “Maria” temos: 

R(x, y) = _“Mário ama Maria”_ 

Se y = “futebol”, temos: 

R(x, y) = _“Mário ama futebol”_ 

## **2.9.2 Universo de discurso** 

A força de distinção de objetos com predicados reside no fato de podermos afirmar coisas sobre vários objetos de uma única vez. 

Exemplo: 

Seja P(x) = “x*2 `≥` x”. Podemos dizer: “Para qualquer número x, P(x) é verdadeiro”, ao invés de: 

A coleção de valores que a variável x pode assumir é denominado universo de discurso de x. 

No exemplo, nossa afirmação será verdadeira quando o universo de discurso de x for o conjunto dos números naturais, mas será falsa se o universo for o conjunto dos números inteiros. 

## **2.9.3 Expressões com quantificadores** 

Quantificadores fornecem uma notação que permite quantificar quantos objetos no U.D. satisfazem determinado predicado. Os dois principais quantificadores são: 

∀ = é o quantificador universal “para todos” 

∃ = é o quantificador universal “existe um” Exemplos: 

∀x P(x) = Para todo x no U.D., P se aplica. 

∃x P(x) = Existe um x no U.D. tal que P se aplica. (onde _um_ pode ser _pelo menos um_ ) 

Seja x com U.D. “alunos de MDL” e P(x) a proposição “x tirou nota 10.” Então ∃x P(x) pode ser entendido como: 

_Algum aluno de MDL tirou nota 10._ ou 

_Existe um aluno de MDL que tirou nota 10._ ou 

_Pelo menos um aluno de MDL tirou nota 10._ 

Já ∀x P(x) pode ser entendido como: 

_“Todos os alunos de MDL tiraram nota 10.”_ 

_“Para cada aluno de MDL, a nota obtida foi 10._ 

## **2.9.4 Variáveis livres e restritas** 

Dizer que uma expressão P(x) tem uma variável livre x, significa que x é indefinida. Um quantificador opera em uma expressão possuindo uma ou mais variáveis livres, e restringe uma ou mais dessas variáveis, para produzir uma expressão que possua uma ou mais variáveis restritas. 

P(x, y) possui duas variáveis livres, x e y. 

∀x P(x, y) possui uma variável livre e uma variável restrita, y e x respectivamente. 

Uma expressão sem variáveis livres passa a ser uma proposição. 

Uma expressão com uma ou mais variáveis livres é similar a um predicado: 

Q(y) = ∀x P(x, y). 

Exemplo: 

Seja o U.D. de x e y pessoas. 

Seja P(x, y) = “x parece com y” (predicado com 2 variáveis livres) 

Então, ∃y P(x, y) = “Existe alguém que parece com x.” (predicado com 1 variável livre) 

∀x(∃y P(x, y)) = “Todo mundo têm alguém com quem parece.” Em outras palavras: “Para 

todo x existe pelo menos um y, tal que x parece com y.” (proposição sem variável livre) 

Outros exemplos: 

∀x ∃x P(x) => x já não é uma variável livre em ∃y P(x), assim a restrição ∀x não têm aplicação nenhuma. 

(∀x P(x)) ∧ Q(x) => x aparece também fora do escopo de ∀x, sendo portanto uma variável 

livre. 

(∀x P(x)) ∧ (∃x Q(x)) => proposição sem variáveis livres e ambos os quantificadores estão sendo aplicados. 

## **2.9.5 Leis de equivalência da lógica de predicados** 

Assim como na lógica proposicional, também teremos algumas leis de equivalência na lógica de predicados: 

∀x P(x) ⬄ ¬ ∃x ¬ P(x) 

∃x P(x) ⬄ ¬ ∀x ¬ P(x) 

∀x P(x) ⬄ P(a) ∧ P(b) ∧ P(c) ∧ ... 

∃x P(x) ⬄ P(a) ∨ P(b) ∨ P(c) ∨ ... 

∀x ∀y P(x, y) ⬄∀y ∀x P(x, y) 

∃x ∃y P(x, y) ⬄∃y ∃x P(x, y) 

∀x (P(x) ∧ Q(x)) ⬄∀x P(x) ∧ ∀x Q(x) 

∃x (P(x) ∨ Q(x)) ⬄∃x P(x) ∨ ∃x Q(x) 

## **2.9.6 Quantificadores e conectivos** 

Seja U.D. os estacionamentos em São Luís. 

Seja P(x) = “x está ocupado.” 

Seja Q(x) = “x é gratuito.” 

1. ∃x (P(x) ∧ Q(x)) : _Alguns estacionamentos são gratuitos e estão ocupados._ 

2. ∀x (P(x) ∧ Q(x)) : _Todos os estacionamentos são gratuitos e estão ocupados._ 

3. ∃x (P(x) → Q(x)) : _Existe ao menos um estacionamento que é gratuito. E se é gratuito,_ 

_então está ocupado._ 

4. ∀x (P(x) → Q(x)) : _Todos os estacionamentos gratuitos estão ocupados._ 

## **2.9.7 Exercícios** 

1. Dada a seguinte fórmula ∀x ∃y ama(x, y) qual das seguintes sentenças em linguagem 

natural ela representa, considerando que ama(x, y) representa que x ama y? 

a) Alguém ama a todos. 

b) Todos amam alguém. 

c) Ninguém ama a todos. 

d) Há alguém que todos amam. 

- e) Nenhuma das alternativas anteriores. 

2. Considere os predicados Par(x) e Primo(x), que significam x é um número par e x é um 

número primo, respectivamente. Exprima as frases seguintes na linguagem da lógica de predicados: 

a) Nenhum número par é primo. 

b) Todo o primo é ímpar ou igual a 2. 

Quais destas sentenças são verdadeiras, considerando o universo de discurso os números naturais? 

3. Verifique se as seguintes equivalências são válidas: 

a) ¬ ∀x P(x) ⬄ ¬ ∃x P(x) 

b) ∀x (P(x) ∧ Q(x)) ⬄ ¬ ∃x ¬ P(x) ∧ ¬ ∃x ¬ Q(x) 

27 

