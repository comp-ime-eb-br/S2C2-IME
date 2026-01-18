import re

from . import terms_functions as tf

###############################################################################
#-----------------------------> Enrich Functions

# main_relations = [{id, from_id, to_id, type, offset_interval}, ...]
def enrich_relations(all_text, relation_models, main_relations):
    for relation in main_relations:
        begin, end = relation.pop('offset_interval') # Dar um pop p tirar o offset_interval na formatacao
        for relation_model in relation_models:
            x, y = relation_model.get_tolerance()
            search_text = all_text[begin:end]
            search_text = search_text[x:(end - begin - y)]
                
            if search_text.rfind(relation_model.get_predicate_search()) != -1:
                relation['type'] = relation_model.get_predicate()
                relation_model.append_relation(relation)
                break   
                
    
###############################################################################
#-----------------------------> Relation Model Class (to enrich)

# Cada objeto da classe representa uma relacao
class Relations:
    predicate_search = ''
    predicate = ''
    relations = list()
    tolerance_interval = (0, 0)
    
    def get_predicate_search(self):
        return self.predicate_search
    
    def get_predicate(self):
        return self.predicate

    def get_relations(self):
        return self.relations
    
    def get_tolerance(self):
        return self.tolerance_interval
    
    def set_relations(self, relations):
        self.relations = relations
        
    def append_relation(self, relation):
        self.relations.append(relation)       
            
    def __init__(self, predicate_search, predicate, tolerance_interval = (0, 0)):
        self.predicate_search = predicate_search
        self.predicate = predicate
        self.relations = list()
        self.tolerance_interval = tolerance_interval
        
    