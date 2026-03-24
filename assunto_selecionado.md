|**Sumário**|**Sumário**|||||
|---|---|---|---|---|---|
|**1**|**Introdução**||||**3**|
|**2**|**Histórico de JavaScript**||||**4**|
|**3**|**Conceitos**||||**6**|
|**4**|**Núcleo da Linguagem JavaScript**||||**9**|
||4.1 Tipos de dados .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
||4.1.1 Tipos numéricos . . . . . . . . . . . . . . . . . . . . . . . . . .||||9|
||4.1.2 Booleano|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
||4.1.3 Indefnido|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
||4.1.4 null . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
||4.1.5 Strings . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||4.1.6 Arrays . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||4.2 Operadores . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||4.2.1 Aritméticos||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||4.2.2 Comparação|||. . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||4.2.3 Bit a bit .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||4.2.4 Atribuição|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||4.2.5 Lógicos . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||4.3 Estruturas de controle<br>. . . . . . . . . . . . . . . . . . . . . . . . . .||||13|
||4.4 Funções . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
||4.5 Objetos<br>. . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|18|
||4.5.1 Objeto String|||. . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
||4.5.2 Objeto Array|||. . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
||4.6 Exceções<br>. . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|**5**|**Web 2.0**||||**31**|
||5.1 O que é Ajax? . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
||5.2 O papel do JavaScript . . . . . . . . . . . . . . . . . . . . . . . . . . .||||31|
||5.3 Exemplo de aplicação Ajax . . . . . . . . . . . . . . . . . . . . . . . .||||35|
|**6**|**Ferramentas**||||**43**|

Na verdade, JavaScript é uma linguagem de programação de propósito geral, dinâmica e possui características do paradigma de orientação a objetos. Ela é capaz de realizar virtualmente qualquer tipo de aplicação, e rodará no _browser_ do cliente.

Strings são sequências de caractéres. Em JavaScript a string pode ser tanto um tipo primitivo de dado como um objeto; no entanto, ao manipulá-la temos a impressão de que sejam objetos pois as strings em JavaScript possuem métodos que podemos invocar para realizar determinadas operações sobre elas. Essa confusão ocorre porque quando criamos uma string primitiva, o JavaScript cria também um objeto string e converte automaticamente entre esses tipos quando necessário.

Este conceito será explicado melhor adiante, quando tratarmos de objetos. Para se declarar uma string, basta colocar uma sequência de caractéres entre aspas simples ou duplas.

var str = "Eu sou uma string!"; var str2 = ’Eu também sou uma string’; // Declaração de strings primitivas var str3 = new String("Outra string"); // Acima um objeto string declarado de forma explícita // não há diferença nenhuma entre esses dois tipos no que se refere // a seu uso.

Os Arrays são pares do tipo inteiro-valor para se mapear valores a partir de um índice numérico. Em JavaScript os Arrays são objetos com métodos próprios. Um objeto do tipo Array serve para se guardar uma coleção de ítens em uma única variável.

Na maioria das vezes, quando usamos um laço do tipo _while_ também construímos uma estrutura com um contador que é incrementado a cada passo para controle do laço e manipulação interna de objetos, arrays como nos exemplos anteriores. Os laços _for_ oferecem a vantagem de já possuírem em sua estrutura essa variável de contador e incrementá-la de maneira implícita. Exemplo:

A segunda forma de se declarar uma função é utilizando o construtor _Function()_ e o operador _new_ , pois em JavaScript funções e objetos são interligados.

## **4.5 Objetos**

No paradigma de orientação a objetos, os métodos são simplesmente funções que são invocadas por meio de um objeto! E em JavaScript isso é levado tão a sério que a maneira de se criar métodos para seus objetos leva isso ao pé da letra. Basta criarmos uma função e atribuí-la a uma propriedade do objeto.

