---
hide:
  - navigation
  - toc
---

Esta seção apresenta os softwares desenvolvidos no contexto do projeto S2C2 pela equipe do IME e seus colaboradores.

#MiScManager/MiniManager

O software [MiScManager](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/deliverables/MiScManager) é uma extensão do software MiniManager, que foi desenvolvido com o objetivo de ampliar as suas funcionalidades, permitindo a configuração de cenários de operações militares. Essa configuração é feita através do acesso a uma ontologia, previamente instanciada com um cenário específico. A arquitetura do MiScManager foi desenvolvida utilizando o Django Framework para funcionar como um sistema web seguindo o padrão MTV (Model-Template-View). O fato de o Django Framework estar escrito em linguagem Python facilita a comunicação com o Mininet-WiFi, também escrito na mesma linguagem. Ainda, possui como sistema gerenciador de banco de dados (SGBD) o PostgreSQL. Uma descrição mais detalhada do desenvolvimento e funcionamento desses softwares pode ser encontrada em [Dissertação André Demori](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/publi/DissertaçãoAndreMunizDemori_IME_versao_final.pdf), em [vídeo](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/videos/apresentacao.mp4) e em [PFC Rodrigues e Albuquerque](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/publi/PFC_MININET.pdf). 


#MAISC2

Para apoiar a troca de mensagens em operações de C2, foi desenvolvido o “Método de Apoio à Interoperabilidade Semântica de C2 utilizando PLN” (MAISC2). O método MAISC2 é apresentado na forma de uma especificação constituída de etapas, atividades e tarefas, detalhando como atuar na intermediação das mensagens trocadas em um ambiente de C2, enriquecendo-as semanticamente. Para avaliar a viabilidade do método foi implementado o [protótipo MAISC2](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/deliverables/Maisc2) utilizando a abordagem de microserviços. Uma descrição mais detalhada do desenvolvimento e funcionamento do MAISC2 pode ser encontrada no artigo [Performance Evaluation of Monolithic and Microservice Architectures for Natural Language Processing in Command and Control Applications](https://ieeexplore.ieee.org/document/11146751), em [vídeo do chat MAISC2](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/videos/MAISC2 - Chat for exchanging messages in c2.mp4) e em [vídeo do Método MAISC2](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/videos/MAISC2 - Method To Support Semantic Interoperability in Command and Control.mp4).

#IDEA-C2-tool

O [IDEA-C2-Tool](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/deliverables/idea-c2/) é um protótipo de software baseado no método IDEA-C2 ((generatIon of knowleDge graphs basEd on Artificial intelligence of C2 Domain), que é uma abordagem híbrida de apoio ao desenvolvimento de um Modelo Conceitual de Domínio (MD) através da combinação de componentes Data-Driven (DD) e Theory-Driven (TD), utilizando recursos semânticos (taxonomia) e um metamodelo baseado em Large Languagem Model (LLM) e um Knowledge Graph (KG) ajustados no domínio militar. O IDEA-C2-tool inclui um módulo que é responsável pela préanotação dos textos que servem de base para o treinamento do LLM. Uma descrição mais detalhada desse software pode ser encontrada no artigo [PREAnoTe: Uma abordagem de anotação de corpus para o ajuste fino de Large Language Model pré-treinado](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/publi/SBBD_2024___PREAnoTe.pdf).

#Athena Evaluator

A abordagem Athena foi implementada como uma combinação de módulos de software. Primeiro, um repositório FAIR Data Point foi instanciado para publicar metadados sobre conjuntos de dados. Em segundo lugar, o módulo [Athena Evaluator](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/deliverables/AthenaEvaluator/) foi implementado para analisar os metadados publicados no repositório com base em um conjunto de métricas de qualidade específicas e em métricas alinhadas com os princípios FAIR. Uma descrição dessa abordagem pode ser encontrada no artigo 
[Athena: A FAIR approach to publish and evaluate cybersecurity datasets](https://github.com/comp-ime-eb-br/S2C2-IME/blob/main/publi/ONTOBRAS_2025_paper_19.pdf).
