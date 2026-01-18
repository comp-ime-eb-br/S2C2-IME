import re

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

#-----------------------------> Basic Functions
def get_ids(terms):
    return [term['id'] for term in terms]

def get_offsets(terms):
    return [term['start_offset'] for term in terms]
    
def get_keys(terms):
    return [term['texto_key'] for term in terms]
    
def terms_and_lines(lines, tere, dere):
    terms = extract_terms_ids(lines, tere, dere)
    formated_lines = format_lines_terms(lines, terms)
    
    # print(terms)
    # print(len(terms))
    return terms, formated_lines

#-----------------------> Other Functions

def sort_and_escape(terms):
    terms_list = get_keys(terms)
    new_terms = [re.escape(term)for term in terms_list]
    new_terms = sorted(new_terms, key=len, reverse=True)
    
    # Tiramos qualquer caracter do portugues de estar ao lado do termo
    # new_terms = [r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ]' + term + r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ]' 
    #              for term in new_terms]
    new_terms = [r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ-–˗⁻−(﹣]' + term + r'[^a-zà-öø-þA-ZÀ-ÖØ-Þ-–˗⁻−(﹣]' 
                  for term in new_terms]
    
    return new_terms

def shift_terms(terms, offset):
    for term in terms:
        term['start_offset'] -= offset
        term['end_offset'] -= offset   
    
# ----------------->  Term Extraction Function:

def extract_terms_ids(lines, term_regex, delimiter_regex):
    '''
    Funcao para extrair os termos dados os regex
    Precisamos juntar os dois regex pois assume-se que
    o termo seguido do regex de delimitador reconhece o termo
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
                match2 = re.search(fr'{delimiter_regex}', match.group())
                term += line[:match2.start()]
                
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
    keys = list(terms.keys()) 
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
    
#----------------------------------> Old Functions

def terms_to_json_entities(jsonEntities, terms, entitiesId = 0, main_entity = True):
    for key, id, offset in zip(get_keys(terms), get_ids(terms), get_offsets(terms)):
        try:
            jsonEntities['entities'].append(
                {
                    "id": id,
                    "label": "entity",
                    "start_offset": offset + entitiesId,
                    "end_offset": offset + (entitiesId + 1)  + len(key),
                    "texto_key": key
                }
            )
            if main_entity:
                entitiesId = entitiesId + 1

        except:
            continue