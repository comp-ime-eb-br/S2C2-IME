This repository contains the source code and data used in the experiment for the article entitled "Towards a hybrid conceptual modeling  approach combining a fine-tuned Language Model and a metamodel".

# IDEA-C2-Tool
IDEA-C2-Tool is a software prototype based on IDEA-C2 (generatIon of knowleDge graphs basEd on Artificial intelligence of C2 Domain), which is a hybrid approach hat supports Domain Model (DM) development by combining Data-Driven (DD) and Theory-Driven (TD) components, leveraging semantic resources and a metamodel to produce a fine-tuned Large Languagem Model (LLM) and a Knowledge Graph (KG) focused on the military domain.

# Source of Textual Database for LLM Training
- Glossário de Termos do EB (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/298/1/C-20-1.pdf) - **Semantic Resource (SR)**
- **Excerpts from Military doctrines**:
  - Movimento e Manobra (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/80/1/EB20-MC-10.203.pdf)
  - Inteligência (link: https://bdex.eb.mil.br/jspui/bitstream/1/2595/1/EB20-MC-10.207.pdf)
  - Doutrina Militar Terrestre (https://bdex.eb.mil.br/jspui/bitstream/123456789/11768/1/EB20MF10102.pdf)
  - Doutrina de Operações Conjuntas - Vol I (https://www.gov.br/defesa/pt-br/arquivos/ajuste-01/legislacao/emcfa/publicacoes/doutrina/md30-m-01-vol-1-2a-edicao-2020-dou-178-de-15-set.pdf)
  - Doutrina de Garantia da Lei e da Ordem (GLO) (https://www.gov.br/defesa/pt-br/arquivos/ajuste-01/2014/mes02/md33-m-10-garantia-da-lei-e-da-ordem-2a-ed-2014-31-jan.pdf)
  - Doutrina de Operações (https://bdex.eb.mil.br/jspui/bitstream/1/848/3/EB70-MC-10.223-%20Opera%c3%a7%c3%b5es)
  - Manual de Campanha - As comunicações nas operações (https://bdex.eb.mil.br/jspui/bitstream/123456789/7073/1/EB70-MC-10.246_PDF.pdf)
- **Corpus**:
  - Pre-annotated Corpus: **/texts/Corpus-PreAnotated.jsonl**
  - Curate Corpus: **/texts/Corpus-Curate.jsonl**
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
- [PreAnoTeTool] (https://github.com/jonesavelino/preanotetool) responsible for pre-annotating the texts in the corpus using the Command and Control Relations Metamodel (C2RM) of the IDEA-C2 approach.
- [Python 3.10.12] (https://www.python.org/downloads/release/python-31012/) programming language to run the libraries and development.
- [Google Colab Pro] Integrated Development Environment (IDE), in notebook format, for implementing and executing source code, using the Python programming language.
- [GraphDB 9.11] (https://www.ontotext.com/products/graphdb/graphdb-free/) is a database for dealing with Graphs that allows the manipulation of data based on RDF Graphs and uses the SPARQL language for retrieval and query processing. (Not mandatory!).

- **Libraries**: 
  - [SpaCy 3.5] it is a machine learning library focused on Natural Language Processing (NLP). 
  - [Pipeline] pt_core_news_sm (https://spacy.io/models/pt) (customizable)
  - [Architecture] spacy-transformers.TransformerModel.v3 (https://spacy.io/universe/project/spacy-transformers)
  - [Large Language Model] neuralmind/bert-base-portuguese-cased (https://github.com/neuralmind-ai/portuguese-bert) (BERTimbau)
  - [RDFLib] - Python library for working with RDF (RDF, N3, and TTL extensions)
  - [Graphviz] - Library that allows you to visualize RDF graphs visually. (https://pypi.org/project/graphviz/) (Optional)
  - [PyPDF2] - PDF library capable of splitting, merging, cropping, and transforming PDF file pages. (https://pypi.org/project/PyPDF2/)
  - [PyDotPlus] - Python library based on the evolution of pydot that provides a Python interface to the Graphviz Dot language. (https://pypi.org/project/pydotplus/)

# Experiment
- To carry out the experiment, it is important to follow the step-by-step actions in the project booklet..
  - 1) Recover the "Glossário de Termos do EB" (SR) (link: https://bdex.eb.mil.br/jspui/bitstream/123456789/298/1/C-20-1.pdf)
  - 2) Run the operations: (it corresponds to the stages of the IDEA-C2 sub-processes: Corpus Annotation and Language model Fine-Tuning)  
    - 2.1) Step 1: Pré-anotação (IDEA-C2-Metamodel - Entity e Relations) - Generate JSONL files for curation in Doccano (IDEA-ETAPA 1-Pre-Anotacao.ipynb);
    - 2.2) Step 2: Retrieve documents curated in Doccano (JSONL) to generate file .SpaCy (IDEA-ETAPA 2-ConverterDoccanoSpacy3-2.ipynb);
    - 2.3) Step 3: Run NER (IDEA-ETAPA 3-FineTuneBERT_Spacy_NER.ipynb);
    - 2.4) Step 4: Run RE (IDEA-ETAPA 4-FineTunBERT_Spacy_RE.ipynb);
  - 3) Run de operations: (it corresponds to the stages of the IDEA-C2 sub-process: Trained language model application)
model application;
    - 3.1) Step 5: Run NE + RE (IDEA-ETAPA 5-RodaModeloNEReRE.ipynb): Submit texts for IDEA-C2-LM to infer named entities and extract relationships;
  - 4) Run de operations: (it corresponds to the stages of the IDEA-C2 sub-process: Conceptual Modeling)
    - 4.1) Step 6: Conceptual Modeling: (Etapa 6 - Graph.ipynb): Retrieves the curated .JSOL file from Doccano to generate the RDF graph in .TTL format. From this TTL file it is possible to execute SPARQL queries, exploiting the properties of the C2RM metamodel. It also retrieves the lists of inferences from Etapa-5 Run NE + RE (IDEA-ETAPA 5-RodaModeloNEReRE.ipynb) to generate graph visualization and integrate it into IDEA-C2-KG.

# Acknowledgments
- This research has been funded by FINEP/DCT/FAPEB (no. 2904/20 - 01.20.0272.00) under the “Systems of Command and Control Systems” project (“Sistemas de Sistemas de Comando e Controle”, in Portuguese). We would also like to thank the domain experts who contributed to the experiment.
