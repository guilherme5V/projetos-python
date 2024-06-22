import cores as cr
msg = cr.branco_forte('Olá mundo')
cr.lin('--+')
print(msg)
cr.lin('--=')

# crie um  mampeamento entre estados e siglas
estados = {
    'São paulo': 'SP',
    'Rio de janeiro': 'RJ',
    'Minas gerais': 'MG',
    'Bahia': 'BH',
    'Ceará': 'CR'
}
# crie um conjunto básico de estados e algumas cidades deles 
cidades = {
    'BH': 'Belo Vale',
    'MG': 'Abre Campo',
    'RJ': 'Niteroí',
    'SP': 'São paulo'
}
# adicione mais algumas cidades
cidades ['CR'] = 'Fortaleza'
cidades ['MT'] = 'Mato grosso do sul'
# imprima algumas cidades

print('Estado de CR: ', cidades['CR'])
cr.lin('-')
print('Estado de RJ: ', cidades['RJ'])
cr.lin('-')
# imprima alguns estados
abrSP = cr.fundo_vermelho('São paulo Recebe a abreviação de: '+ estados['São paulo'])
print(abrSP)
cr.lin('-')
abrRJ = cr.fundo_azul('Rio de janeiro Recebe a abreviação de: ' +  estados['Rio de janeiro'])
print(abrRJ)
# faça isso usando o dic state e depois o  cities
cr.lin('-')
print('São paulo veio de: ', cidades[estados['São paulo']])
cr.lin('-')
print('Rio de janeiro veio de: ', cidades[estados['Rio de janeiro']])
#imprima todas as siglas dos estados
for estado, abrev in list(estados.items()):
    cr.lin('-')
    print(f'{estado}, é abreviado {abrev}')
    
    
# imprima cada cidade no estado
for abrev, cidade in list(cidades.items()):
    print(f'{abrev} tem a cidade -> {cidade}')
    cr.lin('/')
# agora faça ambos ao mesmo tempo
for estado, abrev in list(estados.items()):
    cr.lin('+-=')
    print(f'{estado} estado é abreviado {abrev}')
    print(f'e tem a cidade {cidades[abrev]}')
    cr.lin('+-=')
# com segurança obtenha uma sigla de um estado que pode nao estar ali
estado = estados.get('Juazeiro')
if not estado:
    print('Desculpe não há juazeiro')
#obtenha uma cidade com um valor padrão

cidade = cidades.get('JZ', 'Não existe')
print(f'A cidade do estado "JZ" é: {cidade}')