'Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!'

while True:
    nome = input('Qual o seu nome?: ')
    break




def transforma_base(lista):
    d = {}
    for dicio in lista:
        nivel = dicio['nivel']
        if nivel not in d:
            d[nivel] = []
        d[nivel].append(dicio)
    
        
    return d

def valida_questao(questao):
    d = {}
    if 'titulo' not in questao:
        d['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao:
        d['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao:
        d['opcoes'] = 'nao_encontrado'
    
    
    if 'correta' not in questao:
        d['correta'] = 'nao_encontrado'

    else:
        if questao['correta'] not in 'ABCD':
            d['correta'] = 'valor_errado'
    

    if len(questao) != 4:
        d['outro'] = 'numero_chaves_invalido'
    
    if 'titulo' in questao:
        if len(questao['titulo'].strip()) == 0:
            d['titulo'] = 'vazio'
    
    if 'nivel' in questao:
        nivel = questao['nivel']
        if nivel != 'facil' and nivel != 'medio' and nivel != 'dificil':
            d['nivel'] = 'valor_errado'
    
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            d['opcoes'] = 'tamanho_invalido'

        else:
            d2 = {}
            if 'A' not in questao['opcoes'] or  'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or  'D' not in questao['opcoes']:
                d['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                if len(questao['opcoes']['A'].strip()) == 0:
                    d2['A'] = 'vazia'
                    d['opcoes'] = d2
                    
                if len(questao['opcoes']['B'].strip()) == 0:
                    d2['B'] = 'vazia'
                    d['opcoes'] = d2
                    
                if len(questao['opcoes']['C'].strip()) == 0:
                    d2['C'] = 'vazia'
                    d['opcoes'] = d2
                    
                if len(questao['opcoes']['D'].strip()) == 0:
                    d2['D'] = 'vazia'
                    d['opcoes'] = d2
                    
    return d


def valida_questoes(lista):
    l = []
    for questao in lista:
        quest = valida_questao(questao)
        if len(quest) > 0:
            l.append(quest)
        else:
            l.append({})
    return l


import random
def sorteia_questao(dicionario,nivel):
    for dificuldade, lista in dicionario.items():
        if nivel == dificuldade:
            dic_aleatorio = random.choice(lista)

    return dic_aleatorio

def sorteia_questao_inedita(dicionario, nivel, lis):
    sorteada = sorteia_questao (dicionario, nivel)
    if sorteada in lis:
        sorteada = sorteia_questao (dicionario, nivel)
    if sorteada not in lis:
        lis.append(sorteada)
    return sorteada

def questao_para_texto(dicionario,numero):
    
    texto=f'''----------------------------------------
QUESTAO {numero}\n
{dicionario['titulo']}\n
RESPOSTAS:
A: {dicionario['opcoes']['A']}
B: {dicionario['opcoes']['B']}
C: {dicionario['opcoes']['C']}
D: {dicionario['opcoes']['D']}\n'''

    return texto




                

