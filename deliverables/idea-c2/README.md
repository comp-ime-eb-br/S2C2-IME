# IDEA-C2-Tool
O IDEA-C2-Tool é um protótipo de software baseado no IDEA-C2 ((generatIon of knowleDge graphs basEd on Artificial intelligence of C2 Domain), que é uma abordagem híbrida de apoio ao desenvolvimento de um Modelo de Domínio (MD) através da combinação de componentes Data-Driven (DD) e Theory-Driven (TD), utilizando recursos semânticos (taxonomia) e um metamodelo baseado em Large Languagem Model (LLM) e um Knowledge Graph (KG) ajustados no domínio militar.

# Fonte de dados textuais base
- Glossário de Termos do EB (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/298/1/C-20-1.pdf) - **Semantic Resource (SR)**
- **Trechos extraídos de doutrinas militares**:
  - Movimento e Manobra (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/80/1/EB20-MC-10.203.pdf)
  - Inteligência (link: https://bdex.eb.mil.br/jspui/bitstream/1/2595/1/EB20-MC-10.207.pdf)
  - Doutrina Militar Terrestre (https://bdex.eb.mil.br/jspui/bitstream/123456789/11768/1/EB20MF10102.pdf)
  - Doutrina de Operações Conjuntas - Vol I (https://www.gov.br/defesa/pt-br/arquivos/ajuste-01/legislacao/emcfa/publicacoes/doutrina/md30-m-01-vol-1-2a-edicao-2020-dou-178-de-15-set.pdf)
  - Doutrina de Garantia da Lei e da Ordem (GLO) (https://www.gov.br/defesa/pt-br/arquivos/ajuste-01/2014/mes02/md33-m-10-garantia-da-lei-e-da-ordem-2a-ed-2014-31-jan.pdf)
  - Doutrina de Operações (https://bdex.eb.mil.br/jspui/bitstream/1/848/3/EB70-MC-10.223-%20Opera%c3%a7%c3%b5es)
  - Manual de Campanha - As comunicações nas operações (https://bdex.eb.mil.br/jspui/bitstream/123456789/7073/1/EB70-MC-10.246_PDF.pdf)
- **Corpus**:
  - Corpus pré-anotado: **/texts/Corpus-PreAnotated.jsonl**
  - Corpus anotado e curado: **/texts/Corpus-Curate.jsonl**
- **Dataset Fine-tuning (DEV/TRAIN: 80% and TEST: 20%)**:
  - **SPLIT -> JSONL**
    - DEV: **/outputs/Dataset_exporta_anotacao-dev.jsonl**
    - TRAIN: **/outputs/Dataset_exporta_anotacao-train.jsonl**
    - TEST: **/outputs/Dataset_exporta_anotacao-test.jsonl**
  - **SPLIT -> SPACY**
    - DEV: **/outputs/Dataset_exporta_anotacao-dev.spacy**
    - TRAIN: **/outputs/Dataset_exporta_anotacao-train.spacy**
    - TEST: **/outputs/Dataset_exporta_anotacao-test.spacy**
- **GRAPH DATABASE -> RDF TURTLE**
   - FILE 1: **/outputs/corpus_completo_curado.ttl** (RDF-Turtle)
   - FILE 2: **/outputs/corpus_completo_curado.json** (JSON)
# Pre-requisites
- [PreAnoTeTool] (https://github.com/jonesavelino/preanotetool) responsável pela pré-anotação dos textos do corpus utilizando o Command and Control Relations Metamodel (C2RM) da abordagem IDEA-C2.
- [Python 3.10.12] (https://www.python.org/downloads/release/python-31012/) linguagem de programação utilizada no desenvolvimento.
- [Google Colab Pro] Integrated Development Environment (IDE), no formato notebook, para implementação e execução de código fonte, utilizando a linguagem de programação Python.
- [GraphDB 9.11] (https://www.ontotext.com/products/graphdb/graphdb-free/), um sistema gerenciador de banco de dados em grafo que permite a manipulação de dados baseados em grafos em RDF e utiliza a linguagem SPARQL para recuperação e processamento de consultas. (Opcional!).
- **Libraries**: 
  - [SpaCy 3.5] biblioteca para implementar rotinas baseadas em Natural Language Processing (NLP). 
  - [Pipeline] pt_core_news_sm (https://spacy.io/models/pt) (customizável)
  - [Architecture] spacy-transformers.TransformerModel.v3 (https://spacy.io/universe/project/spacy-transformers)
  - [Large Language Model] neuralmind/bert-base-portuguese-cased (https://github.com/neuralmind-ai/portuguese-bert) (BERTimbau)
  - [RDFLib] - Biblioteca em Python para lidar com RDF (RDF, N3, and TTL extensions)
  - [Graphviz] - Biblioteca que permite visualizar visualmente grafos RDF. (https://pypi.org/project/graphviz/) (Optional)
  - [PyPDF2] - Biblioteca em Python capaz de dividir, fundir, recortar e transformar páginas de arquivos PDF. (https://pypi.org/project/PyPDF2/)
  - [PyDotPlus] - Biblioteca em Python baseada na evolução do pydot que fornece uma interface Python para a linguagem Dot do Graphviz. (https://pypi.org/project/pydotplus/)

# Experiment
- Passo a passo para executar os experimentos.
  - 1) Recuperar o "Glossário de Termos do EB" (SR) (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/298/1/C-20-1.pdf)
  - 2) Executar os seguintes passos: (Esses passos correspondem aos subprocessos: Corpus Annotation and Language model Fine-Tuning)  
    - 2.1) Passo 1: Pré-anotação (IDEA-C2-Metamodel - Entity e Relations) - Generate JSONL files for curation in Doccano (IDEA-ETAPA 1-Pre-Anotacao.ipynb);
    - 2.2) Passo 2: Recuperar documentos curados no Doccano (JSONL) to generate file .SpaCy (IDEA-ETAPA 2-ConverterDoccanoSpacy3-2.ipynb);
    - 2.3) Passo 3: Executar NER (IDEA-ETAPA 3-FineTuneBERT_Spacy_NER.ipynb);
    - 2.4) Passo 4: Executar RE (IDEA-ETAPA 4-FineTunBERT_Spacy_RE.ipynb);
  - 3) Executar operações: (Esse passo corresponde ao subprocesso: Trained language model application)
model application;
    - 3.1) Passo 5: Run NE + RE (IDEA-ETAPA 5-RodaModeloNEReRE.ipynb): Submit texts for IDEA-C2-LM to infer named entities and extract relationships;
  - 4) Run de operations: (Esse passo corresponde ao subprocesso: Conceptual Modeling)
    - 4.1) Passo 6: Conceptual Modeling: (Etapa 6 - Graph.ipynb): Obtém o arquivo .JSOL do Doccano para gerar o grafo RDF em formato .TTL. A partir deste arquivo TTL é possível executar consultas SPARQL, explorando as propriedades do metamodelo C2RM. Também recupera as listas de inferências do Etapa-5 Run NE + RE (IDEA-ETAPA 5-RodaModeloNEReRE.ipynb) para gerar a visualização do grafo e integrá-la no IDEA-C2-KG.
