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

   
#... 
def load_priority_simbols():
    simbols_priority = '?'
    return simbols_priority

#...
def load_priority_words():
    priority_words = ['confirme', 'gostaria', 'analise','verifique', 'saber',
    'descubra','avalie','identifique', 'conseguiram']

    return priority_words

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_interrogative_pronouns():
    interrogative_pronouns = ['quem','quando','qual','quanto','que','por que',\
    'onde', 'quantos', 'quais', 'quer', 'quanta', 'quantas', 'porque']

    return interrogative_pronouns

# 

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def load_categ_ents_c2():
    categ_ents_action = ['atacar','atirar','abrir fogo','avançar','retonar','esperar','disparar','agir', 
                         'combater','matar','destruir','combate', 'combates', 'treinar','treinamento', 
                         'treinamentos','proteger','protecao','protecoes','emboscada','emboscadas', 'missao',
                         'missoes', 'operacao','operacoes', 'estartegico', 'estrategicos', 'deslocamento',
                         'deslocamentos', 'ataque', 'atacar', 'ataques', 'decisao','decisoes', 'perigo',
                         'perigos', 'perigoso', 'perigosa', 'fogo', 'fire']
    
    categ_ents_agent  = ['soldado','soldados', 'cabo','cabos', 'sargento','sargentos','tenente','tenentes',
                         'capitao','capitoes','major', 'coronel','corneis', 'general', 'generais', 'ministro', 
                         'ministrros','presidente','presidentes','comandante', 'comandantes', 'operador', 
                         'operadores','comandado', 'comandados', 'guerreiro','guerreiros','sentinela','sentinelas',
                         'gurada','guardas','recruta','recrutas', 'engenheiro','engenheiros','elemento', 'elementos',
                         'almirante', 'brigadeiro','militar', 'militares']
    
    categ_ents_direction = ['norte', 'sul', 'leste', 'oeste', 'nordeste', 'suldeste', 'centroeste', 'sudoeste', 
                            'oriente', 'ocidente', 'flanco', 'flancos', ]
    
    categ_ents_weapon = ['fuzil','pistola','pistolas','revolver','revolveres','faca','facas','baioneta','baionetas',
                         'metralhadora','metralhadoras','cassetete','cassetetes','bastão','bastões','granada', 
                         'granadas','lança foguete','arma de choque','rifle','rifles','canhao','canhoes','missil',
                         'misseis','foguete','foguetes','carabina','carabinas','morteiro','morteiros','espingarda',
                         'espingardas','r15', 'torpedo','torpedos']
    
    categ_ents_unit = ['inimigo','inimiga','inimigos','inimigas','regimento','regimentos','pelotao','pelotoes',
                       'cia','cias','companhia','companhias','esquadras','esquadra','quartel','quarteis','alvo',
                       'alvos','comando','comandos','batalhao','batalhoes','exercito','exercitos','marinha', 
                       'marinhas','aeronautica','aeronauticas','bombeiro','bombeiros','policia', 'policiais',
                       'policia civil','policia militar','tropa','tropas','esquadrao','esquadroes','frota',
                       'frotas','infantaria','infantarias', 'cavalaria','cavalarias','fileira', 'fieliras',
                       'comboio', 'comboios', 'coluna','colunas','patrulha', 'patrulhas','unidade','unidades',
                       'divisao', 'divisoes']
    
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
                        'mar','mares','oceano','oceanos','espaco','espacos', 'terra','caverna','cavernas','monte',
                        'montes','alto-mar','area','areas','zona','zonas','perimetro','perimetros', 'campo', 'campos',
                        'ponte','pontes', 'nacao', 'destrito','sitio','sitios','chacarra', 'chacarras','fazenda', 'fazendas',
                        'area', 'areas','rural','vila','vilas','villa', 'villas']  

    return categ_ents_action, categ_ents_agent, categ_ents_direction, categ_ents_weapon, categ_ents_unit, \
    categ_ents_vehicle, categ_ents_place


#---------------------------------------------------
#
#---------------------------------------------------
def load_nlp():
    nlp_maisc2 = spacy.load("model/model-best")
    nlp_spacy = spacy.load('pt_core_news_sm')  

    return nlp_maisc2, nlp_spacy 



#Quanto custa o quilo de tomate?
# Você quer ir ao cinema comigo?
# Onde fica o museu de Belas Artes?
# Pode fechar a janela?
# Você pode me ajudar a levar esta caixa até o carro?
# Que tal se sairmos para jantar amanhã?
# Com que frequência visita seus avós?
# Acha bem agir assim?
# Quantos habitantes têm a Dinamarca?
# Quantas vezes são realizadas eleições presidenciais?
# Para onde vamos na nossa lua de mel?
# Por que ele ficaria bravo?
# Você não acha um pouco estranha a forma como ele reagiu?
# Quais ingredientes têm esta salada?
# Qual cor a Maria gosta mais para esta parede?
# Qual é o cargo do seu pai no banco?
# Não acha que é falta de consideração essa atitude?
# O cãozinho que está perto daquela árvore é seu?
# Qual é a melhor peça de Shakespeare na sua opinião?
# Como conseguiu montar o quebra-cabeça tão depressa?
# Quer que levemos o móvel para a sua casa ou o senhor passa a retirá-lo?
# Por que se demitiu?
# Pedimos sorvete para levar?
# Quem votou contra a nova lei?
# Você conhece esse homem?
# A que horas nos encontramos amanhã?
# Você bebe água ou refrigerante?
# Quando a viu pela última vez?
# Por que saiu tão cedo?
# Com que antecedência temos que comprar os ingressos para o show do Roberto Carlos?
# Quando é o seu aniversário?
# Por que se atrasou?
# Você entendeu a lição?
# De onde veio esta carta?
# Há quanto tempo vivem neste bairro?
# De que tipo de filmes você gosta?
# Para onde viaja este ônibus?
# Gostaria de saber como a história termina?
# Quando fizeram a denúncia?
# Por onde posso entrar?
# O que está dentro da caixa?
# Como estão organizados estes livros?
# Quanto custa uma noite neste hotel?
# Quem são os responsáveis por este atropelamento?
# Quando o filme vai estrear?
# Como podem estar tão calmos?
# Eles chegaram a tempo?
# Dá para acreditar nisso?
# Você está por conta própria aqui?
# Porque os lucros da empresa aumentaram, mas o rendimento diminuiu?
# Exemplos de frases interrogativas indiretas
# Eu gostaria que me explicasse onde está todo o dinheiro que te dei.
# O homem perguntou-lhe se tinha irmãos.
# Consultei-o porque não tinha me mantido informado sobre a situação.
# Pergunto-me se valeu a pena fazer tantas mudanças.
# Perguntamos-lhes com que frequência pintam a casa.
# O teste foi sobre como a Primeira Guerra Mundial se desenvolveu.
# Meu irmão me perguntou porque estão vendendo o carro agora.
# Posso imaginar de onde veio esse rumor.
# Quero saber quanto falta para chegar.
# Pedi a minha prima para descobrir onde se pode comprar essas peças.
# Ele me perguntou se eu poderia ir com ele.
# Diz-me quem foi o responsável pelo que aconteceu.
# Perguntaram-me porque não cheguei a tempo com a entrega.
# Ele teve dificuldade em confessar porque tinha mentido.
# Há dias que o Luís tenta lembrar-se de onde deixou os documentos.
# Sabe-se lá quanto custa uma casa de praia igual a esta.
# Ainda não entendo como conseguiram encontrá-lo.
# Gostaria de saber por que ninguém estudou para a prova.
# Não se lembrava onde tinha guardado a carteira.
# Pergunto-me se algum dia poderemos viver em outro planeta.
# Pedi-lhe que me indicasse para onde ir.
# Saberemos como o paciente está quando o médico chegar.
# Viajou para conhecer suas origens.
# Temos que descobrir como sair daqui o mais rápido possível.
# Todos se perguntam o que aconteceu.
# Peço que me lembre qual é a data da viagem.
# Diga-me para quando precisa da peça que me pediu.
# O garoto não quis dizer onde estava escondido.
# Explicarei quais são suas opções agora.
# Eu gostaria de saber como te satisfazer.
# Já não sabia como falar com ela.
# Peço que me explique como resolver este problema.
# Nunca saberão o que aconteceu naquela noite.
# Pense no que gostaria de fazer nas férias.
# O homem não conseguiu explicar com quem estava no dia do crime.
# Digam-me o que preferem esta noite: pizza ou massa.
# Você deve buscar em seu interior qual é sua verdadeira essência.
# O menino pergunta onde está a sua mãe.
# Não gosta que lhe digam como deve agir.
# Para saber como proceder, leia as instruções.
# As placas da estrada indicam aos turistas que caminho devem tomar.
# Gostaria de saber por que agiu assim.
# Diga-me qual é o motivo da sua consulta.
# Pergunto-me se alguma vez concordaram comigo.
# O chefe não sabe o que esperam dele.
# Quero saber quem comeu os doces.
# A polícia quer descobrir quem estava envolvido no incidente.
# Vou te dizer o que é melhor para você nesta situação.
# A mulher perguntou se podia ir com ele no carro.
# O jovem quer saber que ferramenta deve usar para trabalhar com madeira.