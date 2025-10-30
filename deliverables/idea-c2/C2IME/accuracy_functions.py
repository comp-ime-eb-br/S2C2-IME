from . import terms_functions as tf

###############################################################################
#-----------------------------------> User Variables


###############################################################################
#-----------------------------------> Auxiliary Functions

def test_entities(gabarito, predicted):    
    lpredicted = [tf.get_interval(t['entities']) for t in predicted]
    lgabarito = [tf.get_interval(t['entities']) for t in gabarito]
    
    if len(lpredicted) != len(lgabarito):
        raise ValueError("Os dois arquivos devem possuir o mesmo tamanho de linhas.")
    
    else:   
        p = [item for sublist in lpredicted for item in sublist]
        g = [item for sublist in lgabarito for item in sublist]
        
        metrics = calculate_metrics(g, p)
        print(f'Metricas Entidades (TP, FP, FN): {metrics}')
        return fprecision(metrics), frecall(metrics), ff1(metrics)
    
def test_relations_aux(gabarito, predicted):
    lpredicted = [tf.get_interval_by_id(t['entities']) for t in predicted]
    lgabarito = [tf.get_interval_by_id(t['entities']) for t in gabarito]
    
    lpredicted_relations = [t['relations'] for t in predicted]
    lgabarito_relations = [t['relations'] for t in gabarito]
    
    p = {key: value for d in lpredicted for key, value in d.items()}
    g = {key: value for d in lgabarito for key, value in d.items()}
    
    if len(lpredicted) != len(lgabarito):
        raise ValueError("Os dois arquivos devem possuir o mesmo tamanho de linhas.")
    
    else:   
        lp_relations = [item for sublist in lpredicted_relations for item in sublist]
        lg_relations = [item for sublist in lgabarito_relations for item in sublist]
        
        return p, g, lp_relations, lg_relations
    
def test_relations_notype(gabarito, predicted):
    p, g, lp_relations, lg_relations = test_relations_aux(gabarito, predicted)
    
    p_relations = [(p[item['from_id']], p[item['to_id']]) for item in lp_relations]
    g_relations = [(g[item['from_id']], g[item['to_id']]) for item in lg_relations]
    
    metrics = calculate_metrics(g_relations, p_relations)
    print(f'Metricas Relacoes sem Tipo (TP, FP, FN): {metrics}')
    return fprecision(metrics), frecall(metrics), ff1(metrics)

def test_relations_typed(gabarito, predicted):
    p, g, lp_relations, lg_relations = test_relations_aux(gabarito, predicted)
    
    p_relations = [(p[item['from_id']], p[item['to_id']], item['type']) for item in lp_relations]
    g_relations = [(g[item['from_id']], g[item['to_id']], item['type']) for item in lg_relations]
    
    metrics = calculate_metrics(g_relations, p_relations)
    print(f'Metricas Relacoes com Tipo (TP, FP, FN): {metrics}')
    return fprecision(metrics), frecall(metrics), ff1(metrics)


###############################################################################
#-----------------------------------> Accuracy Functions

def fprecision(metrics):
    tp, fp  = metrics[0], metrics[1]
    return tp / (tp+fp)

def frecall(metrics):
    tp, fn  = metrics[0], metrics[2]
    return tp / (tp+fn)

def ff1(metrics):
    precision = fprecision(metrics)
    recall = frecall(metrics)
    
    return 2*precision*recall / (precision+recall)
    

def calculate_metrics(gabarito, predicted):    
    tp = len([t1 for t1 in predicted if t1 in gabarito])
    fp = len([t1 for t1 in predicted if t1 not in gabarito])
    fn = len([t2 for t2 in gabarito if t2 not in predicted])
    
    # metrics format
    return tp, fp, fn