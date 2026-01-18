# !pip install PyPDF2
import PyPDF2
import re
import json
import os

from . import terms_functions as tf
from datetime import datetime

###############################################################################
#-----------------------------------> User Variables

raw_lines_file = './output/raw_lines.txt'
formated_lines_file =  './output/formated_lines.txt'


###############################################################################
#-----------------------------------> Decorators

def preprocess_file_argument(func):
    def wrapper(arg):
        if os.path.exists(arg):  # Check if the argument is a file path
            with open(arg, 'r') as file:
                content = file.read()
            return func(content)  # Pass the content of the file to the decorated function
        else:
            return func(arg)  # Pass the argument directly to the decorated function
    return wrapper


###############################################################################
#-----------------------------------> PDF Functions

# Uso do PyPDF2
def pdf_to_text(pdf_path, page_start, page_end):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(page_start, page_end):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Formatar as linhas de forma que comece com os termos
def filter_page_number(lines, page_regex):
    '''
    Detalhe para alguns PDFs: a quebra de linha ou página
    que retiramos aqui pode estar dentro das linhas (ou seja nao
    podemos deletar a linha toda). Ajustar.
    '''
    return [l for l in lines if not page_regex.match(l)]

###############################################################################
#-----------------------------------> Basic Input Functions

def jsonl_to_list(data):
    if type(data) == dict:
        return [data]
    if type(data) == list:
        return data
    if os.path.isfile(data):
        outb = list()
        with open(data, 'r') as file:
            for line in file:
                data_dict = json.loads(line)
                outb.append(data_dict)
        return outb
    else:
        raise TypeError
            


###############################################################################
#-----------------------------------> Input Manipulation Functions
    

def input_doc_to_lines_list(input_path, regex_dict):
    if input_path[-4:] == '.pdf':
        input_text = pdf_to_text(input_path, page_start=12, page_end=363)  
        raw_lines = input_text.split('\n')
        page_regex = re.compile(regex_dict['page_regex'])
        lines = filter_page_number(raw_lines, page_regex)
        
    elif input_path[-4:] == '.txt':
        f = open(input_path, 'r')
        input_text = f.read()
        lines = input_text.split('\n') # Mudar aqui qualquer coisa
          
    else:
        lines = 'Ic Hocum'
    
    return lines


def input_anotated_jsonl_to_knowledge(input):
    knowledge_list = jsonl_to_list(input)
    
    print(knowledge_list)
    
    entities = list()
    relations = list()
    for k_dict in knowledge_list:
        if not k_dict: continue
        text = k_dict["text"]
        for e in k_dict["entities"]:
            tf.add_entity_key_from_text(e, text)
            entities.append(e['texto_key'])
            
        for r in k_dict['relations']:
            from_id, to_id = r["from_id"], r["to_id"]
            relations.append([
                tf.find_entity_by_id(k_dict["entities"], from_id)["texto_key"],
                r["type"],
                tf.find_entity_by_id(k_dict["entities"], to_id)["texto_key"]
            ])

    return entities, relations
    

def _relations_list_to_dict(relations_n3):
    result_dict = dict()
    for sublist in relations_n3:
        key = sublist[0]
        predicate = sublist[1]
        value = sublist[2]

        # Check if the key is already in the dictionary
        if key in result_dict:
            # If the key is already present, append the value to the existing list
            result_dict[key].append((predicate, value.strip()))
        else:
            # If the key is not present, create a new list with the value
            result_dict[key] = [(predicate, value.strip())]
            
    return result_dict

def relations_file_to_dict(relations_file):
    with open(relations_file, 'r') as file:
        lines = file.read().splitlines()
        
    try:
        line0 = eval(lines[0])
        if len(lines) == 1 and isinstance(line0, list) and all(isinstance(item, list) for item in line0):
            relations_n3 = [r[1:] for r in line0]
        else:
            relations_n3 = [eval(relation.replace("'", '"')) for relation in lines]
            
        return _relations_list_to_dict(relations_n3)
    
    except (SyntaxError, NameError):
        print("Error on reading relations file. It should be either: \n - Each line a n3 triple like [sub, type, obj]\n - Single line with list of relations as lists, each like: [id, sub, type, obj]")
        return

###############################################################################
#-----------------------------------> Output Manipulation Functions

def write_list(out_list, ffile):
    with open(ffile, 'w') as f:
        f.write('\n'.join(out_list))
            
def write_intermediates(lines, formated_lines):
    write_list(lines, raw_lines_file)
    write_list(formated_lines, formated_lines_file)


def create_json(json_file, formated_lines, main_relations, all_terms):
    jsonString = {
        "id": 0,
        "text": ' '.join(formated_lines), # Unimos as linhas aqui (usar o separador desejado)
        "entities": list(all_terms),
        "relations": list(main_relations),
        "Comments": []
    }

    data_e_hora = datetime.now()
    data_e_hora = data_e_hora.strftime('%d-%m-%Y %H:%M:%S')
    json_file = './output/output_'+data_e_hora+'.jsonl'
    print(json_file)

    # Escrita dos JSON   
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(jsonString, json_file, ensure_ascii=False)
        
    print(f"Resultados salvos em {json_file}")
    
    return jsonString
    

###############################################################################
#-----------------------------------> Tests Functions

def get_tests(gabarito_path, predicted_path):
    return (jsonl_to_list(gabarito_path), jsonl_to_list(predicted_path))