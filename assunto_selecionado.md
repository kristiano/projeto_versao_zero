## **Aprendendo JavaScript**

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

_– Por que aprender JavaScript?_

- "JavaScript é a ferramenta que dá acesso a um grande número de truques e de funcionalidades avançadas que estão ao alcance de todos".

- "JavaScript é usada em milhões de páginas Web com intuito de melhorar todo projeto"

- "Com JavaScript você pode deixar a sua página muito mais legal!"

De fato, concordamos que essas respostas falam verdade! Mas essa fama de ser uma linguagem ’leve’, para fazer truques em páginas, faz com que muitas pessoas pensem que JavaScript não é uma linguagem de programação séria. Muitos lembram dela como se fosse apenas uma extensão do HTML. A sigla DHTML ( _Dynamic HTML_ ) é uma das causadoras dessa impressão, porque sugere que é um novo tipo de HTML e não que é usado JavaScript e HTML juntos.

Na verdade, JavaScript é uma linguagem de programação de propósito geral, dinâmica e possui características do paradigma de orientação a objetos. Ela é capaz de realizar virtualmente qualquer tipo de aplicação, e rodará no _browser_ do cliente.

Atualmente, uma empresa que utiliza JavaScript em praticamente todos os seus aplicativos é a Google Inc., como por exemplo: no site de busca Google Search[1] , no GMail[2] , no Google Maps[3] , entre outros. O que torna esses aplicativos tão populares é a forma como são interativos, e isso se deve em maior parte ao JavaScript.

A linguagem JavaScript foi objeto de estudo do projeto de iniciação científica deste autor, e foi utilizada no desenvolvimento de um editor de diagramas online, via Web, utilizando SVG ( _Scalable Vector Graphics_ ) e JavaScript.

**2 HISTÓRICO DE JAVASCRIPT**

## **2 Histórico de JavaScript**

A linguagem JavaScript foi criada pela Netscape Communications Corporation[4] e foi desenvolvida com o nome de _Mocha_ , depois passou a se chamar _LiveScript_ e foi finalmente lançada como _JavaScript_ em 1995 integrando a versão 2.0B3 do navegador Netscape e visava implementar uma tecnologia de processamento modo cliente.

A denominação da linguagem, _JavaScript_ , se deve a similaridades com a sintaxe do Java e embora as duas linguagens não tenham nenhuma outra relação além desta, os nomes ainda causam confusão para alguns usuários.

JavaScript permite criar pequenos programas embutidos no próprio código de uma página HTML e capazes de gerar números, processar alguns dados, verificar formulários, alterar valor de elementos HTML e criar elementos HTML. Tudo isso diretamente no computador cliente, evitando a troca de informações com o servidor e o tempo passa a depender somente do processamento local do cliente, não mais da latência da rede[5] .

A versão mais recente da linguagem é a 1.7, até o momento de redação deste documento. Esta versão 1.7 é suportada pela versão 2.0 do Mozilla Firefox, mas versões anteriores continuam funcionando. Além disso, outras versões de testes já estão sendo desenvolvidas, por exemplo, a versão, chamada de JavaScript 2.0, desenvolvida pela Mozilla que pode vir a se tornar padrão.

JavaScript é uma linguagem completa e poderosa que possui muitas das qualidades de diversas outras linguagens, como: listas associativas, tipagem dinâmica[6] e expressões regulares de Perl e a sintaxe similar a C/C++, linguagens de grande reconhecimento tanto no mundo acadêmico quanto comercialmente. Além disso, JavaScript é multiparadigma e entre eles destacam-se a programação estrutural e orientada a objeto; possui funções de ordem superior; entre outros.

Mesmo com o alto potencial de recursos para desenvolvimento de programas oferecido pela linguagem, grande parte das pessoas que usam JavaScript

**2 HISTÓRICO DE JAVASCRIPT**

não são programadores e isso lhe deu a reputação de ser uma linguagem para amadores, o que não é verdade, como pode ser observado com o surgimento de técnicas Ajax, que será explicado neste documento, e poderosas aplicações web. Além disso, JavaScript se tornou o carro chefe da chamada _Web 2.0_ que também será explicada mais adiante.

Nesta seção, são descritos alguns conceitos que estão bastante relacionados com a linguagem JavaScript. Esses conceitos possibilitam caracterizar melhor a linguagem e seu potencial de utilização.

