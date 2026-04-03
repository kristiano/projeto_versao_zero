|**1 Introdução**|**1**|
|---|---|
|1.1 Por que estudar Estatística para Ciência de Dados?|1|
|1.2 Conceitos fundamentais|4|
|1.3 Estatística e Ciência de Dados|10|
|**2 Estatística Descritiva: Conceitos básicos, tipos de variáveis e**||
|**gráficos**|**12**|
|2.1 Conceitos básicos|13|
|2.2 Variáveis e tipos de variáveis|16|
|2.3 Gráficos adequados a cada tipo de variável|18|
|2.4 Correlação|30|
|**3 Estatística Descritiva: Medidas de tendência central e de**||
|**dispersão**|**36**|
|3.1 Medidas de tendência central|36|
|3.2 Medidas de dispersão|56|
|3.3 Boxplot, ou diagrama de caixas|60|
|3.4 Resumo|62|
|**4 Cálculo das Probabilidades: Conceitos e fundamentos**|**64**|

## 3.3 BOXPLOT, OU DIAGRAMA DE CAIXAS

Para trabalharmos com as medidas de tendência central e de dispersão graficamente, podemos usar o diagrama de caixas (em inglês, boxplot), que é uma representação gráfica da distribuição dos dados. Esse diagrama nos dá informação da assimetria da distribuição, da presença de outliers (valores atípicos) e da variabilidade dos dados por meio da amplitude (Máx-Min). Esse conceito é ilustrado pela figura a seguir:

**60** 3.3 BOXPLOT, OU DIAGRAMA DE CAIXAS

Figura 3.18: Diagrama de Boxplot.

Há diversas bibliotecas em Python que podemos utilizar para gerar boxplots. No exemplo a seguir, utilizaremos as bibliotecas **Seaborn** e **Pyplot** para gerar boxplots agrupados por espécies da característica "Petal Length" do conhecido dataset de flores Iris (para saber mais sobre este dataset https://en.wikipedia.org/wiki/Iris_flower_data_set):

# Carregando o dataset dados = sns.load_dataset('iris') # Plotando um boxplot por species da característica petal length sns.boxplot(x=dados["species"], y=dados["petal_length"]) plt.show()

Um boxplot pode ser criado em R chamando a função ggplot()  e passando como parâmetros os dados, os eixos x e y e a geometria de interesse:  geom_boxplot() :

# Carregando a biblioteca library(ggplot2) # Utilizando o dataset nativo Iris dados = iris # Plotando um boxplot por Species da característica Petal.Length ggplot(dados, aes(x=Species, y=Petal.Length, fill=Species)) + geom_boxplot()

3.3 BOXPLOT, OU DIAGRAMA DE CAIXAS **61**

Sejam os eventos A e B, dispostos no diagrama de Venn:

Vejamos um exemplo de código em Python usando a biblioteca scikit-learn. Primeiramente, vamos carregar o dataset e separar em bases de treino e teste através do método holdout. Em seguida, para a base de treino, vamos avaliar a acurácia dos modelos treinados com os algoritmos Regressão Logística, KNN, Árvore de Classificação, Naive Bayes e SVM, utilizando sua configuração padrão da biblioteca Scikit-learn, ou seja, sem variar seus hiperparâmetros (exceto na Regressão Logística, em que utilizaremos um parâmetro para limitar o número de iterações e evitar que o código demore muito tempo para ser executado). Para uma melhor avaliação, utilizaremos o método de validação cruzada (10 folds) e compararemos os resultados graficamente através de boxplots.

# Avaliando um modelo por vez for name, model in models: cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring) results.append(cv_results) names.append(name) msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std( )) # média e desvio padrão dos 10 resultados da validação cruzada print(msg) # boxplot de comparação dos algoritmos fig = plt.figure() fig.suptitle('Comparação da Acurácia dos Modelos') ax = fig.add_subplot(111) plt.boxplot(results) ax.set_xticklabels(names) plt.show()

Analisando os resultados, verificamos que, considerando a acurácia média, o modelo treinado com o Naïve Bayes apresentou os melhores resultados (95% de acurácia média) seguido do modelo treinado com a Regressão Logística (94% de acurácia média), ambos com desvio padrão equivalente (5%). Já analisando os boxplots, vemos que a mediana da acurácia do modelo treinado com o Naïve Bayes é superior à do modelo treinado com a Regressão Logística, indicando que possivelmente seguiríamos com o Naïve Bayes como escolha de algoritmo. Neste caso, faríamos: