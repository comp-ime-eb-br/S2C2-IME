import spacy
from spacy import displacy

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_term_sentiment_analisys():
    sentiment_good = ['alegre','feliz','contente','satisfeito','bendito', \
    'abençoado','venturoso','bem-aventurado','ditoso','próspero','beato', \
    'risonho','fausto','radiante','afortunado','delicioso','agradável','suave', \
    'gostoso','doce','aprazível','deleitoso','belo','apetitoso','cordial',\
    'ameno','saboroso','amenoso','bom','delicado','voluptuoso','aconchegado', \
    'confortável','agasalhado','conchegado','deslumbrado','paradisíaco', \
    'edênico','encantado','edêneo','fascinado','puro','vencido','cativo', \
    'entusiasmado','maravilhado','embebido','surpreso','surpreendido', \
    'admirado','espantado','pasmado','atônito','pasmo','estupefato', \
    'maravilhado','orgulho']

    sentiment_bad = ['triste','sentido','infeliz','desgraçado','consternado', \
    'mísero','coitado','perturbado','desolado','entristecido','desgostoso', \
    'pesaroso','contristado','miserável','dor','desditoso','mal-afortunado', \
    'infausto','desafortunado','desventurado','infortunado','mal-aventurado',
    'malventuroso','perdido','condenado','maldito','danado','sentenciado', \
    'sofredor','padecente','sofrido','penado','padecedor','alanceado','angustiado', \
    'atormentado','aflito','amargurado','doloroso','apertado','torturado', \
    'dilacerado','flagelado','atribulado','afligido','ansiado','agoniado', \
    'mortificado','amargado']

    return sentiment_good, sentiment_bad

   
#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_priority_simbols():
    simbols_priority = ['?','!']

    return simbols_priority


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_interrogative_pronouns():
    interrogative_pronouns = \
    ['quem','quando','qual','quanto','que','por que','onde']

    return interrogative_pronouns


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_categ_ents_c2():
    
    categ_ents_action = ['atacar','atirar','fogo','avançar','retonar','esperar','disparar','agir', 
                         'combater','matar','destruir','combate', 'combates', 'treinar','treinamento', 
                         'treinamentos','proteger','protecao','protecoes','emboscada','emboscadas', 'missao',
                         'missoes', 'operacao','operacoes', 'estartegico', 'estrategicos', 'deslocamento',
                         'deslocamentos', 'ataque', 'atacar', 'ataques', 'decisao','decisoes']
    
    categ_ents_agent  = ['soldado','soldados', 'cabo','cabos', 'sargento','sargentos','tenente','tenentes',
                         'capitao','capitoes','major', 'coronel','corneis', 'general', 'generais', 'ministro', 
                         'ministrros','presidente','presidentes','comandante', 'comandantes', 'operador', 
                         'operadores','comandado', 'comandados', 'guerreiro','guerreiros','sentinela',
                         'sentinelas','gurada','guardas','recruta','recrutas', 'engenheiro','engenheiros',
                         'elemento', 'elementos']
    
    categ_ents_direction = ['norte', 'sul', 'leste', 'oeste', 'nordeste', 'suldeste', 'centroeste', 'sudoeste', 
                            'oriente', 'ocidente', 'flanco', 'flancos',]
    
    categ_ents_weapon = ['fuzil','pistola','pistolas','revolver','revolveres','faca','facas','baioneta','baionetas',
                         'metralhadora','metralhadoras','cassetete','cassetetes','bastão','bastões','granada', 
                         'granadas','lança foguete','arma de choque','rifle','rifles','canhao','canhoes','missil',
                         'misseis','foguete','foguetes','carabina','carabinas','morteiro','morteiros','espingarda',
                         'espingardas','r15', 'torpedo','torpedos','arma','armas', 'bomba','bombas', 'dinamite',
                         'dinamites',]
    
    categ_ents_unit = ['inimigo','inimiga','inimigos','inimigas','regimento','regimentos','pelotao','pelotoes',
                       'cia','cias','companhia','companhias','esquadras','esquadra','quartel','quarteis','alvo',
                       'alvos','comando','comandos','batalhao','batalhoes','exercito','exercitos','marinha', 
                       'marinhas','aeronautica','aeronauticas','bombeiro','bombeiros','policia', 'policiais',
                       'policia civil','policia militar','tropa','tropas','esquadrao','esquadroes','frota',
                       'frotas','infantaria','infantarias', 'cavalaria','cavalarias','fileira', 'fieliras',
                       'comboio', 'comboios', 'coluna','colunas','patrulha', 'patrulhas','unidade', 'unidades',
                       'artilharia','artilharias']
    
    categ_ents_vehicle = ['blindado','blindados', 'carro','carros', 'moto','motos', 'motocicleta','motocicletas',
                          'aeronave', 'aeronaves', 'aviao', 'avioes', 'drone', 'drones', 'jato', 'jatos',
                          'navio', 'navios', 'tanque','tanques', 'bote','botes', 'barco','barcos', 'viatura',
                          'viaturas', 'trator','tratores', 'reboque','reboques','ambulancia','ambulancias', 
                          'motoneta','motonetas','triciclo','triciclos','automovel','automoveis','micro-onibus',
                          'onibus','caminhao','caminhoes','helicoptero','helicopteros','balao','baloes','dirigivel',
                          'dirigiveis','planador','planadores','submarino','submarinos','veiculo','veiculos',
                          'embarcacao','embarcacoes','navio-tanque','frota','frotas'] 
    
    categ_ents_place = ['estrada','estradas', 'rodovia','rodovias', 'rua','ruas', 'lago', 'lagos', 'lagoa', 'lagoas',
                        'montanha', 'montanhas', 'floresta', 'florestas', 'morro','morros','mata', 'matas','bairro',
                        'bairros','cidade','cidades','municipio','municipios', 'estado','estados', 'pais', 'paises',
                        'continente', 'continentes', 'avenida', 'avenidas', 'favela','favelas','comunidade', 'comunidades', 
                        'praça','praças','rio','rios','riacho','riachos','distrito','distritos','terreno','terrenos',
                        'mar','mares','oceano','oceanos','espaço aereo','alto-mar','terra','caverna','cavernas','monte',
                        'montes','alto-mar','area','areas','zona','zonas','perimetro','perimetros', 'campo', 'campos',
                        'ponte','pontes', 'nacao', 'destrito','sitio','sitios','chacarra', 'chacarras','fazenda', 'fazendas',
                        'area', 'areas', 'aeroporto','aeroportos']  

    return categ_ents_action, categ_ents_agent, categ_ents_direction, categ_ents_weapon, categ_ents_unit, \
    categ_ents_vehicle, categ_ents_place


#---------------------------------------------------
#
#---------------------------------------------------
def load_nlp():
    nlp_maisc2 = spacy.load("model/model-best")
    nlp_spacy = spacy.load('pt_core_news_sm')  

    return nlp_maisc2, nlp_spacy 
