import rdflib
import networkx as nx
import matplotlib.pyplot as plt

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, FOAF, RDFS, XSD
from rdflib import URIRef, BNode, Literal

from . import file_functions as ff
from . import relations_functions as rf
from . import rdf_functions as frdf
from . import graph_rules as fgr
from . import main_function

import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot

###############################################################################
#-----------------------------> Basic Variables

# Load and parse the Turtle file
turtle_filename = '/Users/gustavodanon/Desktop/Projetos - Programação/PIBIT/docs/ICEIS-2024-ARTIGO-GRAFO.ttl'

base = Namespace('http://idea-c2.org/')
rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
c2rm = Namespace('http://idea-c2.org/c2rm/#')
cnt = Namespace('http://idea-c2.org/data/#')

###############################################################################
#-------------------> Graph Functions

def search_predicate_in_graph(graph, predicate_to_search):
  """
  Simply search a predicate in a RDFLib graph and return all

  Returns:
      list(tuple(nodes)): [(subject, predicate, object), ...]
  """  
  return [(s, p, o) for s, p, o in graph if p == predicate_to_search]


###############################################################################
#-----------------------------> Data-Graph Functions

def salvar_graph_ttl(g, filename_out):
  """
  Save RDFLib graph as turtle
  
  """  
  g.serialize(destination=filename_out)

def load_jsonl_to_graph(anotated_filename):
  """
  Get the anotated jsonl from file and add them to a graph containing the basic nodes

  Args:
      anotated_filename (str): jsonl file

  Returns:
      RDFLib.Graph: knowledge graph
  """  
  entities, relations = ff.input_anotated_jsonl_to_knowledge(anotated_filename)
  g = create_basic_graph()
  
  entities = list(set([frdf.rdf_term_codification(e) for e in entities]))
  for e in entities:
      ent = URIRef(str(cnt + frdf.rdf_term_codification(e)))
      g.add((ent, RDF.type, c2rm.entity))
  
  for r in relations:
      subj = URIRef(str(cnt + frdf.rdf_term_codification(r[0])))
      typ = URIRef(str(c2rm + frdf.rdf_term_codification(r[1])))
      obj =  URIRef(str(cnt + frdf.rdf_term_codification(r[2])))

      # Tive que fazer um tratamento para lidar com o TYPE_OF a direção dele é inversa das outras triplas
      if r[1]=='type_of':
        g.add((obj, typ, subj))
      else:
        g.add((subj, typ, obj))
  return g
        

def load_turtle_to_graph(filename):
    g = rdflib.Graph()
    g.parse(filename, format='ttl')
    return g
  
def load_files_to_graph(terms_file, relations_file, text_file):
  if text_file is None:
    text_file = 'docs/trecho.txt'

  if relations_file=='':
    relations_path = 'docs/relations.txt'

  USER_VARIABLES = {
    'regex_dict':
        {
            'page_regex' : '',
            'delimiter_regex' : '',
            'term_regex': terms_file
        },
    'relations_path': relations_file,
    'input_path': text_file,
    
    'relations_models': None,
  }
  
  jsonl_graph = main_function.main_input(**USER_VARIABLES)
  return load_jsonl_to_graph(jsonl_graph)
  

def visualize_graph_with_networkx(g):
  """
  Visualize the graph using networkx library
  Usually not very visual, depreciated

  Args:
      g (RDFLib.Graph): knowledge graph
  """  
  G = nx.Graph()
  for subj, pred, obj in g.triples((None, None, None)):
      G.add_node(subj)
      G.add_node(obj)
      G.add_edge(subj, obj, label=pred)

  # Visualize the graph
  plt.figure(figsize=(12, 8))  # Larger figure size
  pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
  nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', linewidths=1, font_size=12)
  edge_labels = nx.get_edge_attributes(G, 'label')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
  
  plt.title('Graph Visualization', fontsize=14)
  plt.rc('legend', fontsize=8)

  # Save the visualization as a PNG file
  output_file = 'graph_visualization.png'
  plt.savefig(output_file, bbox_inches='tight')
  plt.show() 
    
