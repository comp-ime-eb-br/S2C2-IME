import re

from . import terms_functions as tf
from . import file_functions as ff

'''
term:
{
    'id' : int,
    'label' : 'entity',
    'start_offset' : int,
    'end_offset' : int,
    'texto_key' : str
}

relation:
{
    'id' : int,
    "from_id": int,
    "to_id": int,
    "type": str],
    "offset_interval": tuple(int, int)
}
'''

###############################################################################
#-----------------------------> Find Relations Functions

def find_main_relations(lines, terms, relation_terms, slice_term_index = 0, relation_index = 0, relation_type = 'associated_with'):
    """_summary_

    Args:
        lines (list(str)): _description_
        terms (list(terms as dict)): _description_
        relation_terms (list(terms as dict)): _description_
        slice_term_index (int, optional): _description_. Defaults to 0.
        relation_index (int, optional): _description_. Defaults to 0.
        relation_type (str, optional): _description_. Defaults to 'associated_with'.

    Returns:
        _type_: _description_
    """    
    
    ref_terms = tf.get_keys(terms)
    ref_offsets = tf.get_offsets(terms)
    relations = []
    
    for idx, line in enumerate(lines):
        subject_idx = slice_term_index + idx
        if subject_idx < len(terms) - 1:
            objects_list = [term for term in relation_terms if ref_offsets[subject_idx] <= term['start_offset'] <= ref_offsets[subject_idx + 1]]
        else:
            objects_list = [term for term in relation_terms if ref_offsets[subject_idx] <= term['start_offset']]
            
        for obj in objects_list:
            relations.append({
                'id' : relation_index,
                "from_id": terms[subject_idx]['id'],
                "to_id": obj['id'],
                "type": relation_type,
                "offset_interval": (terms[subject_idx]['start_offset'], obj['end_offset'])
            })
            relation_index += 1
            
    return relations


def relations_from_input(text, relations_file, terms_ref):
    """_summary_

    Args:
        text (_type_): _description_
        relations_file (_type_): _description_
        terms_ref (_type_): _description_

    Returns:
        _type_: _description_
    """    
    # print(terms_ref)
    
    relations = ff.relations_file_to_dict(relations_file)
    relations_list = list()
    relation_index = 0

    for key, values in relations.items():
        subject_list = [term for term in terms_ref if term['texto_key'].lower() == key.lower()]
        for value in values:
            object_list = [term for term in terms_ref if term['texto_key'].lower() == value[1].lower()]
            for sub in subject_list:
                for obj in object_list:
                    if obj['start_offset'] > sub['start_offset']:
                        relations_list.append(
                            {
                                'id' : relation_index,
                                "from_id": sub['id'],
                                "to_id": obj['id'],
                                "type": value[0],
                                "offset_interval": (sub['start_offset'], obj['end_offset'])
                            }
                        )
                        relation_index += 1
                    
    return relations_list