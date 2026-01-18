import terms_functions as tf
import re

def find_relation_terms(lines, terms, term_index, slice_term_index = 0):
    to_search = '|'.join(tf.sort_and_escape(terms))
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


def find_main_relations(lines, terms, relation_terms, slice_term_index = 0, relation_index = 0, relation_type = 'relacionado_com'):
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
            
    return relations