Quando declaramos ou atribuímos um método no construtor de um objeto ele ficará disponível para todas as instâncias criadas a partir desse construtor. No entanto, existe um modo muito mais eficiente de se fazer isso, que é com o uso da propriedade _prototype_ . Tudo o que for definido no _prototype_ de um objeto poderá ser referenciado por todas as instâncias desse objeto. Mesmo as propriedades do _prototype_ que forem definidas ou alteradas depois da instanciação serão acessíveis aos objetos declarados anteriormente. Além disso, é importante ter em mente que os atributos e funções declarados no prototype não são copiados para os objetos, portanto há uma economia significativa de memória quando usamos muitas propriedades compartilhadas e instâncias. Exemplo:

Para finalizar nossa discussão sobre objetos, vamos mostrar como eles podem ser usados como arrays associativos, ou seja, um array com objetos indexados por valores não numéricos. Isso só pode ser feito porque é possível acessarmos atributos de um objeto usando _MeuObjeto["atributo"]_ . Assim podemos simular o comportamento de um array associativo armazenando cada item em um atri-

A seguir, vamos dedicar atenção aos exemplos de métodos e propriedades de dois importantes objetos nativos do JavaScript: os Arrays e Strings.

## **4.5.1 Objeto String**

**valueOf()** - retona o valor primitivo do objeto string. É útil quando desejamos atribuir o valor de um objeto string para uma variável que seja do tipo primitivo string.

**split(separador,limite)** - retorna um objeto Array contendo as substrings que resultaram da separação da string original pelo conteúdo de _separador_ , sem incluí-lo. Se separador for indefinido, o Array resultante terá como elemento apenas a string original. O argumento limite define o número máximo de elementos que o array pode ter, excedido esse valor o Array será truncado. Caso o limite seja indefinido, não haverá um limite no número de elementos do array resultante.

var dados = "Terra, Marte, Jupiter"; var arr1 = dados.split(", "); var arr2 = dados.split(", ",2); // Em arr1 será armazenado um objeto array contendo na posição 1 // "Terra", na posição 2 "Marte" e na posição 3 "Jupiter". // Já em arr2 será armazenado um array da mesma forma que descrito // acima, no entanto apenas com as duas primeiras posições, ou seja, // sem Jupiter.

Quanto a propriedades, os objetos do tipo string só possuem uma:

## **4.5.2 Objeto Array**

Agora faremos uma breve descrição dos métodos que o objeto Array traz consigo.

A seguir, vamos dar uma olhada nas propriedades do objeto Arrays. As propriedades são acessadas de modo similar aos métodos, basta usar o nome do objeto.propriedade e depois disso teremos um exemplo simples.

**constructor** - esta propriedade é uma referência à função que criou este objeto array.

- **prototype** - permite se adicionar propriedades e métodos a este objeto array. Este é usado na orientação a objetos para que um objeto herde elementos do prototype do outro.

Encerramos nossa discussão sobre objetos aqui. Embora haja mais detalhes que podem ser apresentados e caracterizem o potencial de uso sobre sobre eles, não é objetivo deste documento nos aprofundarmos muito nos tópicos abordados e sim proporcionar as ferramentas para um bom uso inicial da linguagem. Aqueles que se interessarem pelo assunto poderão encontrar muitas informações nos materiais referenciados na Bibliografia.

## **4.6 Exceções**

Nas versões atuais, comandos para manipulação de exceções foram incluídos em JavaScript, de forma similar aos que a linguagem Java oferece. Temos os comandos _throw, try, catch_ e _finally_ . Com eles é possível desenvolver uma aplicação em JavaScript capaz de tratar possíveis erros em tempo de execução, aumentando de maneira considerável sua robustez. Vamos mostrar com exemplos o seu funcionamento.

JavaScript não nos obriga a tratar essas exceções enquanto elas não forem lançadas, por exemplo, no caso acima se tivéssemos passado o argumento corretamente, não receberíamos nenhuma mensagem dizendo que existe uma exceção não tratada. O interpretador irá apenas "reclamar" quando essa exceção for lançada e não estiver sendo tratada, como no caso acima. Agora vejamos como podemos tratá-la.

**initXMLHttpRequest()** - esta função existe apenas devido a incompatibilidade entre os browsers. Como nos dois mais usados o objeto XMLHttpRequest possui diferenças na implementação, essa função testa a existência desses objetos e retorna qual foi encontrado para função sendRequest utilizá-lo.