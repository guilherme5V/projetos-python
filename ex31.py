import cores


def linha():
    print(cores.fundo_preto_forte('-_' * 30))
while True:
    linha();
    print(cores.amarelo_forte(f"""\n você está numa estrada a noite com neblina e florestas em volta,
    o que você faria?
        seguiria reto #1 \n        ou \n   entraria na floresta para buscar ajuda?#2
        opção 4: finalizar dialogo.
    """))

    resposta = input(cores.branco_forte('> '))

    if resposta == '1':

        print(cores.vermelho('Você segue reto porém um carro passa e te sequestra.'))
        linha()
        print(cores.verde_forte('O que você faz?'))
        linha()
        print(cores.verde_forte('1. Tenta se defender com um carregador.'))
        linha()
        print(cores.verde_forte('2. Espera uma melhor oportunidade.'))

        sequestro = input(cores.branco_forte('> '))

        if sequestro == '1':
            print(cores.vermelho_forte('Você tenta se defender mas falha miserávelmente \n pois só tinha um carregador.'))
            print(cores.vermelho_forte('O sequestrador te dá um soco e seu nariz sangra.'))
            print('Ele te amarra em um poste e te deixa na chuva. o que você faz?')
            print('1. Espera algo acontecer. \n 2. Faz força para romper a corda.')
            DepoisDoSequestro = input(cores.ciano_forte('> '))

            if DepoisDoSequestro == '1':
                print('Você espera algo acontecer, 1 hora depois ele volta e te mata com uma faca.')
                print(cores.fundo_vermelho_forte('Fim de jogo'))
            if DepoisDoSequestro == '2':
                print('Você rompe a corda e corre para um celeiro.')
                print('O celeiro cheira mal até que você encontra corpos humanos mortos.')
                linha()
                print(cores.amarelo_forte('O que você faz? 1. Sai correndo. \n 2. Explora o local.'))
                DepoisDoSequestro1 = input(cores.azul_forte('> '))
                if DepoisDoSequestro1 == '1':
                    print(cores.fundo_vermelho('Você corre porém Tropeça bate a cabeça e desmaia.'))
                    print(cores.fundo_vermelho_forte('Acorda novamente sequestrado em um lugar escuro com apenas uma luz acesa.'))
                    print('O que você faz?  1. Espera o sequestrador se distrair e se derruba no chão \n ou \n2. Espera algo acontecer.')
        if sequestro == '2':
            print(cores.fundo_vermelho_forte('A van chega a uma fazenda o sequestrador te desce do veículo \n você dá uma cabeçada nele e desmaia ele.'))
        if sequestro != '1' and sequestro != '2':
            print(cores.ciano('Você não considerou nenhuma das opções e acabou mordendo o motorista.'))

    if resposta == '2':
        print(cores.azul('Você entra na floresta encontra uma boa casa de madeira com luzes acesas porém \n descobre que o dono dela é um lenhador malvado.'))
        print(cores.vermelho('1. Fugir imediatamente da casa.'))
        linha()
        print(cores.magenta('2. Ficar na casa e tentar dialogar com o lenhador.'))
        linha()
        print(cores.amarelo('3. Tentar matar ele com uma faca de sua própria casa.'))
        linha()
        decisão  = input(cores.branco_forte('> '))
        linha()
    
        if decisão == '1' or decisão == '3':
            linha()
            print(cores.fundo_verde_forte('Você teve êxito em suas ações e conseguiu sobreviver \n e voltar para a cidade.'))
            linha()
        if decisão  == '2':
            print(cores.fundo_azul_forte('O lenhador estava totalmente alucinado de Drogas \n e te deu um tiro no coração e deixou você sangrar até a morte.'))
    if resposta == '4':
        break


