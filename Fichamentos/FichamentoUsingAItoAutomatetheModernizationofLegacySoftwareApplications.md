# Using AI to Automate the Modernization of Legacy Software Applications

V. Nitin, "Using AI to Automate the Modernization of Legacy Software Applications," 2024 39th IEEE/ACM International Conference on Automated Software Engineering (ASE), Sacramento, CA, USA, 2024, pp. 2514-2517. doi: [10.1145/3691620.3695610](https://doi.org/10.1145/3691620.3695610)

## 1. Fichamento de Conteúdo

O artigo aborda o desafio da modernização de softwares legados, destacando as dificuldades na manutenção e segurança desses sistemas. O autor propõe o uso de inteligência artificial para automatizar três aspectos da modernização: (1) a migração de arquiteturas monolíticas para microserviços, (2) a tradução de códigos escritos em linguagens antigas, como C, para linguagens modernas, como Rust, e (3) a detecção de bugs introduzidos durante esse processo. Para cada um desses aspectos, o artigo apresenta soluções baseadas em pesquisas anteriores do autor. As abordagens incluem o uso de análise gráfica para decomposição de sistemas monolíticos, aprendizado de máquina para tradução de código e ferramentas estáticas para verificação de segurança em Rust. Os resultados indicam melhorias significativas na eficácia da modernização quando essas ferramentas são empregadas, reduzindo erros e aumentando a eficiência do processo.

## 2. Fichamento Bibliográfico

* _Monolith to Microservice Refactoring_: Processo de dividir aplicações monolíticas em microsserviços, melhorando escalabilidade e manutenção (página 2).
* _Code Translation_: Conversão de código de linguagens antigas para modernas usando IA, garantindo melhor segurança e legibilidade (página 3).
* _Detecting Bugs in Modernized Code_: Identificação de erros decorrentes da modernização, especialmente em Rust, onde a conversão de código pode introduzir vulnerabilidades (página 4).
* _CARGO_: Ferramenta que usa análise estática para criar um grafo de dependências e sugerir particionamento eficiente em microsserviços (página 5).
* _SpecTra_: Sistema que melhora a tradução de código por IA, combinando técnicas de transpilers e LLMs para garantir código mais correto e idiomático (página 6).
* _Yuga_: Ferramenta de análise estática para detectar bugs relacionados a anotações de tempo de vida em Rust, um problema crítico na conversão de C para Rust (página 7).

## 3. Fichamento de Citações

* _"There is an urgent need to develop automated techniques to modernize old code."_
* _"Businesses are gradually migrating their existing applications to the cloud as their enterprise applications outgrow their monolithic architectures."_
* _"We propose SpecTra, a system to enhance the code translation capabilities of LLMs by integrating the principles of transpilers into the LLM framework."_
* _"Rust’s memory safety guarantees can be too restrictive for some applications, so Rust provides an 'escape hatch' in the form of unsafe Rust."_
* _"Yuga can detect lifetime annotation bugs with 87.5% precision on a dataset of known vulnerabilities."_

