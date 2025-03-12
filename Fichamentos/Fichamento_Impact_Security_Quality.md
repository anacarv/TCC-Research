# How Does Refactoring Impact Security When Improving Quality? A Security-Aware Refactoring Approach

**Referência:**
C. Abid, M. Kessentini, V. Alizadeh, M. Dhaouadi and R. Kazman, "How Does Refactoring Impact Security When Improving Quality? A Security-Aware Refactoring Approach," in IEEE Transactions on Software Engineering, vol. 48, no. 3, pp. 864-878, 1 March 2022, doi: [10.1109/TSE.2020.3005995](https://doi.org/10.1109/TSE.2020.3005995)

## 1. Fichamento de Conteúdo

O artigo investiga como refatorações que visam melhorar a qualidade do código podem impactar a segurança do software. Os autores analisam correlações entre métricas de qualidade (modelo QMOOD) e métricas de segurança baseadas no acesso a dados. Foi desenvolvida uma abordagem de refatoração multiobjetivo que busca equilibrar qualidade e segurança usando o algoritmo NSGA-II. O estudo empírico avaliou 30 projetos de código aberto e revelou que melhorar atributos como reutilização e extensibilidade pode aumentar a superfície de ataque do sistema. Além disso, um experimento com 15 desenvolvedores confirmou que a consideração da segurança ao refatorar é fundamental para evitar vulnerabilidades.

## 2. Fichamento Bibliográfico

* _Refatoração e Segurança_: Refatorações podem melhorar modularidade e reutilização, mas também expor código sensível a ataques (p. 2).
* _QMOOD Quality Model_: Modelo utilizado para medir atributos de qualidade como reutilização, flexibilidade e extensibilidade (p. 4).
* _Métricas de Segurança_: Incluem acessibilidade de atributos sensíveis (CIDA, CCDA), interação entre métodos críticos (CMAI, CAAI) e peso de métodos classificados (CMW) (p. 6).
* _Algoritmo NSGA-II_: Utilizado para encontrar soluções de refatoração que maximizam qualidade e segurança de forma equilibrada (p. 9).
* _Impacto das Refatorações_:
  * _Positivo na segurança_: Encapsular campos, aumentar segurança de atributos/métodos, empurrar métodos/campos para subclasses.
  * _Negativo na segurança_: Criar superclasses, mover métodos, extrair classes, diminuir segurança de atributos/métodos (p. 12).
* _Estudo Empírico_: Avaliação em 30 projetos de código aberto mostrou correlações negativas entre segurança e qualidade, reforçando a necessidade de um equilíbrio no design (p. 14).

## 3. Fichamento de Citações

* _"Improving reusability may increase the attack surface due to the created abstractions."_
* _"There is a trade-off between code quality and security, and developers should consider both when refactoring."_
* _"Encapsulating fields and increasing method security are the most effective refactorings for improving security."_
* _"Extracting superclasses and moving methods tend to expose sensitive data, reducing system security."_
* _"Our security-aware approach outperformed traditional refactoring tools in preserving software security with minimal quality sacrifices."_