JavaScript é uma linguagem de script.

JavaScript é uma linguagem de programação de tipagem dinâmica.

- JavaScript é uma linguagem de programação que possibilita a definição de funções de ordem superior.

- **Programação** _**Client-side**_ **vs.** _**Server-side**_ - JavaScript é uma linguagem que nasceu como _Client-side_ (que roda no computador cliente) e tem sido muito mais usada essa forma atualmente. Quando o programa é criado com esta característica ele é enviado para o computador cliente ainda na forma de código-fonte, que só então é interpretado e executado, dependendo assim unicamente da capacidade de processamento do cliente.

- Já o programa em uma linguagem _Server-side_ , é executado no computador Servidor e somente é enviado para o cliente o resultado da execução, sejam dados puros ou uma página HTML.

Neste estudo, tratamos JavaScript apenas como uma linguagem de programação _Client-side_ .

- **Segurança** - por ser uma linguagem que é executada no computador do cliente, o JavaScript precisa ter severas restrições para evitar que se façam códigos maliciosos que possam causar danos ao usuário.

As principais limitações do JavaScript para garantia de segurança são a proibição de:

- Acessar o hardware do cliente

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

## **4 Núcleo da Linguagem JavaScript**

Nesta seção estão descritos os conceitos básicos para se programar em JavaScript. Quem já possui algum conhecimento com outras linguagens de programação sabe que os comandos básicos compõem a "caixa de ferramentas" que deve ser utilizada para criar qualquer aplicação, seja ela muito pequena ou gigantesca.

A aplicação em JavaScript sempre será composta desses comandos e elementos menores, e a lógica com que foram colocados juntos para se relacionarem possibilita a criação de uma solução visando o resultado esperado.

Em JavaScript os números são representados pelo padrão IEEE 754. Todos os valores numéricos são "declarados" pela simples atribuição dos valores a uma variável.

O JavaScript converte automaticamente _true_ para 1 e _false_ para 0 quando isso for necessário.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Para efeito de comparação, se usarmos o operador de igualdade "==", JavaScript irá considerar iguais os valores _null_ e _undefined_ . E isso não afeta o uso da comparação _(var.metodo == null)_ quando queremos descobrir se um objeto possui determinado método. No entanto, se for necessário diferenciar os dois valores é recomendável o uso do operador "===" de identicidade. Assim, para efeito de comparação, _undefined_ e _null_ são iguais, mas não idênticos. Exemplo:

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Strings são sequências de caractéres. Em JavaScript a string pode ser tanto um tipo primitivo de dado como um objeto; no entanto, ao manipulá-la temos a impressão de que sejam objetos pois as strings em JavaScript possuem métodos que podemos invocar para realizar determinadas operações sobre elas. Essa confusão ocorre porque quando criamos uma string primitiva, o JavaScript cria também um objeto string e converte automaticamente entre esses tipos quando necessário.

Os Arrays são pares do tipo inteiro-valor para se mapear valores a partir de um índice numérico. Em JavaScript os Arrays são objetos com métodos próprios. Um objeto do tipo Array serve para se guardar uma coleção de ítens em uma única variável.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Em JavaScript os arrays podem conter valores de tipos diferentes sem nenhum problema; podemos colocar em um mesmo array inteiros, strings, booleanos e qualquer objeto que se desejar.

Nesta seção listaremos, de forma sucinta, os principais operadores que compõem o núcleo da linguagem JavaScript.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Funções possuem um papel muito importante na programação estrutural pelo fato de ajudar muito na modularização no programa, ou seja, viabiliza a divisão do programa em partes menores e logicamente relacionadas. Em JavaScript,

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Um ponto importante é que em JavaScript as funções são consideradas como dados, ou seja, podemos atribuir uma função a uma variável ou propriedade de um objeto e a partir desde momento usar a variável ou a propriedade da mesma forma que se usaria a função. Elas também podem ser passadas como argumentos para outras funções e por isso funções de JavaScript são chamadas funções de alta ordem, elas podem tanto receber funções como argumento quanto retornar uma função.

