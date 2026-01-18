import json
import unicodedata

from . import terms_functions

###############################################################################
#-----------------------------> User Variables

rdf_legend_path = './docs/rdf_legend.json'

###############################################################################
#-----------------------------> RDF De-Para

# Botar dobrado com esse espacinho
rdf_legend = dict()
with open(rdf_legend_path, 'r') as ff:
    rdf_legend = json.load(ff)

###############################################################################
#-----------------------------> RDF Functions
'''
Possivel abordagem :
from pluralize import Translator
    T = Translator()
    T.select('br')
    ...
    singular_words = [T(word).format(n=0).text for word in word.split()]
    ...
'''

def rdf_term_codification(term):
    word = term.lower().rstrip()
    singular_words = [w for w in word.split()] # change here
    word = ' '.join(singular_words)
    word = word.replace('ç', 'c')
    word = word.replace(' ', '_')
    word = unicodedata.normalize('NFD', word)
    word = ''.join(char for char in word if unicodedata.category(char) != 'Mn')
    return word

def transform_to_triple(relations, all_terms):
    n3_triples = list()
    ids_terms = terms_functions.get_term_by_id(all_terms)
    
    for relation in relations:
        n3_triples.append(
            [
                rdf_term_codification(ids_terms[relation['from_id']]),
                rdf_legend[relation['type']],
                rdf_term_codification(ids_terms[relation['to_id']])
            ]
        )

    return n3_triples