def visualize_graph_rdf_turtle(g):
  """
  Good visualization of knowledge graph

  Args:
      g (RDFLib.Graph): knowledge graph
  """  
  stream = io.StringIO()
  rdf2dot(g, stream, opts = {display})
  dg = pydotplus.graph_from_dot_data(stream.getvalue())
  png = dg.create_png()
  display(Image(png))
  
###############################################################################
#-------------------> Graph Query Functions
  
def graph_query(g, p_prefix, p_select, p_where, p_orderby):
  """
  Does a query on knowledge graph

  Args:
      g (RDFLib.Graph): knowledge graph
      p_prefix (str): query prefix
      p_select (str): query select
      p_where (str): query where
      p_orderby (str): query order by

  Returns:
      list(dict): [{'suj':suj, 'pred': pred, 'obj':obj}, ...]
  """  
  graph_dict={}
  graph_list = []
  query = ''
  if p_prefix != "":
    query = query + p_prefix

  query = query + """ 
  SELECT DISTINCT """ + p_select + """
  WHERE 
  { """ + p_where + """  
      
  }""" 
  if p_orderby != "":
    query = query + """ ORDER BY """ + p_orderby

  print(query) 
  qres = g.query(query)
  for row in qres:
    # print(f"{row.s} {row.p} {row.o}")
    suj, pred, obj = row.s, row.p, row.o
    graph_dict = {'suj':suj, 'pred': pred, 'obj':obj} 
    graph_list.append(graph_dict)

  return graph_list

    
###############################################################################
#-------------------> Graph Creation Functions

