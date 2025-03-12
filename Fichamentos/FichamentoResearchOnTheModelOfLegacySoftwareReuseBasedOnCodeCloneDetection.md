# Research on the Model of Legacy Software Reuse Based on Code Clone Detection

_Referência:_
M. Fanqi and K. Yunqi, "Research on the Model of Legacy Software Reuse Based on Code Clone Detection," 2013 5th International Conference and Computational Intelligence and Communication Networks, Mathura, India, 2013, pp. 491-495, doi: [10.1109/CICN.2013.107](https://doi.org/10.1109/CICN.2013.107)

## 1. Fichamento de Conteúdo

O artigo apresenta um modelo para reutilização de software legado baseado na detecção de clones de código. A reutilização de código legado pode reduzir custos e tempo no desenvolvimento de novos sistemas. O modelo proposto segue duas etapas principais: engenharia reversa, para analisar e extrair componentes reutilizáveis, e engenharia direta, para integrar esses componentes em novos sistemas. A técnica de detecção de clones de código é usada para identificar funções similares em softwares antigos, permitindo refatoração e encapsulamento em novos componentes reutilizáveis. Ferramentas como _CCFinder_ são utilizadas para identificar padrões de código duplicado e avaliar sua adequação para reuso. O estudo apresenta experimentos com softwares reais (_MySQL_ e _PostgreSQL_), demonstrando que a detecção de clones pode ser útil para localizar código estável e confiável para reaproveitamento.

## 2. Fichamento Bibliográfico

* _Reutilização de software legado_: Processo de reaproveitamento de código de sistemas antigos para reduzir custos e tempo no desenvolvimento de novos sistemas (página 1).
* _Detecção de clones de código_: Método para encontrar trechos de código duplicados, que podem indicar componentes reutilizáveis e simplificar refatoração (página 3).
* _Engenharia reversa e direta_: Abordagem que envolve primeiro analisar e extrair componentes de sistemas legados (engenharia reversa) e depois integrá-los em novos sistemas (engenharia direta) (página 4).
* _CCFinder_: Ferramenta baseada em tokens para detecção de clones de código, ajudando na identificação de padrões reutilizáveis em grandes bases de código (página 5).
* _Refatoração baseada em clones_: Estratégia que consiste em consolidar trechos de código duplicados em funções reutilizáveis, melhorando a manutenção e reuso (página 7).
* _Experimentos com MySQL e PostgreSQL_: Aplicação do modelo em bases de código reais, demonstrando que a detecção de clones pode reduzir a complexidade do código e facilitar a extração de componentes (página 9).

## 3. Fichamento de Citações

* _"The reuse of legacy software is a process of reengineering old systems using component technology."_
* _"Code clone detection is an effective way to identify reusable parts in legacy software, as frequently cloned code is often stable and reliable."_
* _"By identifying cloned functions, we can reduce the search space for reusable components and improve the efficiency of software reuse."_
* _"The use of CCFinder in MySQL and PostgreSQL revealed multiple instances of identical functions across different modules, demonstrating the potential for component extraction."_
* _"Although valuable cloned functions exist, they are not abundant, so this method should be used as a supplementary approach in large-scale software refactoring."_
