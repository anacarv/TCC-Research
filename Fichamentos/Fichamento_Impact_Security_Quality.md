# How Does Refactoring Impact Security When Improving Quality? A Security-Aware Refactoring Approach

**Referência:**
C. Abid, M. Kessentini, V. Alizadeh, M. Dhaouadi and R. Kazman, "How Does Refactoring Impact Security When Improving Quality? A Security-Aware Refactoring Approach," in IEEE Transactions on Software Engineering, vol. 48, no. 3, pp. 864-878, 1 March 2022, doi: [10.1109/TSE.2020.3005995](https://doi.org/10.1109/TSE.2020.3005995)

## 1. Fichamento de Conteúdo

O artigo investiga como a refatoração de código impacta a segurança do *software* ao tentar melhorar atributos de qualidade. Embora a refatoração seja amplamente utilizada para aumentar a reutilização e modularidade, essas melhorias podem ampliar a superfície de ataque. O estudo avalia a correlação entre atributos de qualidade definidos pelo modelo *QMOOD* e métricas de segurança baseadas no acesso a dados. Utilizando 30 projetos *open-source*, a pesquisa propõe uma abordagem de recomendação de refatoração multiobjetiva, buscando equilíbrio entre segurança e qualidade. A ferramenta proposta foi avaliada tanto por experimentos empíricos quanto por *feedback* de desenvolvedores, demonstrando que muitas melhorias de qualidade podem comprometer a segurança e exigem *trade-offs* cuidadosos.

## 2. Fichamento Bibliográfico
* _QMOOD Quality Model_: Conjunto de seis atributos de qualidade utilizados para avaliar o *design* de *software*: reutilização, flexibilidade, compreensibilidade, funcionalidade, extensibilidade e eficácia (página 4).
* _Métricas de Segurança_: Incluem acessibilidade de atributos sensíveis (*CIDA*, *CCDA*), interação entre métodos críticos (*CMAI*, *CAAI*) e peso de métodos classificados (*CMW*) (página 6).
* _Algoritmo NSGA-II_: Algoritmo de otimização multiobjetiva usado para encontrar um equilíbrio entre qualidade e segurança na recomendação de refatorações (página 9).
* _Estudo Empírico_: Avaliação em 30 projetos de código aberto mostrou correlações negativas entre segurança e qualidade, reforçando a necessidade de um equilíbrio no *design* (página 14).

## 3. Fichamento de Citações

* _"Refactoring to improve the design structure while preserving behavior is widely used to enhance the quality of software systems."_
* _"There is a trade-off between code quality and security, and developers should consider both when refactoring."_
* _"Encapsulating fields and increasing method security are the most effective refactorings for improving security."_
* _"Extracting superclasses and moving methods tend to expose sensitive data, reducing system security."_
* _"Improving modularity may result in spreading dependencies on security-critical files into many other components."_
