import re

from . import terms_functions as tf

'''
term:
{
    'id' : int,
    'label' : 'entity',
    'start_offset' : int,
    'end_offset' : int,
    'texto_key' : str
}
'''

###############################################################################
#-----------------------------------> Basic Functions

def terms_and_lines(lines, tere, dere):
    if tere[-4:] == '.txt':
        terms = find_terms_on_text(lines, tere) 
    else:
        terms = find_terms_ids(lines, tere, dere)
        
    formated_lines = format_lines_terms(lines, terms)
    
    # print(terms)
    # print(len(terms))
    return terms, formated_lines

def get_ids(terms):
    return [term['id'] for term in terms]

def get_offsets(terms):
    return [term['start_offset'] for term in terms]

def get_interval(terms):
    return [(term['start_offset'], term['end_offset']) for term in terms]
   
##### 
def get_keys(terms):
    if type(terms) == list:
        return terms
    if type(terms) == str:
        return terms.split('\n')
    
    else:
        try:
            return [term['texto_key'] for term in terms]
        except:
            return list(terms.keys())
##### trocar
        
def get_term_by_id(terms):
    ids = get_ids(terms)
    keys = get_keys(terms)
    return {id: key for id, key in zip(ids, keys)}

def get_interval_by_id(terms):
    ids = get_ids(terms)
    intervals = get_interval(terms)
    return {id: interval for id, interval in zip(ids, intervals)}
    
    
def fhash(id):
    return id

#######3 funcoes boas
def add_entity_key_from_text(term, text):
    term['texto_key'] = text[term["start_offset"]:term["end_offset"]]
    
def find_entity_by_id(entities, id):
    for entity in entities:
        if entity["id"] == id:
            return entity
    return None

###############################################################################
#-----------------------------------> Auxiliary Functions

def get_terms_from(term_regex, limited = False):
    with open(term_regex, 'r') as f:
        if limited:
            terms = sort_and_escape(f.read().splitlines())

        else:
            terms = sort_and_escape(f.read().splitlines())
        
    return re.compile('|'.join([x for x in terms]), re.IGNORECASE)

# def sort_and_escape(terms):
#     terms_list = get_keys(terms)
#     new_terms = [re.escape(term)for term in terms_list]
#     new_terms = sorted(new_terms, key=len, reverse=True)
   
#     return new_terms

def sort_and_escape(terms):
    terms_list = get_keys(terms)
    new_terms = sorted(terms_list, key=len, reverse=True)
    new_terms = [rf'\b{re.escape(word)}\b' for word in terms]
    
    return new_terms


def sort_and_escape_limited(terms):
    # Tiramos qualquer caracter do portugues de estar ao lado do termo
    return [r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ-–˗⁻−﹣]' + term + r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ-–˗⁻−﹣(]' for term in sort_and_escape(terms)]

def shift_terms(terms, offset):
    for term in terms:
        term['start_offset'] -= offset
        term['end_offset'] -= offset 
        
def hashed_terms_relations(terms, relations):
    hashed_ids = {id: fhash(id) for id in get_ids(terms)}
    hashed_terms = terms.copy()
    hashed_relations = relations.copy()
    
    for term in hashed_terms:
        term["id"] = hashed_ids[term["id"]]
        
    for relation in hashed_relations:
        relation["from_id"] = hashed_ids[relation["from_id"]]
        relation["to_id"] = hashed_ids[relation["to_id"]]
    
    print(f'Terms: {len(terms)}, Hashed: {len(hashed_ids)}')
        
    return hashed_terms, hashed_relations
    
    
###############################################################################
# ------------------------------>  Main Terms Functions:

def find_terms_ids(lines, term_regex, delimiter_regex = None):
    """    
    Funcao para extrair os termos dados os regex
    Precisamos juntar os dois regex pois assume-se que
    o termo seguido do regex de delimitador reconhece o termo

    Args:
        lines (_type_): _description_
        term_regex (_type_): _description_
        delimiter_regex (_type_): _description_

    Returns:
        _type_: _description_
    """    
    '''

    '''
    terms = dict()
    to_search = term_regex + delimiter_regex
    to_search = re.compile(to_search)
    
    term = ''
    full_match = False
    line_nr = 0
    iterator = iter(enumerate(lines))
    while True:
        try:
            idx, line = next(iterator)
            # Tratamos o caso onde um termo pode ocupar mais de uma linha toda
            while re.fullmatch(fr'{term_regex}', fr'{line}'):
                line_nr = min(idx, line_nr)
                if line[-1] == '-':
                    term += line[:-1]
                else:
                    term += line + ' '
                idx, line = next(iterator)
                full_match = True
            
            match = re.search(to_search, line)
            if match:
                if delimiter_regex:
                    match2 = re.search(fr'{delimiter_regex}', match.group())
                    term += line[:match2.start()]
                else:
                    term += match.group()
                    
                term = term.rstrip()
                    
                if terms.get(term) is not None:
                    continue
                
                # Aqui setamos o ID do termo à linha que ele começa
                terms[term] = {'id' : min(idx, line_nr)}
                
                term = ''
                line_nr = len(lines)
                continue
                
            if full_match:
                term = ''
                line_nr = len(lines)    
        
        except StopIteration:
            break
            
    return terms


def format_lines_terms(lines, terms, change_terms = True):    
    '''
    Funcao para formatar corretamente as linhas
    Fazemos a uniao das linhas raw de forma que cada linha
    passe a representar um termo
    '''
    offset, start_index, entitiesId = 0, 0, 0
    
    output_lines = []
    keys = get_keys(terms) 
    terms = [term for term in terms.values() if term]
    
    end_indexes = [term['id'] for term in terms[1:]]
    end_indexes.append(None)
    for idx, end_index in enumerate(end_indexes):
        full_line = ''
        subject = keys[idx]
        for line in lines[start_index:end_index]:
            if line[-1] == '-':
                full_line += line[:-1]
            else:
                full_line += line + ' '
                
        # Incluimos aqui tambem o valor offset junto ao termo a pedidos
        if change_terms:
            terms[idx].update({ 
                'label': 'entity',
                'start_offset': offset + entitiesId,
                'end_offset': offset + (entitiesId + 1)  + len(subject),
                'texto_key': subject
            })
            
            entitiesId += 1      
            
        offset += len(full_line)
        if full_line:
            output_lines.append(full_line)
            
        start_index = end_index
        
    return output_lines


def find_terms_on_text(text, term_regex):
    terms = list(dict())
    
    to_search = get_terms_from(term_regex)
    matches = re.finditer(to_search, text)
    
    idx = 0
    for match in matches:
        terms.append({
                'id': idx,
                'label': 'entity',
                'start_offset': match.start() + idx,
                'end_offset': match.end() + (idx + 1),
                'texto_key': text[match.start():match.end()]
            })
        idx += 1
        
    return terms
    
###############################################################################
# ------------------------------>  Relations Terms Functions:

def find_relation_terms(lines, terms, term_index, slice_term_index = 0, to_search_terms = None):
    '''
    Funcao para extrair os termos das relacoes
    Apos cada termo principal identificado identificamos aqueles
    termos que existem na mesma linha do mesmo (lembrando que com a formatação
    há equivalencia 1 termo para 1 linha)
    '''
    to_search = to_search_terms
    
    if not to_search_terms:
        to_search = '|'.join(tf.sort_and_escape_limited(terms))
        to_search = re.compile(to_search, re.IGNORECASE)

    ref_terms = tf.get_keys(terms)
    ref_offsets = tf.get_offsets(terms)
    output_terms = []
        
    for idx, line in enumerate(lines):
        subject_index = slice_term_index + idx
        subject = ref_terms[subject_index]
        for obj in re.finditer(to_search, line[len(subject):]):
            if obj and obj.group() != subject:
                output_terms.append(
                    {
                        'id' : term_index,
                        'label' : 'entity',
                        'start_offset' : ref_offsets[subject_index] + len(subject) + obj.start() + 1,
                        'end_offset' : ref_offsets[subject_index] + len(subject) + obj.start() + 1 + len(obj.group()[1:-1]),
                        'texto_key' : obj.group()[1:-1]
                    }
                )
                term_index += 1
                
    return output_terms