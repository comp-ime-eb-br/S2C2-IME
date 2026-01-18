import rdflib

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

from . import graph_functions
from . import rdf_functions

###############################################################################
#-----------------------------> Relations Types Functions

def _apply_general_triple_rule(triple, graph):
    subj_term, obj_term = triple[0], triple[2]
    subj_triple = (
                    subj_term, 
                    URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), 
                    URIRef("http://idea-c2.org/c2rm/#entity")
                )
    
    obj_triple = (
                    obj_term, 
                    URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), 
                    URIRef("http://idea-c2.org/c2rm/#entity")
                )
    
    if subj_triple not in graph:
        graph.add(subj_triple)
    
    if obj_triple not in graph:
        graph.add(obj_triple)
        
    if triple not in graph:
        graph.add(triple)
        
    return graph

def getindexdefault(self, elem, default):
        try:
            thing_index = self.index(elem)
            return thing_index
        except ValueError:
            return default

def _rule_basic_rule(graph, new_graph, predicate_to_search, predicate_to_graph):
    triples = graph_functions.search_predicate_in_graph(graph, predicate_to_search=predicate_to_search)
    if not triples:
        return new_graph  
    
    texto = predicate_to_search.strip()
    lista_bag=[]
    lista_bag_simplificada=[]
    sujeito_aux_pos=0
    bag=""
    
    for triple in triples:
      # tratamento especial para o composed_of
      if (texto=="http://idea-c2.org/c2rm/#composed_of"):
        # print('sujeito_anterior: ', sujeito_anterior)
        # print('triple[0]: ', triple[0])
        #if (sujeito_anterior != triple[0]):
        #sujeito_anterior = triple[0]
        sujeito_aux_pos=getindexdefault(lista_bag_simplificada, triple[0], -1)

        if sujeito_aux_pos==-1:
          bag = rdflib.BNode()
          # print('bag:', bag)
          lista_bag_simplificada.append(triple[0])

          dict_bag = {
            "bag": bag,
            "sujeito": triple[0]
          }
          lista_bag.append(dict_bag)

          # print('triple1: INÍCIO -----------')
          # print('triple1: topo da tripla Bag')
          new_triple = (
          URIRef(f'{rdf_functions.rdf_term_codification(triple[0])}'),
          predicate_to_search,
          URIRef(f'{rdf_functions.rdf_term_codification(bag)}')
          )
          new_graph = _apply_general_triple_rule(new_triple, new_graph)
          # print('new_triple 1: ', new_triple)
          # print('triple1: FIM----------------')

          # print('triple2: INÍCIO -----------')
          # print('triple2: segunda etapa da tripla Bag')
          new_triple = (
          URIRef(f'{rdf_functions.rdf_term_codification(bag)}'),
          rdflib.RDF.type,
          rdflib.RDF.Bag
          )
          new_graph = _apply_general_triple_rule(new_triple, new_graph)
          # print('new_triple 2: ', new_triple)
          # print('triple2: FIM----------------')

          # print('triple3: INÍCIO -----------')
          new_triple = (
          URIRef(f'{rdf_functions.rdf_term_codification(bag)}'),
          rdflib.RDF.type,
          URIRef(f'{rdf_functions.rdf_term_codification(triple[2])}')
          )
          new_graph = _apply_general_triple_rule(new_triple, new_graph)
          # print('new_triple 3: ', new_triple)
          # print('triple3: FIM----------------')         
        else:
            bag = lista_bag[sujeito_aux_pos]['bag']
            # print('triple4: INÍCIO -----------')
            new_triple = (
              URIRef(f'{rdf_functions.rdf_term_codification(bag)}'),
              predicate_to_graph,
              URIRef(f'{rdf_functions.rdf_term_codification(triple[2])}')
            )
            new_graph = _apply_general_triple_rule(new_triple, new_graph)
            # print('new_triple 4: ', new_triple)
            # print('triple4: FIM----------------')
            
    # fim do if do bag
      else:
        new_triple = (
              URIRef(f'{rdf_functions.rdf_term_codification(triple[0])}'),
              predicate_to_graph,
              URIRef(f'{rdf_functions.rdf_term_codification(triple[2])}')
        )
        new_graph = _apply_general_triple_rule(new_triple, new_graph)
    return new_graph            

def rule_equivalent_to(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#equivalent_to"), 
                                predicate_to_graph=URIRef("http://www.w3.org/2002/07/owl#equivalentClass"))
                                

def rule_associated_with(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#associated_with"), 
                                predicate_to_graph=URIRef("http://www.w3.org/2000/01/rdf-schema#seeAlso"))

def rule_composed_of(graph, new_graph):
    ### aqui o bag
      return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#composed_of"),
                                predicate_to_graph=URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag"))

def rule_type_of(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#type_of"), 
                                predicate_to_graph=URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"))

def rule_defined_by(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#defined_by"), 
                                predicate_to_graph=URIRef("http://www.w3.org/2000/01/rdf-schema#comment"))

def rule_co_referenced(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#coreferenced"),
                                predicate_to_graph=URIRef("http://idea-c2.org/c2rm/#coreferenced"))

def rule_instace_of(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#instance_of"), 
                                predicate_to_graph=URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"))

def rule_responsible_for(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#responsible_for"),
                                predicate_to_graph=URIRef("http://idea-c2.org/c2rm/#responsible_for"))

def rule_capacity_of(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#capacity_of"),
                                predicate_to_graph=URIRef("http://idea-c2.org/c2rm/#capacity_of"))

def rule_occurs_in(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#occurs_in"),
                                predicate_to_graph=URIRef("http://idea-c2.org/c2rm/#occurs_in"))

def rule_applied_to(graph, new_graph):
    return _rule_basic_rule(graph, new_graph, 
                                predicate_to_search=URIRef("http://idea-c2.org/c2rm/#applied_to"),
                                predicate_to_graph=URIRef("http://idea-c2.org/c2rm/#applied_to"))