def _bind_to_graph_basic_prefixes(g):
  """
  Bind prefixes to graph
  
  """  
  g.bind("base", Namespace('http://idea-c2.org/'))
  g.bind("rdfs", Namespace('http://www.w3.org/2000/01/rdf-schema#'))
  g.bind("rdf", Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'))
  g.bind("c2rm", Namespace('http://idea-c2.org/c2rm/#'))
  g.bind("cnt", Namespace('http://idea-c2.org/data/#'))
  return g

def _create_basic_c2_nodes_on_graph(g):
  """
  Create basic nodes on graph: entity, relation, domain and general domain

  """  
  entity_node = c2rm.entity
  relation_node = c2rm.relation
  general_domain_relation_node = c2rm.generaldomainrelation
  c2_domain_relation_node = c2rm.c2domainrelation
  
  g.add((entity_node, RDF.type, RDFS.Class))
  
  g.add((relation_node, RDF.type, RDF.Property))
  g.add((general_domain_relation_node, RDF.type, RDF.Property))
  g.add((c2_domain_relation_node, RDF.type, RDF.Property))
  
  g.add((relation_node, RDFS.domain, entity_node))
  g.add((relation_node, RDFS.range, entity_node))
  g.add((general_domain_relation_node, RDFS.subPropertyOf, relation_node))
  g.add((c2_domain_relation_node, RDFS.subPropertyOf, relation_node))
  
  return g

def _create_c2_relations_nodes_on_graph(g):
  """
  IMPORTANTE!
  Define all relation nodes types on graph

  Args:
      g (RDFLib.Graph): knowledge graph

  Returns:
      RDFLib.Graph: graph but more
  """  

  equivalent_to_node = c2rm.equivalent_to
  associated_with_node = c2rm.associated_with
  composed_of_node = c2rm.composed_of
  type_of_node = c2rm.type_of
  defined_by_node = c2rm.defined_by
  coreferenced_node = c2rm.coreferenced
  instance_of_node = c2rm.instance_of
  responsible_for_node = c2rm.responsible_for
  capacity_of_node = c2rm.capacity_of
  occurs_in_node = c2rm.occurs_in
  applied_to_node = c2rm.applied_to

  g.add((equivalent_to_node, RDF.type, RDF.Property))
  g.add((associated_with_node, RDF.type, RDF.Property))
  g.add((composed_of_node, RDF.type, RDF.Property))
  g.add((type_of_node, RDF.type, RDF.Property))
  g.add((defined_by_node, RDF.type, RDF.Property))
  g.add((coreferenced_node, RDF.type, RDF.Property))
  g.add((instance_of_node, RDF.type, RDF.Property))
  g.add((responsible_for_node, RDF.type, RDF.Property))
  g.add((capacity_of_node, RDF.type, RDF.Property))
  g.add((occurs_in_node, RDF.type, RDF.Property))
  g.add((applied_to_node, RDF.type, RDF.Property))
      
  g.add((equivalent_to_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((associated_with_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((composed_of_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((type_of_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((defined_by_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((coreferenced_node, RDFS.subPropertyOf, c2rm.c2domainrelation))
  g.add((instance_of_node, RDFS.subPropertyOf, c2rm.generaldomainrelation))
  g.add((responsible_for_node, RDFS.subPropertyOf, c2rm.c2domainrelation))
  g.add((capacity_of_node, RDFS.subPropertyOf, c2rm.c2domainrelation))
  g.add((occurs_in_node, RDFS.subPropertyOf, c2rm.c2domainrelation))
  g.add((applied_to_node, RDFS.subPropertyOf, c2rm.c2domainrelation))
  return g

def create_basic_graph():
    g = rdflib.Graph()
    g = _bind_to_graph_basic_prefixes(g)
    g = _create_basic_c2_nodes_on_graph(g)
    g = _create_c2_relations_nodes_on_graph(g)
    return g
  
def create_subgraph(p_subgraph:list):
  sg = rdflib.Graph()
  sg = _bind_to_graph_basic_prefixes(sg)
  for pos in range(len(p_subgraph)):
    sg.add((p_subgraph[pos]['suj'], p_subgraph[pos]['pred'], p_subgraph[pos]['obj']))
  return sg

    
###############################################################################

def run(g):
    new_graph = create_basic_graph()
    
    new_graph = fgr.rule_applied_to(g, new_graph)
    new_graph = fgr.rule_capacity_of(g, new_graph)
    new_graph = fgr.rule_co_referenced(g, new_graph)
    new_graph = fgr.rule_composed_of(g, new_graph)
    new_graph = fgr.rule_defined_by(g, new_graph)
    new_graph = fgr.rule_equivalent_to(g, new_graph)
    new_graph = fgr.rule_instace_of(g, new_graph)
    new_graph = fgr.rule_occurs_in(g, new_graph)
    new_graph = fgr.rule_responsible_for(g, new_graph)
    new_graph = fgr.rule_type_of(g, new_graph)
    new_graph = fgr.rule_associated_with(g, new_graph)

    return new_graph
  
def run_anotated_file(anotated_filename):
    g = load_jsonl_to_graph(anotated_filename)
    return run(g)
  
def run_files_input_files(terms_file, relations_file, text_file):
    g = load_files_to_graph(terms_file, relations_file, text_file)
    return run(g)

def select_grafo(g, p_prefix, p_select, p_where, p_orderby):
  graph_dict={}
  graph_list = []
  query = ''
  if p_prefix != "":
    query = query + p_prefix

  query = query + """ 
  SELECT DISTINCT """ + p_select + """
  WHERE 
  { """ + p_where + """  
      
  }""" 
  if p_orderby != "":
    query = query + """ ORDER BY """ + p_orderby

  print(query) 
  qres = g.query(query)
  for row in qres:
    print(f"{row.s} {row.p} {row.o}")
    suj, pred, obj = row.s, row.p, row.o
    graph_dict = {'suj':suj, 'pred': pred, 'obj':obj} 
    graph_list.append(graph_dict)

  return graph_list


def select_grafo2(g, p_sql):
  graph_dict={}
  graph_list = []
  query = ''
  if p_sql != "":
    query = query + p_sql

  print(query) 
  qres = g.query(query)
  for row in qres:
    print(f"{row.s} {row.p} {row.o}")
    suj, pred, obj = row.s, row.p, row.o
    graph_dict = {'suj':suj, 'pred': pred, 'obj':obj} 
    graph_list.append(graph_dict)

  return graph_list