A primeira maneira de se declarar uma função é através do uso da palavra chave _function_ de maneira similar a como elas são declaradas na linguagem C, com as diferenças de que em JavaScript não definimos o tipo de retorno e nem mesmo o tipo dos argumentos. Uma função complexa pode ser capaz de tratar argumentos diferentes e retornar argumentos diferentes dependendo das circunstâncias nas quais foi invocada. Deve-se definir seu nome e seus argumentos conforme mostra o exemplo a seguir.

A segunda forma de se declarar uma função é utilizando o construtor _Function()_ e o operador _new_ , pois em JavaScript funções e objetos são interligados.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Uma terceira e última forma de se declarar uma função em JavaScript é através de literais.

Essa forma é basicamente a mesma que declarar através do construtor _Function()_ . No entanto, ela é melhor porque os comandos podem ser declarados com a sintaxe normal de JavaScript ao invés de ser uma string como é o caso do construtor. Com literais não há necessidade de manter a função em uma linha, dentro das chaves podemos construir a função usando um comando por linha normalmente.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

No paradigma de orientação a objetos, os métodos são simplesmente funções que são invocadas por meio de um objeto! E em JavaScript isso é levado tão a sério que a maneira de se criar métodos para seus objetos leva isso ao pé da letra. Basta criarmos uma função e atribuí-la a uma propriedade do objeto.

Também podemos definir os métodos dentro do próprio construtor de uma função, tanto definindo a função fora e atribuindo no construtor, como definindo a própria função dentro do próprio construtor uma vez que JavaScript suporta o aninhamento de funções.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

A seguir, vamos dedicar atenção aos exemplos de métodos e propriedades de dois importantes objetos nativos do JavaScript: os Arrays e Strings.

Vamos nos ater agora aos métodos das Strings, e embora existam outros, aqui serão relacionados apenas os que fazem parte da ECMA 262-3 que equivale ao JavaScript 1.6, pois estes métodos são comuns a uma grande variedade de _browsers_ como FireFox, Netscape e Internet Explorer.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Nas versões atuais, comandos para manipulação de exceções foram incluídos em JavaScript, de forma similar aos que a linguagem Java oferece. Temos os comandos _throw, try, catch_ e _finally_ . Com eles é possível desenvolver uma aplicação em JavaScript capaz de tratar possíveis erros em tempo de execução, aumentando de maneira considerável sua robustez. Vamos mostrar com exemplos o seu funcionamento.

**4 NÚCLEO DA LINGUAGEM JAVASCRIPT**

Agora vamos introduzir o comando _Throw_ para fazer com que essa função gere uma exceção que possa ser tratada pela própria aplicação. Exemplo 2:

JavaScript não nos obriga a tratar essas exceções enquanto elas não forem lançadas, por exemplo, no caso acima se tivéssemos passado o argumento corretamente, não receberíamos nenhuma mensagem dizendo que existe uma exceção não tratada. O interpretador irá apenas "reclamar" quando essa exceção for lançada e não estiver sendo tratada, como no caso acima. Agora vejamos como podemos tratá-la.

**5 WEB 2.0**

## **5 Web 2.0**

## **5.1 O que é Ajax?**

O nome Ajax foi cunhado por Jesse James Garrett em 2005 para se referir a um conjunto de tecnologias que já existiam, mas que passaram a ser usadas de forma inovadora, enriquecendo as possibilidades de interação na web para torná-las o mais próximo de aplicações _desktop_ quanto possível.

As páginas web sempre sofreram com falta de interação devido a própria natureza caótica da internet, de possuir uma latência alta e ser pouco confiável. Assim, é muito comum clicarmos em um link e termos que esperar as vezes até alguns segundos, dependendo da conexão, até que a próxima página seja carregada do servidor para sua máquina. É claro que as conexões têm melhorado dia a dia, mas ainda assim o simples fato de que a cada mudança de página precisamos exibir um documento totalmente novo que contém, além dos dados que requisitamos, todas as informações de _layout_ novamente, representa um gasto de banda considerável.

Uma grande diferença do Ajax é que as páginas apresentadas no _browser_ passam a ser aplicações, ou seja, a primeira vez que entramos em uma página, a aplicação é carregada para nossa máquina e depois essa aplicação fica responsável por requisitar ou enviar os dados para o servidor de forma assíncrona. Como a aplicação está o tempo todo no _browser_ do cliente, este não perde a interação e pode realizar ações mesmo enquanto espera a requisição de algum dado do servidor. Por exemplo, continuar trabalhando com os dados que já foram carregados no passado. A Figura 1 ilustra essa diferença, nela podemos observar que as aplicações Ajax possuem uma camada a mais entre a interface com o usuário e o servidor, essa camada é a aplicação propriamente dita.

