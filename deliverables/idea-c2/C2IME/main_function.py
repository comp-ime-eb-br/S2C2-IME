
'''
O notebook está especificado para cada regex, então mudar na mao os regex de:
    page_regex : as quebras de página do arquivo (indice da pagina ou ordenacao do glossario)
    term_regex : o regex para extrair os sujeitos
    delimiter_regex : o regex para substituir pelo predicado
Mudar tambem page_start e page_end para pular o glossario e o fim do arquivo
'''

from . import file_functions
from . import terms_functions
from . import relations_functions
from . import rdf_functions
from . import enrich_class as EC

import re
import sys
import json

from datetime import datetime

data_e_hora = datetime.now()
data_e_hora = data_e_hora.strftime('%d-%m-%Y %H:%M:%S')
#json_file = './output/output'+data_e_hora+'.jsonl'
###############################################################################
#-----------------------------> IO Variables

# Output
json_file = './output/output.jsonl'
#json_file = './output/output'+data_e_hora+'.jsonl'
json_file_prenoted = './output/output.jsonl'
#json_file_prenoted = './output/output-'+data_e_hora+'.jsonl'
outfile_prenoted = './output/output.txt'


###############################################################################
#-----------------------------> MAIN
# sad func
def main_log(terms=None, relation_terms=None, main_relations=None, lines=None, formated_lines=None):
    if terms:
        print(f'Terms Length: {len(terms)}\n Terms: {terms}\n')
    if relation_terms:
        print(f'Relation Terms Length: {len(relation_terms)}\n Relation Terms: {relation_terms}\n')
    if main_relations:
        print(f'Main Reltions Length: {len(main_relations)}\n Main Relations Terms: {main_relations}\n')
    
    if lines and formated_lines:
        file_functions.write_intermediates(lines, formated_lines)   
        
    pass

def main_input(regex_dict, input_path, relations_path, relations_models = None, log_bool = True):
    #------> Variaveis Iniciais
    
    text = file_functions.input_doc_to_lines_list(input_path, regex_dict)
    terms = terms_functions.find_terms_on_text(' '.join(text), regex_dict['term_regex'])
    for index, dictionary in enumerate(terms):
        dictionary['start_offset'] -= index
        dictionary['end_offset'] -= index + 1 
    
    # Extrair as informacoes das relacoes identificadas
    relation_terms_config = {
        'text': ' '.join(text), 
        'relations_file': relations_path,
        'terms_ref': terms
        }
        
    main_relations = relations_functions.relations_from_input(**relation_terms_config)

    if relations_models:
        # Enriquecer as relacoes para cada modelo definido pelo usuario
        EC.enrich_relations('\n'.join(text), relations_models, main_relations)
    
    
    # Juntar os termos e criar o json
    data_out = file_functions.create_json(
        json_file=json_file_prenoted,
        formated_lines=text,
        main_relations=main_relations,
        all_terms=terms
    
    )

    try:
        file_functions.write_list([
            str(text),
            str(rdf_functions.transform_to_triple(main_relations, terms)),
            str(terms)],
            outfile_prenoted)
        
    except Exception:
        pass
    
    ################## LOG
    # try:
    #     if log_bool:
    #         main_log(terms, main_relations)
            
    #     print(rdf_functions.transform_to_triple(main_relations, terms))
    #     print(terms_functions.hashed_terms_relations(terms, main_relations))
        
    # except Exception:
    #     pass
        
    return data_out


        
def main(regex_dict, relations_models, input_path, term_interval = (0, None), terms_per_file = -1, log_bool = True):
    #------> Variaveis Iniciais
    FIRST_TERM, LAST_TERM = term_interval 
    
    lines = file_functions.input_doc_to_lines_list(input_path, regex_dict)
    terms, all_formated_lines = terms_functions.terms_and_lines(lines, regex_dict['term_regex'], regex_dict['delimiter_regex'])
    terms = list(terms.values())   

    formated_lines = all_formated_lines[FIRST_TERM:LAST_TERM]
        
    # Extrair as informacoes das relacoes identificadas
    relation_terms_config = {
        'lines': formated_lines, 
        'terms': terms,
        'term_index': max(terms_functions.get_ids(terms)) + 1,
        'slice_term_index': FIRST_TERM,
        'to_search_terms': None
        }
        
    relation_terms = terms_functions.find_relation_terms(**relation_terms_config)
    
    main_relations = relations_functions.find_main_relations(**{
        'lines': formated_lines,
        'terms': terms,
        'relation_terms': relation_terms,
        'slice_term_index': FIRST_TERM
    })

    # Enriquecer as relacoes para cada modelo definido pelo usuario
    EC.enrich_relations('\n'.join(all_formated_lines), relations_models, main_relations)

    # Ajustar o offset para fatiar p texto
    first_offset = terms[FIRST_TERM]['start_offset']
    terms_functions.shift_terms(terms, first_offset)
    terms_functions.shift_terms(relation_terms, first_offset)
    
    # Juntar os termos e criar o json
    all_terms = terms[FIRST_TERM:LAST_TERM]
    all_terms.extend(relation_terms)
    file_functions.create_json(
        json_file=json_file,
        formated_lines=formated_lines,
        main_relations=main_relations,
        all_terms=all_terms
    )

    ############# LOG
    if log_bool:
        main_log(terms, relation_terms, main_relations)
        
    print(rdf_functions.transform_to_triple(main_relations, all_terms))
    print(terms_functions.hashed_terms_relations(all_terms, main_relations))