## **5.2 O papel do JavaScript**

As quatro principais tecnologias utilizadas para o desenvolvimento de aplicações Ajax são esquematizadas na Figura 2. Elas desempenham as seguintes funções:

- **JavaScript** é responsável por interligar todas as outras tecnologias, é a linguagem de programação e portanto com ela é desenvolvida a aplicação que irá ser executada na máquina do cliente.

- **CSS (** _**Cascade Style Sheets**_ **)** é um padrão da W3C para estilizar elementos em uma página _web_ . Ele é utilizado para dar uma boa aparência às páginas, podendo ser acessado e editado pelo JavaScript.

- **DOM (** _**Document Object Model**_ **)** permite que uma linguagem como o JavaScript possa manipular e alterar a estrutura de documentos, por exemplo, uma

**5 WEB 2.0**

Figura 1: As diferenças entre uma página web comum e uma aplicação Ajax [2]

Figura 2: Arquitetura de uma aplicação Ajax. Observe como o código JavaScript é o elemento responsável por organizar todos os outros no cliente e trocar dados com o servidor

página durante seu tempo de vida no _browser_ do cliente.

- **XMLHttpRequest** é um objeto existente em JavaScript que permite a troca de dados com o servidor de forma assíncrona.

**5 WEB 2.0**

Aqui daremos atenção especial ao JavaScript e como ele é utilizado para manipular os elementos listados anteriormente, CSS, DOM e XMLHttpRequest. Sugerimos fortemente que procure entender melhor o uso do DOM e CSS pois são ferramentas essenciais a um bom desenvolvedor web.

Com o código JavaScript, podemos acessar todos os elementos da árvore DOM de um documento e podemos alterá-los, removê-los ou mesmo inserir um novo elemento. Isso nos ajuda a exibir os dados novos que foram requisitados do servidor pelo XMLHttpRequest. A seguir, vamos mostrar um exemplo simples de como acessar a árvore DOM com JavaScript.

**5 WEB 2.0**

dom.js - Arquivo JavaScript -----------------------------------------------------------------------------function divEdit() { /* busca na árvore DOM o elemento com ID "header" */ var header = document.getElementById("header"); /* guarda o código HTML de dentro do elemento */ var conteudo = header.innerHTML; /* reescreve o conteúdo adicionando outras tags */ header.innerHTML = "<strong>"+conteudo+"</strong>"; /* cria um novo elemento DOM */ var paragrafo = document.createElement(’p’); /* configura a propriedade title do elemento */ paragrafo.setAttribute(’title’,’Novo parágrafo’); /* cria um nó de texto */ var txt = document.createTextNode(’Parágrafo adicionado a árvore DOM’); /* insere o texto ao paragráfo */ paragrafo.appendChild(txt); /* insere o paragráfo na página */ header.appendChild(paragrafo); }

index.html - Arquivo HTML -----------------------------------------------------------------------------<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <script type="text/javascript" src="dom.js"></script> </head> <body> <div id="header"> Exemplos de manipulação do DOM por JavaScript. </div> <hr /> <br /> <input type="button" value="Altera árvore DOM" onclick="divEdit()" /> </body> </html>

Quando executar o exemplo acima em seu _browser_ a página irá conter apenas uma frase no início e um botão com o nome "Altera árvore DOM". Quando for clicado esse botão, a função divEdit() é chamada e insere um novo parágrafo na página sem necessidade de recarregá-la. Este exemplo simples mostra apenas como usar JavaScript para manipular a árvore DOM, não entramos na área do Ajax ainda, mas essa é a base para o tratamento dos dados obtidos através da técnica.

**5 WEB 2.0**

## **5.3 Exemplo de aplicação Ajax**

Nessa seção mostraremos um exemplo mais completo de uma aplicação Ajax separada em 4 arquivos, um XML com dados, um CSS com o estilo da página, um JS com a aplicação e o HTML que irá conter a aplicação.

A aplicação consiste em um página que fica constantemente requisitando um arquivo de dados com notícias do servidor e atualizando a página caso haja notícias novas nesse arquivo.

**5 WEB 2.0**

Agora vejamos o arquivo HTML. Devemos notar que o arquivo news.css é importado e o arquivo ajax.js é incluído na página, ambos serão listados a seguir. Além disso, quando a página termina de carregar, a função _timedNews_ é chamada do arquivo de JavasScript com o nome do arquivo de dados como argumento. Também temos algumas _divs_ que serão utilizadas pela aplicação como pontos de entrada de dados.

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt" > <head> <title>notícias 2.0</title> <style type="text/css" media="all"> @import "news.css"; </style> <script type="text/javascript" src="ajax.js"></script> </head> <body onload="timedNews(’data.xml’);"> <div id=’loadDiv’></div> <div id=’lastnews’> <h2>Últimas notícias</h2> <div id=’news’></div> </div> </body> </html>

No nosso caso, por se tratar de um página pequena e com o propósito de mostrar apenas o funcionamento do Ajax, não precisamos de uma folha de estilos muito complexa. Assim, os comandos CSS trabalham mais com as margens, cores e posicionamento das _divs_ vistas no documento HTML anteriormente.

**5 WEB 2.0**

Agora finalmente o arquivo JavaScript com a aplicação. Seu funcionamento será explicado a seguir.

Arquivo: ajax.js -----------------------------------------------------------------------------var req=null; // ’Constante’ para teste de quando os dados estão prontos para serem usados var READY_STATE_COMPLETE = 4; /** *[Função][que][fica][verificando][as][notícias][no][servidor][em][períodos] *[de][tempo] *[@param][data][Endereco][dos][dados][no][servidor] *[/] function timedNews(data) { // Busca os dados no servidor sendRequest(data);

**5 WEB 2.0**

// Programa para ser executada novamente em 30 segundos var t = setTimeout("timedNews(’"+data+"’)",30000); } /** *[Função][para][requisitar][uma][página][com][dados] *[@param][url][URL][do][dado][a][ser][buscado] *[@param][params][Parâmetos][(querystring)][para][páginas][dinâmicas] *[@param][HttpMethod][Método][do][protocolo][HTTP,][se][omitido][será][usado][GET] *[/] function sendRequest(url,params,HttpMethod) { // Verifica se o metodo foi setado, caso contrário seta para GET if (!HttpMethod) { HttpMethod = "GET"; } // Instância o objeto XMLHttpRequest req = initXMLHttpRequest(); if (req) { // Seta a função de callback req.onreadystatechange = onReadyState; req.open(HttpMethod,url,true); req.setRequestHeader ("Content-Type","text/xml"); req.send(params); } } /** *[Função][que][inicia][o][objeto][XMLHttpRequest][de][acordo][com][o][browser][cliente.] *[@return][objeto][do][tipo][XMLHttpRequest.] *[/] function initXMLHttpRequest() { var xRequest = null; // código para o Mozilla if (window.XMLHttpRequest) { xRequest = new XMLHttpRequest(); } // código para o IE else if (window.ActiveXObject) { xRequest = new ActiveXObject("Microsoft.XMLHTTP"); } // Retorna o objeto instânciado return xRequest; } /** *[Função][de][callback][que][verifica][se][o][dado][já][esta][pronto][para][uso.] *[Caso][posistivo,][chama][um][função][para][trata-lo] *[/] function onReadyState() { var ready = req.readyState; // Se a requisição estiver completa if (ready == READY_STATE_COMPLETE)

**5 WEB 2.0**

**5 WEB 2.0**

**5 WEB 2.0**

**timedNews(data)** - esta é a única função que é chamada diretamente pela página HTML da nossa aplicação; ela é a função que chama a sendRequest para requisitar os dados do servidor e em seguida se programa para ser executada novamente a cada 30 segundos, por isso, a cada período de 30 segundos o arquivo de dados é requisitado novamente e as notícias contidas nele são verificadas pela função parseNews.

**sendRequest(url,params,HttpMethod)** - função responsável por requisitar os dados do servidor de forma assíncrona ao servidor; para isso, ela instancia um objeto XMLHttpRequest utilizando a função initXMLHttpRequest e depois configura a funcão onReadyState como callback da chamada.

**5 WEB 2.0**

- **parseNews()** - chamada para tratar os dados quando eles chegam do servidor. Essa função primeiro recupera a data e o título das notícias e os junta formando assim o título que será colocado na página, após isso ela chama a função newDetect para verificar se esse título já se encontra na página, se for retornado false o notícia é inserida na página, caso contrário nada será feito, pois se trata de uma notícia antiga.

Inicialmente, quando as tecnologias para _web_ surgiram, programar para _web_ utilizando JavaScript era extremamente penoso, pois não haviam ferramentas para auxílio de _debugging_ e os próprios interpretadores muitas vezes não indicavam qualquer tipo de erro para o usuário. O resultado de um erro era muitas vezes uma tela branca no _browser_ e nenhuma dica de onde o erro poderia ter ocorrido!

Com o surgimento das técnicas Ajax e a chamada _Web 2.0_ , o uso da linguagem cresceu bastante e vem se tornando cada vez mais popular. Isso trouxe diversos benefícios, pois começaram a surgir consoles melhores, _debuggers_ , ferramentas para auxiliar a documentação e até mesmo uma IDE ( _Integrated Development Environment_ ) para desenvolvimento de aplicações JavaScript.

Nas próximas seções, vamos indicar apenas algumas das ferramentas muito utilizadas quando se trabalha com JavaScript.

Firebug é uma extensão para o _browser_ Firefox que mostra um console muito completo. Ele é capaz de mostrar erros de JavaScript, XML e CSS. Além disso, ele guarda um registro das chamadas ao XMLHttpRequest, o que o torna uma boa ferramenta para _debugging_ de aplicações AJAX.

Com Firebug é possível colocar _breakpoints_ ao longo do código, observar variáveis específicas, alterar tanto o JavaScript quanto CSS e XML em tempo de execução e ver o resultado naquele momento. Também pode ser usado para mostrar a árvore DOM de uma página.

Na Figura 3 pode-se observar as abas que contêm o Console, o código HTML, CSS, o script em JavaScript, a árvore DOM e por último, a guia Net, que mede quanto tempo foi necessário para carregar cada uma das requisições de dados feitas pela página.

Para usuários de outros _browsers_ , o Firebug possui uma versão _lite_ que pode ser usada em qualquer _browser_ . Essa versão consiste em um arquivo na própria linguagem JavaScript que deve ser incluído na página que se deseja utilizá-lo.

JSDoc é uma ferramenta implementada em Perl que faz busca por comentários em arquivos JavaScript e gera documentos HTML com toda a documentação. Ela é baseada nos mesmos comandos da ferramenta javadoc, utilizada para gerar documentação para Java.

Usuários que já estão familiarizados com javadoc não terão nenhum problema para usar o JSDoc, pois a maior parte da sintaxe utilizada para os comentários é a mesma e ela serve tanto para documentar arquivos JavaScript estruturais quanto orientados a objeto. Na Figura 4 vemos uma amostra de como são as páginas geradas pelo aplicativo.

Figura 4: Screenshot do JSDoc mostrando o página de documentação gerada a partir do arquivo ajax.js mostrado no nosso exemplo de aplicação Ajax

Spket é uma IDE para desenvolvimento de JavaScript, SVG, XUL/XBL e _Yahoo! Widget_ . Ele oferece recursos como completar o código enquanto digitamos e destaque visual da sintaxe da linguagem. Podemos encontrá-lo em duas versões, como plugin para o editor Eclipse ou como uma plataforma independente (RCP).

- [1] Douglas Crockford. Javascript: The world’s most misunderstood programming language, 2001. Disponível em

- http://javascript.crockford.com/javascript.html , Último acesso em 10/01/2007.

- [2] Jesse J. Garrett. Ajax: A new approach to web applications, 2005. Disponível em

- [3] Gavin Kistner. Object-oriented programming in javascript, 2003. Disponível em http://phrogz.net/JS/Classes/OOPinJS.html , Último acesso em 10/01/2007.

- [4] Mozilla Development Center MDC. Core javascript 1.5 guide. Disponível em http://developer.mozilla.org/en/docs/Core_JavaScript_1.5_Guide , Último acesso em 10/01/2007.

- [5] Wikipedia the free encyclopedia. Javascript. Disponível em

- [6] w3 schools. Javascript tutorial. Disponível em